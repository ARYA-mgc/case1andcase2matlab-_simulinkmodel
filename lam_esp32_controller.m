function [p1_duty, p2_duty, p3_duty, ov01_cmd, fsm_state, flush_vol] = ...
    lam_esp32_controller(switch_on, float_high, flow_lpm, total_vol, t_sim)
%#codegen
%% =========================================================================
%  LAM Research Challenge 3.0 - Stage 2
%  Pure Automation Controller (ESP32 Firmware FSM Engine)
%  =========================================================================
%  This block implements strictly the embedded control logic:
%    - Sump fill delay timer (10s)
%    - Flow stability verification (8 samples at 500ms intervals, +/-0.25 L/m)
%    - Sump float switch alert protection (pause P1, drain with P2)
%    - 5s operator transition warning
%    - 5s valve settling delay (OV-01 closed, pumps quiet)
%    - Case 2 closed-loop flush cutoff (4.20 - 4.50 L target via FT-01)
%  =========================================================================

persistent state state_start
persistent p2_started float_triggered p1_restarted p1_restarted_at
persistent last_stable_q c1_stable_count last_stable_check
persistent c1_flow_stable c1_trans_at c1_trans_warned
persistent c2_p3_started c2_start_vol c2_low_flow_since

if isempty(state)
    state              = 0;       % ST_IDLE
    state_start        = 0.0;
    p2_started         = false;
    float_triggered    = false;
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
end

%% Calibration & Timing Thresholds
C1_P1_DUTY         = 50.0;  % %
C1_P2_DUTY         = 100.0; % %
SUMP_FILL_DELAY    = 10.0;  % s
C1_MAX_TIMEOUT     = 300.0; % s
C1_FLOW_MIN        = 1.50;  % L/min
C1_FLOW_DELTA      = 0.25;  % L/min
C1_STABLE_REQ      = 8;     % samples
C1_DRY_FALLBACK    = 120.0; % s
C1_WARN_TIME       = 5.0;   % s

C2_DUTY            = 100.0; % %
C2_VALVE_DELAY     = 5.0;   % s
C2_MAX_TIMEOUT     = 75.0;  % s
C2_TARGET_L        = 4.20;  % L
C2_MAX_L           = 4.50;  % L
C2_LOW_Q_TH        = 0.35;  % L/min

switch_req = (switch_on > 0.5);
level_high = (float_high > 0.5);

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
            p2_started         = false;
            float_triggered    = false;
            p1_restarted       = false;
            p1_restarted_at    = 0.0;
            last_stable_q      = 0.0;
            c1_stable_count    = 0;
            last_stable_check  = t_sim;
            c1_flow_stable     = false;
            c1_trans_at        = 0.0;
            c1_trans_warned    = false;
        end

    case 1 % ST_CASE1_FILL (Sump Priming)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = C1_P1_DUTY;
            cmd_p2   = 0.0;
            cmd_p3   = 0.0;

            elapsed = t_sim - state_start;
            if elapsed >= SUMP_FILL_DELAY || level_high
                p2_started = true;
                state      = 2; % ST_CASE1_RUN
            end
        end

    case 2 % ST_CASE1_RUN (Process Recirculation)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            elapsed  = t_sim - state_start;

            if level_high
                float_triggered    = true;
                p1_restarted       = false;
                c1_flow_stable     = false;
                c1_stable_count    = 0;
                state              = 3; % ST_CASE1_FLOAT_PROT
                cmd_p1             = 0.0;
                cmd_p2             = C1_P2_DUTY;
            elseif elapsed >= C1_MAX_TIMEOUT
                state       = 6; % ST_CASE2_DELAY
                state_start = t_sim;
            else
                cmd_p1 = C1_P1_DUTY;
                cmd_p2 = C1_P2_DUTY;
            end
        end

    case 3 % ST_CASE1_FLOAT_PROT (Sump Level Alert)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = 0.0;        % Stop P1 immediately
            cmd_p2   = C1_P2_DUTY; % Drain sump with P2 at 100%

            if ~level_high
                p1_restarted       = true;
                p1_restarted_at    = t_sim;
                last_stable_q      = flow_lpm;
                c1_stable_count    = 0;
                last_stable_check  = t_sim;
                c1_flow_stable     = false;
                c1_trans_warned    = false;
                state              = 4; % ST_CASE1_STABILIZING
                cmd_p1             = C1_P1_DUTY;
            end
        end

    case 4 % ST_CASE1_STABILIZING (Verify Steady State)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = C1_P1_DUTY;
            cmd_p2   = C1_P2_DUTY;

            if level_high
                state = 3;
            else
                time_since_restart = t_sim - p1_restarted_at;

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

                if ~c1_flow_stable && time_since_restart >= C1_DRY_FALLBACK
                    state       = 6; % ST_CASE2_DELAY
                    state_start = t_sim;
                end
            end
        end

    case 5 % ST_CASE1_TRANSITION_WARN (5s Warning Countdown)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 1.0;
            cmd_p1   = C1_P1_DUTY;
            cmd_p2   = C1_P2_DUTY;

            if t_sim >= c1_trans_at
                state       = 6; % Case 2 Delay
                state_start = t_sim;
            end
        end

    case 6 % ST_CASE2_DELAY (Isolate Tank 1, 5s Valve Delay)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 0.0; % OV-01 CLOSED
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

    case 7 % ST_CASE2_FLUSH (Active Flush Sequence)
        if ~switch_req
            state = 0;
        else
            cmd_ov01 = 0.0;
            cmd_p1   = C2_DUTY;
            cmd_p2   = C2_DUTY;
            cmd_p3   = C2_DUTY;

            flush_l = total_vol - c2_start_vol;
            elapsed = t_sim - state_start;

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

            target_reached      = (flush_l >= C2_TARGET_L && flow_lpm < C2_LOW_Q_TH);
            upper_limit_reached = (flush_l >= C2_MAX_L);
            timeout_failsafe    = (elapsed >= C2_MAX_TIMEOUT);

            if empty_at_target || target_reached || upper_limit_reached || timeout_failsafe
                state    = 8; % ST_DONE
                cmd_p1   = 0.0;
                cmd_p2   = 0.0;
                cmd_p3   = 0.0;
                cmd_ov01 = 0.0;
            end
        end

    case 8 % ST_DONE (Safe Shutdown)
        cmd_p1   = 0.0;
        cmd_p2   = 0.0;
        cmd_p3   = 0.0;
        cmd_ov01 = 0.0;

        if ~switch_req
            state = 0;
        end

    otherwise
        state = 0;
end

p1_duty   = cmd_p1;
p2_duty   = cmd_p2;
p3_duty   = cmd_p3;
ov01_cmd  = cmd_ov01;
fsm_state = double(state);

flush_cur = 0.0;
if state >= 6
    flush_cur = max(0.0, total_vol - c2_start_vol);
end
flush_vol = flush_cur;

end
