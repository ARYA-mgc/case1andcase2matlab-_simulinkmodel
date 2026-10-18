import os

def generate_human_model():
    mdl = '''Model {
  Name                    "lam_stage2_system"
  Version                 8.5
  MdlSubVersion           0
  SavedCharacterEncoding  "UTF-8"
  GraphicalInterface {
    NumRootInports        0
    NumRootOutports       0
    ParameterArgumentNames  ""
    ComputedModelVersion  "7.0"
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
  ModelVersionFormat      "7.%<AutoIncrement:1>"
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
    Location                [30, 40, 1500, 900]
    Open                    on
    ScreenColor             "white"
    ZoomFactor              "100"
    ReportName              "simulink-default.rpt"
    SIDHighWaterMark        "200"

    Annotation {
      SID                     "1"
      Name                    "LAM RESEARCH CHALLENGE 3.0 - STAGE 2 DIGITAL TWIN"
      Position                [700, 35, 700, 35]
      FontSize                14
      FontWeight              "bold"
    }
    Annotation {
      SID                     "2"
      Name                    "P&ID Dwg PID-001: Automated Chemical Distribution, Line Flush & Automatic Sump Protection Rig"
      Position                [700, 58, 700, 58]
      FontSize                10
    }

    // =========================================================================
    // 4 HIGH-LEVEL CLEAN BLOCKS (No spider-web wires, pure black and white)
    // =========================================================================

    // Block 1: HMI Operator Inputs
    Block {
      BlockType               SubSystem
      Name                    "HMI_Operator_Inputs"
      SID                     "10"
      Ports                   [0, 1]
      Position                [40, 160, 180, 300]
      System {
        Name                    "HMI_Operator_Inputs"
        Location                [100, 100, 450, 400]
        Open                    off
        Block {
          BlockType               Step
          Name                    "Rig_Push_Button"
          SID                     "11"
          Position                [30, 40, 90, 70]
          Time                    "1.0"
          Before                  "0"
          After                   "1"
        }
        Block {
          BlockType               Step
          Name                    "Flush_Ball_Valve_BV01"
          SID                     "12"
          Position                [30, 95, 90, 125]
          Time                    "70.0"
          Before                  "0"
          After                   "1"
        }
        Block {
          BlockType               Step
          Name                    "Disturbance_Valve"
          SID                     "13"
          Position                [30, 150, 90, 180]
          Time                    "180.0"
          Before                  "0"
          After                   "1"
        }
        Block {
          BlockType               Clock
          Name                    "Master_Clock"
          SID                     "14"
          Position                [40, 205, 80, 235]
        }
        Block {
          BlockType               Mux
          Name                    "Mux_HMI"
          SID                     "15"
          Ports                   [4, 1]
          Position                [160, 35, 170, 240]
          Inputs                  "4"
        }
        Block {
          BlockType               Outport
          Name                    "HMI_Cmds"
          SID                     "16"
          Position                [220, 130, 250, 150]
          Port                    "1"
        }
        Line {
          SrcBlock                "Rig_Push_Button"
          SrcPort                 1
          DstBlock                "Mux_HMI"
          DstPort                 1
        }
        Line {
          SrcBlock                "Flush_Ball_Valve_BV01"
          SrcPort                 1
          DstBlock                "Mux_HMI"
          DstPort                 2
        }
        Line {
          SrcBlock                "Disturbance_Valve"
          SrcPort                 1
          DstBlock                "Mux_HMI"
          DstPort                 3
        }
        Line {
          SrcBlock                "Master_Clock"
          SrcPort                 1
          DstBlock                "Mux_HMI"
          DstPort                 4
        }
        Line {
          SrcBlock                "Mux_HMI"
          SrcPort                 1
          DstBlock                "HMI_Cmds"
          DstPort                 1
        }
      }
    }

    // Block 2: ESP32 Automation Controller
    Block {
      BlockType               SubSystem
      Name                    "ESP32_Automation_Controller"
      SID                     "20"
      Ports                   [2, 2]
      Position                [250, 160, 430, 300]
      System {
        Name                    "ESP32_Automation_Controller"
        Location                [100, 100, 650, 450]
        Open                    off
        Block {
          BlockType               Inport
          Name                    "HMI_Cmds"
          SID                     "21"
          Position                [30, 50, 60, 70]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Sensor_Feedback"
          SID                     "22"
          Position                [30, 150, 60, 170]
          Port                    "2"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_HMI"
          SID                     "23"
          Ports                   [1, 4]
          Position                [100, 35, 105, 85]
          Outputs                 "4"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Sensors"
          SID                     "24"
          Ports                   [1, 5]
          Position                [100, 135, 105, 185]
          Outputs                 "5"
        }
        Block {
          BlockType               Mux
          Name                    "Mux_FSM"
          SID                     "25"
          Ports                   [7, 1]
          Position                [180, 40, 190, 240]
          Inputs                  "7"
        }
        Block {
          BlockType               MATLABFcn
          Name                    "Embedded_FSM_Logic"
          SID                     "26"
          Ports                   [1, 1]
          Position                [230, 115, 330, 165]
          MATLABFcn               "lam_controller_wrapper"
          OutputDimensions        "6"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_FSM"
          SID                     "27"
          Ports                   [1, 6]
          Position                [370, 100, 375, 180]
          Outputs                 "6"
        }
        Block {
          BlockType               Mux
          Name                    "Mux_Actuators"
          SID                     "28"
          Ports                   [5, 1]
          Position                [430, 80, 440, 160]
          Inputs                  "5"
        }
        Block {
          BlockType               Outport
          Name                    "Actuator_Commands"
          SID                     "29"
          Position                [480, 110, 510, 130]
          Port                    "1"
        }
        Block {
          BlockType               Outport
          Name                    "State_Code"
          SID                     "30"
          Position                [480, 160, 510, 180]
          Port                    "2"
        }
        Line {
          SrcBlock                "HMI_Cmds"
          SrcPort                 1
          DstBlock                "Demux_HMI"
          DstPort                 1
        }
        Line {
          SrcBlock                "Sensor_Feedback"
          SrcPort                 1
          DstBlock                "Demux_Sensors"
          DstPort                 1
        }
        // Demux_HMI: 1=Rig_PB, 2=BV01, 3=Dist, 4=Clock
        // Demux_Sensors: 1=FT01_Flow, 2=FS01_Float, 3=T01_Level, 4=Sump_Level, 5=Total_Volume
        // FSM input order: [PB, Float, Flow, TotVol, BV01, Dist, Time]
        Line {
          SrcBlock                "Demux_HMI"
          SrcPort                 1
          DstBlock                "Mux_FSM"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 2
          DstBlock                "Mux_FSM"
          DstPort                 2
        }
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 1
          DstBlock                "Mux_FSM"
          DstPort                 3
        }
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 5
          DstBlock                "Mux_FSM"
          DstPort                 4
        }
        Line {
          SrcBlock                "Demux_HMI"
          SrcPort                 2
          DstBlock                "Mux_FSM"
          DstPort                 5
        }
        Line {
          SrcBlock                "Demux_HMI"
          SrcPort                 3
          DstBlock                "Mux_FSM"
          DstPort                 6
        }
        Line {
          SrcBlock                "Demux_HMI"
          SrcPort                 4
          DstBlock                "Mux_FSM"
          DstPort                 7
        }
        Line {
          SrcBlock                "Mux_FSM"
          SrcPort                 1
          DstBlock                "Embedded_FSM_Logic"
          DstPort                 1
        }
        Line {
          SrcBlock                "Embedded_FSM_Logic"
          SrcPort                 1
          DstBlock                "Demux_FSM"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_FSM"
          SrcPort                 1
          DstBlock                "Mux_Actuators"
          DstPort                 1
        }
        Line {
          SrcBlock                "Demux_FSM"
          SrcPort                 2
          DstBlock                "Mux_Actuators"
          DstPort                 2
        }
        Line {
          SrcBlock                "Demux_FSM"
          SrcPort                 3
          DstBlock                "Mux_Actuators"
          DstPort                 3
        }
        Line {
          SrcBlock                "Demux_FSM"
          SrcPort                 4
          DstBlock                "Mux_Actuators"
          DstPort                 4
        }
        Line {
          SrcBlock                "Demux_FSM"
          SrcPort                 5
          DstBlock                "Mux_Actuators"
          DstPort                 5
        }
        Line {
          SrcBlock                "Demux_FSM"
          SrcPort                 6
          DstBlock                "State_Code"
          DstPort                 1
        }
        Line {
          SrcBlock                "Mux_Actuators"
          SrcPort                 1
          DstBlock                "Actuator_Commands"
          DstPort                 1
        }
      }
    }

    // Block 3: Hydraulic Process Plant (The complete P&ID loop matching Drawing PID-001)
    Block {
      BlockType               SubSystem
      Name                    "Hydraulic_Process_Plant_PID001"
      SID                     "40"
      Ports                   [1, 1]
      Position                [520, 160, 780, 300]
      System {
        Name                    "Hydraulic_Process_Plant_PID001"
        Location                [50, 50, 1250, 750]
        Open                    off

        Annotation {
          SID                     "41"
          Name                    "P&ID HYDRAULIC FLOW LOOP (Dwg No. PID-001)"
          Position                [600, 30, 600, 30]
          FontSize                12
          FontWeight              "bold"
        }

        // Inport from Controller: Actuator Commands
        Block {
          BlockType               Inport
          Name                    "Actuator_Commands"
          SID                     "42"
          Position                [30, 120, 60, 140]
          Port                    "1"
        }
        Block {
          BlockType               Demux
          Name                    "Demux_Cmds"
          SID                     "43"
          Ports                   [1, 5]
          Position                [90, 75, 95, 185]
          Outputs                 "5"
        }
        // Demux_Cmds: 1=P1_Duty, 2=P2_Duty, 3=P3_Duty, 4=OV01_Cmd, 5=BV01_Cmd

        // --- TOP FLUSH BRANCH: T-02 -> BV-01 -> P-03 -> TE-01 ---
        Block {
          BlockType               SubSystem
          Name                    "T-02_Flush_Tank_4p2L"
          SID                     "44"
          Ports                   [1, 2]
          Position                [480, 80, 580, 130]
          System {
            Name                    "T-02_Flush_Tank_4p2L"
            Location                [100, 100, 550, 300]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "Q_Drain"
              SID                     "45"
              Position                [30, 40, 60, 60]
              Port                    "1"
            }
            Block {
              BlockType               Gain
              Name                    "Lpm_to_Lps"
              SID                     "46"
              Position                [100, 35, 140, 65]
              Gain                    "-0.01666667"
            }
            Block {
              BlockType               DiscreteIntegrator
              Name                    "Level_Int"
              SID                     "47"
              Position                [180, 30, 230, 70]
              InitialCondition        "4.2"
              LimitOutput             on
              UpperSaturationLimit    "4.2"
              LowerSaturationLimit    "0.0"
            }
            Block {
              BlockType               Constant
              Name                    "Head_Capacity"
              SID                     "48"
              Position                [180, 110, 220, 130]
              Value                   "4.12"
            }
            Block {
              BlockType               Outport
              Name                    "V_T02"
              SID                     "49"
              Position                [280, 40, 310, 60]
              Port                    "1"
            }
            Block {
              BlockType               Outport
              Name                    "FW_2"
              SID                     "50"
              Position                [280, 110, 310, 130]
              Port                    "2"
            }
            Line {
              SrcBlock                "Q_Drain"
              SrcPort                 1
              DstBlock                "Lpm_to_Lps"
              DstPort                 1
            }
            Line {
              SrcBlock                "Lpm_to_Lps"
              SrcPort                 1
              DstBlock                "Level_Int"
              DstPort                 1
            }
            Line {
              SrcBlock                "Level_Int"
              SrcPort                 1
              DstBlock                "V_T02"
              DstPort                 1
            }
            Line {
              SrcBlock                "Head_Capacity"
              SrcPort                 1
              DstBlock                "FW_2"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "BV-01_Manual_Valve"
          SID                     "51"
          Ports                   [2, 1]
          Position                [490, 160, 570, 205]
          System {
            Name                    "BV-01_Manual_Valve"
            Location                [100, 100, 400, 250]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "Inflow"
              SID                     "52"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "Cmd"
              SID                     "53"
              Position                [30, 85, 60, 105]
              Port                    "2"
            }
            Block {
              BlockType               Product
              Name                    "Mult"
              SID                     "54"
              Ports                   [2, 1]
              Position                [120, 35, 150, 95]
            }
            Block {
              BlockType               Outport
              Name                    "Outflow"
              SID                     "55"
              Position                [200, 55, 230, 75]
              Port                    "1"
            }
            Line {
              SrcBlock                "Inflow"
              SrcPort                 1
              DstBlock                "Mult"
              DstPort                 1
            }
            Line {
              SrcBlock                "Cmd"
              SrcPort                 1
              Points                  [40, 0]
              DstBlock                "Mult"
              DstPort                 2
            }
            Line {
              SrcBlock                "Mult"
              SrcPort                 1
              DstBlock                "Outflow"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "P-03_Flush_Pump"
          SID                     "56"
          Ports                   [2, 1]
          Position                [490, 235, 570, 280]
          System {
            Name                    "P-03_Flush_Pump"
            Location                [100, 100, 450, 280]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "Fluid_In"
              SID                     "57"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "Duty"
              SID                     "58"
              Position                [30, 85, 60, 105]
              Port                    "2"
            }
            Block {
              BlockType               Gain
              Name                    "Gain_Duty"
              SID                     "59"
              Position                [90, 80, 130, 110]
              Gain                    "0.01"
            }
            Block {
              BlockType               Product
              Name                    "Mult"
              SID                     "60"
              Ports                   [2, 1]
              Position                [160, 35, 190, 95]
            }
            Block {
              BlockType               Outport
              Name                    "Q_P3"
              SID                     "61"
              Position                [240, 55, 270, 75]
              Port                    "1"
            }
            Line {
              SrcBlock                "Fluid_In"
              SrcPort                 1
              DstBlock                "Mult"
              DstPort                 1
            }
            Line {
              SrcBlock                "Duty"
              SrcPort                 1
              DstBlock                "Gain_Duty"
              DstPort                 1
            }
            Line {
              SrcBlock                "Gain_Duty"
              SrcPort                 1
              Points                  [10, 0]
              DstBlock                "Mult"
              DstPort                 2
            }
            Line {
              SrcBlock                "Mult"
              SrcPort                 1
              DstBlock                "Q_P3"
              DstPort                 1
            }
          }
        }

        // --- UPPER HORIZONTAL LINE: T-01 -> OV-01 -> TE-01 -> P-01 -> S-01 ---
        Block {
          BlockType               SubSystem
          Name                    "T-01_10L_Process"
          SID                     "62"
          Ports                   [2, 2]
          Position                [50, 320, 150, 390]
          System {
            Name                    "T-01_10L_Process"
            Location                [100, 100, 600, 350]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_8_Return"
              SID                     "63"
              Position                [30, 40, 60, 60]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "PW_1_Out"
              SID                     "64"
              Position                [30, 90, 60, 110]
              Port                    "2"
            }
            Block {
              BlockType               Sum
              Name                    "Sum_Net"
              SID                     "65"
              Ports                   [2, 1]
              Position                [110, 35, 130, 95]
              Inputs                  "+-"
            }
            Block {
              BlockType               Gain
              Name                    "Lpm_to_Lps"
              SID                     "66"
              Position                [160, 50, 200, 80]
              Gain                    "0.01666667"
            }
            Block {
              BlockType               DiscreteIntegrator
              Name                    "Level_Int"
              SID                     "67"
              Position                [230, 45, 280, 85]
              InitialCondition        "8.0"
              LimitOutput             on
              UpperSaturationLimit    "10.0"
              LowerSaturationLimit    "0.0"
            }
            Block {
              BlockType               Constant
              Name                    "Head_Flow"
              SID                     "68"
              Position                [230, 120, 270, 140]
              Value                   "3.85"
            }
            Block {
              BlockType               Outport
              Name                    "PW_1"
              SID                     "69"
              Position                [320, 120, 350, 140]
              Port                    "1"
            }
            Block {
              BlockType               Outport
              Name                    "V_T01"
              SID                     "70"
              Position                [320, 55, 350, 75]
              Port                    "2"
            }
            Line {
              SrcBlock                "PW_8_Return"
              SrcPort                 1
              DstBlock                "Sum_Net"
              DstPort                 1
            }
            Line {
              SrcBlock                "PW_1_Out"
              SrcPort                 1
              Points                  [15, 0; 0, -20]
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
              DstBlock                "Level_Int"
              DstPort                 1
            }
            Line {
              SrcBlock                "Level_Int"
              SrcPort                 1
              DstBlock                "V_T01"
              DstPort                 1
            }
            Line {
              SrcBlock                "Head_Flow"
              SrcPort                 1
              DstBlock                "PW_1"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "OV-01_Solenoid_Valve"
          SID                     "71"
          Ports                   [2, 1]
          Position                [240, 330, 320, 375]
          System {
            Name                    "OV-01_Solenoid_Valve"
            Location                [100, 100, 400, 250]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_1"
              SID                     "72"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "Cmd"
              SID                     "73"
              Position                [30, 85, 60, 105]
              Port                    "2"
            }
            Block {
              BlockType               Product
              Name                    "Mult"
              SID                     "74"
              Ports                   [2, 1]
              Position                [120, 35, 150, 95]
            }
            Block {
              BlockType               Outport
              Name                    "PW_2"
              SID                     "75"
              Position                [200, 55, 230, 75]
              Port                    "1"
            }
            Line {
              SrcBlock                "PW_1"
              SrcPort                 1
              DstBlock                "Mult"
              DstPort                 1
            }
            Line {
              SrcBlock                "Cmd"
              SrcPort                 1
              Points                  [40, 0]
              DstBlock                "Mult"
              DstPort                 2
            }
            Line {
              SrcBlock                "Mult"
              SrcPort                 1
              DstBlock                "PW_2"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               Sum
          Name                    "TE-01_Tee_Junction"
          SID                     "76"
          Ports                   [2, 1]
          Position                [510, 335, 540, 370]
          Inputs                  "++"
        }

        Block {
          BlockType               SubSystem
          Name                    "P-01_Feed_Pump"
          SID                     "77"
          Ports                   [2, 1]
          Position                [640, 330, 720, 375]
          System {
            Name                    "P-01_Feed_Pump"
            Location                [100, 100, 450, 280]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_3"
              SID                     "78"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "Duty"
              SID                     "79"
              Position                [30, 85, 60, 105]
              Port                    "2"
            }
            Block {
              BlockType               Gain
              Name                    "Gain_Duty"
              SID                     "80"
              Position                [90, 80, 130, 110]
              Gain                    "0.01"
            }
            Block {
              BlockType               Product
              Name                    "Mult"
              SID                     "81"
              Ports                   [2, 1]
              Position                [160, 35, 190, 95]
            }
            Block {
              BlockType               Outport
              Name                    "PW_4"
              SID                     "82"
              Position                [240, 55, 270, 75]
              Port                    "1"
            }
            Line {
              SrcBlock                "PW_3"
              SrcPort                 1
              DstBlock                "Mult"
              DstPort                 1
            }
            Line {
              SrcBlock                "Duty"
              SrcPort                 1
              DstBlock                "Gain_Duty"
              DstPort                 1
            }
            Line {
              SrcBlock                "Gain_Duty"
              SrcPort                 1
              Points                  [10, 0]
              DstBlock                "Mult"
              DstPort                 2
            }
            Line {
              SrcBlock                "Mult"
              SrcPort                 1
              DstBlock                "PW_4"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "External_Fluid"
          SID                     "83"
          Ports                   [0, 1]
          Position                [830, 235, 900, 270]
          System {
            Name                    "External_Fluid"
            Location                [100, 100, 400, 250]
            Open                    off
            Block {
              BlockType               DiscretePulseGenerator
              Name                    "Pulse"
              SID                     "84"
              Position                [30, 45, 70, 85]
              Period                  "250"
              PulseWidth              "30"
              PhaseDelay              "180"
              SampleTime              "0.001"
            }
            Block {
              BlockType               Gain
              Name                    "Gain"
              SID                     "85"
              Position                [110, 50, 150, 80]
              Gain                    "0.8"
            }
            Block {
              BlockType               Outport
              Name                    "Q_Ext"
              SID                     "86"
              Position                [200, 55, 230, 75]
              Port                    "1"
            }
            Line {
              SrcBlock                "Pulse"
              SrcPort                 1
              DstBlock                "Gain"
              DstPort                 1
            }
            Line {
              SrcBlock                "Gain"
              SrcPort                 1
              DstBlock                "Q_Ext"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "S-01_Sump_4p2L"
          SID                     "87"
          Ports                   [3, 2]
          Position                [820, 315, 920, 395]
          System {
            Name                    "S-01_Sump_4p2L"
            Location                [100, 100, 650, 400]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_4"
              SID                     "88"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "Q_Ext"
              SID                     "89"
              Position                [30, 85, 60, 105]
              Port                    "2"
            }
            Block {
              BlockType               Inport
              Name                    "PW_5_Drain"
              SID                     "90"
              Position                [30, 135, 60, 155]
              Port                    "3"
            }
            Block {
              BlockType               Sum
              Name                    "Sum_Sump"
              SID                     "91"
              Ports                   [3, 1]
              Position                [120, 35, 140, 140]
              Inputs                  "++-"
            }
            Block {
              BlockType               Gain
              Name                    "Lpm_to_Lps"
              SID                     "92"
              Position                [170, 70, 210, 100]
              Gain                    "0.01666667"
            }
            Block {
              BlockType               DiscreteIntegrator
              Name                    "Level_Int"
              SID                     "93"
              Position                [240, 65, 290, 105]
              InitialCondition        "0.0"
              LimitOutput             on
              UpperSaturationLimit    "4.2"
              LowerSaturationLimit    "0.0"
            }
            Block {
              BlockType               Constant
              Name                    "Capacity"
              SID                     "94"
              Position                [240, 150, 280, 170]
              Value                   "4.20"
            }
            Block {
              BlockType               Outport
              Name                    "V_Sump"
              SID                     "95"
              Position                [340, 75, 370, 95]
              Port                    "1"
            }
            Block {
              BlockType               Outport
              Name                    "PW_5"
              SID                     "96"
              Position                [340, 150, 370, 170]
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
              SrcBlock                "PW_5_Drain"
              SrcPort                 1
              Points                  [20, 0; 0, -25]
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
              DstBlock                "Level_Int"
              DstPort                 1
            }
            Line {
              SrcBlock                "Level_Int"
              SrcPort                 1
              DstBlock                "V_Sump"
              DstPort                 1
            }
            Line {
              SrcBlock                "Capacity"
              SrcPort                 1
              DstBlock                "PW_5"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               Relay
          Name                    "FS-01_Float_Switch"
          SID                     "97"
          Position                [980, 335, 1030, 375]
          OnSwitchValue           "3.5"
          OffSwitchValue          "2.5"
          OnOutputValue           "1"
          OffOutputValue          "0"
        }

        // --- LOWER RETURN LINE: S-01 -> P-02 -> BV-02 -> FT-01 -> T-01 ---
        Block {
          BlockType               SubSystem
          Name                    "P-02_Recirc_Pump"
          SID                     "98"
          Ports                   [2, 1]
          Position                [830, 460, 910, 505]
          Orientation             "left"
          System {
            Name                    "P-02_Recirc_Pump"
            Location                [100, 100, 450, 280]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_5"
              SID                     "99"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Inport
              Name                    "Duty"
              SID                     "100"
              Position                [30, 85, 60, 105]
              Port                    "2"
            }
            Block {
              BlockType               Gain
              Name                    "Gain_Duty"
              SID                     "101"
              Position                [90, 80, 130, 110]
              Gain                    "0.01"
            }
            Block {
              BlockType               Product
              Name                    "Mult"
              SID                     "102"
              Ports                   [2, 1]
              Position                [160, 35, 190, 95]
            }
            Block {
              BlockType               Outport
              Name                    "PW_6"
              SID                     "103"
              Position                [240, 55, 270, 75]
              Port                    "1"
            }
            Line {
              SrcBlock                "PW_5"
              SrcPort                 1
              DstBlock                "Mult"
              DstPort                 1
            }
            Line {
              SrcBlock                "Duty"
              SrcPort                 1
              DstBlock                "Gain_Duty"
              DstPort                 1
            }
            Line {
              SrcBlock                "Gain_Duty"
              SrcPort                 1
              Points                  [10, 0]
              DstBlock                "Mult"
              DstPort                 2
            }
            Line {
              SrcBlock                "Mult"
              SrcPort                 1
              DstBlock                "PW_6"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "BV-02_Manual_Valve"
          SID                     "104"
          Ports                   [1, 1]
          Position                [670, 460, 740, 505]
          Orientation             "left"
          System {
            Name                    "BV-02_Manual_Valve"
            Location                [100, 100, 350, 200]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_6"
              SID                     "105"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Gain
              Name                    "Gain"
              SID                     "106"
              Position                [100, 30, 140, 60]
              Gain                    "1.0"
            }
            Block {
              BlockType               Outport
              Name                    "PW_7"
              SID                     "107"
              Position                [180, 35, 210, 55]
              Port                    "1"
            }
            Line {
              SrcBlock                "PW_6"
              SrcPort                 1
              DstBlock                "Gain"
              DstPort                 1
            }
            Line {
              SrcBlock                "Gain"
              SrcPort                 1
              DstBlock                "PW_7"
              DstPort                 1
            }
          }
        }

        Block {
          BlockType               SubSystem
          Name                    "FT-01_Flow_Transmitter"
          SID                     "108"
          Ports                   [1, 1]
          Position                [480, 455, 560, 510]
          Orientation             "left"
          System {
            Name                    "FT-01_Flow_Transmitter"
            Location                [100, 100, 350, 200]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "PW_7"
              SID                     "109"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Gain
              Name                    "Sensor_Filter"
              SID                     "110"
              Position                [100, 30, 140, 60]
              Gain                    "1.0"
            }
            Block {
              BlockType               Outport
              Name                    "PW_8"
              SID                     "111"
              Position                [180, 35, 210, 55]
              Port                    "1"
            }
            Line {
              SrcBlock                "PW_7"
              SrcPort                 1
              DstBlock                "Sensor_Filter"
              DstPort                 1
            }
            Line {
              SrcBlock                "Sensor_Filter"
              SrcPort                 1
              DstBlock                "PW_8"
              DstPort                 1
            }
          }
        }

        // Telemetry Bus Output Mux
        Block {
          BlockType               Mux
          Name                    "Mux_Telemetry"
          SID                     "112"
          Ports                   [5, 1]
          Position                [1100, 300, 1110, 480]
          Inputs                  "5"
        }
        Block {
          BlockType               Outport
          Name                    "Sensor_Feedback"
          SID                     "113"
          Position                [1160, 380, 1190, 400]
          Port                    "1"
        }

        // --- INTERNAL CONNECTIONS OF THE P&ID CIRCUIT ---
        // Actuator commands routing from Demux_Cmds:
        // 1=P1_Duty, 2=P2_Duty, 3=P3_Duty, 4=OV01_Cmd, 5=BV01_Cmd
        Line {
          SrcBlock                "Demux_Cmds"
          SrcPort                 5
          Points                  [20, 0; 0, 20]
          DstBlock                "BV-01_Manual_Valve"
          DstPort                 2
        }
        Line {
          SrcBlock                "Demux_Cmds"
          SrcPort                 3
          Points                  [30, 0; 0, 140]
          DstBlock                "P-03_Flush_Pump"
          DstPort                 2
        }
        Line {
          SrcBlock                "Demux_Cmds"
          SrcPort                 4
          Points                  [40, 0; 0, 215]
          DstBlock                "OV-01_Solenoid_Valve"
          DstPort                 2
        }
        Line {
          SrcBlock                "Demux_Cmds"
          SrcPort                 1
          Points                  [50, 0; 0, 280]
          DstBlock                "P-01_Feed_Pump"
          DstPort                 2
        }
        Line {
          SrcBlock                "Demux_Cmds"
          SrcPort                 2
          Points                  [60, 0; 0, 395]
          DstBlock                "P-02_Recirc_Pump"
          DstPort                 2
        }

        // Vertical Flush Line: T-02 -> BV-01 -> P-03 -> TE-01
        Line {
          SrcBlock                "T-02_Flush_Tank_4p2L"
          SrcPort                 2
          Points                  [10, 0; 0, 45; -120, 0; 0, 10]
          DstBlock                "BV-01_Manual_Valve"
          DstPort                 1
        }
        Line {
          SrcBlock                "BV-01_Manual_Valve"
          SrcPort                 1
          Points                  [10, 0; 0, 40; -110, 0; 0, 25]
          DstBlock                "P-03_Flush_Pump"
          DstPort                 1
        }
        Line {
          SrcBlock                "P-03_Flush_Pump"
          SrcPort                 1
          Points                  [10, 0; 0, 30]
          Branch {
            Points                [-120, 0; 0, -215]
            DstBlock              "T-02_Flush_Tank_4p2L"
            DstPort               1
          }
          Branch {
            Points                [0, 50; -50, 0]
            DstBlock              "TE-01_Tee_Junction"
            DstPort               2
          }
        }

        // Horizontal Line: T-01 -> OV-01 -> TE-01 -> P-01 -> S-01
        Line {
          SrcBlock                "T-01_10L_Process"
          SrcPort                 1
          Points                  [30, 0; 0, -35]
          DstBlock                "OV-01_Solenoid_Valve"
          DstPort                 1
        }
        Line {
          SrcBlock                "OV-01_Solenoid_Valve"
          SrcPort                 1
          Points                  [20, 0; 0, -10]
          DstBlock                "TE-01_Tee_Junction"
          DstPort                 1
        }
        Line {
          SrcBlock                "TE-01_Tee_Junction"
          SrcPort                 1
          Points                  [40, 0; 0, -10]
          Branch {
            DstBlock              "P-01_Feed_Pump"
            DstPort               1
          }
          Branch {
            Points                [0, -70; -620, 0; 0, 90]
            DstBlock              "T-01_10L_Process"
            DstPort               2
          }
        }
        Line {
          SrcBlock                "P-01_Feed_Pump"
          SrcPort                 1
          Points                  [40, 0; 0, -25]
          DstBlock                "S-01_Sump_4p2L"
          DstPort                 1
        }
        Line {
          SrcBlock                "External_Fluid"
          SrcPort                 1
          Points                  [10, 0; 0, 90; -110, 0; 0, 15]
          DstBlock                "S-01_Sump_4p2L"
          DstPort                 2
        }

        // Sump Level to Float Switch
        Line {
          SrcBlock                "S-01_Sump_4p2L"
          SrcPort                 1
          Points                  [20, 0]
          Branch {
            DstBlock              "FS-01_Float_Switch"
            DstPort               1
          }
          Branch {
            Points                [0, 80; 120, 0; 0, 10]
            DstBlock              "Mux_Telemetry"
            DstPort               4
          }
        }

        // Float Switch to Telemetry
        Line {
          SrcBlock                "FS-01_Float_Switch"
          SrcPort                 1
          Points                  [30, 0; 0, -10]
          DstBlock                "Mux_Telemetry"
          DstPort                 2
        }

        // Bottom Return Line: S-01 -> P-02 -> BV-02 -> FT-01 -> T-01
        Line {
          SrcBlock                "S-01_Sump_4p2L"
          SrcPort                 2
          Points                  [20, 0; 0, 95]
          DstBlock                "P-02_Recirc_Pump"
          DstPort                 1
        }
        Line {
          SrcBlock                "P-02_Recirc_Pump"
          SrcPort                 1
          Points                  [-10, 0; 0, 20]
          Branch {
            DstBlock              "BV-02_Manual_Valve"
            DstPort               1
          }
          Branch {
            Points                [0, 60; 100, 0; 0, -170]
            DstBlock              "S-01_Sump_4p2L"
            DstPort               3
          }
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
          Points                  [-15, 0]
          Branch {
            Points                [-385, 0; 0, -145]
            DstBlock              "T-01_10L_Process"
            DstPort               1
          }
          Branch {
            Points                [0, 80; 600, 0; 0, -250]
            DstBlock              "Mux_Telemetry"
            DstPort               1
          }
        }

        // Tank 1 and Tank 2 levels to Telemetry
        Line {
          SrcBlock                "T-01_10L_Process"
          SrcPort                 2
          Points                  [15, 0; 0, 180; 900, 0; 0, -165]
          DstBlock                "Mux_Telemetry"
          DstPort                 3
        }
        Line {
          SrcBlock                "T-02_Flush_Tank_4p2L"
          SrcPort                 1
          Points                  [20, 0; 0, 390]
          DstBlock                "Mux_Telemetry"
          DstPort                 5
        }

        Line {
          SrcBlock                "Mux_Telemetry"
          SrcPort                 1
          DstBlock                "Sensor_Feedback"
          DstPort                 1
        }
      }
    }

    // Block 4: SCADA Monitoring, Displays & Scopes
    Block {
      BlockType               SubSystem
      Name                    "SCADA_Monitoring_and_Scopes"
      SID                     "120"
      Ports                   [3, 0]
      Position                [870, 160, 1140, 300]
      System {
        Name                    "SCADA_Monitoring_and_Scopes"
        Location                [50, 50, 950, 750]
        Open                    off

        Block {
          BlockType               Inport
          Name                    "Sensor_Feedback"
          SID                     "121"
          Position                [30, 80, 60, 100]
          Port                    "1"
        }
        Block {
          BlockType               Inport
          Name                    "Actuator_Commands"
          SID                     "122"
          Position                [30, 220, 60, 240]
          Port                    "2"
        }
        Block {
          BlockType               Inport
          Name                    "State_Code"
          SID                     "123"
          Position                [30, 360, 60, 380]
          Port                    "3"
        }

        Block {
          BlockType               Demux
          Name                    "Demux_Sensors"
          SID                     "124"
          Ports                   [1, 5]
          Position                [100, 40, 105, 140]
          Outputs                 "5"
        }
        // 1=FT01_Flow, 2=FS01_Float, 3=T01_Level, 4=Sump_Level, 5=T02_Level

        // Hydrodynamics Computer
        Block {
          BlockType               SubSystem
          Name                    "Hydrodynamics_Computer"
          SID                     "125"
          Ports                   [1, 2]
          Position                [180, 35, 270, 85]
          System {
            Name                    "Hydrodynamics_Computer"
            Location                [100, 100, 450, 250]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "Q_FT01"
              SID                     "126"
              Position                [30, 45, 60, 65]
              Port                    "1"
            }
            Block {
              BlockType               Gain
              Name                    "Gain_Vel"
              SID                     "127"
              Position                [100, 40, 140, 70]
              Gain                    "0.331572"
            }
            Block {
              BlockType               Gain
              Name                    "Gain_Re"
              SID                     "128"
              Position                [190, 75, 240, 105]
              Gain                    "8000"
            }
            Block {
              BlockType               Outport
              Name                    "Velocity"
              SID                     "129"
              Position                [280, 45, 310, 65]
              Port                    "1"
            }
            Block {
              BlockType               Outport
              Name                    "Reynolds"
              SID                     "130"
              Position                [280, 80, 310, 100]
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
                DstBlock              "Velocity"
                DstPort               1
              }
              Branch {
                Points                [0, 35]
                DstBlock              "Gain_Re"
                DstPort               1
              }
            }
            Line {
              SrcBlock                "Gain_Re"
              SrcPort                 1
              DstBlock                "Reynolds"
              DstPort                 1
            }
          }
        }

        // Totalizer
        Block {
          BlockType               SubSystem
          Name                    "Totalizer"
          SID                     "131"
          Ports                   [1, 1]
          Position                [180, 100, 270, 140]
          System {
            Name                    "Totalizer"
            Location                [100, 100, 400, 220]
            Open                    off
            Block {
              BlockType               Inport
              Name                    "Q_Lpm"
              SID                     "132"
              Position                [30, 35, 60, 55]
              Port                    "1"
            }
            Block {
              BlockType               Gain
              Name                    "Gain"
              SID                     "133"
              Position                [100, 30, 140, 60]
              Gain                    "0.01666667"
            }
            Block {
              BlockType               DiscreteIntegrator
              Name                    "Int"
              SID                     "134"
              Position                [180, 25, 230, 65]
              InitialCondition        "0.0"
            }
            Block {
              BlockType               Outport
              Name                    "Total_L"
              SID                     "135"
              Position                [270, 35, 300, 55]
              Port                    "1"
            }
            Line {
              SrcBlock                "Q_Lpm"
              SrcPort                 1
              DstBlock                "Gain"
              DstPort                 1
            }
            Line {
              SrcBlock                "Gain"
              SrcPort                 1
              DstBlock                "Int"
              DstPort                 1
            }
            Line {
              SrcBlock                "Int"
              SrcPort                 1
              DstBlock                "Total_L"
              DstPort                 1
            }
          }
        }

        // 7 Live Displays
        Block {
          BlockType               Display
          Name                    "Disp_10L_Tank_L"
          SID                     "136"
          Position                [400, 35, 470, 65]
          Decimation              "1"
        }
        Block {
          BlockType               Display
          Name                    "Disp_Sump_Vessel_L"
          SID                     "137"
          Position                [400, 80, 470, 110]
          Decimation              "1"
        }
        Block {
          BlockType               Display
          Name                    "Disp_Flush_Tank_L"
          SID                     "138"
          Position                [400, 125, 470, 155]
          Decimation              "1"
        }
        Block {
          BlockType               Display
          Name                    "Disp_FT01_Flow_Lpm"
          SID                     "139"
          Position                [400, 170, 470, 200]
          Decimation              "1"
        }
        Block {
          BlockType               Display
          Name                    "Disp_Cumulative_Vol_L"
          SID                     "140"
          Position                [400, 215, 470, 245]
          Decimation              "1"
        }
        Block {
          BlockType               Display
          Name                    "Disp_FSM_State_Code"
          SID                     "141"
          Position                [400, 260, 470, 290]
          Decimation              "1"
        }
        Block {
          BlockType               Display
          Name                    "Disp_Reynolds_Number"
          SID                     "142"
          Position                [400, 305, 470, 335]
          Decimation              "1"
        }

        // 5 Scopes & 5 Loggers
        Block {
          BlockType               Mux
          Name                    "Mux_Tanks"
          SID                     "143"
          Ports                   [3, 1]
          Position                [550, 40, 560, 100]
          Inputs                  "3"
        }
        Block {
          BlockType               Scope
          Name                    "Scope_Process_Tanks"
          SID                     "144"
          Position                [610, 50, 650, 90]
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_Tanks"
          SID                     "145"
          Position                [700, 60, 770, 80]
          VariableName            "tank_levels"
        }

        Block {
          BlockType               Scope
          Name                    "Scope_Pump_Duties"
          SID                     "146"
          Position                [610, 140, 650, 180]
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_Duties"
          SID                     "147"
          Position                [700, 150, 770, 170]
          VariableName            "pump_duties"
        }

        Block {
          BlockType               Scope
          Name                    "Scope_Flow_Sensor_FT01"
          SID                     "148"
          Position                [610, 230, 650, 270]
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_FT01"
          SID                     "149"
          Position                [700, 240, 770, 260]
          VariableName            "ft01_flow"
        }

        Block {
          BlockType               ToWorkspace
          Name                    "Save_TotalVol"
          SID                     "150"
          Position                [700, 310, 770, 330]
          VariableName            "total_volume"
        }

        Block {
          BlockType               Scope
          Name                    "Scope_Automation_State"
          SID                     "151"
          Position                [610, 360, 650, 400]
        }
        Block {
          BlockType               ToWorkspace
          Name                    "Save_State"
          SID                     "152"
          Position                [700, 370, 770, 390]
          VariableName            "system_state"
        }

        Block {
          BlockType               Scope
          Name                    "Scope_Reynolds_Number"
          SID                     "153"
          Position                [610, 440, 650, 480]
        }

        // Connecting Signals to Displays, Scopes & Loggers
        Line {
          SrcBlock                "Sensor_Feedback"
          SrcPort                 1
          DstBlock                "Demux_Sensors"
          DstPort                 1
        }
        // FT01 Flow to Hydrodynamics & Totalizer
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 1
          Points                  [25, 0]
          Branch {
            DstBlock              "Hydrodynamics_Computer"
            DstPort               1
          }
          Branch {
            Points                [0, 65]
            Branch {
              DstBlock            "Totalizer"
              DstPort             1
            }
            Branch {
              Points              [0, 65]
              Branch {
                DstBlock          "Disp_FT01_Flow_Lpm"
                DstPort           1
              }
              Branch {
                Points            [0, 65; 420, 0]
                Branch {
                  DstBlock        "Scope_Flow_Sensor_FT01"
                  DstPort         1
                }
                Branch {
                  DstBlock        "Save_FT01"
                  DstPort         1
                }
              }
            }
          }
        }
        // T-01 level to display & Scope
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 3
          Points                  [200, 0]
          Branch {
            Points                [0, -40]
            DstBlock              "Disp_10L_Tank_L"
            DstPort               1
          }
          Branch {
            Points                [200, 0; 0, -40]
            DstBlock              "Mux_Tanks"
            DstPort               1
          }
        }
        // Sump level to display & Scope
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 4
          Points                  [180, 0]
          Branch {
            Points                [0, -15]
            DstBlock              "Disp_Sump_Vessel_L"
            DstPort               1
          }
          Branch {
            Points                [210, 0; 0, -40]
            DstBlock              "Mux_Tanks"
            DstPort               2
          }
        }
        // T-02 level to display & Scope
        Line {
          SrcBlock                "Demux_Sensors"
          SrcPort                 5
          Points                  [160, 0]
          Branch {
            Points                [0, 10]
            DstBlock              "Disp_Flush_Tank_L"
            DstPort               1
          }
          Branch {
            Points                [230, 0; 0, -40]
            DstBlock              "Mux_Tanks"
            DstPort               3
          }
        }
        Line {
          SrcBlock                "Mux_Tanks"
          SrcPort                 1
          Points                  [15, 0]
          Branch {
            DstBlock              "Scope_Process_Tanks"
            DstPort               1
          }
          Branch {
            DstBlock              "Save_Tanks"
            DstPort               1
          }
        }
        // Total Volume
        Line {
          SrcBlock                "Totalizer"
          SrcPort                 1
          Points                  [50, 0; 0, 110]
          Branch {
            DstBlock              "Disp_Cumulative_Vol_L"
            DstPort               1
          }
          Branch {
            Points                [0, 90; 330, 0]
            DstBlock              "Save_TotalVol"
            DstPort               1
          }
        }
        // Reynolds Number
        Line {
          SrcBlock                "Hydrodynamics_Computer"
          SrcPort                 2
          Points                  [40, 0; 0, 250]
          Branch {
            DstBlock              "Disp_Reynolds_Number"
            DstPort               1
          }
          Branch {
            Points                [0, 140; 270, 0]
            DstBlock              "Scope_Reynolds_Number"
            DstPort               1
          }
        }
        // Actuators to Scope & Save_Duties
        Line {
          SrcBlock                "Actuator_Commands"
          SrcPort                 1
          Points                  [450, 0; 0, -70]
          Branch {
            DstBlock              "Scope_Pump_Duties"
            DstPort               1
          }
          Branch {
            DstBlock              "Save_Duties"
            DstPort               1
          }
        }
        // State code to display, scope & Save_State
        Line {
          SrcBlock                "State_Code"
          SrcPort                 1
          Points                  [300, 0]
          Branch {
            Points                [0, -95]
            DstBlock              "Disp_FSM_State_Code"
            DstPort               1
          }
          Branch {
            Points                [220, 0; 0, 10]
            Branch {
              DstBlock            "Scope_Automation_State"
              DstPort             1
            }
            Branch {
              DstBlock            "Save_State"
              DstPort             1
            }
          }
        }
      }
    }

    // =========================================================================
    // ROOT LEVEL CONNECTIONS (Clean, horizontal, straight, normal human lines!)
    // =========================================================================

    // HMI -> Controller
    Line {
      SrcBlock                "HMI_Operator_Inputs"
      SrcPort                 1
      DstBlock                "ESP32_Automation_Controller"
      DstPort                 1
    }

    // Controller -> Hydraulic Process Plant (Actuator Commands)
    Line {
      SrcBlock                "ESP32_Automation_Controller"
      SrcPort                 1
      Points                  [35, 0]
      Branch {
        DstBlock              "Hydraulic_Process_Plant_PID001"
        DstPort               1
      }
      Branch {
        Points                [0, 80; 380, 0; 0, -45]
        DstBlock              "SCADA_Monitoring_and_Scopes"
        DstPort               2
      }
    }

    // Controller -> SCADA (State Code)
    Line {
      SrcBlock                "ESP32_Automation_Controller"
      SrcPort                 2
      Points                  [20, 0; 0, 80; 390, 0; 0, -70]
      DstBlock                "SCADA_Monitoring_and_Scopes"
      DstPort                 3
    }

    // Hydraulic Process Plant -> Controller Feedback & SCADA
    Line {
      SrcBlock                "Hydraulic_Process_Plant_PID001"
      SrcPort                 1
      Points                  [35, 0]
      Branch {
        DstBlock              "SCADA_Monitoring_and_Scopes"
        DstPort               1
      }
      Branch {
        Points                [0, 100; -600, 0; 0, -65]
        DstBlock              "ESP32_Automation_Controller"
        DstPort               2
      }
    }
  }
}
'''
    with open(r'd:\matalb_;lam\lam_stage2_system.mdl', 'w', encoding='utf-8') as f:
        f.write(mdl)
    print('Generated clean normal-human black & white model at d:\\matalb_;lam\\lam_stage2_system.mdl')

    # Also update build_full_pid_simulink_model.py
    code = f'''import sys

def build_pid_model():
    mdl = \'\'\'{mdl}\'\'\'
    with open(r'd:\\matalb_;lam\\lam_stage2_system.mdl', 'w', encoding='utf-8') as f:
        f.write(mdl)
    print('Successfully generated complete P&ID Flow Diagram Model at d:\\\\matalb_;lam\\\\lam_stage2_system.mdl')

if __name__ == '__main__':
    build_pid_model()
'''
    with open(r'd:\matalb_;lam\build_full_pid_simulink_model.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print('Updated d:\\matalb_;lam\\build_full_pid_simulink_model.py')

if __name__ == '__main__':
    generate_human_model()
