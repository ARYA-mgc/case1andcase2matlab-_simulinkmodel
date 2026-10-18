function [tank_levels, pump_flows, ft01_flow, total_volume, system_state, pump_duties, status_signals] = ...
    lam_plant_controller(switch_on, bv_open, q_dist, t_sim)
%#codegen
%% =========================================================================
%  LAM Research Challenge 3.0 - Stage 2
%  Integrated Controller State Machine & Plant Hydraulics Model
%  =========================================================================
%  This function executes both the ESP32 firmware state machine and the
%  physical liquid-handling plant dynamics for each simulation time step.
%
%  Inputs:
%    switch_on   : Rig push button ON/OFF command (0 = OFF, 1 = ON)
%    bv_open     : Manual flush ball valve BV-01 (0 = Closed, 1 = Open)
%    q_dist      : External fluid disturbance inflow to sump (L/min)
%    t_sim       : Current simulation time (seconds)
%
%  Outputs:
%    tank_levels   : [V_10L; V_sump; V_flush] (Liters)
%    pump_flows    : [Q_p1; Q_p2; Q_p3] (Liters/min)
%    ft01_flow     : Flow sensor FT-01 reading (Liters/min)
%    total_volume  : Cumulative volume measured by FT-01 (Liters)
%    system_state  : Controller state integer (0=IDLE, 1=C1_FILL, 2=C1_RUN,
%                    3=C1_FLOAT, 4=C1_STABLE, 5=C1_WARN, 6=C2_DELAY,
%                    7=C2_FLUSH, 8=DONE)
%    pump_duties   : [duty_p1; duty_p2; duty_p3] Slew-limited duty cycles (%)
%    status_signals: [ov01_valve; float_high; flush_volume]
%  =========================================================================

%% ---- Persistent State Memory ----
persistent state state_start
persistent p2_started float_triggered float_triggered_at
persistent p1_restarted p1_restarted_at last_stable_q c1_stable_count
persistent last_stable_check c1_flow_stable c1_trans_at c1_trans_warned
persistent c2_p3_started c2_start_vol c2_low_flow_since c2_done
persistent duty_p1_act duty_p2_act duty_p3_act
persistent v_10L v_sump v_flush q1_filt q2_filt q3_filt total_vol float_high_state
persistent prev_t

%% ---- Initialization on First Call ----
if isempty(state)
    state              = 0;       % 0: ST_IDLE
    state_start        = 0.0;
    p2_started         = false;
    float_triggered    = false;
    float_triggered_at = 0.0;
    p1_restarted       = false;
    p1_restarted_at    = 0.0;
    last_stable_q      = 0.0;
    c1_stable_count    = 0;
    last_stable_check  = 0.0;
    c1_flow_stable     = false;
    c1_trans_at        = 0.0;
    c1_trans_warned    = false;
    c2_p3_started      = false;
    c2_start_vol       = 0.0;
    c2_low_flow_since  = 0.0;
    c2_done            = false;

    % Slew-rate limited duty cycles
    duty_p1_act        = 0.0;
    duty_p2_act        = 0.0;
    duty_p3_act        = 0.0;

    % Initial tank volumes (from lam_system_params.m)
    v_10L              = 8.0;     % L (10L process tank initial level)
    v_sump             = 0.5;     % L (sump initial level)
    v_flush            = 4.2;     % L (flush tank full)

    % Plant dynamics filters
    q1_filt            = 0.0;
    q2_filt            = 0.0;
    q3_filt            = 0.0;
    total_vol          = 0.0;
    float_high_state   = false;
    prev_t             = t_sim;
end

%% ---- Compute Discrete Time Step ----
dt = t_sim - prev_t;
if dt <= 0.0 || dt > 0.05
    dt = 0.001; % Default fixed step (1 ms)
end
prev_t = t_sim;

%% ---- System Parameters & Thresholds ----
% Tank capacities (L)
CAP_10L            = 10.0;
CAP_SUMP           = 4.2;
CAP_FLUSH          = 4.2;
AVAIL_TH           = 1.0;   % Minimum volume threshold for full draw availability (L)

% Pump maximum capacities at 100% duty (L/min)
P1_QMAX            = 6.0;   % Pump-01 (process transfer)
P2_QMAX            = 4.5;   % Pump-02 (recirculation through FT-01)
P3_QMAX            = 5.0;   % Pump-03 (flush transfer)
PUMP_TAU           = 0.3;   % Motor/hydraulic lag time constant (s)

