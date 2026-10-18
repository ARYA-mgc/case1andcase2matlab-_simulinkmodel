# LAM Research Challenge 3.0 — Stage 2: Digital Twin & Industrial Automation

> **P&ID Drawing PID-001: Automated Chemical Distribution, Line Flush & Sump Protection System**  
> Complete Hardware-in-the-Loop (HIL) Simulink Digital Twin, Embedded ESP32 Automation Controller Firmware, and Hydrodynamic Process Analytics.

---

## 📌 Table of Contents
1. [Executive Summary](#executive-summary)
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
6. [Repository Files & Explanations](#repository-files--explanations)
7. [Getting Started (Run in MATLAB)](#getting-started-run-in-matlab)
8. [Git Instructions (Pushing to GitHub)](#git-instructions-pushing-to-github)

---

## Executive Summary

In high-precision semiconductor fab environments (such as LAM Research chemical delivery systems), precise chemical dosing, line flushing, and sump overflow protection are critical to wafer yield and cleanroom safety.

This project delivers a **full-scale Industrial Digital Twin** for **LAM Research Challenge 3.0 (Stage 2)**:
* **Physics-Based Hydraulic Model**: Models conservation of mass across three fluid vessels, pump motor characteristics, valve gating, and piping hydrodynamics ($8\text{ mm}$ lines, Reynolds number $Re \approx 8000$, turbulent flow).
* **Firmware-Accurate Embedded Control**: Full embedded state machine matching ESP32 C++ firmware (`lam_stage2.ino`) with flow-rate stabilization checks, Schmitt-trigger float switch sump protection, and closed-loop volumetric flush shutdown.
* **Professional Engineering Architecture**: 100% clean, standard black-and-white Simulink design with 4 modular subsystems, zero crossing wires, and no dangling tags.

---

## Process Flow & P&ID Drawing (PID-001)

The system strictly adheres to the engineering process flow schematic shown below:

![P&ID Process Flow Schematic](images/pid_drawing_pid001.png)

### Key Hydraulic Components:
| Tag | Component | Description | Specification |
| :--- | :--- | :--- | :--- |
| **T-01** | Process Supply Tank | Primary process fluid reservoir | $10.0\text{ L}$ capacity ($8.0\text{ L}$ initial fill) |
| **OV-01** | Solenoid Valve | Electronic shutoff valve on process line `PW-1` | 2-position solenoid (Open / Closed) |
| **T-02** | Flush Tank | Dedicated DI water / solvent flush reservoir | $4.2\text{ L}$ capacity ($4.2\text{ L}$ initial fill) |
| **BV-01** | Manual Ball Valve | Manual isolation valve on flush line `FW-2` | Quarter-turn ball valve ($100\%$ open) |
| **P-03** | Flush Pump | DC pump delivering flush solvent into tee `TE-01` | $Q_{\max} = 5.0\text{ L/min}$, PWM controlled |
| **TE-01** | Pipe Tee Junction | Connects process line `PW-2` and flush line `PW-3` | Standard $8\text{ mm}$ hydraulic tee |
| **P-01** | Process Feed Pump | Pulls from `TE-01` and discharges into sump `S-01` | $Q_{\max} = 6.0\text{ L/min}$ ($3.0\text{ L/min}$ at $50\%$ duty) |
| **S-01** | Collection Sump | Intermediate buffer vessel | $4.2\text{ L}$ capacity ($0.5\text{ L}$ initial fill) |
| **FS-01** | Sump Float Switch | Dual-threshold liquid level sensor with hysteresis | $3.5\text{ L}$ High Trip / $2.5\text{ L}$ Low Reset |
| **P-02** | Recirculation Pump | Draws from sump bottom line `PW-5` into return loop | $Q_{\max} = 4.5\text{ L/min}$, PWM controlled |
| **BV-02** | Manual Ball Valve | Isolation valve on return line `PW-6` | Quarter-turn ball valve ($100\%$ open) |
| **FT-01** | Turbine Flow Sensor | In-line pulse flow transmitter ($5266\text{ pulses/L}$) | Passthrough reading with digital totalizer |

---

## Simulink Digital Twin Architecture

The model [`lam_stage2_system.mdl`](lam_stage2_system.mdl) is structured hierarchically into 4 modular subsystems.

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

* **Signal Flow**: 
  1. Operator commands flow from `HMI_Operator_Inputs` to `ESP32_Automation_Controller`.
  2. The controller computes actuator PWMs and valve states, passing them to `Hydraulic_Process_Plant_PID001`.
  3. Physical plant sensor signals flow back to the controller via closed feedback loop (`Sensor_Feedback`).
  4. Real-time telemetry, actuator duties, and state codes feed directly into `SCADA_Monitoring_and_Scopes`.

---

### Subsystem 1: HMI Operator Inputs

![HMI Operator Inputs](images/simulink_02_hmi_operator_inputs.png)

* **`Rig_Push_Button`**: Step input representing the hardware push button pressed at $t = 1.0\text{ s}$ to initiate the automated sequence.
* **`Flush_Ball_Valve_BV01`**: Manual ball valve state for line flush readiness.
* **`Disturbance_Valve`**: Simulates sudden introduction of external liquid into the sump at $t = 90\text{ s}$ ($10\text{ L/min}$ for $25\text{ s}$) to test overflow protection.
* **`Master_Clock`**: System clock providing elapsed simulation time.
* **`Mux_HMI`**: Packs the 4 operator signals into the unified bus `HMI_Cmds`.

---

### Subsystem 2: Embedded ESP32 Automation Controller

![ESP32 Automation Controller](images/simulink_03_esp32_controller.png)

* **Inputs**:
  - `HMI_Cmds`: Operator start command, valve states, and clock.
  - `Sensor_Feedback`: Sump float switch state, FT-01 flow rate, and cumulative totalizer volume.
* **`Embedded_FSM_Logic`**: High-performance Interpreted MATLAB Function executing firmware logic (`lam_esp32_controller.m`).
* **Outputs**:
  - `Actuator_Commands` (Bus): P1 duty ($0\text{--}100\%$), P2 duty ($0\text{--}100\%$), P3 duty ($0\text{--}100\%$), and OV-01 Solenoid command ($0$ or $1$).
  - `State_Code`: Current operational state ($0\text{ to }8$) sent to SCADA.

---

### Subsystem 3: Hydraulic Process Plant (P&ID PID-001)

![Hydraulic Process Plant](images/simulink_04_hydraulic_plant_pid001.png)

This subsystem implements the exact physical flow loop of P&ID Drawing PID-001:
* **Flush Line Branch (Top)**:
  - `T-02_Flush_Tank_4p2L`: Integrates outflow; drains as flush pump operates.
  - `BV-01_Manual_Valve`: Multiplies available flush solvent by valve position.
  - `P-03_Flush_Pump`: Delivers flush fluid into `TE-01_Tee_Junction`.
* **Process Chemical Branch (Middle)**:
  - `T-01_10L_Process`: $10\text{ L}$ reservoir; mass balance: $\frac{dV}{dt} = \frac{Q_{\text{return}} - Q_{\text{feed}}}{60}$.
  - `OV-01_Solenoid_Valve`: Electronic shutoff valve.
  - `TE-01_Tee_Junction`: Adds process fluid and flush fluid.
  - `P-01_Feed_Pump`: Primary process pump discharging into the sump.
  - `S-01_Sump_4p2L`: Buffer vessel; net flow: $\frac{dV}{dt} = \frac{Q_{\text{in}} + Q_{\text{dist}} - Q_{\text{out}}}{60}$.
  - `FS-01_Float_Switch`: Relay block modeling Schmitt-trigger hysteresis ($3.5\text{ L}$ trip, $2.5\text{ L}$ reset).
* **Recirculation Return Branch (Bottom)**:
  - `P-02_Recirc_Pump`: Draws from sump bottom line `PW-5`.
  - `BV-02_Manual_Valve`: Return loop isolation valve.
  - `FT-01_Flow_Transmitter`: In-line turbine flow meter sending fluid back into `T-01`.
* **`Mux_Telemetry`**: Bundles all tank levels, flow rates, and sensor flags into `Sensor_Feedback`.

---

### Subsystem 4: SCADA Monitoring, Scopes & Analytics

![SCADA Monitoring & Scopes](images/simulink_05_scada_monitoring_scopes.png)

* **Hydrodynamics Computer**: Continuously computes pipeline fluid mechanics:
  $$\text{Velocity: } v = \frac{Q}{A} = \frac{Q_{\text{Lpm}} / 60 / 1000}{\frac{\pi}{4} D^2} \quad [\text{m/s}]$$
  $$\text{Reynolds Number: } Re = \frac{\rho \cdot v \cdot D}{\mu} \approx 8000 \cdot v$$
* **Digital Totalizer**: Integrates flow through FT-01 to compute cumulative transferred volume.
* **7 Live Digital Displays**:
  1. `Disp_10L_Tank_L`: T-01 level in Liters.
  2. `Disp_Sump_Vessel_L`: S-01 Sump level in Liters.
  3. `Disp_Flush_Tank_L`: T-02 Flush tank level in Liters.
  4. `Disp_FT01_Flow_Lpm`: Instantaneous flow in L/min.
  5. `Disp_Cumulative_Vol_L`: Cumulative volume in Liters.
  6. `Disp_FSM_State_Code`: Current active state ($0\text{--}8$).
  7. `Disp_Reynolds_Number`: Dimensionless flow regime indicator.
* **5 Dedicated Scopes & To Workspace Data Loggers**:
  - `Scope_Process_Tanks` / `Save_Tanks` $\rightarrow$ `tank_levels`
  - `Scope_Pump_Duties` / `Save_Duties` $\rightarrow$ `pump_duties`
  - `Scope_Flow_Sensor_FT01` / `Save_FT01` $\rightarrow$ `ft01_flow`
  - `Save_TotalVol` $\rightarrow$ `total_volume`
  - `Scope_Automation_State` / `Save_State` $\rightarrow$ `system_state`
  - `Scope_Reynolds_Number`

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

Simulation executed with fixed-step discrete solver ($\Delta t = 1.0\text{ ms}$, duration $T = 250\text{ s}$).

### Figure 1: Tank Levels & Mass Conservation
Shows volume conservation across all three vessels. In Case 1, Sump level remains tightly bounded between $1.7\text{ L}$ and $3.5\text{ L}$. At $t = 90\text{ s}$, an external disturbance causes the sump level to rise; `FS-01` trips at $3.5\text{ L}$, pauses `P-01`, and `P-02` rapidly drains the sump back to $2.5\text{ L}$ before resuming. In Case 2, Flush Tank `T-02` smoothly discharges its $4.2\text{ L}$ charge.

![Tank Levels](images/fig1_tank_levels.png)

### Figure 2: Dynamic Flow Profiles & Regulation
Illustrates process feed rate ($3.0\text{ L/min}$ during Case 1), FT-01 recirculation flow, and the high-speed flush flow during Case 2 reaching $5.0\text{ L/min}$.

![Flow Rates](images/fig2_flow_rates.png)

### Figure 3: Pump PWM Duty Cycles & Valve States
Shows actuator sequencing: P-01 ($50\%$), P-02 ($100\%$), OV-01 Solenoid (Open), the disturbance trip response, valve settling, and all pumps ramping to $100\%$ during the Case 2 flush.

![Pump Duties & Valves](images/fig3_pump_duties_valves.png)

### Figure 4: FSM Automation Trajectory
Step-by-step state code progression demonstrating autonomous transition through all 9 operational states without operator intervention.

![FSM Trajectory](images/fig4_state_trajectory.png)

### Figure 5: Totalizer Cumulative Volume & Cutoff
Cumulative volumetric totalizer tracking fluid through `FT-01`. Shows linear accumulation during Case 1, followed by precise automated cutoff when the Case 2 flush volume reaches the target $4.20\text{ L}$ ($4.33\text{ L}$ including piping hold-up, well below the $4.50\text{ L}$ ceiling).

![Total Volume](images/fig5_total_volume.png)

### Figure 6: Fluid Velocity & Reynolds Number Dynamics
Fluid mechanics analytics: line velocity reaches $0.99\text{ m/s}$ in Case 1 and $1.5\text{ m/s}$ in Case 2. Reynolds number maintains $Re \approx 8000$ to $12000$, ensuring fully turbulent cleaning flow through the $8\text{ mm}$ line.

![Fluid Dynamics](images/fig6_fluid_dynamics.png)

---

## Repository Files & Explanations

| File | Purpose / Role |
| :--- | :--- |
| **`lam_stage2_system.mdl`** | **Primary Simulink Digital Twin Model**. Contains the 4 modular subsystems, clean black & white styling, and P&ID flow loop. |
| **`lam_system_params.m`** | **System Parameters Script**. Defines tank capacities, pump flow ratings, valve timings, sensor thresholds, and pipe diameters in the base workspace. |
| **`lam_esp32_controller.m`** | **Embedded Firmware Engine**. Pure MATLAB function implementing the 9-state finite state machine with timing delays and float switch protection. |
| **`lam_controller_wrapper.m`** | **Simulink Block Interface**. Formats bus vector inputs and outputs between Simulink and `lam_esp32_controller.m`. |
| **`run_lam_simulation.m`** | **Automated Test & Plotting Runner**. Runs the simulation, extracts logged telemetry, generates all 6 publication figures, and prints an engineering KPI report. |
| **`lam_plant_controller.m`** | **Discrete State-Space Engine**. Standalone script simulating both plant and controller without requiring Simulink for rapid batch verification. |
| **`build_clean_pid_model.py`** | **Model Generator Utility**. Python script that regenerates `lam_stage2_system.mdl` with pure black-and-white standard layout. |
| **`build_human_pid_model.py`** | **Source Definition of Clean Model**. Complete ASCII definition of the 4 subsystems and clean P&ID routing. |
| **`.gitignore`** | **Git Ignore File**. Prevents MATLAB compilation caches (`*.slxc`), autosaves (`*.asv`), and temporary files from cluttering the repo. |
| **`images/`** | **Documentation Assets**. Contains the official P&ID drawing, all 5 Simulink subsystem screenshots, and all 6 simulation results figures. |

---

## Getting Started (Run in MATLAB)

### Prerequisites
* MATLAB R2020a through R2024b (or newer)
* Simulink

### Quick Execution
1. Open MATLAB and navigate to the project directory:
   ```matlab
   cd('d:\matalb_;lam');
   ```
2. Open the Simulink model:
   ```matlab
   open_system('lam_stage2_system.mdl');
   ```
3. Run the automated simulation and plot all 6 engineering figures:
   ```matlab
   run_lam_simulation;
   ```

---

## Git Instructions (Pushing to GitHub)

To push this repository to your GitHub account:

```bash
# 1. Open PowerShell or Command Prompt in the project folder
cd "d:\matalb_;lam"

# 2. Check the staged files
git status

# 3. Add all files
git add .

# 4. Create your initial commit
git commit -m "feat: complete LAM Stage 2 industrial digital twin and P&ID documentation"

# 5. Set the main branch
git branch -M main

# 6. Add your GitHub remote URL (replace with your personal GitHub URL)
git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git

# 7. Push to GitHub
git push -u origin main
```

---
*Developed for LAM Research Challenge 3.0 — Stage 2 Process Automation & Digital Twin Architecture.*
