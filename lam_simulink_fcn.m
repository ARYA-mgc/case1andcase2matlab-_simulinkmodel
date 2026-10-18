function y = lam_simulink_fcn(u)
%#codegen
%% =========================================================================
%  LAM Research Challenge 3.0 - Stage 2: Simulink Vector Interface
%  =========================================================================
%  Interface wrapper bridging Simulink MATLAB Fcn block with the
%  comprehensive lam_plant_controller state machine and plant dynamics.
%
%  Input vector u (4x1):
%    u(1) : switch_on   (0 = OFF, 1 = ON)
%    u(2) : bv_open     (0 = Closed, 1 = Open)
%    u(3) : q_dist      (External disturbance flow, L/min)
%    u(4) : t_sim       (Simulation time, seconds)
%
%  Output vector y (15x1):
%    y(1:3)   : tank_levels   [V_10L; V_sump; V_flush] (Liters)
%    y(4:6)   : pump_flows    [Q_p1; Q_p2; Q_p3] (L/min)
%    y(7)     : ft01_flow     (L/min)
%    y(8)     : total_volume  (Liters)
%    y(9)     : system_state  (0 to 8)
%    y(10:12) : pump_duties   [duty_p1; duty_p2; duty_p3] (%)
%    y(13:15) : status_signals [ov01_valve; float_high; flush_volume]
%  =========================================================================

sw     = u(1);
bv     = u(2);
q_dist = u(3);
t_sim  = u(4);

[tanks, flows, q_ft, tot, st, duties, stats] = ...
    lam_plant_controller(sw, bv, q_dist, t_sim);

y = [tanks(:); flows(:); q_ft; tot; st; duties(:); stats(:)];

end