% Slew rate limits (%/s)
SLEW_RISE          = 300.0; % +300 %/s
SLEW_FALL          = -500.0;% -500 %/s

% Float sensor hysteresis thresholds (L)
FLOAT_HI_TH        = 3.5;   % High level trigger (stop P1)
FLOAT_LO_TH        = 2.5;   % Low level release (resume P1)

% Case 1 parameters (firmware)
C1_P1_DUTY         = 50.0;  % %
C1_P2_DUTY         = 100.0; % %
SUMP_FILL_DELAY    = 10.0;  % s (simulated fill delay; firmware=60s)
C1_MAX_TIMEOUT     = 300.0; % s (5 min fallback)
C1_FLOW_MIN        = 1.50;  % L/min minimum established flow
C1_FLOW_DELTA      = 0.25;  % L/min stability window
C1_STABLE_REQ      = 8;     % Consecutive 500ms samples needed (4s)
C1_DRY_FALLBACK    = 120.0; % s bench fallback
C1_WARN_TIME       = 5.0;   % s warning before Case 2

% Case 2 parameters (firmware)
C2_DUTY            = 100.0; % %
C2_VALVE_DELAY     = 5.0;   % s
C2_MAX_TIMEOUT     = 75.0;  % s
C2_TARGET_L        = 4.20;  % L nominal flush volume
C2_MAX_L           = 4.50;  % L upper cutoff limit
C2_LOW_Q_TH        = 0.35;  % L/min low flow settling threshold

%% =========================================================================
%% 1. CONTROLLER STATE MACHINE
%% =========================================================================
switch_req = (switch_on > 0.5);
level_high = float_high_state;
flow_lpm   = q2_filt; % Current FT-01 flow measurement

cmd_p1   = 0.0;
cmd_p2   = 0.0;
cmd_p3   = 0.0;
cmd_ov01 = 0.0;

