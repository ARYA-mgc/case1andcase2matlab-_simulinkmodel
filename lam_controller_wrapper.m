function y = lam_controller_wrapper(u)
%#codegen
% Interface wrapper for ESP32 controller block in Simulink
% u: [switch_on; float_high; flow_lpm; total_vol; t_sim]
sw         = u(1);
float_high = u(2);
flow_lpm   = u(3);
total_vol  = u(4);
t_sim      = u(5);

[p1, p2, p3, ov01, st, fvol] = ...
    lam_esp32_controller(sw, float_high, flow_lpm, total_vol, t_sim);

y = [p1; p2; p3; ov01; st; fvol];
end
