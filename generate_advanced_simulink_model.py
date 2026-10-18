import sys

def build_advanced_model():
    mdl = '''Model {
  Name                    "lam_stage2_system"
  Version                 8.5
  MdlSubVersion           0
  SavedCharacterEncoding  "UTF-8"
  GraphicalInterface {
    NumRootInports        0
    NumRootOutports       0
    ParameterArgumentNames  ""
    ComputedModelVersion  "3.0"
    NumModelReferences    0
    NumTestPointedSignals 0
  }
  ScopeRefreshTime        0.035000
  OverrideScopeRefreshTime on
  DisableAllScopes        off
  DataTypeOverride        "UseLocalSettings"
  MinMaxOverflowLogging   "UseLocalSettings"
  MinMaxOverflowArchiveMode "Overwrite"
  FPTRunName              "Run 1"
  MaxMDLFileLineLength    120
  Created                 "Sun Oct 18 2026"
  Creator                 "LAM Process Automation Engineer"
  UpdateHistory           "UpdateHistoryNever"
  ModifiedByFormat        "%<Auto>"
  ModifiedDateFormat      "%<Auto>"
  LastModifiedDate        "Sun Oct 18 2026"
  ModelVersionFormat      "3.%<AutoIncrement:1>"
  ConfigurationManager    "none"
  SampleTimeColors        off
  WideLines               on
  ShowLineDimensions      on
  ShowPortDataTypes       off
  ShowLoopsOnError        on
  ToolBar                 on
  StatusBar               on
  BrowserShowLibraryLinks off
  BrowserLookUnderMasks   off
  SimulationMode          "normal"
  Array {
    Type                  "Handle"
    Dimension             1
    Simulink.ConfigSet {
      $ObjectID              1
      Version                "1.14.3"
      Array {
        Type                  "Handle"
        Dimension             8
        Simulink.SolverCC {
          $ObjectID              2
          Version                "1.14.3"
          StartTime              "0.0"
          StopTime               "250.0"
          AbsTol                 "auto"
          FixedStep              "0.001"
          Solver                 "FixedStepDiscrete"
          SolverName             "FixedStepDiscrete"
        }
        Simulink.DataIOCC {
          $ObjectID              3
          Version                "1.14.3"
          SaveFormat             "Array"
          SaveOutput             on
          SaveTime               on
          TimeSaveName           "tout"
          OutputSaveName         "yout"
        }
        Simulink.OptimizationCC {
          $ObjectID              4
          Version                "1.14.3"
          BlockReduction         on
          BooleanDataType        on
        }
        Simulink.DebuggingCC {
          $ObjectID              5
          Version                "1.14.3"
        }
        Simulink.HardwareCC {
          $ObjectID              6
          Version                "1.14.3"
        }
        Simulink.ModelReferenceCC {
          $ObjectID              7
          Version                "1.14.3"
        }
        Simulink.SFSimCC {
          $ObjectID              8
          Version                "1.14.3"
        }
        Simulink.RTWCC {
          $ObjectID              9
          Version                "1.14.3"
        }
        PropName              "Components"
      }
      Name                    "Configuration"
      CurrentDlgPage          "Solver"
    }
    PropName              "ConfigurationSets"
  }
  Simulink.ConfigSet {
    $PropName               "ActiveConfigurationSet"
    $ObjectID              1
  }
  BlockDefaults {
    ForegroundColor         "black"
    BackgroundColor         "white"
    DropShadow              off
    NamePlacement           "normal"
    FontName                "Helvetica"
    FontSize                10
    FontWeight              "normal"
    FontAngle               "normal"
    ShowName                on
  }
  AnnotationDefaults {
    HorizontalAlignment     "center"
    VerticalAlignment       "middle"
    ForegroundColor         "black"
    BackgroundColor         "white"
    DropShadow              off
    FontName                "Helvetica"
    FontSize                10
    FontWeight              "normal"
  }
  LineDefaults {
    FontName                "Helvetica"
    FontSize                9
  }
  BlockParameterDefaults {
    Block {
      BlockType               Clock
      DisplayTime             off
      Decimation              "10"
    }
    Block {
      BlockType               Constant
      Value                   "1"
      VectorParams1D          on
      SamplingMode            "Sample based"
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: Inherit from 'Constant value'"
      LockScale               off
      SampleTime              "inf"
      FramePeriod             "inf"
    }
    Block {
      BlockType               Demux
      Outputs                 "4"
      DisplayOption           "none"
      BusSelectionMode        off
    }
    Block {
      BlockType               DiscretePulseGenerator
      PulseType               "Sample based"
      TimeSource              "Use simulation time"
      Amplitude               "1"
      Period                  "2"
      PulseWidth              "1"
      PhaseDelay              "0"
      SampleTime              "1"
      VectorParams1D          on
    }
    Block {
      BlockType               Display
      Format                  "short"
      Decimation              "10"
      Floating                off
      Lockdown                off
      SampleTime              "-1"
    }
    Block {
      BlockType               Gain
      Gain                    "1"
      Multiplication          "Element-wise(K.*u)"
      ParamDataTypeStr        "Inherit: Same as input"
      OutDataTypeStr          "Inherit: Same as input"
      SaturateOnIntegerOverflow on
      SampleTime              "-1"
    }
    Block {
      BlockType               Inport
      Port                    "1"
      OutputFunctionCall      off
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: auto"
      LockScale               off
      BusOutputAsStruct       off
      PortDimensions          "-1"
      VarSizeSig              "Inherit"
      SampleTime              "-1"
      SignalType              "auto"
      SamplingMode            "auto"
      LatchByDelayingOutsideSignal off
      LatchInputForFeedbackSignals off
      Interpolate             on
    }
    Block {
      BlockType               MATLABFcn
      MATLABFcn               "sin"
      OutputDimensions        "-1"
      OutputSignalType        "auto"
      Output1D                on
      SampleTime              "-1"
    }
    Block {
      BlockType               Mux
      Inputs                  "4"
      DisplayOption           "none"
      UseBusObject            off
      BusObject               "BusObject"
      NonVirtualBus           off
    }
    Block {
      BlockType               Outport
      Port                    "1"
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: auto"
      LockScale               off
      BusOutputAsStruct       off
      PortDimensions          "-1"
      VarSizeSig              "Inherit"
      SampleTime              "-1"
      SignalType              "auto"
      SamplingMode            "auto"
      SourceOfInitialOutputValue "Dialog"
      OutputWhenDisabled      "held"
      InitialOutput           "[]"
    }
    Block {
      BlockType               RateLimiter
      RisingSlewLimit         "1"
      FallingSlewLimit        "-1"
      SampleTimeMode          "continuous"
      InitialCondition        "0"
      LinearizeAsGain         on
    }
    Block {
      BlockType               Relay
      OnSwitchValue           "3.5"
      OffSwitchValue          "2.5"
      OnOutputValue           "1"
      OffOutputValue          "0"
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: All ports same datatype"
      LockScale               off
      InputProcessing         "Inherited"
      ZeroCross               on
      SampleTime              "-1"
    }
    Block {
      BlockType               Saturate
      UpperLimit              "100"
      LowerLimit              "0"
      LinearizeAsGain         on
      ZeroCross               on
      SampleTime              "-1"
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: Same as input"
      LockScale               off
      RndMeth                 "Floor"
    }
    Block {
      BlockType               Scope
      ModelBased              off
      TickLabels              "OneTimeTick"
      ZoomMode                "on"
      Grid                    "on"
      TimeRange               "auto"
      YMin                    "-5"
      YMax                    "5"
      SaveToWorkspace         off
      SaveName                "ScopeData"
      DataFormat              "Array"
      LimitDataPoints         on
      MaxDataPoints           "5000"
      Decimation              "1"
      SampleInput             off
      SampleTime              "-1"
    }
    Block {
      BlockType               Step
      Time                    "1"
      Before                  "0"
      After                   "1"
      SampleTime              "-1"
      VectorParams1D          on
      ZeroCross               on
    }
    Block {
      BlockType               SubSystem
      ShowPortLabels          "FromPortIcon"
      Permissions             "ReadWrite"
      PermitHierarchicalResolution "All"
      TreatAsAtomicUnit       off
      CheckFcnCallInpInsideContextMsg off
      SystemSampleTime        "-1"
      RTWFcnNameOpts          "Auto"
      RTWFileNameOpts         "Auto"
      FunctionInterfaceSpec   "void_void"
      RTWMemSecFuncInitTerm   "Inherit from model"
      RTWMemSecFuncExecute    "Inherit from model"
      RTWMemSecDataConstants  "Inherit from model"
      RTWMemSecDataInternal   "Inherit from model"
      RTWMemSecDataParameters "Inherit from model"
      SimViewingDevice        off
      DataTypeOverride        "UseLocalSettings"
      MinMaxOverflowLogging   "UseLocalSettings"
    }
    Block {
      BlockType               ToWorkspace
      VariableName            "simulink_output"
      MaxDataPoints           "inf"
      Decimation              "1"
      SampleTime              "-1"
      SaveFormat              "Array"
      FixptAsFi               off
      NumInputs               "1"
    }
  }
  System {
    Name                    "lam_stage2_system"
    Location                [10, 30, 1680, 1020]
    Open                    on
    ScreenColor             "white"
    ZoomFactor              "100"
    ReportName              "simulink-default.rpt"
    SIDHighWaterMark        "80"

    Annotation {
      SID                     "1"
      Name                    "LAM RESEARCH CHALLENGE 3.0 - STAGE 2 DIGITAL TWIN"
      Position                [850, 25, 850, 25]
      ForegroundColor         "navy"
      FontSize                16
      FontWeight              "bold"
    }
    Annotation {
      SID                     "2"
      Name                    "Industrial Automated Liquid Chemical Distribution, Dynamic Sump Protection & Closed-Loop Line Flush Rig"
      Position                [850, 48, 850, 48]
      ForegroundColor         "gray"
      FontSize                11
    }

    Block {
      BlockType               SubSystem
      Name                    "1_HMI_Operator_Console"
      SID                     "3"
      Ports                   [0, 4]
      Position                [50, 100, 220, 320]
      ForegroundColor         "blue"
      BackgroundColor         "lightBlue"
      System {
        Name                    "1_HMI_Operator_Console"
        Location                [50, 50, 750, 550]
        Open                    off
        Block {
          BlockType               Step
          Name                    "Push_Button_Switch_Run"
          SID                     "4"
          Position                [60, 50, 160, 90]
          Time                    "2.0"
          Before                  "0"
          After                   "1"
          SampleTime              "0.001"
        }
        Block {
          BlockType               Step
          Name                    "Manual_Ball_Valve_BV01"
          SID                     "5"
          Position                [60, 140, 160, 180]
          Time                    "5.0"
          Before                  "0"
          After                   "1"
          SampleTime              "0.001"
        }
        Block {
          BlockType               DiscretePulseGenerator
          Name                    "External_Disturbance_Injector"
          SID                     "6"
          Position                [60, 230, 160, 270]
          PulseType               "Time based"
          Amplitude               "10"
          Period                  "500"
          PulseWidth              "5"
          PhaseDelay              "90"
        }
        Block {
          BlockType               Clock
          Name                    "Master_Clock"
          SID                     "7"
          Position                [60, 320, 160, 360]
        }
        Block {
          BlockType               Outport
          Name                    "Switch_Run"
          SID                     "8"
          Position                [250, 60, 280, 80]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "BV01_Open"
          SID                     "9"
          Position                [250, 150, 280, 170]
          Port                    "2"
        }
        Block {
          BlockType               Outport
          Name                    "Disturbance_Flow"
          SID                     "10"
          Position                [250, 240, 280, 260]
          Port                    "3"
        }
        Block {
          BlockType               Outport
          Name                    "Sim_Time"
          SID                     "11"
          Position                [250, 330, 280, 350]
          Port                    "4"
        }
        Line {
          SrcBlock                "Push_Button_Switch_Run"
          SrcPort                 1
          DstBlock                "Switch_Run"
          DstPort                 1
        }
        Line {
          SrcBlock                "Manual_Ball_Valve_BV01"
          SrcPort                 1
          DstBlock                "BV01_Open"
          DstPort                 1
        }
        Line {
          SrcBlock                "External_Disturbance_Injector"
          SrcPort                 1
          DstBlock                "Disturbance_Flow"
          DstPort                 1
        }
        Line {
          SrcBlock                "Master_Clock"
          SrcPort                 1
          DstBlock                "Sim_Time"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               SubSystem
      Name                    "2_ESP32_Automation_Controller"
      SID                     "12"
      Ports                   [8, 6]
      Position                [300, 100, 560, 520]
      ForegroundColor         "navy"
      BackgroundColor         "lightBlue"
      System {
        Name                    "2_ESP32_Automation_Controller"
        Location                [50, 50, 950, 750]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Switch_Run"
          SID                     "13"
          Position                [50, 70, 80, 90]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "BV01_Open"
          SID                     "14"
          Position                [50, 120, 80, 140]
          Port                    "2"
        }
        Block {
          BlockType               Inport
          Name                    "Disturbance_Flow"
          SID                     "15"
          Position                [50, 170, 80, 190]
          Port                    "3"
        }
        Block {
          BlockType               Inport
          Name                    "Sim_Time"
          SID                     "16"
          Position                [50, 220, 80, 240]
          Port                    "4"
        }
        Block {
          BlockType               Inport
          Name                    "FT01_Flow_Rate"
          SID                     "17"
          Position                [50, 270, 80, 290]
          Port                    "5"
        }
        Block {
          BlockType               Inport
          Name                    "Sump_Float_Alert"
          SID                     "18"
          Position                [50, 320, 80, 340]
          Port                    "6"
        }
        Block {
          BlockType               Inport
          Name                    "Sump_Volume_L"
          SID                     "19"
          Position                [50, 370, 80, 390]
          Port                    "7"
        }
        Block {
          BlockType               Inport
          Name                    "FT01_Total_Vol_L"
          SID                     "20"
          Position                [50, 420, 80, 440]
          Port                    "8"
        }

        Block {
          BlockType               Mux
          Name                    "FSM_Input_Mux"
          SID                     "21"
          Ports                   [4, 1]
          Position                [160, 60, 170, 250]
          Inputs                  "4"
        }
        Block {
          BlockType               MATLABFcn
          Name                    "Firmware_State_Machine_Engine"
          SID                     "22"
          Position                [220, 60, 450, 250]
          MATLABFcn               "lam_simulink_fcn(u)"
          OutputDimensions        "15"
          SampleTime              "0.001"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_FSM_Signals"
          SID                     "23"
          Ports                   [1, 7]
          Position                [510, 50, 520, 450]
          Outputs                 "[3, 3, 1, 1, 1, 3, 3]"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Pump_Duties"
          SID                     "24"
          Ports                   [1, 3]
          Position                [590, 335, 600, 425]
          Outputs                 "3"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Status"
          SID                     "25"
          Ports                   [1, 3]
          Position                [590, 440, 600, 500]
          Outputs                 "3"
        }

        Block {
          BlockType               Outport
          Name                    "P1_Duty_Cmd"
          SID                     "26"
          Position                [680, 340, 710, 360]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "P2_Duty_Cmd"
          SID                     "27"
          Position                [680, 370, 710, 390]
          Port                    "2"
        }
        Block {
          BlockType               Outport
          Name                    "P3_Duty_Cmd"
          SID                     "28"
          Position                [680, 400, 710, 420]
          Port                    "3"
        }
        Block {
          BlockType               Outport
          Name                    "OV01_Solenoid_Cmd"
          SID                     "29"
          Position                [680, 440, 710, 460]
          Port                    "4"
        }
        Block {
          BlockType               Outport
          Name                    "FSM_State_Code"
          SID                     "30"
          Position                [680, 280, 710, 300]
          Port                    "5"
        }
        Block {
          BlockType               Outport
          Name                    "Delivered_Flush_Vol"
          SID                     "31"
          Position                [680, 480, 710, 500]
          Port                    "6"
        }

        Line {
          SrcBlock                "Switch_Run"
          SrcPort                 1
          DstBlock                "FSM_Input_Mux"
          DstPort                 1
        }
        Line {
          SrcBlock                "BV01_Open"
          SrcPort                 1
          DstBlock                "FSM_Input_Mux"
          DstPort                 2
        }
        Line {
          SrcBlock                "Disturbance_Flow"
          SrcPort                 1
          DstBlock                "FSM_Input_Mux"
          DstPort                 3
        }
        Line {
          SrcBlock                "Sim_Time"
          SrcPort                 1
          DstBlock                "FSM_Input_Mux"
          DstPort                 4
        }
        Line {
          SrcBlock                "FSM_Input_Mux"
          SrcPort                 1
          DstBlock                "Firmware_State_Machine_Engine"
          DstPort                 1
        }
        Line {
          SrcBlock                "Firmware_State_Machine_Engine"
          SrcPort                 1
          DstBlock                "Demux_FSM_Signals"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_FSM_Signals"
          SrcPort                 5
          DstBlock                "FSM_State_Code"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_FSM_Signals"
          SrcPort                 6
          DstBlock                "Demux_Pump_Duties"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Pump_Duties"
          SrcPort                 1
          DstBlock                "P1_Duty_Cmd"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Pump_Duties"
          SrcPort                 2
          DstBlock                "P2_Duty_Cmd"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Pump_Duties"
          SrcPort                 3
          DstBlock                "P3_Duty_Cmd"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_FSM_Signals"
          SrcPort                 7
          DstBlock                "Demux_Status"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Status"
          SrcPort                 1
          DstBlock                "OV01_Solenoid_Cmd"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Status"
          SrcPort                 3
          DstBlock                "Delivered_Flush_Vol"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               SubSystem
      Name                    "3_BTS7960_Motor_Drivers"
      SID                     "32"
      Ports                   [3, 4]
      Position                [620, 100, 840, 360]
      ForegroundColor         "orange"
      BackgroundColor         "yellow"
      System {
        Name                    "3_BTS7960_Motor_Drivers"
        Location                [100, 100, 850, 600]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "P1_Duty_Cmd"
          SID                     "33"
          Position                [50, 70, 80, 90]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "P2_Duty_Cmd"
          SID                     "34"
          Position                [50, 170, 80, 190]
          Port                    "2"
        }
        Block {
          BlockType               Inport
          Name                    "P3_Duty_Cmd"
          SID                     "35"
          Position                [50, 270, 80, 290]
          Port                    "3"
        }

        Block {
          BlockType               RateLimiter
          Name                    "Rate_Limiter_P1"
          SID                     "36"
          Position                [140, 60, 200, 100]
          RisingSlewLimit         "300"
          FallingSlewLimit        "-500"
        }
        Block {
          BlockType               Saturate
          Name                    "Saturate_P1"
          SID                     "37"
          Position                [240, 60, 280, 100]
          UpperLimit              "100"
          LowerLimit              "0"
        }
        Block {
          BlockType               Gain
          Name                    "P1_Current_Est"
          SID                     "38"
          Position                [320, 100, 360, 130]
          Gain                    "0.05"
        }

        Block {
          BlockType               RateLimiter
          Name                    "Rate_Limiter_P2"
          SID                     "39"
          Position                [140, 160, 200, 200]
          RisingSlewLimit         "300"
          FallingSlewLimit        "-500"
        }
        Block {
          BlockType               Saturate
          Name                    "Saturate_P2"
          SID                     "40"
          Position                [240, 160, 280, 200]
          UpperLimit              "100"
          LowerLimit              "0"
        }
        Block {
          BlockType               Gain
          Name                    "P2_Current_Est"
          SID                     "41"
          Position                [320, 200, 360, 230]
          Gain                    "0.08"
        }

        Block {
          BlockType               RateLimiter
          Name                    "Rate_Limiter_P3"
          SID                     "42"
          Position                [140, 260, 200, 300]
          RisingSlewLimit         "300"
          FallingSlewLimit        "-500"
        }
        Block {
          BlockType               Saturate
          Name                    "Saturate_P3"
          SID                     "43"
          Position                [240, 260, 280, 300]
          UpperLimit              "100"
          LowerLimit              "0"
        }
        Block {
          BlockType               Gain
          Name                    "P3_Current_Est"
          SID                     "44"
          Position                [320, 300, 360, 330]
          Gain                    "0.08"
        }

        Block {
          BlockType               Mux
          Name                    "Mux_Currents"
          SID                     "45"
          Ports                   [3, 1]
          Position                [410, 200, 420, 320]
          Inputs                  "3"
        }

        Block {
          BlockType               Outport
          Name                    "P1_Duty_Filt"
          SID                     "46"
          Position                [470, 70, 500, 90]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "P2_Duty_Filt"
          SID                     "47"
          Position                [470, 170, 500, 190]
          Port                    "2"
        }
        Block {
          BlockType               Outport
          Name                    "P3_Duty_Filt"
          SID                     "48"
          Position                [470, 270, 500, 290]
          Port                    "3"
        }
        Block {
          BlockType               Outport
          Name                    "Motor_Currents_Amps"
          SID                     "49"
          Position                [470, 250, 500, 270]
          Port                    "4"
        }

        Line {
          SrcBlock                "P1_Duty_Cmd"
          SrcPort                 1
          DstBlock                "Rate_Limiter_P1"
          DstPort                 1
        }
        Line {
          SrcBlock                "Rate_Limiter_P1"
          SrcPort                 1
          DstBlock                "Saturate_P1"
          DstPort                 1
        }
        Line {
          SrcBlock                "Saturate_P1"
          SrcPort                 1
          Points                  [15, 0]
          Branch {
            DstBlock              "P1_Duty_Filt"
            DstPort               1
          }
          Branch {
            Points                [0, 35]
            DstBlock              "P1_Current_Est"
            DstPort               1
          }
        }
        Line {
          SrcBlock                "P1_Current_Est"
          SrcPort                 1
          Points                  [25, 0; 0, 105]
          DstBlock                "Mux_Currents"
          DstPort                 1
        }

        Line {
          SrcBlock                "P2_Duty_Cmd"
          SrcPort                 1
          DstBlock                "Rate_Limiter_P2"
          DstPort                 1
        }
        Line {
          SrcBlock                "Rate_Limiter_P2"
          SrcPort                 1
          DstBlock                "Saturate_P2"
          DstPort                 1
        }
        Line {
          SrcBlock                "Saturate_P2"
          SrcPort                 1
          Points                  [15, 0]
          Branch {
            DstBlock              "P2_Duty_Filt"
            DstPort               1
          }
          Branch {
            Points                [0, 35]
            DstBlock              "P2_Current_Est"
            DstPort               1
          }
        }
        Line {
          SrcBlock                "P2_Current_Est"
          SrcPort                 1
          Points                  [20, 0; 0, 45]
          DstBlock                "Mux_Currents"
          DstPort                 2
        }

        Line {
          SrcBlock                "P3_Duty_Cmd"
          SrcPort                 1
          DstBlock                "Rate_Limiter_P3"
          DstPort                 1
        }
        Line {
          SrcBlock                "Rate_Limiter_P3"
          SrcPort                 1
          DstBlock                "Saturate_P3"
          DstPort                 1
        }
        Line {
          SrcBlock                "Saturate_P3"
          SrcPort                 1
          Points                  [15, 0]
          Branch {
            DstBlock              "P3_Duty_Filt"
            DstPort               1
          }
          Branch {
            Points                [0, 35]
            DstBlock              "P3_Current_Est"
            DstPort               1
          }
        }
        Line {
          SrcBlock                "P3_Current_Est"
          SrcPort                 1
          DstBlock                "Mux_Currents"
          DstPort                 3
        }

        Line {
          SrcBlock                "Mux_Currents"
          SrcPort                 1
          DstBlock                "Motor_Currents_Amps"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               SubSystem
      Name                    "4_Multi_Tank_Hydraulic_Plant"
      SID                     "50"
      Ports                   [6, 6]
      Position                [900, 100, 1160, 460]
      ForegroundColor         "darkGreen"
      BackgroundColor         "lightBlue"
      System {
        Name                    "4_Multi_Tank_Hydraulic_Plant"
        Location                [50, 50, 1100, 750]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Duty_P1"
          SID                     "51"
          Position                [50, 70, 80, 90]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Duty_P2"
          SID                     "52"
          Position                [50, 130, 80, 150]
          Port                    "2"
        }
        Block {
          BlockType               Inport
          Name                    "Duty_P3"
          SID                     "53"
          Position                [50, 190, 80, 210]
          Port                    "3"
        }
        Block {
          BlockType               Inport
          Name                    "OV01_Solenoid"
          SID                     "54"
          Position                [50, 250, 80, 270]
          Port                    "4"
        }
        Block {
          BlockType               Inport
          Name                    "BV01_Ball_Valve"
          SID                     "55"
          Position                [50, 310, 80, 330]
          Port                    "5"
        }
        Block {
          BlockType               Inport
          Name                    "Disturbance_Flow"
          SID                     "56"
          Position                [50, 370, 80, 390]
          Port                    "6"
        }

        Block {
          BlockType               Mux
          Name                    "Plant_Mux"
          SID                     "57"
          Ports                   [4, 1]
          Position                [160, 60, 170, 240]
          Inputs                  "4"
        }
        Block {
          BlockType               MATLABFcn
          Name                    "Hydraulic_Network_Solver"
          SID                     "58"
          Position                [220, 60, 480, 240]
          MATLABFcn               "lam_simulink_fcn(u)"
          OutputDimensions        "15"
          SampleTime              "0.001"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Plant_Out"
          SID                     "59"
          Ports                   [1, 7]
          Position                [540, 50, 550, 450]
          Outputs                 "[3, 3, 1, 1, 1, 3, 3]"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Tanks"
          SID                     "60"
          Ports                   [1, 3]
          Position                [600, 60, 610, 140]
          Outputs                 "3"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Flows"
          SID                     "61"
          Ports                   [1, 3]
          Position                [600, 160, 610, 240]
          Outputs                 "3"
        }

        Block {
          BlockType               Outport
          Name                    "V_10L_Tank"
          SID                     "62"
          Position                [690, 65, 720, 85]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "V_Sump_Vessel"
          SID                     "63"
          Position                [690, 95, 720, 115]
          Port                    "2"
        }
        Block {
          BlockType               Outport
          Name                    "V_Flush_Tank"
          SID                     "64"
          Position                [690, 125, 720, 145]
          Port                    "3"
        }
        Block {
          BlockType               Outport
          Name                    "Q_Pump_01"
          SID                     "65"
          Position                [690, 165, 720, 185]
          Port                    "4"
        }
        Block {
          BlockType               Outport
          Name                    "Q_Pump_02_FT01"
          SID                     "66"
          Position                [690, 195, 720, 215]
          Port                    "5"
        }
        Block {
          BlockType               Outport
          Name                    "Q_Pump_03"
          SID                     "67"
          Position                [690, 225, 720, 245]
          Port                    "6"
        }

        Line {
          SrcBlock                "Duty_P1"
          SrcPort                 1
          Points                  [35, 0; 0, 5]
          DstBlock                "Plant_Mux"
          DstPort                 1
        }
        Line {
          SrcBlock                "BV01_Ball_Valve"
          SrcPort                 1
          Points                  [45, 0; 0, -190]
          DstBlock                "Plant_Mux"
          DstPort                 2
        }
        Line {
          SrcBlock                "Disturbance_Flow"
          SrcPort                 1
          Points                  [55, 0; 0, -210]
          DstBlock                "Plant_Mux"
          DstPort                 3
        }
        Line {
          SrcBlock                "Duty_P2"
          SrcPort                 1
          Points                  [25, 0; 0, 75]
          DstBlock                "Plant_Mux"
          DstPort                 4
        }

        Line {
          SrcBlock                "Plant_Mux"
          SrcPort                 1
          DstBlock                "Hydraulic_Network_Solver"
          DstPort                 1
        }
        Line {
          SrcBlock                "Hydraulic_Network_Solver"
          SrcPort                 1
          DstBlock                "Demux_Plant_Out"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Plant_Out"
          SrcPort                 1
          DstBlock                "Demux_Tanks"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Tanks"
          SrcPort                 1
          DstBlock                "V_10L_Tank"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Tanks"
          SrcPort                 2
          DstBlock                "V_Sump_Vessel"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Tanks"
          SrcPort                 3
          DstBlock                "V_Flush_Tank"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Plant_Out"
          SrcPort                 2
          DstBlock                "Demux_Flows"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Flows"
          SrcPort                 1
          DstBlock                "Q_Pump_01"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Flows"
          SrcPort                 2
          DstBlock                "Q_Pump_02_FT01"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Flows"
          SrcPort                 3
          DstBlock                "Q_Pump_03"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               SubSystem
      Name                    "5_Instrumentation_and_Fluid_Mechanics"
      SID                     "68"
      Ports                   [3, 6]
      Position                [620, 580, 1000, 880]
      ForegroundColor         "magenta"
      BackgroundColor         "lightBlue"
      System {
        Name                    "5_Instrumentation_and_Fluid_Mechanics"
        Location                [100, 100, 950, 750]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Q_Recirc_FT01"
          SID                     "69"
          Position                [50, 80, 80, 100]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "V_Sump_Level"
          SID                     "70"
          Position                [50, 200, 80, 220]
          Port                    "2"
        }
        Block {
          BlockType               Inport
          Name                    "FSM_State_Code"
          SID                     "71"
          Position                [50, 320, 80, 340]
          Port                    "3"
        }

        Block {
          BlockType               Gain
          Name                    "FT01_Pulse_Gen_Hz"
          SID                     "72"
          Position                [160, 75, 230, 105]
          Gain                    "87.766667"
        }
        Block {
          BlockType               Gain
          Name                    "FT01_Lpm_Cal"
          SID                     "73"
          Position                [280, 75, 350, 105]
          Gain                    "0.0113938"
        }

        Block {
          BlockType               Gain
          Name                    "Gain_mLs"
          SID                     "74"
          Position                [160, 140, 220, 170]
          Gain                    "16.666667"
        }
        Block {
          BlockType               Gain
          Name                    "Gain_Velocity_mps"
          SID                     "75"
          Position                [260, 140, 320, 170]
          Gain                    "0.019894"
        }
        Block {
          BlockType               Gain
          Name                    "Gain_Reynolds_Number"
          SID                     "76"
          Position                [360, 140, 420, 170]
          Gain                    "8000"
        }

        Block {
          BlockType               Relay
          Name                    "Float_Switch_Schmitt_Trigger"
          SID                     "77"
          Position                [160, 195, 220, 225]
          OnSwitchValue           "3.5"
          OffSwitchValue          "2.5"
          OnOutputValue           "1"
          OffOutputValue          "0"
        }

        Block {
          BlockType               Gain
          Name                    "Flow_to_L_per_sec"
          SID                     "78"
          Position                [160, 260, 220, 290]
          Gain                    "0.01666667"
        }

        Block {
          BlockType               Outport
          Name                    "FT01_Flow_Rate_Lpm"
          SID                     "79"
          Position                [500, 80, 530, 100]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "FT01_Pulse_Freq_Hz"
          SID                     "80"
          Position                [500, 115, 530, 135]
          Port                    "2"
        }
        Block {
          BlockType               Outport
          Name                    "Cumulative_Total_Volume_L"
          SID                     "81"
          Position                [500, 265, 530, 285]
          Port                    "3"
        }
        Block {
          BlockType               Outport
          Name                    "Float_Switch_High_Alert"
          SID                     "82"
          Position                [500, 200, 530, 220]
          Port                    "4"
        }
        Block {
          BlockType               Outport
          Name                    "Line_Velocity_mps"
          SID                     "83"
          Position                [500, 150, 530, 170]
          Port                    "5"
        }
        Block {
          BlockType               Outport
          Name                    "Reynolds_Number"
          SID                     "84"
          Position                [500, 175, 530, 195]
          Port                    "6"
        }

        Line {
          SrcBlock                "Q_Recirc_FT01"
          SrcPort                 1
          Points                  [30, 0]
          Branch {
            DstBlock              "FT01_Pulse_Gen_Hz"
            DstPort               1
          }
          Branch {
            Points                [0, 65]
            Branch {
              DstBlock            "Gain_mLs"
              DstPort             1
            }
            Branch {
              Points              [0, 120]
              DstBlock            "Flow_to_L_per_sec"
              DstPort             1
            }
          }
        }
        Line {
          SrcBlock                "FT01_Pulse_Gen_Hz"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "FT01_Lpm_Cal"
            DstPort               1
          }
          Branch {
            Points                [0, 35]
            DstBlock              "FT01_Pulse_Freq_Hz"
            DstPort               1
          }
        }
        Line {
          SrcBlock                "FT01_Lpm_Cal"
          SrcPort                 1
          DstBlock                "FT01_Flow_Rate_Lpm"
          DstPort                 1
        }

        Line {
          SrcBlock                "Gain_mLs"
          SrcPort                 1
          DstBlock                "Gain_Velocity_mps"
          DstPort                 1
        }
        Line {
          SrcBlock                "Gain_Velocity_mps"
          SrcPort                 1
          Points                  [15, 0]
          Branch {
            DstBlock              "Gain_Reynolds_Number"
            DstPort               1
          }
          Branch {
            Points                [0, 5]
            DstBlock              "Line_Velocity_mps"
            DstPort               1
          }
        }
        Line {
          SrcBlock                "Gain_Reynolds_Number"
          SrcPort                 1
          Points                  [40, 0; 0, 30]
          DstBlock                "Reynolds_Number"
          DstPort                 1
        }

        Line {
          SrcBlock                "V_Sump_Level"
          SrcPort                 1
          DstBlock                "Float_Switch_Schmitt_Trigger"
          DstPort                 1
        }
        Line {
          SrcBlock                "Float_Switch_Schmitt_Trigger"
          SrcPort                 1
          DstBlock                "Float_Switch_High_Alert"
          DstPort                 1
        }
        Line {
          SrcBlock                "Flow_to_L_per_sec"
          SrcPort                 1
          DstBlock                "Cumulative_Total_Volume_L"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               SubSystem
      Name                    "6_Supervisory_Console_and_Scopes"
      SID                     "85"
      Ports                   [10, 0]
      Position                [1240, 100, 1540, 920]
      ForegroundColor         "darkGreen"
      BackgroundColor         "white"
      System {
        Name                    "6_Supervisory_Console_and_Scopes"
        Location                [50, 50, 1150, 850]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "V_10L_Tank"
          SID                     "86"
          Position                [50, 60, 80, 80]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "V_Sump_Vessel"
          SID                     "87"
          Position                [50, 130, 80, 150]
          Port                    "2"
        }
        Block {
          BlockType               Inport
          Name                    "V_Flush_Tank"
          SID                     "88"
          Position                [50, 200, 80, 220]
          Port                    "3"
        }
        Block {
          BlockType               Inport
          Name                    "Q_P1_Flow"
          SID                     "89"
          Position                [50, 270, 80, 290]
          Port                    "4"
        }
        Block {
          BlockType               Inport
          Name                    "FT01_Flow_Rate"
          SID                     "90"
          Position                [50, 340, 80, 360]
          Port                    "5"
        }
        Block {
          BlockType               Inport
          Name                    "FSM_State"
          SID                     "91"
          Position                [50, 410, 80, 430]
          Port                    "6"
        }
        Block {
          BlockType               Inport
          Name                    "Motor_Currents"
          SID                     "92"
          Position                [50, 480, 80, 500]
          Port                    "7"
        }
        Block {
          BlockType               Inport
          Name                    "Float_Alert"
          SID                     "93"
          Position                [50, 550, 80, 570]
          Port                    "8"
        }
        Block {
          BlockType               Inport
          Name                    "Line_Velocity"
          SID                     "94"
          Position                [50, 620, 80, 640]
          Port                    "9"
        }
        Block {
          BlockType               Inport
          Name                    "Reynolds_No"
          SID                     "95"
          Position                [50, 690, 80, 710]
          Port                    "10"
        }

        Block {
          BlockType               Mux
          Name                    "Tanks_Mux"
          SID                     "96"
          Ports                   [3, 1]
          Position                [160, 50, 170, 230]
          Inputs                  "3"
        }
        Block {
          BlockType               Display
          Name                    "Live_Tanks_10L_Sump_Flush"
          SID                     "97"
          Position                [220, 80, 340, 140]
          Decimation              "50"
        }
        Block {
          BlockType               Scope
          Name                    "Scope_Process_Tanks"
          SID                     "98"
          Ports                   [1]
          Position                [380, 80, 440, 140]
          TimeRange               "250"
          YMin                    "0"
          YMax                    "11"
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_Tanks"
          SID                     "99"
          Position                [480, 90, 580, 130]
          VariableName            "tank_levels"
          SaveFormat              "Array"
        }

        Block {
          BlockType               Display
          Name                    "Live_FT01_Flow_Lpm"
          SID                     "100"
          Position                [220, 325, 340, 365]
          Decimation              "50"
        }
        Block {
          BlockType               Scope
          Name                    "Scope_FT01_Flow"
          SID                     "101"
          Ports                   [1]
          Position                [380, 325, 440, 365]
          TimeRange               "250"
          YMin                    "0"
          YMax                    "6"
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_FT01"
          SID                     "102"
          Position                [480, 325, 580, 365]
          VariableName            "ft01_flow"
          SaveFormat              "Array"
        }

        Block {
          BlockType               Display
          Name                    "Live_FSM_State_Code"
          SID                     "103"
          Position                [220, 395, 340, 435]
          Decimation              "50"
        }
        Block {
          BlockType               Scope
          Name                    "Scope_FSM_States"
          SID                     "104"
          Ports                   [1]
          Position                [380, 395, 440, 435]
          TimeRange               "250"
          YMin                    "0"
          YMax                    "9"
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_State"
          SID                     "105"
          Position                [480, 395, 580, 435]
          VariableName            "system_state"
          SaveFormat              "Array"
        }

        Block {
          BlockType               Display
          Name                    "Live_Motor_Currents_A"
          SID                     "106"
          Position                [220, 470, 340, 510]
          Decimation              "50"
        }
        Block {
          BlockType               Scope
          Name                    "Scope_Motor_Currents"
          SID                     "107"
          Ports                   [1]
          Position                [380, 470, 440, 510]
          TimeRange               "250"
          YMin                    "0"
          YMax                    "10"
        }

        Block {
          BlockType               Display
          Name                    "Live_Velocity_mps"
          SID                     "108"
          Position                [220, 615, 300, 645]
          Decimation              "50"
        }
        Block {
          BlockType               Display
          Name                    "Live_Reynolds_No"
          SID                     "109"
          Position                [320, 615, 400, 645]
          Decimation              "50"
        }
        Block {
          BlockType               Scope
          Name                    "Scope_Fluid_Mechanics"
          SID                     "110"
          Ports                   [1]
          Position                [440, 615, 500, 655]
          TimeRange               "250"
          YMin                    "0"
          YMax                    "14000"
        }

        Line {
          SrcBlock                "V_10L_Tank"
          SrcPort                 1
          DstBlock                "Tanks_Mux"
          DstPort                 1
        }
        Line {
          SrcBlock                "V_Sump_Vessel"
          SrcPort                 1
          DstBlock                "Tanks_Mux"
          DstPort                 2
        }
        Line {
          SrcBlock                "V_Flush_Tank"
          SrcPort                 1
          DstBlock                "Tanks_Mux"
          DstPort                 3
        }
        Line {
          SrcBlock                "Tanks_Mux"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "Live_Tanks_10L_Sump_Flush"
            DstPort               1
          }
          Branch {
            DstBlock              "Scope_Process_Tanks"
            DstPort               1
          }
          Branch {
            DstBlock              "Save_Tanks"
            DstPort               1
          }
        }

        Line {
          SrcBlock                "FT01_Flow_Rate"
          SrcPort                 1
          Points                  [25, 0]
          Branch {
            DstBlock              "Live_FT01_Flow_Lpm"
            DstPort               1
          }
          Branch {
            DstBlock              "Scope_FT01_Flow"
            DstPort               1
          }
          Branch {
            DstBlock              "Save_FT01"
            DstPort               1
          }
        }

        Line {
          SrcBlock                "FSM_State"
          SrcPort                 1
          Points                  [25, 0]
          Branch {
            DstBlock              "Live_FSM_State_Code"
            DstPort               1
          }
          Branch {
            DstBlock              "Scope_FSM_States"
            DstPort               1
          }
          Branch {
            DstBlock              "Save_State"
            DstPort               1
          }
        }

        Line {
          SrcBlock                "Motor_Currents"
          SrcPort                 1
          Points                  [25, 0]
          Branch {
            DstBlock              "Live_Motor_Currents_A"
            DstPort               1
          }
          Branch {
            DstBlock              "Scope_Motor_Currents"
            DstPort               1
          }
        }

        Line {
          SrcBlock                "Line_Velocity"
          SrcPort                 1
          DstBlock                "Live_Velocity_mps"
          DstPort                 1
        }
        Line {
          SrcBlock                "Reynolds_No"
          SrcPort                 1
          Points                  [15, 0]
          Branch {
            DstBlock              "Live_Reynolds_No"
            DstPort               1
          }
          Branch {
            Points                [0, -65]
            DstBlock              "Scope_Fluid_Mechanics"
            DstPort               1
          }
        }
      }
    }

    Line {
      SrcBlock                "1_HMI_Operator_Console"
      SrcPort                 1
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 1
    }
    Line {
      SrcBlock                "1_HMI_Operator_Console"
      SrcPort                 2
      Points                  [25, 0; 0, -25]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 2
    }
    Line {
      SrcBlock                "1_HMI_Operator_Console"
      SrcPort                 3
      Points                  [35, 0; 0, -35]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 3
    }
    Line {
      SrcBlock                "1_HMI_Operator_Console"
      SrcPort                 4
      Points                  [45, 0; 0, -45]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 4
    }

    Line {
      SrcBlock                "2_ESP32_Automation_Controller"
      SrcPort                 1
      DstBlock                "3_BTS7960_Motor_Drivers"
      DstPort                 1
    }
    Line {
      SrcBlock                "2_ESP32_Automation_Controller"
      SrcPort                 2
      Points                  [20, 0; 0, 10]
      DstBlock                "3_BTS7960_Motor_Drivers"
      DstPort                 2
    }
    Line {
      SrcBlock                "2_ESP32_Automation_Controller"
      SrcPort                 3
      Points                  [25, 0; 0, 10]
      DstBlock                "3_BTS7960_Motor_Drivers"
      DstPort                 3
    }

    Line {
      SrcBlock                "3_BTS7960_Motor_Drivers"
      SrcPort                 1
      DstBlock                "4_Multi_Tank_Hydraulic_Plant"
      DstPort                 1
    }
    Line {
      SrcBlock                "3_BTS7960_Motor_Drivers"
      SrcPort                 2
      DstBlock                "4_Multi_Tank_Hydraulic_Plant"
      DstPort                 2
    }
    Line {
      SrcBlock                "3_BTS7960_Motor_Drivers"
      SrcPort                 3
      DstBlock                "4_Multi_Tank_Hydraulic_Plant"
      DstPort                 3
    }
    Line {
      SrcBlock                "2_ESP32_Automation_Controller"
      SrcPort                 4
      Points                  [280, 0; 0, -85]
      DstBlock                "4_Multi_Tank_Hydraulic_Plant"
      DstPort                 4
    }
    Line {
      SrcBlock                "1_HMI_Operator_Console"
      SrcPort                 2
      Points                  [40, 0; 0, 180; 600, 0; 0, -40]
      DstBlock                "4_Multi_Tank_Hydraulic_Plant"
      DstPort                 5
    }
    Line {
      SrcBlock                "1_HMI_Operator_Console"
      SrcPort                 3
      Points                  [30, 0; 0, 120; 630, 0; 0, -10]
      DstBlock                "4_Multi_Tank_Hydraulic_Plant"
      DstPort                 6
    }

    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 5
      Points                  [40, 0; 0, 220; -620, 0; 0, 170]
      DstBlock                "5_Instrumentation_and_Fluid_Mechanics"
      DstPort                 1
    }
    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 2
      Points                  [25, 0; 0, 480; -590, 0; 0, 50]
      DstBlock                "5_Instrumentation_and_Fluid_Mechanics"
      DstPort                 2
    }
    Line {
      SrcBlock                "2_ESP32_Automation_Controller"
      SrcPort                 5
      Points                  [30, 0; 0, 400]
      DstBlock                "5_Instrumentation_and_Fluid_Mechanics"
      DstPort                 3
    }

    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 1
      Points                  [-40, 0; 0, -280]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 5
    }
    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 4
      Points                  [-55, 0; 0, -380]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 6
    }
    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 2
      Points                  [15, 0; 0, -40; -630, 0; 0, 310]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 7
    }
    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 3
      Points                  [-65, 0; 0, -220]
      DstBlock                "2_ESP32_Automation_Controller"
      DstPort                 8
    }

    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 1
      Points                  [40, 0; 0, 15]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 1
    }
    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 2
      Points                  [40, 0; 0, 45]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 2
    }
    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 3
      Points                  [40, 0; 0, 75]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 3
    }
    Line {
      SrcBlock                "4_Multi_Tank_Hydraulic_Plant"
      SrcPort                 4
      Points                  [40, 0; 0, 95]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 4
    }
    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 1
      Points                  [210, 0; 0, -170]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 5
    }
    Line {
      SrcBlock                "2_ESP32_Automation_Controller"
      SrcPort                 5
      Points                  [650, 0; 0, 90]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 6
    }
    Line {
      SrcBlock                "3_BTS7960_Motor_Drivers"
      SrcPort                 4
      Points                  [120, 0; 0, 340; 230, 0; 0, -30]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 7
    }
    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 4
      Points                  [220, 0; 0, -10]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 8
    }
    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 5
      Points                  [205, 0; 0, 25]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 9
    }
    Line {
      SrcBlock                "5_Instrumentation_and_Fluid_Mechanics"
      SrcPort                 6
      Points                  [190, 0; 0, 50]
      DstBlock                "6_Supervisory_Console_and_Scopes"
      DstPort                 10
    }
  }
}
'''
    with open(r'd:\matalb_;lam\lam_stage2_system.mdl', 'w', encoding='utf-8') as f:
        f.write(mdl)
    print('Successfully generated hierarchical advanced model lam_stage2_system.mdl')

if __name__ == '__main__':
    build_advanced_model()