switch state
    case 0 % ST_IDLE
        cmd_p1   = 0.0;
        cmd_p2   = 0.0;
        cmd_p3   = 0.0;
        cmd_ov01 = 0.0;

        if switch_req
            state              = 1; % Start Case 1 Fill
            state_start        = t_sim;
            total_vol          = 0.0;
            p2_started         = false;
            float_triggered    = false;
            float_triggered_at = 0.0;
            p1_restarted       = false;
            p1_restarted_at    = 0.0;
            last_stable_q      = 0.0;
            c1_stable_count    = 0;
            c1_flow_stable     = false;
            c1_trans_at        = 0.0;
            c1_trans_warned    = false;
        end

    case 1 % ST_CASE1_FILL (Phase A: Sump filling)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0; % Solenoid OV-01 Open
            cmd_p1   = C1_P1_DUTY;
            cmd_p2   = 0.0;
            cmd_p3   = 0.0;

            elapsed = t_sim - state_start;
            % Transition to Case 1 Run when fill delay elapses or float switch trips
            if elapsed >= SUMP_FILL_DELAY || level_high
                p2_started = true;
                state      = 2; % ST_CASE1_RUN
            end
        end

    case 2 % ST_CASE1_RUN (Phase B: Recirculation)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            elapsed  = t_sim - state_start;

            % Float switch trigger detection (external fluid ingress)
            if level_high
                float_triggered    = true;
                p1_restarted       = false;
                c1_flow_stable     = false;
                c1_stable_count    = 0;
                state              = 3; % ST_CASE1_FLOAT_PROT
                cmd_p1             = 0.0;
                cmd_p2             = C1_P2_DUTY;
            elseif elapsed >= C1_MAX_TIMEOUT
                % Timeout fallback transition
                state       = 6; % ST_CASE2_DELAY
                state_start = t_sim;
            else
                cmd_p1 = C1_P1_DUTY;
                cmd_p2 = C1_P2_DUTY;
            end
        end

    case 3 % ST_CASE1_FLOAT_PROT (Float High Protection)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = 0.0;        % Stop P1 immediately
            cmd_p2   = C1_P2_DUTY; % P2 drains sump at 100%

            % Check if level has reduced back to normal (float cleared)
            if ~level_high
                p1_restarted       = true;
                p1_restarted_at    = t_sim;
                last_stable_q      = flow_lpm;
                c1_stable_count    = 0;
                last_stable_check  = t_sim;
                c1_flow_stable     = false;
                c1_trans_warned    = false;
                state              = 4; % ST_CASE1_STABILIZING
                cmd_p1             = C1_P1_DUTY; % Resume P1
            end
        end

    case 4 % ST_CASE1_STABILIZING (Verify flow stability)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = C1_P1_DUTY;
            cmd_p2   = C1_P2_DUTY;

            if level_high
                % Re-enter protection if float re-triggers
                state = 3;
            else
                time_since_restart = t_sim - p1_restarted_at;

                % Stability check sampled every 500 ms (DATA_INTERVAL_MS in firmware)
                if (t_sim - last_stable_check) >= 0.5
                    last_stable_check = t_sim;

                    if flow_lpm >= C1_FLOW_MIN
                        if abs(flow_lpm - last_stable_q) <= C1_FLOW_DELTA
                            c1_stable_count = c1_stable_count + 1;
                        else
                            last_stable_q   = flow_lpm;
                            c1_stable_count = 1;
                        end

                        if c1_stable_count >= C1_STABLE_REQ
                            c1_flow_stable = true;
                            c1_trans_at    = t_sim + C1_WARN_TIME;
                            state          = 5; % ST_CASE1_TRANSITION_WARN
                        end
                    end
                end

                % Fallback timeout
                if ~c1_flow_stable && time_since_restart >= C1_DRY_FALLBACK
                    state       = 6; % ST_CASE2_DELAY
                    state_start = t_sim;
                end
            end
        end

    case 5 % ST_CASE1_TRANSITION_WARN (5s warning countdown)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = C1_P1_DUTY;
            cmd_p2   = C1_P2_DUTY;

            if t_sim >= c1_trans_at
                state       = 6; % Transition to Case 2 Delay
                state_start = t_sim;
            end
        end

    case 6 % ST_CASE2_DELAY (Isolate 10L tank, 5s valve settling delay)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 0.0; % OV-01 Closed (isolate 10L process tank)
            cmd_p1   = 0.0;
            cmd_p2   = 0.0;
            cmd_p3   = 0.0;

            elapsed = t_sim - state_start;
            if elapsed >= C2_VALVE_DELAY
                state             = 7; % ST_CASE2_FLUSH
                state_start       = t_sim;
                c2_p3_started     = true;
                c2_start_vol      = total_vol;
                c2_low_flow_since = 0.0;
            end
        end

    case 7 % ST_CASE2_FLUSH (Active flush sequence)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 0.0; % OV-01 remains closed
            cmd_p1   = C2_DUTY; % 100%
            cmd_p2   = C2_DUTY; % 100%
            cmd_p3   = C2_DUTY; % 100%

            flush_l = total_vol - c2_start_vol;
            elapsed = t_sim - state_start;

            % Condition 1: 4.00L reached and flow drops below 0.25 L/min for 1s
            empty_at_target = false;
            if flush_l >= 4.00
                if flow_lpm < 0.25
                    if c2_low_flow_since == 0.0
                        c2_low_flow_since = t_sim;
                    end
                    if (t_sim - c2_low_flow_since) >= 1.0
                        empty_at_target = true;
                    end
                else
                    c2_low_flow_since = 0.0;
                end
            end

            % Condition 2: Target 4.20L reached and low flow settles
            target_reached = (flush_l >= C2_TARGET_L && flow_lpm < C2_LOW_Q_TH);

            % Condition 3: Upper cutoff limit 4.50L reached
            upper_limit_reached = (flush_l >= C2_MAX_L);

            % Condition 4: Max timeout failsafe
            timeout_failsafe = (elapsed >= C2_MAX_TIMEOUT);

            if empty_at_target || target_reached || upper_limit_reached || timeout_failsafe
                state    = 8; % ST_DONE
                cmd_p1   = 0.0;
                cmd_p2   = 0.0;
                cmd_p3   = 0.0;
                cmd_ov01 = 0.0;
            end
        end

    case 8 % ST_DONE (Cycle completed, all off)
        cmd_p1   = 0.0;
        cmd_p2   = 0.0;
        cmd_p3   = 0.0;
        cmd_ov01 = 0.0;

        if ~switch_req
            state = 0; % Reset back to IDLE
        end

    otherwise
        state = 0;
end

%% =========================================================================
%% 2. PUMP SLEW RATE LIMITING (KICK-START & SOFT-START BEHAVIOR)
%% =========================================================================
% Slew Pump 1 duty
rate1 = (cmd_p1 - duty_p1_act) / dt;
if rate1 > SLEW_RISE
    duty_p1_act = duty_p1_act + SLEW_RISE * dt;
