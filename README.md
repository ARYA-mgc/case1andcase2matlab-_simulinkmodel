# LAM Research Challenge 3.0 - Stage 2: Digital Twin & Industrial Automation

> **P&ID Drawing PID-001: Automated Chemical Distribution, Line Flush & Sump Protection System**  
> Hardware-in-the-Loop (HIL) Simulink Digital Twin, Embedded ESP32 Automation Controller Firmware, and Hydrodynamic Process Analytics.

---

## Table of Contents
1. [Overview](#overview)
2. [Process Flow & P&ID Drawing (PID-001)](#process-flow--pid-drawing-pid-001)
3. [Simulink Digital Twin Architecture](#simulink-digital-twin-architecture)
   - [Top-Level Architecture Overview](#top-level-architecture-overview)
   - [Subsystem 1: HMI Operator Inputs](#subsystem-1-hmi-operator-inputs)
   - [Subsystem 2: Embedded ESP32 Automation Controller](#subsystem-2-embedded-esp32-automation-controller)
   - [Subsystem 3: Hydraulic Process Plant (P&ID PID-001)](#subsystem-3-hydraulic-process-plant-pid-001)
   - [Subsystem 4: SCADA Monitoring, Scopes & Analytics](#subsystem-4-scada-monitoring-scopes--analytics)
4. [Embedded Controller Firmware State Machine (FSM)](#embedded-controller-firmware-state-machine-fsm)
5. [Simulation Results & Verification](#simulation-results--verification)
   - [Figure 1: Tank Levels & Mass Conservation](#figure-1-tank-levels--mass-conservation)
   - [Figure 2: Dynamic Flow Profiles & Regulation](#figure-2-dynamic-flow-profiles--regulation)
   - [Figure 3: Pump PWM Duty Cycles & Valve States](#figure-3-pump-pwm-duty-cycles--valve-states)
   - [Figure 4: FSM Automation Trajectory](#figure-4-fsm-automation-trajectory)
   - [Figure 5: Totalizer Cumulative Volume & Cutoff](#figure-5-totalizer-cumulative-volume--cutoff)
   - [Figure 6: Fluid Velocity & Reynolds Number Dynamics](#figure-6-fluid-velocity--reynolds-number-dynamics)
6. [Repository Files & Descriptions](#repository-files--descriptions)
7. [Running the Model in MATLAB](#running-the-model-in-matlab)

---

## Overview

In semiconductor wafer manufacturing, chemical distribution rigs require precise dosing, controlled line flushing, and rapid sump overflow protection to prevent tool contamination and cleanroom safety hazards.

This repository contains the dynamic simulation model and embedded control logic developed for the **LAM Research Challenge 3.0 (Stage 2)**:
* **Hydraulic System Simulation**: Solves conservation of mass and pressure-driven flow dynamics across three fluid vessels, pump motor curves, solenoid valve transitions, and pipe friction losses ($8\text{ mm}$ inner diameter lines, operating at turbulent conditions with $Re \approx 8000$).
* **Firmware Implementation**: Incorporates the complete 9-state finite state machine (FSM) matching the ESP32 microcontroller C++ firmware (`lam_stage2.ino`), including digital filtering on the turbine flow meter, float switch hysteresis, and closed-loop volumetric cutoff.
* **Simulink Model Structure**: Organized into four clean subsystems using standard, unstyled Simulink blocks and straight bus connections for clarity and ease of maintenance.

---

## Process Flow & P&ID Drawing (PID-001)

The simulation architecture mirrors the physical piping and instrumentation diagram (PID-001):

![P&ID Process Flow Schematic](images/pid_drawing_pid001.png)

### Equipment Specifications:
| Tag | Component | Function | Operating Parameters |
| :--- | :--- | :--- | :--- |
| **T-01** | Process Supply Tank | Chemical reservoir | $10.0\text{ L}$ capacity, starting volume $8.0\text{ L}$ |
| **OV-01** | Solenoid Valve | Electronic shutoff valve on process line `PW-1` | 2-position solenoid (Open / Closed) |
| **T-02** | Flush Tank | Dedicated flush solvent reservoir | $4.2\text{ L}$ capacity, starting volume $4.2\text{ L}$ |
| **BV-01** | Manual Ball Valve | Isolation valve on flush line `FW-2` | Quarter-turn manual valve ($100\%$ open) |
| **P-03** | Flush Pump | DC motor-driven pump delivering flush fluid | $Q_{\max} = 5.0\text{ L/min}$, PWM controlled |
| **TE-01** | Pipe Tee Junction | Merges process line `PW-2` with flush line `PW-3` | Standard $8\text{ mm}$ hydraulic junction |
| **P-01** | Process Feed Pump | Pulls from `TE-01` and discharges into sump `S-01` | $Q_{\max} = 6.0\text{ L/min}$ ($3.0\text{ L/min}$ target at $50\%$ duty) |
| **S-01** | Collection Sump | Intermediate buffer vessel | $4.2\text{ L}$ capacity, starting volume $0.5\text{ L}$ |
| **FS-01** | Sump Float Switch | Dual-threshold level sensor with Schmitt hysteresis | $3.5\text{ L}$ High Trip / $2.5\text{ L}$ Low Reset |
| **P-02** | Recirculation Pump | Pulls from sump drain line `PW-5` to recirculation line | $Q_{\max} = 4.5\text{ L/min}$, PWM controlled |
| **BV-02** | Manual Ball Valve | Return line isolation valve | Quarter-turn manual valve ($100\%$ open) |
| **FT-01** | Flow Transmitter | Turbine pulse flow meter ($5266\text{ pulses/L}$) | Passthrough reading with digital volume totalizer |

---

## Simulink Digital Twin Architecture

The model [`lam_stage2_system.mdl`](lam_stage2_system.mdl) is constructed using four decoupled subsystems connected by straight bus lines without crossing signals or floating tags.

### Top-Level Architecture Overview

![Simulink Top-Level Architecture](images/simulink_01_top_level_architecture.png)

```text
+-----------------------+                 +-----------------------------+                 +--------------------------------+                 +-------------------------------+
|                       |   HMI_Cmds      |                             | Actuator_Cmds   |                                | Plant_Telemetry |                               |
|  HMI_Operator_Inputs  |---------------->| ESP32_Automation_Controller |---------------->| Hydraulic_Process_Plant_PID001 |---------------->|  SCADA_Monitoring_and_Scopes  |
|                       |                 |                             |                 |                                |                 |                               |
+-----------------------+                 +--------------+--------------+                 +---------------+----------------+                 +---------------+---------------+
                                                         ^                                                |                                                  ^
                                                         |                                                | Sensor_Feedback                                  | State_Code
                                                         +------------------------------------------------+                                                  |
                                                         |                                                                                                   |
                                                         +---------------------------------------------------------------------------------------------------+
```

* **Signal Routing**:
  1. Operator commands are packed into `HMI_Cmds` and routed to the `ESP32_Automation_Controller`.
  2. The controller evaluates the current state and passes `Actuator_Commands` (pump PWMs and valve gating signals) to `Hydraulic_Process_Plant_PID001`.
  3. Sensor telemetry (`Sensor_Feedback`) is fed back to the controller to close the loop on flow rate and sump liquid level.
  4. Both telemetry and internal state codes are broadcast to `SCADA_Monitoring_and_Scopes` for logging and visualization.

---

### Subsystem 1: HMI Operator Inputs

![HMI Operator Inputs](images/simulink_02_hmi_operator_inputs.png)

* **`Rig_Push_Button`**: Generates a step command at $t = 1.0\text{ s}$ representing the hardware operator start switch.
* **`Flush_Ball_Valve_BV01`**: Manual valve state confirmation flag.
* **`Disturbance_Valve`**: Step pulse introducing external fluid ($10\text{ L/min}$ for $25\text{ s}$ starting at $t = 90\text{ s}$) to test the automatic sump high-level interlock.
* **`Master_Clock`**: System simulation time source.
* **`Mux_HMI`**: Combines operator inputs into the 4-signal `HMI_Cmds` bus.

---

### Subsystem 2: Embedded ESP32 Automation Controller

![ESP32 Automation Controller](images/simulink_03_esp32_controller.png)

* **Inputs**:
  - `HMI_Cmds`: Operator start signal, valve statuses, and simulation clock.
  - `Sensor_Feedback`: Sump float switch boolean, FT-01 measured flow rate, and cumulative volume.
* **`Embedded_FSM_Logic`**: Executes the discrete-time firmware state machine via [`lam_esp32_controller.m`](lam_esp32_controller.m).
* **Outputs**:
  - `Actuator_Commands`: Multiplexed bus containing P-01 duty ($0\text{--}100\%$), P-02 duty ($0\text{--}100\%$), P-03 duty ($0\text{--}100\%$), and OV-01 solenoid state ($0$ or $1$).
  - `State_Code`: Current integer state ($0\text{ to }8$) routed to the SCADA subsystem.

---

### Subsystem 3: Hydraulic Process Plant (P&ID PID-001)

![Hydraulic Process Plant](images/simulink_04_hydraulic_plant_pid001.png)

This subsystem implements the full hydraulic loop defined in P&ID Drawing PID-001:
* **Flush Line Branch (Top)**:
  - `T-02_Flush_Tank_4p2L`: Integrator modeling inventory drawdown as P-03 operates.
  - `BV-01_Manual_Valve`: Multiplies available solvent head by valve position.
  - `P-03_Flush_Pump`: Delivers flush solvent into `TE-01_Tee_Junction`.
* **Process Chemical Branch (Middle)**:
  - `T-01_10L_Process`: Primary vessel mass balance: $\frac{dV}{dt} = \frac{Q_{\text{return}} - Q_{\text{feed}}}{60}$.
  - `OV-01_Solenoid_Valve`: Two-way isolation valve.
  - `TE-01_Tee_Junction`: Flow convergence point for process fluid and flush solvent.
  - `P-01_Feed_Pump`: Feed pump discharging into the collection sump.
  - `S-01_Sump_4p2L`: Buffer vessel mass balance: $\frac{dV}{dt} = \frac{Q_{\text{feed}} + Q_{\text{dist}} - Q_{\text{recirc}}}{60}$.
  - `FS-01_Float_Switch`: Relay block modeling physical float switch hysteresis ($3.5\text{ L}$ trip, $2.5\text{ L}$ reset).
* **Recirculation Return Branch (Bottom)**:
  - `P-02_Recirc_Pump`: Recirculation pump pulling from line `PW-5`.
  - `BV-02_Manual_Valve`: Manual return line valve.
  - `FT-01_Flow_Transmitter`: Flow sensor inline with return line `PW-8` returning to `T-01`.
* **`Mux_Telemetry`**: Combines tank volumes, line flow rates, and sensor flags into `Sensor_Feedback`.

---

### Subsystem 4: SCADA Monitoring, Scopes & Analytics

![SCADA Monitoring & Scopes](images/simulink_05_scada_monitoring_scopes.png)

* **Hydrodynamics Computer**: Computes continuous physical line metrics:
  $$\text{Velocity: } v = \frac{Q}{A} = \frac{Q_{\text{Lpm}} / 60 / 1000}{\frac{\pi}{4} D^2} \quad [\text{m/s}]$$
  $$\text{Reynolds Number: } Re = \frac{\rho \cdot v \cdot D}{\mu} \approx 8000 \cdot v$$
* **Digital Totalizer**: Integrates flow through `FT-01` to determine net delivered volume.
* **Digital Readouts**:
  - `Disp_10L_Tank_L`: T-01 level ($L$).
  - `Disp_Sump_Vessel_L`: Sump level ($L$).
  - `Disp_Flush_Tank_L`: T-02 level ($L$).
  - `Disp_FT01_Flow_Lpm`: Instantaneous flow rate ($\text{L/min}$).
  - `Disp_Cumulative_Vol_L`: Integrated volume ($L$).
  - `Disp_FSM_State_Code`: Current operational state ($0\text{--}8$).
  - `Disp_Reynolds_Number`: Flow regime indicator.
* **Scopes & Data Loggers (`To Workspace`)**:
  - `tank_levels`: Matrix of volumes across all three tanks.
  - `pump_duties`: PWM duty cycles for P-01, P-02, and P-03.
  - `ft01_flow`: Time series of the flow transmitter signal.
  - `total_volume`: Cumulative volume output.
  - `system_state`: State machine trajectory over time.

---

## Embedded Controller Firmware State Machine (FSM)

The controller executes an industrial finite state machine with safety interlocks:

| State Code | State Name | Action / Condition | Actuator Configuration |
| :---: | :--- | :--- | :--- |
| `0` | **ST_IDLE** | Awaiting operator Start push button | All pumps OFF, OV-01 Closed |
| `1` | **ST_CASE1_FILL** | Sump priming delay ($10\text{ s}$) or until float trips | OV-01 Open, P1 at $50\%$, P2 OFF |
| `2` | **ST_CASE1_RUN** | Recirculation active; monitoring flow stability | OV-01 Open, P1 at $50\%$, P2 at $100\%$ |
| `3` | **ST_CASE1_ALERT** | Float switch tripped ($S\text{-}01 \ge 3.5\text{ L}$); pause P1, drain sump | OV-01 Open, P1 at $0\%$, P2 at $100\%$ |
| `4` | **ST_CASE1_STABLE** | Flow rate steady at $3.0 \pm 0.25\text{ L/min}$ for 8 checks | OV-01 Open, P1 at $50\%$, P2 at $100\%$ |
| `5` | **ST_TRANS_WARN** | $5\text{ s}$ operator audible/visual warning before flush | OV-01 Open, P1 at $50\%$, P2 at $100\%$ |
| `6` | **ST_SETTLE** | Valve transition settling delay ($5\text{ s}$) | OV-01 Closed, all pumps OFF |
| `7` | **ST_CASE2_FLUSH** | High-velocity flush; closed-loop cutoff at $4.20\text{ L}$ | OV-01 Closed, P1 at $100\%$, P2 at $100\%$, P3 at $100\%$ |
| `8` | **ST_COMPLETE** | System safe shutdown; process complete | All pumps OFF, OV-01 Closed |

---

## Simulation Results & Verification

The model was verified using a fixed-step discrete solver ($\Delta t = 1.0\text{ ms}$, duration $T = 250\text{ s}$).

### Figure 1: Tank Levels & Mass Conservation
Verifies volume conservation across all three vessels. In Case 1, Sump level remains bounded between $1.7\text{ L}$ and $3.5\text{ L}$. At $t = 90\text{ s}$, the disturbance causes the sump level to rise; `FS-01` trips at $3.5\text{ L}$, pauses `P-01`, and `P-02` drains the sump back to $2.5\text{ L}$ before feed flow resumes. In Case 2, Flush Tank `T-02` discharges its $4.2\text{ L}$ volume.

![Tank Levels](images/fig1_tank_levels.png)

### Figure 2: Dynamic Flow Profiles & Regulation
Shows process feed rate ($3.0\text{ L/min}$ during Case 1 steady state), FT-01 recirculation flow, and the high-speed flush flow during Case 2 reaching $5.0\text{ L/min}$.

![Flow Rates](images/fig2_flow_rates.png)

### Figure 3: Pump PWM Duty Cycles & Valve States
Illustrates actuator sequencing: P-01 ($50\%$), P-02 ($100\%$), OV-01 Solenoid (Open), the disturbance interlock response, valve settling, and all pumps operating at $100\%$ during the Case 2 flush.

![Pump Duties & Valves](images/fig3_pump_duties_valves.png)

### Figure 4: FSM Automation Trajectory
Step-by-step state code progression demonstrating autonomous transition through all 9 operational states.

![FSM Trajectory](images/fig4_state_trajectory.png)

### Figure 5: Totalizer Cumulative Volume & Cutoff
Cumulative volumetric totalizer tracking fluid through `FT-01`. Shows linear accumulation during Case 1, followed by automated cutoff when the Case 2 flush volume reaches the target $4.20\text{ L}$ ($4.33\text{ L}$ actual, safely below the $4.50\text{ L}$ maximum limit).

![Total Volume](images/fig5_total_volume.png)

### Figure 6: Fluid Velocity & Reynolds Number Dynamics
Pipeline velocity reaches $0.99\text{ m/s}$ in Case 1 and $1.5\text{ m/s}$ in Case 2. Reynolds number maintains $Re \approx 8000$ to $12000$, ensuring fully turbulent flow throughout the flush cycle.

![Fluid Dynamics](images/fig6_fluid_dynamics.png)

---

## Repository Files & Descriptions

| File | Description |
| :--- | :--- |
| **`lam_stage2_system.mdl`** | Primary Simulink Digital Twin Model containing the four modular subsystems. |
| **`lam_system_params.m`** | Physical and controller parameters script loaded into the MATLAB workspace. |
| **`lam_esp32_controller.m`** | Embedded firmware logic implementing the 9-state finite state machine. |
| **`lam_controller_wrapper.m`** | Signal bus interface wrapper between Simulink and `lam_esp32_controller.m`. |
| **`run_lam_simulation.m`** | Automated script to run the simulation and generate all 6 verification plots. |
| **`.gitignore`** | Excludes temporary MATLAB caches (`*.slxc`), autosaves, and backup files. |
| **`images/`** | Contains the P&ID drawing, all 5 subsystem screenshots, and simulation result figures. |

---

## Running the Model in MATLAB

### Prerequisites
* MATLAB R2020a through R2024b (or newer)
* Simulink

### Execution Steps
1. Navigate to the project directory:
   ```matlab
   cd('d:\matalb_;lam');
   ```
2. Open the Simulink model:
   ```matlab
   open_system('lam_stage2_system.mdl');
   ```
3. Run the automated test script to simulate and generate all figures:
   ```matlab
   run_lam_simulation;
   ```
