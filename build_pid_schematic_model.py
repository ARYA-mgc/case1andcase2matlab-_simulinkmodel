import os

def generate_pid_model():
    mdl = '''Model {
  Name                    "lam_stage2_system"
  Version                 8.5
  MdlSubVersion           0
  SavedCharacterEncoding  "UTF-8"
  GraphicalInterface {
    NumRootInports        0
    NumRootOutports       0
    ParameterArgumentNames  ""
    ComputedModelVersion  "6.0"
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
  ModelVersionFormat      "6.%<AutoIncrement:1>"
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
    Orientation             "right"
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
      SampleTime              "inf"
    }
    Block {
      BlockType               Demux
      Outputs                 "4"
      DisplayOption           "none"
      BusSelectionMode        off
    }
    Block {
      BlockType               DiscreteIntegrator
      IntegratorMethod        "Integration: Forward Euler"
      gainval                 "1.0"
      ExternalReset           "none"
      InitialConditionSource  "internal"
      InitialCondition        "0"
      InitialConditionMode    "State and output"
      SampleTime              "0.001"
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: Inherit via internal rule"
      LockScale               off
      RndMeth                 "Floor"
      SaturateOnIntegerOverflow off
      LimitOutput             off
      UpperSaturationLimit    "inf"
      LowerSaturationLimit    "-inf"
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
      BlockType               From
      GotoTag                 "A"
      IconDisplay             "Tag"
      TagVisibility           "local"
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
      BlockType               Goto
      GotoTag                 "A"
      IconDisplay             "Tag"
      TagVisibility           "local"
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
    }
    Block {
      BlockType               Product
      Inputs                  "2"
      Multiplication          "Element-wise(.*)"
      CollapseMode            "All dimensions"
      CollapseDim             "1"
      InputSameDT             on
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: Same as first input"
      LockScale               off
      RndMeth                 "Zero"
      SaturateOnIntegerOverflow on
      SampleTime              "-1"
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
      BlockType               Sum
      IconShape               "rectangular"
      Inputs                  "++"
      CollapseMode            "All dimensions"
      CollapseDim             "1"
      InputSameDT             on
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: Same as first input"
      LockScale               off
      RndMeth                 "Floor"
      SaturateOnIntegerOverflow on
      SampleTime              "-1"
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
    Location                [15, 25, 1620, 980]
    Open                    on
    ScreenColor             "white"
    ZoomFactor              "100"
    ReportName              "simulink-default.rpt"
    SIDHighWaterMark        "150"

    Annotation {
      SID                     "1"
      Name                    "LAM RESEARCH CHALLENGE 3.0 - STAGE 2 DIGITAL TWIN"
      Position                [800, 25, 800, 25]
      ForegroundColor         "navy"
      FontSize                16
      FontWeight              "bold"
    }
    Annotation {
      SID                     "2"
      Name                    "P&ID Dwg No. PID-001: Automated Chemical Distribution, Line Flush & Sump Protection Rig"
      Position                [800, 48, 800, 48]
      ForegroundColor         "gray"
      FontSize                11
    }

    Annotation {
      SID                     "3"
      Name                    "[1. PHYSICAL P&ID HYDRAULIC LOOP: 8mm PROCESS & FLUSH CIRCUITS (Dwg PID-001)]"
      Position                [750, 78, 750, 78]
      ForegroundColor         "darkGreen"
      FontSize                12
      FontWeight              "bold"
    }
    Annotation {
      SID                     "4"
      Name                    "[2. EMBEDDED ESP32 AUTOMATION CONTROLLER & OPERATOR HMI]"
      Position                [340, 565, 340, 565]
      ForegroundColor         "navy"
      FontSize                11
      FontWeight              "bold"
    }
    Annotation {
      SID                     "5"
      Name                    "[3. FLUID MECHANICS & SCADA GAUGES]"
      Position                [880, 565, 880, 565]
      ForegroundColor         "purple"
      FontSize                11
      FontWeight              "bold"
    }
    Annotation {
      SID                     "6"
      Name                    "[4. INDUSTRIAL SCOPES & DATA LOGGERS]"
      Position                [1420, 565, 1420, 565]
      ForegroundColor         "blue"
      FontSize                11
      FontWeight              "bold"
    }

    // =========================================================================
    // SECTION 1: PHYSICAL P&ID HYDRAULIC LOOP (Matching Drawing PID-001)
    // =========================================================================

    // Top Flush Tank: T-02 (4.2 L Flush)
    Block {
      BlockType               SubSystem
      Name                    "T-02_4p2L_Flush"
      SID                     "10"
      Ports                   [0, 2]
      Position                [490, 105, 590, 155]
      ForegroundColor         "darkGreen"
      BackgroundColor         "lightBlue"
      System {
        Name                    "T-02_4p2L_Flush"
        Location                [100, 100, 600, 350]
        Open                    off
        Block {
          BlockType               From
          Name                    "From_P3_Q"
          SID                     "11"
          Position                [30, 40, 90, 60]
          GotoTag                 "Q_P3_Act"
        }
        Block {
          BlockType               Gain
          Name                    "Lpm_to_Lps"
          SID                     "12"
          Position                [120, 35, 160, 65]
          Gain                    "-0.01666667"
        }
        Block {
          BlockType               DiscreteIntegrator
          Name                    "Flush_Integrator"
          SID                     "13"
          Position                [200, 30, 250, 70]
          InitialCondition        "4.2"
          LimitOutput             on
          UpperSaturationLimit    "4.2"
          LowerSaturationLimit    "0.0"
        }
        Block {
          BlockType               Constant
          Name                    "Head_Flow"
          SID                     "14"
          Position                [200, 110, 240, 130]
          Value                   "4.12"
        }
        Block {
          BlockType               Outport
          Name                    "V_T02"
          SID                     "15"
          Position                [320, 40, 350, 60]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "FW_2_Flow"
          SID                     "16"
          Position                [320, 110, 350, 130]
          Port                    "2"
        }
        Line {
          SrcBlock                "From_P3_Q"
          SrcPort                 1
          DstBlock                "Lpm_to_Lps"
          DstPort                 1
        }
        Line {
          SrcBlock                "Lpm_to_Lps"
          SrcPort                 1
          DstBlock                "Flush_Integrator"
          DstPort                 1
        }
        Line {
          SrcBlock                "Flush_Integrator"
          SrcPort                 1
          DstBlock                "V_T02"
          DstPort                 1
        }
        Line {
          SrcBlock                "Head_Flow"
          SrcPort                 1
          DstBlock                "FW_2_Flow"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               Goto
      Name                    "Goto_T02_Level"
      SID                     "17"
      Position                [620, 110, 690, 130]
      GotoTag                 "T02_Level"
      ShowName                off
    }

    // Ball Valve: BV-01 (Manual)
    Block {
      BlockType               From
      Name                    "From_BV01_Cmd"
      SID                     "18"
      Position                [400, 195, 470, 215]
      GotoTag                 "BV01_Cmd"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "BV-01_Manual_Valve"
      SID                     "19"
      Ports                   [2, 1]
      Position                [505, 180, 575, 230]
      ForegroundColor         "darkGreen"
      BackgroundColor         "yellow"
      System {
        Name                    "BV-01_Manual_Valve"
        Location                [100, 100, 450, 300]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "FW_2"
          SID                     "20"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Cmd_Open"
          SID                     "21"
          Position                [30, 90, 60, 110]
          Port                    "2"
        }
        Block {
          BlockType               Product
          Name                    "Valve_Mult"
          SID                     "22"
          Ports                   [2, 1]
          Position                [120, 40, 150, 95]
        }
        Block {
          BlockType               Outport
          Name                    "PW_3_in"
          SID                     "23"
          Position                [200, 60, 230, 80]
          Port                    "1"
        }
        Line {
          SrcBlock                "FW_2"
          SrcPort                 1
          DstBlock                "Valve_Mult"
          DstPort                 1
        }
        Line {
          SrcBlock                "Cmd_Open"
          SrcPort                 1
          Points                  [40, 0]
          DstBlock                "Valve_Mult"
          DstPort                 2
        }
        Line {
          SrcBlock                "Valve_Mult"
          SrcPort                 1
          DstBlock                "PW_3_in"
          DstPort                 1
        }
      }
    }

    // Flush Feed Pump: P-03
    Block {
      BlockType               From
      Name                    "From_P3_Duty"
      SID                     "24"
      Position                [400, 275, 470, 295]
      GotoTag                 "P3_Duty"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "P-03_Flush_Pump"
      SID                     "25"
      Ports                   [2, 1]
      Position                [505, 260, 575, 310]
      ForegroundColor         "orange"
      BackgroundColor         "goldenrod"
      System {
        Name                    "P-03_Flush_Pump"
        Location                [100, 100, 500, 320]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Fluid_In"
          SID                     "26"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Duty_Cmd"
          SID                     "27"
          Position                [30, 90, 60, 110]
          Port                    "2"
        }
        Block {
          BlockType               Gain
          Name                    "Duty_Frac"
          SID                     "28"
          Position                [90, 85, 130, 115]
          Gain                    "0.01"
        }
        Block {
          BlockType               Product
          Name                    "Pump_Mult"
          SID                     "29"
          Ports                   [2, 1]
          Position                [160, 40, 190, 95]
        }
        Block {
          BlockType               Goto
          Name                    "Goto_Internal_P3"
          SID                     "30"
          Position                [230, 110, 300, 130]
          GotoTag                 "Q_P3_Act"
        }
        Block {
          BlockType               Outport
          Name                    "PW_3_out"
          SID                     "31"
          Position                [250, 60, 280, 80]
          Port                    "1"
        }
        Line {
          SrcBlock                "Fluid_In"
          SrcPort                 1
          DstBlock                "Pump_Mult"
          DstPort                 1
        }
        Line {
          SrcBlock                "Duty_Cmd"
          SrcPort                 1
          DstBlock                "Duty_Frac"
          DstPort                 1
        }
        Line {
          SrcBlock                "Duty_Frac"
          SrcPort                 1
          Points                  [10, 0]
          DstBlock                "Pump_Mult"
          DstPort                 2
        }
        Line {
          SrcBlock                "Pump_Mult"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "PW_3_out"
            DstPort               1
          }
          Branch {
            Points                [0, 50]
            DstBlock              "Goto_Internal_P3"
            DstPort               1
          }
        }
      }
    }

    // Main 10L Process Tank: T-01
    Block {
      BlockType               SubSystem
      Name                    "T-01_10L_Process"
      SID                     "32"
      Ports                   [1, 2]
      Position                [60, 345, 170, 425]
      ForegroundColor         "darkGreen"
      BackgroundColor         "lightBlue"
      System {
        Name                    "T-01_10L_Process"
        Location                [100, 100, 700, 450]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "PW_8_Return"
          SID                     "33"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               From
          Name                    "From_P1_Q"
          SID                     "34"
          Position                [30, 100, 90, 120]
          GotoTag                 "Q_P1_Act"
        }
        Block {
          BlockType               Sum
          Name                    "Sum_Net"
          SID                     "35"
          Ports                   [2, 1]
          Position                [120, 40, 140, 100]
          Inputs                  "+-"
        }
        Block {
          BlockType               Gain
          Name                    "Lpm_to_Lps"
          SID                     "36"
          Position                [170, 55, 210, 85]
          Gain                    "0.01666667"
        }
        Block {
          BlockType               DiscreteIntegrator
          Name                    "Level_Integrator"
          SID                     "37"
          Position                [240, 50, 290, 90]
          InitialCondition        "8.0"
          LimitOutput             on
          UpperSaturationLimit    "10.0"
          LowerSaturationLimit    "0.0"
        }
        Block {
          BlockType               Constant
          Name                    "Process_Head_Flow"
          SID                     "38"
          Position                [240, 130, 280, 150]
          Value                   "3.85"
        }
        Block {
          BlockType               Outport
          Name                    "PW_1_Outflow"
          SID                     "39"
          Position                [350, 130, 380, 150]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "V_T01"
          SID                     "40"
          Position                [350, 60, 380, 80]
          Port                    "2"
        }
        Line {
          SrcBlock                "PW_8_Return"
          SrcPort                 1
          DstBlock                "Sum_Net"
          DstPort                 1
        }
        Line {
          SrcBlock                "From_P1_Q"
          SrcPort                 1
          Points                  [10, 0]
          DstBlock                "Sum_Net"
          DstPort                 2
        }
        Line {
          SrcBlock                "Sum_Net"
          SrcPort                 1
          DstBlock                "Lpm_to_Lps"
          DstPort                 1
        }
        Line {
          SrcBlock                "Lpm_to_Lps"
          SrcPort                 1
          DstBlock                "Level_Integrator"
          DstPort                 1
        }
        Line {
          SrcBlock                "Level_Integrator"
          SrcPort                 1
          DstBlock                "V_T01"
          DstPort                 1
        }
        Line {
          SrcBlock                "Process_Head_Flow"
          SrcPort                 1
          DstBlock                "PW_1_Outflow"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               Goto
      Name                    "Goto_T01_Level"
      SID                     "41"
      Position                [200, 400, 270, 420]
      GotoTag                 "T01_Level"
      ShowName                off
    }

    // Solenoid Valve: OV-01 (Solenoid)
    Block {
      BlockType               From
      Name                    "From_OV01_Cmd"
      SID                     "42"
      Position                [220, 320, 290, 340]
      GotoTag                 "OV01_Cmd"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "OV-01_Solenoid_Valve"
      SID                     "43"
      Ports                   [2, 1]
      Position                [310, 345, 380, 395]
      ForegroundColor         "red"
      BackgroundColor         "yellow"
      System {
        Name                    "OV-01_Solenoid_Valve"
        Location                [100, 100, 450, 300]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "PW_1"
          SID                     "44"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Cmd_Open"
          SID                     "45"
          Position                [30, 90, 60, 110]
          Port                    "2"
        }
        Block {
          BlockType               Product
          Name                    "Valve_Mult"
          SID                     "46"
          Ports                   [2, 1]
          Position                [120, 40, 150, 95]
        }
        Block {
          BlockType               Outport
          Name                    "PW_2"
          SID                     "47"
          Position                [200, 60, 230, 80]
          Port                    "1"
        }
        Line {
          SrcBlock                "PW_1"
          SrcPort                 1
          DstBlock                "Valve_Mult"
          DstPort                 1
        }
        Line {
          SrcBlock                "Cmd_Open"
          SrcPort                 1
          Points                  [40, 0]
          DstBlock                "Valve_Mult"
          DstPort                 2
        }
        Line {
          SrcBlock                "Valve_Mult"
          SrcPort                 1
          DstBlock                "PW_2"
          DstPort                 1
        }
      }
    }

    // Tee Junction: TE-01
    Block {
      BlockType               Sum
      Name                    "TE-01_Tee_Junction"
      SID                     "48"
      Ports                   [2, 1]
      Position                [525, 355, 555, 385]
      ForegroundColor         "darkGreen"
      BackgroundColor         "cyan"
      Inputs                  "++"
    }

    // Process Feed Pump: P-01
    Block {
      BlockType               From
      Name                    "From_P1_Duty"
      SID                     "49"
      Position                [590, 320, 660, 340]
      GotoTag                 "P1_Duty"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "P-01_Feed_Pump"
      SID                     "50"
      Ports                   [2, 1]
      Position                [680, 345, 750, 395]
      ForegroundColor         "orange"
      BackgroundColor         "goldenrod"
      System {
        Name                    "P-01_Feed_Pump"
        Location                [100, 100, 500, 320]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Fluid_In"
          SID                     "51"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Duty_Cmd"
          SID                     "52"
          Position                [30, 90, 60, 110]
          Port                    "2"
        }
        Block {
          BlockType               Gain
          Name                    "Duty_Frac"
          SID                     "53"
          Position                [90, 85, 130, 115]
          Gain                    "0.01"
        }
        Block {
          BlockType               Product
          Name                    "Pump_Mult"
          SID                     "54"
          Ports                   [2, 1]
          Position                [160, 40, 190, 95]
        }
        Block {
          BlockType               Goto
          Name                    "Goto_Internal_P1"
          SID                     "55"
          Position                [230, 110, 300, 130]
          GotoTag                 "Q_P1_Act"
        }
        Block {
          BlockType               Outport
          Name                    "PW_4"
          SID                     "56"
          Position                [250, 60, 280, 80]
          Port                    "1"
        }
        Line {
          SrcBlock                "Fluid_In"
          SrcPort                 1
          DstBlock                "Pump_Mult"
          DstPort                 1
        }
        Line {
          SrcBlock                "Duty_Cmd"
          SrcPort                 1
          DstBlock                "Duty_Frac"
          DstPort                 1
        }
        Line {
          SrcBlock                "Duty_Frac"
          SrcPort                 1
          Points                  [10, 0]
          DstBlock                "Pump_Mult"
          DstPort                 2
        }
        Line {
          SrcBlock                "Pump_Mult"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "PW_4"
            DstPort               1
          }
          Branch {
            Points                [0, 50]
            DstBlock              "Goto_Internal_P1"
            DstPort               1
          }
        }
      }
    }

    // External Fluid Disturbance
    Block {
      BlockType               SubSystem
      Name                    "External_Fluid"
      SID                     "57"
      Ports                   [0, 1]
      Position                [870, 240, 950, 280]
      ForegroundColor         "magenta"
      BackgroundColor         "magenta"
      System {
        Name                    "External_Fluid"
        Location                [100, 100, 450, 280]
        Open                    off
        Block {
          BlockType               DiscretePulseGenerator
          Name                    "Dist_Pulse"
          SID                     "58"
          Position                [40, 50, 80, 90]
          Period                  "250"
          PulseWidth              "30"
          PhaseDelay              "180"
          SampleTime              "0.001"
        }
        Block {
          BlockType               Gain
          Name                    "Dist_Gain"
          SID                     "59"
          Position                [130, 55, 170, 85]
          Gain                    "0.8"
        }
        Block {
          BlockType               Outport
          Name                    "Q_Ext"
          SID                     "60"
          Position                [220, 60, 250, 80]
          Port                    "1"
        }
        Line {
          SrcBlock                "Dist_Pulse"
          SrcPort                 1
          DstBlock                "Dist_Gain"
          DstPort                 1
        }
        Line {
          SrcBlock                "Dist_Gain"
          SrcPort                 1
          DstBlock                "Q_Ext"
          DstPort                 1
        }
      }
    }

    // Sump Tank: S-01 (4.2 L Sump)
    Block {
      BlockType               SubSystem
      Name                    "S-01_Sump_4p2L"
      SID                     "61"
      Ports                   [2, 2]
      Position                [860, 335, 960, 415]
      ForegroundColor         "red"
      BackgroundColor         "orange"
      System {
        Name                    "S-01_Sump_4p2L"
        Location                [100, 100, 750, 450]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "PW_4"
          SID                     "62"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Q_Ext"
          SID                     "63"
          Position                [30, 90, 60, 110]
          Port                    "2"
        }
        Block {
          BlockType               From
          Name                    "From_P2_Q"
          SID                     "64"
          Position                [30, 140, 90, 160]
          GotoTag                 "Q_P2_Act"
        }
        Block {
          BlockType               Sum
          Name                    "Sum_Sump"
          SID                     "65"
          Ports                   [3, 1]
          Position                [130, 40, 150, 140]
          Inputs                  "++-"
        }
        Block {
          BlockType               Gain
          Name                    "Lpm_to_Lps"
          SID                     "66"
          Position                [180, 75, 220, 105]
          Gain                    "0.01666667"
        }
        Block {
          BlockType               DiscreteIntegrator
          Name                    "Sump_Integrator"
          SID                     "67"
          Position                [250, 70, 300, 110]
          InitialCondition        "0.0"
          LimitOutput             on
          UpperSaturationLimit    "4.2"
          LowerSaturationLimit    "0.0"
        }
        Block {
          BlockType               Constant
          Name                    "Recirc_Capacity"
          SID                     "68"
          Position                [250, 170, 290, 190]
          Value                   "4.20"
        }
        Block {
          BlockType               Outport
          Name                    "V_Sump"
          SID                     "69"
          Position                [360, 80, 390, 100]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "PW_5_Drain"
          SID                     "70"
          Position                [360, 170, 390, 190]
          Port                    "2"
        }
        Line {
          SrcBlock                "PW_4"
          SrcPort                 1
          DstBlock                "Sum_Sump"
          DstPort                 1
        }
        Line {
          SrcBlock                "Q_Ext"
          SrcPort                 1
          DstBlock                "Sum_Sump"
          DstPort                 2
        }
        Line {
          SrcBlock                "From_P2_Q"
          SrcPort                 1
          Points                  [20, 0]
          DstBlock                "Sum_Sump"
          DstPort                 3
        }
        Line {
          SrcBlock                "Sum_Sump"
          SrcPort                 1
          DstBlock                "Lpm_to_Lps"
          DstPort                 1
        }
        Line {
          SrcBlock                "Lpm_to_Lps"
          SrcPort                 1
          DstBlock                "Sump_Integrator"
          DstPort                 1
        }
        Line {
          SrcBlock                "Sump_Integrator"
          SrcPort                 1
          DstBlock                "V_Sump"
          DstPort                 1
        }
        Line {
          SrcBlock                "Recirc_Capacity"
          SrcPort                 1
          DstBlock                "PW_5_Drain"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               Goto
      Name                    "Goto_Sump_Level"
      SID                     "71"
      Position                [1000, 335, 1070, 355]
      GotoTag                 "Sump_Level"
      ShowName                off
    }

    // Float Switch: FS-01 (Schmitt Trigger)
    Block {
      BlockType               Relay
      Name                    "FS-01_Float_Switch"
      SID                     "72"
      Position                [1020, 370, 1070, 410]
      ForegroundColor         "red"
      BackgroundColor         "lightBlue"
      OnSwitchValue           "3.5"
      OffSwitchValue          "2.5"
      OnOutputValue           "1"
      OffOutputValue          "0"
    }

    Block {
      BlockType               Goto
      Name                    "Goto_FS01_Float"
      SID                     "73"
      Position                [1100, 380, 1180, 400]
      GotoTag                 "FS01_Float"
      ShowName                off
    }

    // Recirculation Pump: P-02 (Orientation left, flows right-to-left)
    Block {
      BlockType               From
      Name                    "From_P2_Duty"
      SID                     "74"
      Position                [990, 520, 1060, 540]
      GotoTag                 "P2_Duty"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "P-02_Recirc_Pump"
      SID                     "75"
      Ports                   [2, 1]
      Position                [865, 470, 935, 520]
      Orientation             "left"
      ForegroundColor         "orange"
      BackgroundColor         "goldenrod"
      System {
        Name                    "P-02_Recirc_Pump"
        Location                [100, 100, 500, 320]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "PW_5"
          SID                     "76"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Duty_Cmd"
          SID                     "77"
          Position                [30, 90, 60, 110]
          Port                    "2"
        }
        Block {
          BlockType               Gain
          Name                    "Duty_Frac"
          SID                     "78"
          Position                [90, 85, 130, 115]
          Gain                    "0.01"
        }
        Block {
          BlockType               Product
          Name                    "Pump_Mult"
          SID                     "79"
          Ports                   [2, 1]
          Position                [160, 40, 190, 95]
        }
        Block {
          BlockType               Goto
          Name                    "Goto_Internal_P2"
          SID                     "80"
          Position                [230, 110, 300, 130]
          GotoTag                 "Q_P2_Act"
        }
        Block {
          BlockType               Outport
          Name                    "PW_6"
          SID                     "81"
          Position                [250, 60, 280, 80]
          Port                    "1"
        }
        Line {
          SrcBlock                "PW_5"
          SrcPort                 1
          DstBlock                "Pump_Mult"
          DstPort                 1
        }
        Line {
          SrcBlock                "Duty_Cmd"
          SrcPort                 1
          DstBlock                "Duty_Frac"
          DstPort                 1
        }
        Line {
          SrcBlock                "Duty_Frac"
          SrcPort                 1
          Points                  [10, 0]
          DstBlock                "Pump_Mult"
          DstPort                 2
        }
        Line {
          SrcBlock                "Pump_Mult"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "PW_6"
            DstPort               1
          }
          Branch {
            Points                [0, 50]
            DstBlock              "Goto_Internal_P2"
            DstPort               1
          }
        }
      }
    }

    // Manual Return Valve: BV-02 (Orientation left)
    Block {
      BlockType               SubSystem
      Name                    "BV-02_Manual_Valve"
      SID                     "82"
      Ports                   [1, 1]
      Position                [695, 470, 765, 520]
      Orientation             "left"
      ForegroundColor         "darkGreen"
      BackgroundColor         "yellow"
      System {
        Name                    "BV-02_Manual_Valve"
        Location                [100, 100, 400, 250]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "PW_6"
          SID                     "83"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Gain
          Name                    "Through_Gain"
          SID                     "84"
          Position                [110, 35, 150, 65]
          Gain                    "1.0"
        }
        Block {
          BlockType               Outport
          Name                    "PW_7"
          SID                     "85"
          Position                [200, 40, 230, 60]
          Port                    "1"
        }
        Line {
          SrcBlock                "PW_6"
          SrcPort                 1
          DstBlock                "Through_Gain"
          DstPort                 1
        }
        Line {
          SrcBlock                "Through_Gain"
          SrcPort                 1
          DstBlock                "PW_7"
          DstPort                 1
        }
      }
    }

    // Flow Transmitter: FT-01 (Orientation left, field instrument circle)
    Block {
      BlockType               SubSystem
      Name                    "FT-01_Flow_Transmitter"
      SID                     "86"
      Ports                   [1, 1]
      Position                [490, 465, 570, 525]
      Orientation             "left"
      ForegroundColor         "magenta"
      BackgroundColor         "cyan"
      System {
        Name                    "FT-01_Flow_Transmitter"
        Location                [100, 100, 450, 280]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "PW_7"
          SID                     "87"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Gain
          Name                    "Turbine_Filter"
          SID                     "88"
          Position                [110, 35, 150, 65]
          Gain                    "1.0"
        }
        Block {
          BlockType               Outport
          Name                    "PW_8"
          SID                     "89"
          Position                [200, 40, 230, 60]
          Port                    "1"
        }
        Line {
          SrcBlock                "PW_7"
          SrcPort                 1
          DstBlock                "Turbine_Filter"
          DstPort                 1
        }
        Line {
          SrcBlock                "Turbine_Filter"
          SrcPort                 1
          DstBlock                "PW_8"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               Goto
      Name                    "Goto_FT01_Flow"
      SID                     "90"
      Position                [470, 435, 550, 455]
      Orientation             "left"
      GotoTag                 "FT01_Flow"
      ShowName                off
    }

    // =========================================================================
    // SECTION 2: EMBEDDED ESP32 AUTOMATION CONTROLLER & OPERATOR HMI
    // =========================================================================

    Block {
      BlockType               Step
      Name                    "Rig_Push_Button"
      SID                     "91"
      Position                [50, 600, 120, 630]
      Time                    "1.0"
      Before                  "0"
      After                   "1"
    }

    Block {
      BlockType               From
      Name                    "From_FS01_In"
      SID                     "92"
      Position                [160, 625, 230, 645]
      GotoTag                 "FS01_Float"
      ShowName                off
    }

    Block {
      BlockType               From
      Name                    "From_FT01_In"
      SID                     "93"
      Position                [160, 655, 230, 675]
      GotoTag                 "FT01_Flow"
      ShowName                off
    }

    Block {
      BlockType               From
      Name                    "From_TotVol_In"
      SID                     "94"
      Position                [160, 685, 230, 705]
      GotoTag                 "Total_Volume"
      ShowName                off
    }

    Block {
      BlockType               Step
      Name                    "Flush_Ball_Valve_BV01"
      SID                     "95"
      Position                [50, 715, 120, 745]
      Time                    "70.0"
      Before                  "0"
      After                   "1"
    }

    Block {
      BlockType               Step
      Name                    "Disturbance_Valve"
      SID                     "96"
      Position                [50, 765, 120, 795]
      Time                    "180.0"
      Before                  "0"
      After                   "1"
    }

    Block {
      BlockType               Clock
      Name                    "Master_Clock"
      SID                     "97"
      Position                [60, 815, 100, 845]
    }

    Block {
      BlockType               Mux
      Name                    "Mux_FSM_Inputs"
      SID                     "98"
      Ports                   [7, 1]
      Position                [265, 595, 275, 855]
      Inputs                  "7"
    }

    Block {
      BlockType               MATLABFcn
      Name                    "ESP32_Automation_FSM"
      SID                     "99"
      Ports                   [1, 1]
      Position                [310, 655, 430, 795]
      ForegroundColor         "navy"
      BackgroundColor         "lightBlue"
      MATLABFcn               "lam_controller_wrapper"
      OutputDimensions        "6"
    }

    Block {
      BlockType               Demux
      Name                    "Demux_FSM_Outputs"
      SID                     "100"
      Ports                   [1, 6]
      Position                [465, 655, 475, 795]
      Outputs                 "6"
    }

    Block {
      BlockType               Goto
      Name                    "Goto_P1_Duty"
      SID                     "101"
      Position                [510, 655, 580, 675]
      GotoTag                 "P1_Duty"
      ShowName                off
    }

    Block {
      BlockType               Goto
      Name                    "Goto_P2_Duty"
      SID                     "102"
      Position                [510, 680, 580, 700]
      GotoTag                 "P2_Duty"
      ShowName                off
    }

    Block {
      BlockType               Goto
      Name                    "Goto_P3_Duty"
      SID                     "103"
      Position                [510, 705, 580, 725]
      GotoTag                 "P3_Duty"
      ShowName                off
    }

    Block {
      BlockType               Goto
      Name                    "Goto_OV01_Cmd"
      SID                     "104"
      Position                [510, 730, 580, 750]
      GotoTag                 "OV01_Cmd"
      ShowName                off
    }

    Block {
      BlockType               Goto
      Name                    "Goto_BV01_Cmd"
      SID                     "105"
      Position                [510, 755, 580, 775]
      GotoTag                 "BV01_Cmd"
      ShowName                off
    }

    Block {
      BlockType               Goto
      Name                    "Goto_FSM_State"
      SID                     "106"
      Position                [510, 780, 580, 800]
      GotoTag                 "FSM_State"
      ShowName                off
    }

    // =========================================================================
    // SECTION 3: FLUID MECHANICS & SCADA GAUGES
    // =========================================================================

    // Fluid Mechanics Computer
    Block {
      BlockType               From
      Name                    "From_FT01_Hydro"
      SID                     "107"
      Position                [660, 620, 730, 640]
      GotoTag                 "FT01_Flow"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "Hydrodynamics_Computer"
      SID                     "108"
      Ports                   [1, 2]
      Position                [760, 605, 870, 665]
      ForegroundColor         "purple"
      BackgroundColor         "cyan"
      System {
        Name                    "Hydrodynamics_Computer"
        Location                [100, 100, 550, 320]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Q_FT01"
          SID                     "109"
          Position                [30, 50, 60, 70]
          Port                    "1"
        }
        Block {
          BlockType               Gain
          Name                    "Gain_Vel"
          SID                     "110"
          Position                [120, 45, 170, 75]
          Gain                    "0.331572"
        }
        Block {
          BlockType               Gain
          Name                    "Gain_Re"
          SID                     "111"
          Position                [220, 85, 270, 115]
          Gain                    "8000"
        }
        Block {
          BlockType               Outport
          Name                    "Velocity_mps"
          SID                     "112"
          Position                [320, 50, 350, 70]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "Reynolds_Num"
          SID                     "113"
          Position                [320, 90, 350, 110]
          Port                    "2"
        }
        Line {
          SrcBlock                "Q_FT01"
          SrcPort                 1
          DstBlock                "Gain_Vel"
          DstPort                 1
        }
        Line {
          SrcBlock                "Gain_Vel"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "Velocity_mps"
            DstPort               1
          }
          Branch {
            Points                [0, 40]
            DstBlock              "Gain_Re"
            DstPort               1
          }
        }
        Line {
          SrcBlock                "Gain_Re"
          SrcPort                 1
          DstBlock                "Reynolds_Num"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               Goto
      Name                    "Goto_Reynolds_Num"
      SID                     "114"
      Position                [900, 640, 970, 660]
      GotoTag                 "Reynolds_Num"
      ShowName                off
    }

    // Totalizer Computer
    Block {
      BlockType               From
      Name                    "From_FT01_Tot"
      SID                     "115"
      Position                [660, 700, 730, 720]
      GotoTag                 "FT01_Flow"
      ShowName                off
    }

    Block {
      BlockType               SubSystem
      Name                    "Totalizer_Cumulative_Volume"
      SID                     "116"
      Ports                   [1, 1]
      Position                [760, 690, 860, 735]
      ForegroundColor         "magenta"
      BackgroundColor         "lightBlue"
      System {
        Name                    "Totalizer_Cumulative_Volume"
        Location                [100, 100, 450, 260]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "Q_Lpm"
          SID                     "117"
          Position                [30, 40, 60, 60]
          Port                    "1"
        }
        Block {
          BlockType               Gain
          Name                    "Gain_Lpm_to_Lps"
          SID                     "118"
          Position                [100, 35, 140, 65]
          Gain                    "0.01666667"
        }
        Block {
          BlockType               DiscreteIntegrator
          Name                    "Integrator_Volume"
          SID                     "119"
          Position                [180, 30, 230, 70]
          InitialCondition        "0.0"
        }
        Block {
          BlockType               Outport
          Name                    "Total_Liters"
          SID                     "120"
          Position                [280, 40, 310, 60]
          Port                    "1"
        }
        Line {
          SrcBlock                "Q_Lpm"
          SrcPort                 1
          DstBlock                "Gain_Lpm_to_Lps"
          DstPort                 1
        }
        Line {
          SrcBlock                "Gain_Lpm_to_Lps"
          SrcPort                 1
          DstBlock                "Integrator_Volume"
          DstPort                 1
        }
        Line {
          SrcBlock                "Integrator_Volume"
          SrcPort                 1
          DstBlock                "Total_Liters"
          DstPort                 1
        }
      }
    }

    Block {
      BlockType               Goto
      Name                    "Goto_Total_Vol"
      SID                     "121"
      Position                [890, 705, 960, 725]
      GotoTag                 "Total_Volume"
      ShowName                off
    }

    // Live SCADA Displays Column
    Block {
      BlockType               From
      Name                    "Disp_From_T01"
      SID                     "122"
      Position                [1020, 600, 1085, 620]
      GotoTag                 "T01_Level"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_10L_Tank_L"
      SID                     "123"
      Position                [1110, 595, 1180, 625]
      Decimation              "1"
    }

    Block {
      BlockType               From
      Name                    "Disp_From_Sump"
      SID                     "124"
      Position                [1020, 640, 1085, 660]
      GotoTag                 "Sump_Level"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_Sump_Vessel_L"
      SID                     "125"
      Position                [1110, 635, 1180, 665]
      Decimation              "1"
    }

    Block {
      BlockType               From
      Name                    "Disp_From_T02"
      SID                     "126"
      Position                [1020, 680, 1085, 700]
      GotoTag                 "T02_Level"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_Flush_Tank_L"
      SID                     "127"
      Position                [1110, 675, 1180, 705]
      Decimation              "1"
    }

    Block {
      BlockType               From
      Name                    "Disp_From_FT01"
      SID                     "128"
      Position                [1020, 720, 1085, 740]
      GotoTag                 "FT01_Flow"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_FT01_Flow_Lpm"
      SID                     "129"
      Position                [1110, 715, 1180, 745]
      Decimation              "1"
    }

    Block {
      BlockType               From
      Name                    "Disp_From_TotVol"
      SID                     "130"
      Position                [1020, 760, 1085, 780]
      GotoTag                 "Total_Volume"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_Cumulative_Vol_L"
      SID                     "131"
      Position                [1110, 755, 1180, 785]
      Decimation              "1"
    }

    Block {
      BlockType               From
      Name                    "Disp_From_State"
      SID                     "132"
      Position                [1020, 800, 1085, 820]
      GotoTag                 "FSM_State"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_FSM_State_Code"
      SID                     "133"
      Position                [1110, 795, 1180, 825]
      Decimation              "1"
    }

    Block {
      BlockType               From
      Name                    "Disp_From_Re"
      SID                     "134"
      Position                [1020, 840, 1085, 860]
      GotoTag                 "Reynolds_Num"
      ShowName                off
    }
    Block {
      BlockType               Display
      Name                    "Disp_Reynolds_Number"
      SID                     "135"
      Position                [1110, 835, 1180, 865]
      Decimation              "1"
    }

    // =========================================================================
    // SECTION 4: INDUSTRIAL SCOPES & DATA LOGGERS
    // =========================================================================

    // Tanks Scope
    Block {
      BlockType               From
      Name                    "Scope_From_T01"
      SID                     "136"
      Position                [1240, 595, 1300, 615]
      GotoTag                 "T01_Level"
      ShowName                off
    }
    Block {
      BlockType               From
      Name                    "Scope_From_Sump"
      SID                     "137"
      Position                [1240, 620, 1300, 640]
      GotoTag                 "Sump_Level"
      ShowName                off
    }
    Block {
      BlockType               From
      Name                    "Scope_From_T02"
      SID                     "138"
      Position                [1240, 645, 1300, 665]
      GotoTag                 "T02_Level"
      ShowName                off
    }
    Block {
      BlockType               Mux
      Name                    "Mux_Tanks"
      SID                     "139"
      Ports                   [3, 1]
      Position                [1330, 595, 1340, 665]
      Inputs                  "3"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Process_Tanks"
      SID                     "140"
      Position                [1370, 610, 1420, 650]
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_Tanks"
      SID                     "141"
      Position                [1450, 620, 1530, 640]
      VariableName            "tank_levels"
    }

    // Pump Duties Scope
    Block {
      BlockType               From
      Name                    "Scope_From_P1"
      SID                     "142"
      Position                [1240, 685, 1300, 705]
      GotoTag                 "P1_Duty"
      ShowName                off
    }
    Block {
      BlockType               From
      Name                    "Scope_From_P2"
      SID                     "143"
      Position                [1240, 710, 1300, 730]
      GotoTag                 "P2_Duty"
      ShowName                off
    }
    Block {
      BlockType               From
      Name                    "Scope_From_P3"
      SID                     "144"
      Position                [1240, 735, 1300, 755]
      GotoTag                 "P3_Duty"
      ShowName                off
    }
    Block {
      BlockType               Mux
      Name                    "Mux_Duties"
      SID                     "145"
      Ports                   [3, 1]
      Position                [1330, 685, 1340, 755]
      Inputs                  "3"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Pump_Duties"
      SID                     "146"
      Position                [1370, 700, 1420, 740]
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_Duties"
      SID                     "147"
      Position                [1450, 710, 1530, 730]
      VariableName            "pump_duties"
    }

    // FT01 Flow Sensor Scope
    Block {
      BlockType               From
      Name                    "Scope_From_FT01"
      SID                     "148"
      Position                [1240, 775, 1300, 795]
      GotoTag                 "FT01_Flow"
      ShowName                off
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Flow_Sensor_FT01"
      SID                     "149"
      Position                [1370, 765, 1420, 805]
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_FT01"
      SID                     "150"
      Position                [1450, 775, 1530, 795]
      VariableName            "ft01_flow"
    }

    // Automation State Scope
    Block {
      BlockType               From
      Name                    "Scope_From_State"
      SID                     "151"
      Position                [1240, 830, 1300, 850]
      GotoTag                 "FSM_State"
      ShowName                off
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Automation_State"
      SID                     "152"
      Position                [1370, 820, 1420, 860]
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_State"
      SID                     "153"
      Position                [1450, 830, 1530, 850]
      VariableName            "system_state"
    }

    // Reynolds Number Scope
    Block {
      BlockType               From
      Name                    "Scope_From_Re"
      SID                     "154"
      Position                [1240, 885, 1300, 905]
      GotoTag                 "Reynolds_Num"
      ShowName                off
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Reynolds_Number"
      SID                     "155"
      Position                [1370, 875, 1420, 915]
    }

    // =========================================================================
    // LINES (P&ID Flow Piping - Exactly Matching Drawing PID-001)
    // =========================================================================

    // --- Vertical Flush Line (Top): T-02 -> BV-01 -> P-03 -> TE-01 ---
    Line {
      SrcBlock                "T-02_4p2L_Flush"
      SrcPort                 1
      DstBlock                "Goto_T02_Level"
      DstPort                 1
    }
    Line {
      SrcBlock                "T-02_4p2L_Flush"
      SrcPort                 2
      Points                  [10, 0; 0, 50; -60, 0]
      DstBlock                "BV-01_Manual_Valve"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_BV01_Cmd"
      SrcPort                 1
      Points                  [15, 0]
      DstBlock                "BV-01_Manual_Valve"
      DstPort                 2
    }
    Line {
      SrcBlock                "BV-01_Manual_Valve"
      SrcPort                 1
      Points                  [10, 0; 0, 65; -60, 0]
      DstBlock                "P-03_Flush_Pump"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_P3_Duty"
      SrcPort                 1
      Points                  [15, 0]
      DstBlock                "P-03_Flush_Pump"
      DstPort                 2
    }
    Line {
      SrcBlock                "P-03_Flush_Pump"
      SrcPort                 1
      Points                  [10, 0; 0, 90; -30, 0]
      DstBlock                "TE-01_Tee_Junction"
      DstPort                 2
    }

    // --- Horizontal Process Line (Left to Right): T-01 -> OV-01 -> TE-01 -> P-01 -> S-01 ---
    Line {
      SrcBlock                "T-01_10L_Process"
      SrcPort                 1
      Points                  [120, 0]
      DstBlock                "OV-01_Solenoid_Valve"
      DstPort                 1
    }
    Line {
      SrcBlock                "T-01_10L_Process"
      SrcPort                 2
      DstBlock                "Goto_T01_Level"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_OV01_Cmd"
      SrcPort                 1
      Points                  [10, 0; 0, 50]
      DstBlock                "OV-01_Solenoid_Valve"
      DstPort                 2
    }
    Line {
      SrcBlock                "OV-01_Solenoid_Valve"
      SrcPort                 1
      DstBlock                "TE-01_Tee_Junction"
      DstPort                 1
    }
    Line {
      SrcBlock                "TE-01_Tee_Junction"
      SrcPort                 1
      DstBlock                "P-01_Feed_Pump"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_P1_Duty"
      SrcPort                 1
      Points                  [10, 0; 0, 50]
      DstBlock                "P-01_Feed_Pump"
      DstPort                 2
    }
    Line {
      SrcBlock                "P-01_Feed_Pump"
      SrcPort                 1
      Points                  [90, 0]
      DstBlock                "S-01_Sump_4p2L"
      DstPort                 1
    }
    Line {
      SrcBlock                "External_Fluid"
      SrcPort                 1
      Points                  [10, 0; 0, 135; -120, 0]
      DstBlock                "S-01_Sump_4p2L"
      DstPort                 2
    }
    Line {
      SrcBlock                "S-01_Sump_4p2L"
      SrcPort                 1
      Points                  [20, 0]
      Branch {
        DstBlock              "Goto_Sump_Level"
        DstPort               1
      }
      Branch {
        Points                [0, 35]
        DstBlock              "FS-01_Float_Switch"
        DstPort               1
      }
    }
    Line {
      SrcBlock                "FS-01_Float_Switch"
      SrcPort                 1
      DstBlock                "Goto_FS01_Float"
      DstPort                 1
    }

    // --- Bottom Return Line (Right to Left): S-01 -> P-02 -> BV-02 -> FT-01 -> T-01 ---
    Line {
      SrcBlock                "S-01_Sump_4p2L"
      SrcPort                 2
      Points                  [15, 0; 0, 85; -30, 0]
      DstBlock                "P-02_Recirc_Pump"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_P2_Duty"
      SrcPort                 1
      Points                  [-20, 0; 0, -25]
      DstBlock                "P-02_Recirc_Pump"
      DstPort                 2
    }
    Line {
      SrcBlock                "P-02_Recirc_Pump"
      SrcPort                 1
      DstBlock                "BV-02_Manual_Valve"
      DstPort                 1
    }
    Line {
      SrcBlock                "BV-02_Manual_Valve"
      SrcPort                 1
      DstBlock                "FT-01_Flow_Transmitter"
      DstPort                 1
    }
    Line {
      SrcBlock                "FT-01_Flow_Transmitter"
      SrcPort                 1
      Points                  [-10, 0]
      Branch {
        Points                [0, -50]
        DstBlock              "Goto_FT01_Flow"
        DstPort               1
      }
      Branch {
        Points                [-440, 0; 0, -110]
        DstBlock              "T-01_10L_Process"
        DstPort               1
      }
    }

    // --- Embedded Controller Lines ---
    Line {
      SrcBlock                "Rig_Push_Button"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_FS01_In"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 2
    }
    Line {
      SrcBlock                "From_FT01_In"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 3
    }
    Line {
      SrcBlock                "From_TotVol_In"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 4
    }
    Line {
      SrcBlock                "Flush_Ball_Valve_BV01"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 5
    }
    Line {
      SrcBlock                "Disturbance_Valve"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 6
    }
    Line {
      SrcBlock                "Master_Clock"
      SrcPort                 1
      DstBlock                "Mux_FSM_Inputs"
      DstPort                 7
    }
    Line {
      SrcBlock                "Mux_FSM_Inputs"
      SrcPort                 1
      DstBlock                "ESP32_Automation_FSM"
      DstPort                 1
    }
    Line {
      SrcBlock                "ESP32_Automation_FSM"
      SrcPort                 1
      DstBlock                "Demux_FSM_Outputs"
      DstPort                 1
    }
    Line {
      SrcBlock                "Demux_FSM_Outputs"
      SrcPort                 1
      DstBlock                "Goto_P1_Duty"
      DstPort                 1
    }
    Line {
      SrcBlock                "Demux_FSM_Outputs"
      SrcPort                 2
      DstBlock                "Goto_P2_Duty"
      DstPort                 1
    }
    Line {
      SrcBlock                "Demux_FSM_Outputs"
      SrcPort                 3
      DstBlock                "Goto_P3_Duty"
      DstPort                 1
    }
    Line {
      SrcBlock                "Demux_FSM_Outputs"
      SrcPort                 4
      DstBlock                "Goto_OV01_Cmd"
      DstPort                 1
    }
    Line {
      SrcBlock                "Demux_FSM_Outputs"
      SrcPort                 5
      DstBlock                "Goto_BV01_Cmd"
      DstPort                 1
    }
    Line {
      SrcBlock                "Demux_FSM_Outputs"
      SrcPort                 6
      DstBlock                "Goto_FSM_State"
      DstPort                 1
    }

    // --- Fluid Mechanics & Totalizer Lines ---
    Line {
      SrcBlock                "From_FT01_Hydro"
      SrcPort                 1
      DstBlock                "Hydrodynamics_Computer"
      DstPort                 1
    }
    Line {
      SrcBlock                "Hydrodynamics_Computer"
      SrcPort                 2
      DstBlock                "Goto_Reynolds_Num"
      DstPort                 1
    }
    Line {
      SrcBlock                "From_FT01_Tot"
      SrcPort                 1
      DstBlock                "Totalizer_Cumulative_Volume"
      DstPort                 1
    }
    Line {
      SrcBlock                "Totalizer_Cumulative_Volume"
      SrcPort                 1
      DstBlock                "Goto_Total_Vol"
      DstPort                 1
    }

    // --- Displays Lines ---
    Line {
      SrcBlock                "Disp_From_T01"
      SrcPort                 1
      DstBlock                "Disp_10L_Tank_L"
      DstPort                 1
    }
    Line {
      SrcBlock                "Disp_From_Sump"
      SrcPort                 1
      DstBlock                "Disp_Sump_Vessel_L"
      DstPort                 1
    }
    Line {
      SrcBlock                "Disp_From_T02"
      SrcPort                 1
      DstBlock                "Disp_Flush_Tank_L"
      DstPort                 1
    }
    Line {
      SrcBlock                "Disp_From_FT01"
      SrcPort                 1
      DstBlock                "Disp_FT01_Flow_Lpm"
      DstPort                 1
    }
    Line {
      SrcBlock                "Disp_From_TotVol"
      SrcPort                 1
      DstBlock                "Disp_Cumulative_Vol_L"
      DstPort                 1
    }
    Line {
      SrcBlock                "Disp_From_State"
      SrcPort                 1
      DstBlock                "Disp_FSM_State_Code"
      DstPort                 1
    }
    Line {
      SrcBlock                "Disp_From_Re"
      SrcPort                 1
      DstBlock                "Disp_Reynolds_Number"
      DstPort                 1
    }

    // --- Scopes & Loggers Lines ---
    Line {
      SrcBlock                "Scope_From_T01"
      SrcPort                 1
      DstBlock                "Mux_Tanks"
      DstPort                 1
    }
    Line {
      SrcBlock                "Scope_From_Sump"
      SrcPort                 1
      DstBlock                "Mux_Tanks"
      DstPort                 2
    }
    Line {
      SrcBlock                "Scope_From_T02"
      SrcPort                 1
      DstBlock                "Mux_Tanks"
      DstPort                 3
    }
    Line {
      SrcBlock                "Mux_Tanks"
      SrcPort                 1
      Points                  [10, 0]
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
      SrcBlock                "Scope_From_P1"
      SrcPort                 1
      DstBlock                "Mux_Duties"
      DstPort                 1
    }
    Line {
      SrcBlock                "Scope_From_P2"
      SrcPort                 1
      DstBlock                "Mux_Duties"
      DstPort                 2
    }
    Line {
      SrcBlock                "Scope_From_P3"
      SrcPort                 1
      DstBlock                "Mux_Duties"
      DstPort                 3
    }
    Line {
      SrcBlock                "Mux_Duties"
      SrcPort                 1
      Points                  [10, 0]
      Branch {
        DstBlock              "Scope_Pump_Duties"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_Duties"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Scope_From_FT01"
      SrcPort                 1
      Points                  [35, 0]
      Branch {
        DstBlock              "Scope_Flow_Sensor_FT01"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_FT01"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Scope_From_State"
      SrcPort                 1
      Points                  [35, 0]
      Branch {
        DstBlock              "Scope_Automation_State"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_State"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Scope_From_Re"
      SrcPort                 1
      DstBlock                "Scope_Reynolds_Number"
      DstPort                 1
    }
  }
}
'''
    with open(r'd:\matalb_;lam\lam_stage2_system.mdl', 'w', encoding='utf-8') as f:
        f.write(mdl)
    print('Generated clean P&ID model at d:\\matalb_;lam\\lam_stage2_system.mdl')

    # Also overwrite build_full_pid_simulink_model.py so it matches
    code_content = f'''import sys

def build_pid_model():
    mdl = \'\'\'{mdl}\'\'\'
    with open(r'd:\\matalb_;lam\\lam_stage2_system.mdl', 'w', encoding='utf-8') as f:
        f.write(mdl)
    print('Successfully generated complete P&ID Flow Diagram Model at d:\\\\matalb_;lam\\\\lam_stage2_system.mdl')

if __name__ == '__main__':
    build_pid_model()
'''
    with open(r'd:\matalb_;lam\build_full_pid_simulink_model.py', 'w', encoding='utf-8') as f:
        f.write(code_content)
    print('Updated d:\\matalb_;lam\\build_full_pid_simulink_model.py')

if __name__ == '__main__':
    generate_pid_model()
