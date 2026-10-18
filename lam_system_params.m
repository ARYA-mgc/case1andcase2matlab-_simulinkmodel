%% =========================================================================
%  LAM Research Challenge 3.0 - Stage 2: System Parameters
%  All values extracted from ESP32 firmware (lam_stage2.ino)
%  and the Problem Statement process parameters.
%  =========================================================================
%  Run this script before build_lam_simulink_model.m
%  =========================================================================

%% ---- Tank Capacities & Initial Conditions ----
tank_10L_capacity  = 10.0;   % L   (Fluid Tank-01 capacity)
tank_10L_initial   = 8.0;    % L   (starting fill level)
sump_capacity      = 4.2;    % L   (Sump / 4.2L collection vessel)
sump_initial       = 0.5;    % L   (starting level in sump)
flush_capacity     = 4.2;    % L   (Flush Fluid Tank capacity)
flush_initial      = 4.2;    % L   (starts FULL)

%% ---- Pump Maximum Flow Rates (at 100 % duty) ----
%  Determined experimentally from system hydraulics.
%  At 50 % duty P1 delivers ~3 L/min matching the 3 L/min target.
P1_QMAX = 6.0;    % L/min  (Pump-01, process fluid from 10L tank)
P2_QMAX = 4.5;    % L/min  (Pump-02, recirculation through FT-01)
P3_QMAX = 5.0;    % L/min  (Pump-03, flush fluid from 4.2L tank)

%% ---- Pump First-Order Dynamics ----
PUMP_TAU = 0.3;    % s      Motor / hydraulic time constant

%% ---- Pump Slew Rate (duty-cycle rate limiter) ----
%  Prevents instantaneous motor current spikes.
%  Firmware uses a 300 ms kick at 100 % on start-up; the slew
%  rate limiter gives a similar smooth ramp in Simulink.
PUMP_SLEW_RISE =  300;   % %/s   (0 -> 100 % in 0.33 s)
PUMP_SLEW_FALL = -500;   % %/s   (100 -> 0 % in 0.20 s)
PUMP_KICK_MS   =  300;   % ms    (firmware kick duration, for reference)

%% ---- Flow-Availability Threshold ----
%  Pumps cannot draw from an empty tank.  Flow ramps smoothly
%  to zero as tank volume falls below this threshold.
AVAIL_THRESH = 1.0;   % L

%% ---- Float Switch Hysteresis (Sump level sensor) ----
%  PIN_FLOAT = 35;  LOW = High liquid level.
%  Firmware debounce: 500 ms HIGH, 2000 ms LOW.
FLOAT_HIGH_THRESH = 3.5;   % L   (trigger: sump full -> stop P1)
FLOAT_LOW_THRESH  = 2.5;   % L   (release: sump drained -> resume P1)

%% ---- Flow Sensor Calibration (FT-01) ----
%  5266 pulses per Liter (experimentally calibrated)
FT01_PULSES_PER_L = 5266;
FT01_CAL_A = 60.0 / FT01_PULSES_PER_L;   % L/min per Hz  (~0.01139)
FT01_CAL_B = 0.0;                          % offset

%% ---- Case 1 Control Parameters ----
CASE1_P1_DUTY    = 50;     % %   (cfgP1 in firmware)
CASE1_P2_DUTY    = 100;    % %   (cfgP2 in firmware)
SUMP_FILL_DELAY  = 10;     % s   (P2 waits while sump fills; firmware = 60 s)
CASE1_MAX_TIMEOUT = 300;   % s   (cfgCase1 = 300 s = 5 min fallback)

%% ---- Case 1 Flow-Stability Trigger (firmware values) ----
C1_FLOW_STABLE_MIN   = 1.50;   % L/min  (minimum to be "established")
C1_FLOW_STABLE_DELTA = 0.25;   % L/min  (max variation for stability)
C1_STABLE_SAMPLES    = 8;      % consecutive samples needed
C1_CHECK_INTERVAL    = 0.5;    % s      (DATA_INTERVAL_MS = 500 ms)
C1_TRANSITION_WARN   = 5;      % s      (5 s warning before Case 2)
C1_DRY_FALLBACK      = 120;    % s      (bench-test fallback timeout)

%% ---- Case 2 Control Parameters ----
CASE2_ALL_DUTY      = 100;     % %   (all three pumps at 100 %)
CASE2_VALVE_DELAY   = 5;       % s   (C2_VALVE_DELAY_MS = 5000 ms)
CASE2_MAX_TIMEOUT   = 75;      % s   (C2_MAX_TIMEOUT_MS = 75000 ms)

%% ---- Case 2 Flush-Volume Targets (FT-01 closed-loop shutdown) ----
C2_FLUSH_TARGET_L = 4.20;   % L   (nominal flush tank capacity)
C2_FLUSH_MAX_L    = 4.50;   % L   (upper cutoff limit)
C2_LOW_FLOW_THRESH = 0.35;  % L/min  (flow settling threshold)

%% ---- Process / Pipe Parameters (from problem statement) ----
PIPE_DIAMETER   = 0.008;    % m    (8 mm)
PIPE_AREA       = pi/4 * PIPE_DIAMETER^2;   % m^2  (50.27 mm^2)
FLUID_DENSITY   = 1000;     % kg/m^3
FLUID_VISCOSITY = 1e-3;     % Pa.s
TARGET_FLOW_LPM = 3.0;      % L/min (nominal challenge target)

%% ---- PWM / Hardware (reference only, not used in Simulink) ----
PWM_FREQ = 20000;   % Hz
PWM_BITS = 8;        % 8-bit resolution (0-255)

%% ---- Simulation Settings ----
SIM_TIME      = 250;     % s   (total simulation duration)
SIM_STEP      = 0.001;   % s   (fixed-step Euler integration)
SWITCH_ON_TIME = 2;      % s   (ON/OFF switch pressed at t = 2 s)
BV_OPEN_TIME   = 5;      % s   (ball valve opened early; P3 duty = 0 during Case 1)

%% ---- External Fluid Disturbance (sump) ----
%  Simulates sudden introduction of external fluid into the sump
%  to demonstrate the float-switch level protection in Case 1.
DIST_START_TIME = 90;     % s    (disturbance begins)
DIST_RATE       = 10;     % L/min (inflow rate)
DIST_DURATION   = 25;     % s    (duration of external fluid event)

fprintf('LAM Stage 2 parameters loaded.\n');
