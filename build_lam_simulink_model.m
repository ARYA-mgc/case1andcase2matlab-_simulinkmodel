%% =========================================================================
%  LAM Research Challenge 3.0 - Stage 2
%  Programmatic Simulink Model Builder: lam_stage2_system.slx
%  =========================================================================
%  This script builds the complete Simulink model replicating the
%  Stage 2 industrial liquid handling process:
%    - Multi-Tank hydraulics (10L process tank, 4.2L sump, 4.2L flush tank)
%    - 3x Pumps with BTS7960 slew rate limits and motor inertia
%    - OV-01 Solenoid valve & BV-01 Manual flush valve
%    - FT-01 Turbine flow sensor with totalizer
%    - Sump float switch with level-hysteresis protection
%    - Full firmware state machine (IDLE -> CASE1 -> CASE2 -> DONE)
%    - Real-time Scopes & To-Workspace logging sinks
%  =========================================================================

clear; clc;
fprintf('=================================================================\n');
fprintf('  Building LAM Research Challenge 3.0 Stage 2 Simulink Model     \n');
fprintf('=================================================================\n\n');

%% 1. Load System Parameters
lam_system_params;

model_name = 'lam_stage2_system';

%% 2. Check Simulink Availability
has_simulink = false;
try
    has_simulink = license('test', 'Simulink') && ~isempty(ver('simulink'));
catch
    has_simulink = false;
end

if ~has_simulink
    warning('Simulink license or installation not currently active in this session.');
    fprintf(['\nNOTE: You can still run the entire system simulation without Simulink\n', ...
             'using the standalone mathematical engine in "run_lam_simulation.m".\n', ...
             'Attempting to construct the model if possible...\n\n']);
end

%% 3. Close & Remove Any Existing Model
if bdIsLoaded(model_name)
    close_system(model_name, 0);
end
slx_file = [model_name '.slx'];
if exist(slx_file, 'file')
    try
        delete(slx_file);
    catch
        % File might be locked
    end
end

%% 4. Initialize New Simulink System
try
    new_system(model_name);
    open_system(model_name);
catch ME
    warning(['Could not open new Simulink system: ' ME.message]);
    fprintf('You can run the simulation directly with: run_lam_simulation\n');
    return;
end

%% 5. Configure Solver & Simulation Parameters
set_param(model_name, 'SolverType', 'Fixed-step');
set_param(model_name, 'Solver', 'FixedStepDiscrete');
set_param(model_name, 'FixedStep', num2str(SIM_STEP));
set_param(model_name, 'StopTime', num2str(SIM_TIME));
set_param(model_name, 'SaveTime', 'on', 'TimeSaveName', 'tout');
set_param(model_name, 'SaveState', 'off');
set_param(model_name, 'SaveOutput', 'off');

%% 6. Add Source & Stimulus Blocks
% 6.1 ON/OFF Switch (Push Button Stimulus)
blk_switch = [model_name '/Switch_ON'];
add_block('simulink/Sources/Step', blk_switch, ...
    'Position', [50, 60, 130, 95], ...
    'Time', num2str(SWITCH_ON_TIME), ...
    'Before', '0', ...
    'After', '1');

% 6.2 Manual Flush Ball Valve (BV-01)
blk_bv = [model_name '/BV_01'];
add_block('simulink/Sources/Step', blk_bv, ...
    'Position', [50, 135, 130, 170], ...
    'Time', num2str(BV_OPEN_TIME), ...
    'Before', '0', ...
    'After', '1');

% 6.3 External Fluid Disturbance Inflow to Sump
blk_dist = [model_name '/Disturbance_Inflow'];
add_block('simulink/Sources/Pulse Generator', blk_dist, ...
    'Position', [50, 210, 130, 245], ...
    'PulseType', 'Time based', ...
    'Amplitude', num2str(DIST_RATE), ...
    'Period', num2str(SIM_TIME * 2), ...
    'PulseWidth', num2str((DIST_DURATION / (SIM_TIME * 2)) * 100), ...
    'PhaseDelay', num2str(DIST_START_TIME));

% 6.4 Master Simulation Clock
blk_clock = [model_name '/Clock'];
add_block('simulink/Sources/Clock', blk_clock, ...
    'Position', [50, 285, 130, 320]);

%% 7. Add Combined Controller & Plant MATLAB Function Block
blk_core = [model_name '/LAM_System_Core'];
add_block('simulink/User-Defined Functions/MATLAB Function', blk_core, ...
    'Position', [220, 50, 460, 350]);

% Inject the core function code into the MATLAB Function Block
try
    core_code = fileread('lam_plant_controller.m');
    rt = sfroot;
    chart = rt.find('-isa', 'Stateflow.EMChart', 'Path', blk_core);
    if ~isempty(chart)
        chart.Script = core_code;
        fprintf('  [OK] Injected controller state machine & plant dynamics code.\n');
    else
        warning('Stateflow chart for MATLAB Function block could not be located directly.');
    end
catch ME
    warning(['Could not assign script to MATLAB Function block automatically: ' ME.message]);
    fprintf('The code is saved in lam_plant_controller.m and can be opened in the block editor.\n');
end

%% 8. Add Scopes for Real-Time Visualization
% 8.1 Scope: Tank Levels
blk_sc_tanks = [model_name '/Scope_Tanks'];
add_block('simulink/Sinks/Scope', blk_sc_tanks, ...
    'Position', [550, 55, 610, 95]);