elseif rate1 < SLEW_FALL
    duty_p1_act = duty_p1_act + SLEW_FALL * dt;
else
    duty_p1_act = cmd_p1;
end
duty_p1_act = max(0.0, min(100.0, duty_p1_act));

% Slew Pump 2 duty
rate2 = (cmd_p2 - duty_p2_act) / dt;
if rate2 > SLEW_RISE
    duty_p2_act = duty_p2_act + SLEW_RISE * dt;
elseif rate2 < SLEW_FALL
    duty_p2_act = duty_p2_act + SLEW_FALL * dt;
else
    duty_p2_act = cmd_p2;
end
duty_p2_act = max(0.0, min(100.0, duty_p2_act));

% Slew Pump 3 duty
rate3 = (cmd_p3 - duty_p3_act) / dt;
if rate3 > SLEW_RISE
    duty_p3_act = duty_p3_act + SLEW_RISE * dt;
elseif rate3 < SLEW_FALL
    duty_p3_act = duty_p3_act + SLEW_FALL * dt;
else
    duty_p3_act = cmd_p3;
end
duty_p3_act = max(0.0, min(100.0, duty_p3_act));

%% =========================================================================
%% 3. PLANT HYDRAULICS DYNAMICS
%% =========================================================================
% Fluid availability in source tanks [0, 1]
avail_10L   = max(0.0, min(1.0, v_10L   / AVAIL_TH));
avail_sump  = max(0.0, min(1.0, v_sump  / AVAIL_TH));
avail_flush = max(0.0, min(1.0, v_flush / AVAIL_TH));

% Commanded hydraulic flow rates (L/min)
% P1: process fluid from 10L tank through OV-01
q1_cmd = P1_QMAX * (duty_p1_act / 100.0) * (cmd_ov01 > 0.5) * avail_10L;

% P2: recirculation from sump through FT-01
q2_cmd = P2_QMAX * (duty_p2_act / 100.0) * avail_sump;

% P3: flush fluid from flush tank through BV-01
q3_cmd = P3_QMAX * (duty_p3_act / 100.0) * (bv_open > 0.5) * avail_flush;

% First-order lag dynamics (motor inertia & fluid acceleration)
alpha = dt / PUMP_TAU;
if alpha > 1.0, alpha = 1.0; end
q1_filt = q1_filt + alpha * (q1_cmd - q1_filt);
q2_filt = q2_filt + alpha * (q2_cmd - q2_filt);
q3_filt = q3_filt + alpha * (q3_cmd - q3_filt);

q1_act = max(0.0, q1_filt);
q2_act = max(0.0, q2_filt);
q3_act = max(0.0, q3_filt);

% External disturbance inflow
q_dist_act = max(0.0, q_dist);

% Tank Volume Balance Equations (rates in L/s = L/min / 60)
% 10L Process Tank: Inflow from P2 return, Outflow to P1
dv_10L  = (q2_act - q1_act) / 60.0;

% Sump: Inflow from P1, P3, and disturbance; Outflow to P2
dv_sump = (q1_act + q3_act + q_dist_act - q2_act) / 60.0;

% Flush Tank: Outflow to P3
dv_flush = (-q3_act) / 60.0;

% Integrate tank volumes (Euler integration, clamped to physical capacities)
v_10L   = max(0.0, min(CAP_10L,   v_10L   + dt * dv_10L));
v_sump  = max(0.0, min(CAP_SUMP,  v_sump  + dt * dv_sump));
v_flush = max(0.0, min(CAP_FLUSH, v_flush + dt * dv_flush));

% Flow Totalizer through FT-01 (L)
if state >= 1 && state <= 7
    total_vol = total_vol + (q2_act * dt / 60.0);
end

% Float Switch Level Sensing with Hysteresis
if v_sump >= FLOAT_HI_TH
    float_high_state = true;
elseif v_sump <= FLOAT_LO_TH
    float_high_state = false;
end

%% =========================================================================
%% 4. PACKAGING SYSTEM OUTPUTS
%% =========================================================================
tank_levels  = [v_10L; v_sump; v_flush];
pump_flows   = [q1_act; q2_act; q3_act];
ft01_flow    = q2_act;
total_volume = total_vol;
system_state = double(state);
pump_duties  = [duty_p1_act; duty_p2_act; duty_p3_act];

flush_vol_curr = 0.0;
if state >= 6
    flush_vol_curr = max(0.0, total_vol - c2_start_vol);
end
status_signals = [cmd_ov01; double(float_high_state); flush_vol_curr];

end