% 8.2 Scope: Pump Flow Rates
blk_sc_flows = [model_name '/Scope_Flows'];
add_block('simulink/Sinks/Scope', blk_sc_flows, ...
    'Position', [550, 115, 610, 155]);

% 8.3 Scope: Flow Sensor FT-01
blk_sc_ft01 = [model_name '/Scope_FT01'];
add_block('simulink/Sinks/Scope', blk_sc_ft01, ...
    'Position', [550, 175, 610, 215]);

% 8.4 Scope: State Machine Status
blk_sc_state = [model_name '/Scope_State'];
add_block('simulink/Sinks/Scope', blk_sc_state, ...
    'Position', [550, 235, 610, 275]);

% 8.5 Scope: Pump Duty Cycles
blk_sc_duty = [model_name '/Scope_Duties'];
add_block('simulink/Sinks/Scope', blk_sc_duty, ...
    'Position', [550, 295, 610, 335]);

%% 9. Add To-Workspace Blocks for Post-Processing & Analytics
% Configure each block to save as a 2D Array
to_ws_blocks = {
    'Save_Tanks',    'tank_levels',   [660, 55,  760, 95];
    'Save_Flows',    'pump_flows',    [660, 115, 760, 155];
    'Save_FT01',     'ft01_flow',     [660, 175, 760, 215];
    'Save_TotalVol', 'total_volume',  [660, 235, 760, 275];
    'Save_State',    'system_state',  [660, 295, 760, 335];
    'Save_Duties',   'pump_duties',   [660, 355, 760, 395];
    'Save_Status',   'status_signals',[660, 415, 760, 455];
    'Save_Time',     'sim_time',      [220, 385, 320, 420];
};

for i = 1:size(to_ws_blocks, 1)
    bname = to_ws_blocks{i, 1};
    vname = to_ws_blocks{i, 2};
    bpos  = to_ws_blocks{i, 3};
    bpath = [model_name '/' bname];
    add_block('simulink/Sinks/To Workspace', bpath, ...
        'Position', bpos, ...
        'VariableName', vname, ...
        'SaveFormat', 'Array', ...
        'SampleTime', num2str(SIM_STEP));
end

%% 10. Wire Signal Connections
try
    % Input Connections to Core Block
    add_line(model_name, 'Switch_ON/1',          'LAM_System_Core/1', 'autorouting', 'on');
    add_line(model_name, 'BV_01/1',              'LAM_System_Core/2', 'autorouting', 'on');
    add_line(model_name, 'Disturbance_Inflow/1', 'LAM_System_Core/3', 'autorouting', 'on');
    add_line(model_name, 'Clock/1',              'LAM_System_Core/4', 'autorouting', 'on');

    % Clock to Save_Time
    add_line(model_name, 'Clock/1',              'Save_Time/1',       'autorouting', 'on');

    % Core Outputs to Scopes and Sinks
    % Out 1: Tank Levels [10L, Sump, Flush]
    add_line(model_name, 'LAM_System_Core/1',    'Scope_Tanks/1',     'autorouting', 'on');
    add_line(model_name, 'LAM_System_Core/1',    'Save_Tanks/1',      'autorouting', 'on');

    % Out 2: Pump Flows [P1, P2, P3]
    add_line(model_name, 'LAM_System_Core/2',    'Scope_Flows/1',     'autorouting', 'on');
    add_line(model_name, 'LAM_System_Core/2',    'Save_Flows/1',      'autorouting', 'on');

    % Out 3: FT-01 Flow Rate
    add_line(model_name, 'LAM_System_Core/3',    'Scope_FT01/1',      'autorouting', 'on');
    add_line(model_name, 'LAM_System_Core/3',    'Save_FT01/1',       'autorouting', 'on');

    % Out 4: Total Volume
    add_line(model_name, 'LAM_System_Core/4',    'Save_TotalVol/1',   'autorouting', 'on');

    % Out 5: System State
    add_line(model_name, 'LAM_System_Core/5',    'Scope_State/1',     'autorouting', 'on');
    add_line(model_name, 'LAM_System_Core/5',    'Save_State/1',      'autorouting', 'on');

    % Out 6: Pump Duties
    add_line(model_name, 'LAM_System_Core/6',    'Scope_Duties/1',    'autorouting', 'on');
    add_line(model_name, 'LAM_System_Core/6',    'Save_Duties/1',     'autorouting', 'on');

    % Out 7: Status Signals [OV-01, Float, Flush_Vol]
    add_line(model_name, 'LAM_System_Core/7',    'Save_Status/1',     'autorouting', 'on');

    fprintf('  [OK] Successfully routed all block connections.\n');
catch ME
    warning(['Wiring connection error: ' ME.message]);
end

%% 11. Save and Close Model
try
    save_system(model_name, slx_file);
    fprintf('  [OK] Saved Simulink model to: %s\n', slx_file);
catch ME
    warning(['Could not save system to file: ' ME.message]);
end

fprintf('\n=================================================================\n');
fprintf('  Simulink Model "%s" is Ready!                         \n', model_name);
fprintf('  Execute "run_lam_simulation" to run and visualize results.     \n');
fprintf('=================================================================\n');
