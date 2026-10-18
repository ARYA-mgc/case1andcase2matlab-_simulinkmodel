import os

mdl_text = '''Model {
  Name                    "lam_stage2_system"
  Version                 8.5
  MdlSubVersion           0
  SavedCharacterEncoding  "UTF-8"
  GraphicalInterface {
    NumRootInports        0
    NumRootOutports       0
    ParameterArgumentNames  ""
    ComputedModelVersion  "2.0"
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
  RTWModifiedTimeStamp    0
  ModelVersionFormat      "2.%<AutoIncrement:1>"
  ConfigurationManager    "none"
  SampleTimeColors        off
  SampleTimeAnnotations   off
  WideLines               on
  ShowLineDimensions      on
  ShowPortDataTypes       off
  ShowDesignRanges        off
  ShowLoopsOnError        on
  IgnoreBidirectionalLines off
  ShowStorageClass        off
  ShowTestPointIcons      on
  ShowSignalResolutionIcons on
  ShowViewerIcons         on
  SortedOrder             off
  ExecutionContextIcon    off
  ShowLinearizationAnnotations on
  BlockNameDataTip        off
  BlockParametersDataTip  off
  BlockDescriptionStringDataTip off
  ToolBar                 on
  StatusBar               on
  BrowserShowLibraryLinks off
  BrowserLookUnderMasks   off
  SimulationMode          "normal"
  LinearizationMsg        "none"
  Profile                 off
  ParamWorkspaceSource    "MATLABWorkspace"
  AccelSystemTargetFile   "accel.tlc"
  AccelTemplateMakefile   "accel_default_tmf"
  AccelMakeCommand        "make_rtw"
  TryForcingSFcnDF        off
  RecordCoverage          off
  CovPath                 "/"
  CovSaveName             "covdata"
  CovMetricSettings       "dw"
  CovNameIncrementing     off
  CovHtmlReporting        on
  CovForceBlockReductionOff on
  covSaveCumulativeToWorkspaceVar on
  CovSaveSingleToWorkspaceVar on
  CovCumulativeVarName    "covCumulativeData"
  CovCumulativeReport     off
  CovReportOnPause        on
  CovModelRefEnable       "Off"
  CovExternalEMLEnable    off
  ExtModeBatchMode        off
  ExtModeEnableFloating   on
  ExtModeTrigType         "manual"
  ExtModeTrigMode         "normal"
  ExtModeTrigPort         "1"
  ExtModeTrigElement      "any"
  ExtModeTrigDuration     1000
  ExtModeTrigDurationFloating 1000
  ExtModeTrigHoldOff      0
  ExtModeTrigDelay        0
  ExtModeTrigDirection    "rising"
  ExtModeTrigLevel        0
  ExtModeArchiveMode      "off"
  ExtModeAutoIncOneShot   off
  ExtModeIncDirWhenArm    off
  ExtModeAddSuffixToVar   off
  ExtModeWriteAllDataToWs off
  ExtModeArmWhenConnect   on
  ExtModeSkipDownloadWhenConnect off
  ExtModeLogAll           on
  ExtModeAutoUpdateStatusClock on
  BufferReuse             on
  ShowModelReferenceBlockVersion off
  ShowModelReferenceBlockIO off
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
          InitialStep            "auto"
          MaxNumMinSteps         "-1"
          MaxOrder               5
          ZcThreshold            "auto"
          ConsecutiveZCsStepRelTol "10*128*eps"
          MaxConsecutiveZCs      "1000"
          ExtrapolationOrder     4
          NumberNewtonIterations 1
          MaxStep                "auto"
          MinStep                "auto"
          MaxConsecutiveMinSteps "1"
          RelTol                 "1e-3"
          SolverMode             "Auto"
          EnableConcurrentExecution off
          ConcurrentTasks        off
          Solver                 "FixedStepDiscrete"
          SolverName             "FixedStepDiscrete"
          SolverJacobianMethodControl "auto"
          ShapePreserveControl   "DisableAll"
          ZeroCrossControl       "UseLocalSettings"
          ZeroCrossAlgorithm     "Nonadaptive"
          AlgebraicLoopSolver    "TrustRegion"
          SolverResetMethod      "Fast"
          PositivePriorityOrder  off
          AutoInsertRateTranBlk  off
          SampleTimeConstraint   "Unconstrained"
          InsertRTBMode          "Whenever possible"
        }
        Simulink.DataIOCC {
          $ObjectID              3
          Version                "1.14.3"
          Decimation             "1"
          ExternalInput          "[t, u]"
          FinalStateName         "xFinal"
          InitialState           "xInitial"
          LimitDataPoints        on
          MaxDataPoints          "1000"
          LoadExternalInput      off
          LoadInitialState       off
          SaveFinalState         off
          SaveCompleteFinalSimState off
          SaveFormat             "Array"
          SignalLoggingSaveFormat "Dataset"
          SaveOutput             on
          SaveState              off
          SignalLogging          on
          DSMLogging             on
          InspectSignalLogs      off
          VisualizeSimOutput     on
          SaveTime               on
          StateSaveName          "xout"
          TimeSaveName           "tout"
          OutputSaveName         "yout"
          SignalLoggingName      "logsout"
          DSMLoggingName         "dsmout"
          OutputOption           "RefineOutputTimes"
          OutputTimes            "[]"
          ReturnWorkspaceOutputs off
          StateStreamer          ""
        }
        Simulink.OptimizationCC {
          $ObjectID              4
          Version                "1.14.3"
          BlockReduction         on
          BooleanDataType        on
          ConditionallyExecuteInputs on
          InlineParams           off
          UseIntDivNetSlope      off
          UseFloatMulNetSlope    off
          DefaultParameterBehavior "Tunable"
          AreCellArrayLabelsString off
          InitFltsAndDblsToZero  off
          NoFixptDivByZeroProtection off
          EfficientFloat2IntCast off
          EfficientMapNaN2IntZero on
          OptimizeBlockIOStorage on
          BufferReuse            on
          EnhancedBackFolding    off
          CachingGlobalReferences off
          GlobalBufferReuse      on
          StrengthReduction      off
          ExpressionFolding      on
          BooleansAsBitfields    off
          BitfieldContainerType  "uint_T"
          EnableMemcpy           on
          MemcpyThreshold        64
          PassReuseOutputArgsAs  "Structure reference"
          ExpressionDepthLimit   2147483647
          FoldNonRolledExpr      on
          LocalBlockOutputs      on
          RollThreshold          5
          SystemCodeInlineAuto   off
          StateBitsets           off
          DataBitsets            off
          ActiveStateOutputEnumStorageType "Native Integer"
          UseTempVars            off
          ZeroExternalMemoryAtStartup on
          ZeroInternalMemoryAtStartup on
          InitFltsAndDblsToZero  off
          NoFixptDivByZeroProtection off
          EfficientFloat2IntCast off
          EfficientMapNaN2IntZero on
          OptimizeBlockIOStorage on
          BufferReuse            on
        }
        Simulink.DebuggingCC {
          $ObjectID              5
          Version                "1.14.3"
          RTPrefix               "error"
          ConsistencyChecking    "none"
          ArrayBoundsChecking    "none"
          SignalInfNanChecking   "none"
          SignalRangeChecking    "none"
          ReadBeforeWriteMsg     "UseLocalSettings"
          WriteAfterWriteMsg     "UseLocalSettings"
          WriteAfterReadMsg      "UseLocalSettings"
          AlgebraicLoopMsg       "warning"
          ArtificialAlgebraicLoopMsg "warning"
          SaveWithDisabledLinksMsg "warning"
          SaveWithParameterizedLinksMsg "warning"
          CheckSSInitialOutputMsg on
          UnderspecifiedInitializationDetection "Classic"
          MergeDetectMultiDrivingBlocksExec "none"
          CheckExecutionContextPreStartOutput off
          CheckExecutionContextRuntimeOutput off
          SignalResolutionControl "UseLocalSettings"
          BlockPriorityViolationMsg "warning"
          MinStepSizeMsg         "warning"
          TimeAdjustmentMsg      "none"
          MaxConsecutiveZCsMsg   "error"
          MaskedZcDiagnostic     "warning"
          IgnoredZcDiagnostic    "warning"
          SolverPrmCheckMsg      "none"
          InheritedTsInSrcMsg     "warning"
          DiscreteInheritContinuousMsg "warning"
          MultiTaskDSMMsg        "error"
          MultiTaskCondExecSysMsg "error"
          MultiTaskRateTransMsg  "error"
          SingleTaskRateTransMsg "none"
          TasksWithSamePriorityMsg "warning"
          SigSpecEnsureSampleTimeMsg "warning"
          CheckMatrixSingularityMsg "none"
          IntegerOverflowMsg     "warning"
          Int32ToFloatConvMsg    "warning"
          ParameterDowncastMsg   "error"
          ParameterOverflowMsg   "error"
          ParameterUnderflowMsg  "none"
          ParameterPrecisionLossMsg "warning"
          ParameterTunabilityLossMsg "warning"
          FixptConstUnderflowMsg "none"
          FixptConstOverflowMsg  "none"
          FixptConstPrecisionLossMsg "none"
          UnderSpecifiedDataTypeMsg "none"
          UnnecessaryDatatypeConvMsg "none"
          VectorMatrixConversionMsg "none"
          InvalidFcnCallConnMsg  "error"
          FcnCallInpInsideContextMsg "EnableAllAsError"
          SignalLabelMismatchMsg "none"
          UnconnectedInputMsg    "warning"
          UnconnectedOutputMsg   "warning"
          UnconnectedLineMsg     "warning"
          SFcnCompatibilityMsg   "none"
          FrameProcessingMode    "warning"
          UniqueDataStoreMsg     "none"
          BusObjectLabelMismatch "warning"
          RootOutportRequireBusObject "warning"
          AssertControl          "UseLocalSettings"
          EnableOverflowDetection off
          ModelReferenceIOMsg    "none"
          ModelReferenceMultiInstanceNormalModeStructChecksumCheck "error"
          ModelReferenceVersionMismatchMessage "none"
          ModelReferenceIOMismatchMessage "none"
          ModelReferenceCSMismatchMessage "none"
          UnknownTsInhSupMsg     "warning"
          ModelReferenceDataLoggingMessage "warning"
          ModelReferenceSymbolNameMessage "warning"
          ModelReferenceExtraNoncontSigs "error"
          StateNameClashWarn     "none"
          SimStateInterfaceChecksumMismatchMsg "warning"
          SimStateOlderReleaseMsg "error"
          InitInArrayFormatMsg   "warning"
          StrictBusMsg           "ErrorLevel1"
          BusNameAdapt           "WarnAndRepair"
          NonBusSignalsTreatedAsBus "none"
          LoggingUnavailableSignals "error"
          BlockIODiagnostic      "none"
        }
        Simulink.HardwareCC {
          $ObjectID              6
          Version                "1.14.3"
          ProdBitPerChar         8
          ProdBitPerShort        16
          ProdBitPerInt          32
          ProdBitPerLong         32
          ProdBitPerLongLong     64
          ProdBitPerFloat        32
          ProdBitPerDouble       64
          ProdBitPerPointer      32
          ProdLargestAtomicInteger "Char"
          ProdLargestAtomicFloat "None"
          ProdIntDivRoundTo      "Undefined"
          ProdEndianess          "Unspecified"
          ProdWordSize           32
          ProdShiftRightIntArith on
          ProdLongLongMode       off
          ProdHWDeviceType       "32-bit Generic"
          TargetBitPerChar       8
          TargetBitPerShort      16
          TargetBitPerInt        32
          TargetBitPerLong       32
          TargetBitPerLongLong   64
          TargetBitPerFloat      32
          TargetBitPerDouble     64
          TargetBitPerPointer    32
          TargetLargestAtomicInteger "Char"
          TargetLargestAtomicFloat "None"
          TargetShiftRightIntArith on
          TargetLongLongMode     off
          TargetHWDeviceType     "Specified"
          TargetUnknown          off
          ProdEqTarget           on
        }
        Simulink.ModelReferenceCC {
          $ObjectID              7
          Version                "1.14.3"
          UpdateModelReferenceTargets "IfOutOfDateOrStructuralChange"
          CheckModelReferenceTargetMessage "error"
          EnableParallelModelReferenceBuilds off
          ParallelModelReferenceErrorOnInvalidPool on
          ParallelModelReferenceMATLABWorkerInit "None"
          ModelReferenceNumInstancesAllowed "Multi"
          PropagateVarSize       "Infer from blocks in model"
          ModelReferencePassRootInputsByReference on
          ModelReferenceMinAlgLoopOccurrences off
          PropagateSignalLabelsOutOfModel off
          SupportModelReferenceSimTargetCustomCode off
        }
        Simulink.SFSimCC {
          $ObjectID              8
          Version                "1.14.3"
          SFSimEnableDebug       on
          SFSimOverflowDetection on
          SFSimEcho              on
          SimBlas                on
          SimCtrlC               on
          SimExtrinsic           on
          SimIntegrity           on
          SimUseLocalCustomCode  off
          SimParseCustomCode     on
          SimBuildMode           "sf_incremental_build"
          SimGenImportedTypeDefs off
        }
        Simulink.RTWCC {
          $BackupClass           "Simulink.RTWCC"
          $ObjectID              9
          Version                "1.14.3"
          SystemTargetFile       "grt.tlc"
          GenCodeOnly            off
          MakeCommand            "make_rtw"
          GenerateMakefile       on
          TemplateMakefile       "grt_default_tmf"
          GenerateReport         off
          SaveLog                off
          RTWVerbose             on
          RetainRTWFile          off
          ProfileTLC             off
          TLCDebug               off
          TLCCoverage            off
          TLCAssert              off
          ProcessScriptMode      "Default"
          ConfigurationId        "0"
          Toolchain              "Automatically locate an installed toolchain"
          BuildConfiguration     "Faster Builds"
          IncludeHyperlinkInReport off
          LaunchReport           off
          PortableWordSizes      off
          CreateSILPILBlock      "None"
          CodeExecutionProfiling off
          CodeProfilingSaveOptions "SummaryOnly"
          CodeProfilingInstrumentation off
          SILDebugging           off
          TargetLang             "C"
          IncludeBusHierarchyInRTWFileBlockHierarchyMap off
          IncludeERTFirstTime    off
          GenerateTraceInfo      off
          GenerateTraceReport    off
          GenerateTraceReportSl  off
          GenerateTraceReportSf  off
          GenerateTraceReportEml off
          GenerateCodeInfo       off
          GenerateWebview        off
          GenerateCodeMetricsReport off
          GenerateCodeReplacementReport off
          RTWCompilerOptimization "Off"
          CheckMdlBeforeBuild    "Off"
          CustomRebuildMode      "OnUpdate"
          Array {
            Type                  "Handle"
            Dimension             2
            Simulink.CodeAppCC {
              $ObjectID              10
              Version                "1.14.3"
              ForceParamTrailComments off
              GenerateComments       on
              CommentStyle           "Auto"
              IgnoreCustomStorageClasses on
              IgnoreTestpoints       off
              IncHierarchyInIds      off
              MaxIdLength            31
              PreserveName           off
              PreserveNameWithParent off
              ShowEliminatedStatement off
              OperatorAnnotations    off
              IncAutoGenComments     off
              SimulinkDataObjDesc    off
              SFDataObjDesc          off
              MATLABFcnDesc          off
              IncDataTypeInIds       off
              MangleLength           1
              DefineNamingRule       "None"
              ParamNamingRule        "None"
              SignalNamingRule       "None"
              InsertBlockDesc        off
              InsertPolySpaceComments off
              SimulinkBlockComments  on
              MATLABSourceComments   off
              EnableCustomComments   off
              InternalIdentifier     "Shortened"
              InlinedPrmAccess       "Literals"
              ReqsInCode             off
              UseSimReservedNames    off
            }
            Simulink.GRTTargetCC {
              $BackupClass           "Simulink.TargetCC"
              $ObjectID              11
              Version                "1.14.3"
              TargetFcnLib           "ansi_tfl_table_tmw.mat"
              TargetLibSuffix        ""
              TargetPreCompLibLocation ""
              GenFloatMathFcnCalls   "NOT IN USE"
              TargetLangStandard     "C89/C90 (ANSI)"
              CodeReplacementLibrary "None"
              UtilityFuncGeneration  "Auto"
              ERTMultiwordTypeDef    "System defined"
              ERTMultiwordLength     256
              MultiwordLength        2048
              GenerateFullHeader     on
              GenerateSampleERTMain  off
              GenerateTestInterfaces off
              ModelReferenceCompliant on
              ParMdlRefBuildCompliant on
              CompOptLevelCompliant  on
              ConcurrentExecutionCompliant on
              IncludeMdlTerminateFcn on
              CombineOutputUpdateFcns on
              CombineSignalStateStructs off
              SuppressErrorStatus    off
              ERTFirstTimeCompliant  off
              IncludeFileDelimiter   "Auto"
              ERTCustomFileBanners   off
              SupportAbsoluteTime    on
              LogVarNameModifier     "rt_"
              MatFileLogging         on
              MultiInstanceERTCode   off
              CodeInterfacePackaging "Nonreusable function"
              SupportNonFinite       on
              SupportComplex         on
              PurelyIntegerCode      off
              SupportContinuousTime  on
              SupportNonInlinedSFcns on
              SupportVariableSizeSignals off
              EnableShiftOperators   on
              ParenthesesLevel       "Nominal"
              CastingMode            "Nominal"
              ModelStepFunctionPrototypeCodeBehavior "Default"
              CPPClassGenCompliant   on
              AutosarCompliant       off
              GRTInterface           off
              GenerateAllocFcn       off
              GenerateSharedConstants on
              UseMalloc              off
              ExtMode                off
              ExtModeStaticAlloc     off
              ExtModeTesting         off
              ExtModeStaticAllocSize 1000000
              ExtModeTransport       0
              ExtModeMexFile         "ext_comm"
              ExtModeIntrfLevel      "Level1"
              RTWCAPISignals         off
              RTWCAPIParams          off
              RTWCAPIStates          off
              RTWCAPIRootIO          off
              GenerateASAP2          off
              MultiInstanceErrorCode "Error"
            }
            PropName              "Components"
          }
        }
        PropName              "Components"
      }
      Name                    "Configuration"
      CurrentDlgPage          "Solver"
      ConfigPrmDlgPosition     [ 200, 85, 1100, 750 ]
    }
    PropName              "ConfigurationSets"
  }
  Simulink.ConfigSet {
    $PropName               "ActiveConfigurationSet"
    $ObjectID              1
  }
  Object {
    $PropName               "DataPointers"
    $ObjectID              12
    $ClassName              "Simulink.DualDataPointers"
  }
  ExplicitPartitioning    off
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
    BlockRotation           0
    BlockMirror             off
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
    FontAngle               "normal"
    UseDisplayTextAsClickCallback off
  }
  LineDefaults {
    FontName                "Helvetica"
    FontSize                9
    FontWeight              "normal"
    FontAngle               "normal"
  }
  BlockParameterDefaults {
    Block {
      BlockType               Clock
      DisplayTime             off
      Decimation              "10"
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
      ParamMin                "[]"
      ParamMax                "[]"
      ParamDataTypeStr        "Inherit: Same as input"
      OutMin                  "[]"
      OutMax                  "[]"
      OutDataTypeStr          "Inherit: Same as input"
      LockScale               off
      RndMeth                 "Floor"
      SaturateOnIntegerOverflow on
      SampleTime              "-1"
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
    Location                [10, 30, 1620, 1020]
    Open                    on
    ModelBrowserVisibility  off
    ModelBrowserWidth       200
    ScreenColor             "white"
    PaperOrientation        "landscape"
    PaperPositionMode       "auto"
    PaperType               "usletter"
    PaperUnits              "inches"
    TiledPaperMargins       [0.500000, 0.500000, 0.500000, 0.500000]
    TiledPageScale          1
    ShowPageBoundaries      off
    ZoomFactor              "100"
    ReportName              "simulink-default.rpt"
    SIDHighWaterMark        "40"

    Annotation {
      SID                     "1"
      Name                    "LAM RESEARCH CHALLENGE 3.0 - STAGE 2 DIGITAL TWIN"
      Position                [800, 25, 800, 25]
      HorizontalAlignment     "center"
      VerticalAlignment       "middle"
      ForegroundColor         "navy"
      FontSize                16
      FontWeight              "bold"
    }
    Annotation {
      SID                     "2"
      Name                    "Automated Chemical Distribution, Sump Level Protection & High-Purity Flush Rig"
      Position                [800, 48, 800, 48]
      HorizontalAlignment     "center"
      VerticalAlignment       "middle"
      ForegroundColor         "gray"
      FontSize                11
    }
    Annotation {
      SID                     "3"
      Name                    "[1. OPERATOR CONTROLS]"
      Position                [120, 80, 120, 80]
      HorizontalAlignment     "center"
      ForegroundColor         "blue"
      FontSize                10
      FontWeight              "bold"
    }
    Annotation {
      SID                     "4"
      Name                    "[2. FSM AUTOMATION & HYDRAULIC DIGITAL TWIN]"
      Position                [460, 80, 460, 80]
      HorizontalAlignment     "center"
      ForegroundColor         "navy"
      FontSize                10
      FontWeight              "bold"
    }
    Annotation {
      SID                     "5"
      Name                    "[3. LIVE TELEMETRY, FLUID MECHANICS & SCOPES]"
      Position                [1050, 80, 1050, 80]
      HorizontalAlignment     "center"
      ForegroundColor         "darkGreen"
      FontSize                10
      FontWeight              "bold"
    }

    Block {
      BlockType               Step
      Name                    "Rig_Push_Button"
      SID                     "6"
      Position                [50, 110, 160, 150]
      Time                    "2.0"
      Before                  "0"
      After                   "1"
      SampleTime              "0.001"
    }
    Block {
      BlockType               Step
      Name                    "Flush_Ball_Valve_BV01"
      SID                     "7"
      Position                [50, 200, 160, 240]
      Time                    "5.0"
      Before                  "0"
      After                   "1"
      SampleTime              "0.001"
    }
    Block {
      BlockType               DiscretePulseGenerator
      Name                    "Disturbance_Inflow_Valve"
      SID                     "8"
      Position                [50, 290, 160, 330]
      PulseType               "Time based"
      Amplitude               "10"
      Period                  "500"
      PulseWidth              "5"
      PhaseDelay              "90"
    }
    Block {
      BlockType               Clock
      Name                    "Master_Clock"
      SID                     "9"
      Position                [50, 380, 160, 420]
    }

    Block {
      BlockType               Mux
      Name                    "Mux_Stimuli"
      SID                     "10"
      Ports                   [4, 1]
      Position                [210, 95, 220, 435]
      Inputs                  "4"
      DisplayOption           "bar"
    }

    Block {
      BlockType               MATLABFcn
      Name                    "LAM_Process_Plant_Core"
      SID                     "11"
      Position                [270, 95, 590, 435]
      ForegroundColor         "navy"
      BackgroundColor         "lightBlue"
      MATLABFcn               "lam_simulink_fcn(u)"
      OutputDimensions        "15"
      SampleTime              "0.001"
    }

    Block {
      BlockType               Demux
      Name                    "Demux_Bus"
      SID                     "12"
      Ports                   [1, 7]
      Position                [640, 85, 650, 960]
      Outputs                 "[3, 3, 1, 1, 1, 3, 3]"
      DisplayOption           "bar"
    }

    Block {
      BlockType               Display
      Name                    "Live_Tanks_L_10L_Sump_Flush"
      SID                     "13"
      Position                [720, 100, 870, 150]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Process_Tanks"
      SID                     "14"
      Ports                   [1]
      Position                [930, 100, 1010, 150]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "11"
      SaveName                "Scope_Tanks_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_Tanks"
      SID                     "15"
      Position                [1070, 105, 1200, 145]
      VariableName            "tank_levels"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               Display
      Name                    "Live_Pump_Flows_Lpm_P1_P2_P3"
      SID                     "16"
      Position                [720, 220, 870, 270]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Hydraulic_Flows"
      SID                     "17"
      Ports                   [1]
      Position                [930, 220, 1010, 270]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "7"
      SaveName                "Scope_Flows_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_Flows"
      SID                     "18"
      Position                [1070, 225, 1200, 265]
      VariableName            "pump_flows"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               Display
      Name                    "Live_FT01_Flow_Rate_Lpm"
      SID                     "19"
      Position                [720, 335, 870, 375]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_FT01_Sensor"
      SID                     "20"
      Ports                   [1]
      Position                [930, 335, 1010, 375]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "7"
      SaveName                "Scope_FT01_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_FT01"
      SID                     "21"
      Position                [1070, 335, 1200, 375]
      VariableName            "ft01_flow"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               Gain
      Name                    "Gain_Flow_to_mLs"
      SID                     "22"
      Position                [720, 430, 775, 460]
      Gain                    "16.666667"
    }
    Block {
      BlockType               Gain
      Name                    "Gain_Line_Velocity_mps"
      SID                     "23"
      Position                [810, 430, 865, 460]
      Gain                    "0.019894"
    }
    Block {
      BlockType               Gain
      Name                    "Gain_Reynolds_Number"
      SID                     "24"
      Position                [900, 430, 955, 460]
      Gain                    "8000"
    }
    Block {
      BlockType               Display
      Name                    "Live_Line_Velocity_mps"
      SID                     "25"
      Position                [890, 475, 970, 505]
      Decimation              "50"
    }
    Block {
      BlockType               Display
      Name                    "Live_Reynolds_Regime"
      SID                     "26"
      Position                [990, 475, 1080, 505]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Fluid_Mechanics"
      SID                     "27"
      Ports                   [1]
      Position                [1010, 425, 1070, 465]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "14000"
      SaveName                "Scope_Fluid_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }

    Block {
      BlockType               Display
      Name                    "Live_Total_Fluid_L"
      SID                     "28"
      Position                [720, 550, 870, 590]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Totalizer"
      SID                     "29"
      Ports                   [1]
      Position                [930, 550, 1010, 590]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "15"
      SaveName                "Scope_Tot_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_TotalVol"
      SID                     "30"
      Position                [1070, 550, 1200, 590]
      VariableName            "total_volume"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               Display
      Name                    "Live_FSM_State_Code_0_to_8"
      SID                     "31"
      Position                [720, 660, 870, 700]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_FSM_States"
      SID                     "32"
      Ports                   [1]
      Position                [930, 660, 1010, 700]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "9"
      SaveName                "Scope_State_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_State"
      SID                     "33"
      Position                [1070, 660, 1200, 700]
      VariableName            "system_state"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               Display
      Name                    "Live_Pumps_PWM_Duty_Pct"
      SID                     "34"
      Position                [720, 770, 870, 820]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Actuator_PWM"
      SID                     "35"
      Ports                   [1]
      Position                [930, 770, 1010, 820]
      TimeRange               "250"
      YMin                    "0"
      YMax                    "110"
      SaveName                "Scope_Duties_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_Duties"
      SID                     "36"
      Position                [1070, 775, 1200, 815]
      VariableName            "pump_duties"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               Display
      Name                    "Live_Valves_And_Alerts"
      SID                     "37"
      Position                [720, 885, 870, 935]
      Decimation              "50"
    }
    Block {
      BlockType               Scope
      Name                    "Scope_Interlocks"
      SID                     "38"
      Ports                   [1]
      Position                [930, 885, 1010, 935]
      TimeRange               "250"
      YMin                    "-0.5"
      YMax                    "5"
      SaveName                "Scope_Status_Data"
      DataFormat              "StructureWithTime"
      LimitDataPoints         off
    }
    Block {
      BlockType               ToWorkspace
      Name                    "Save_Status"
      SID                     "39"
      Position                [1070, 890, 1200, 930]
      VariableName            "status_signals"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Block {
      BlockType               ToWorkspace
      Name                    "Save_Time"
      SID                     "40"
      Position                [210, 470, 310, 505]
      VariableName            "sim_time"
      MaxDataPoints           "inf"
      SampleTime              "0.001"
      SaveFormat              "Array"
    }

    Line {
      SrcBlock                "Rig_Push_Button"
      SrcPort                 1
      DstBlock                "Mux_Stimuli"
      DstPort                 1
    }
    Line {
      SrcBlock                "Flush_Ball_Valve_BV01"
      SrcPort                 1
      DstBlock                "Mux_Stimuli"
      DstPort                 2
    }
    Line {
      SrcBlock                "Disturbance_Inflow_Valve"
      SrcPort                 1
      DstBlock                "Mux_Stimuli"
      DstPort                 3
    }
    Line {
      SrcBlock                "Master_Clock"
      SrcPort                 1
      Points                  [15, 0]
      Branch {
        DstBlock              "Mux_Stimuli"
        DstPort               4
      }
      Branch {
        Points                [0, 85]
        DstBlock              "Save_Time"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Mux_Stimuli"
      SrcPort                 1
      DstBlock                "LAM_Process_Plant_Core"
      DstPort                 1
    }

    Line {
      SrcBlock                "LAM_Process_Plant_Core"
      SrcPort                 1
      DstBlock                "Demux_Bus"
      DstPort                 1
    }

    Line {
      SrcBlock                "Demux_Bus"
      SrcPort                 1
      Points                  [35, 0]
      Branch {
        DstBlock              "Live_Tanks_L_10L_Sump_Flush"
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
      SrcBlock                "Demux_Bus"
      SrcPort                 2
      Points                  [35, 0]
      Branch {
        DstBlock              "Live_Pump_Flows_Lpm_P1_P2_P3"
        DstPort               1
      }
      Branch {
        DstBlock              "Scope_Hydraulic_Flows"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_Flows"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Demux_Bus"
      SrcPort                 3
      Points                  [25, 0]
      Branch {
        DstBlock              "Live_FT01_Flow_Rate_Lpm"
        DstPort               1
      }
      Branch {
        DstBlock              "Scope_FT01_Sensor"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_FT01"
        DstPort               1
      }
      Branch {
        Points                [0, 90]
        DstBlock              "Gain_Flow_to_mLs"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Gain_Flow_to_mLs"
      SrcPort                 1
      DstBlock                "Gain_Line_Velocity_mps"
      DstPort                 1
    }

    Line {
      SrcBlock                "Gain_Line_Velocity_mps"
      SrcPort                 1
      Points                  [10, 0]
      Branch {
        DstBlock              "Gain_Reynolds_Number"
        DstPort               1
      }
      Branch {
        Points                [0, 45]
        DstBlock              "Live_Line_Velocity_mps"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Gain_Reynolds_Number"
      SrcPort                 1
      Points                  [15, 0]
      Branch {
        DstBlock              "Scope_Fluid_Mechanics"
        DstPort               1
      }
      Branch {
        Points                [0, 45]
        DstBlock              "Live_Reynolds_Regime"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Demux_Bus"
      SrcPort                 4
      Points                  [35, 0]
      Branch {
        DstBlock              "Live_Total_Fluid_L"
        DstPort               1
      }
      Branch {
        DstBlock              "Scope_Totalizer"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_TotalVol"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Demux_Bus"
      SrcPort                 5
      Points                  [35, 0]
      Branch {
        DstBlock              "Live_FSM_State_Code_0_to_8"
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
      SrcBlock                "Demux_Bus"
      SrcPort                 6
      Points                  [35, 0]
      Branch {
        DstBlock              "Live_Pumps_PWM_Duty_Pct"
        DstPort               1
      }
      Branch {
        DstBlock              "Scope_Actuator_PWM"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_Duties"
        DstPort               1
      }
    }

    Line {
      SrcBlock                "Demux_Bus"
      SrcPort                 7
      Points                  [35, 0]
      Branch {
        DstBlock              "Live_Valves_And_Alerts"
        DstPort               1
      }
      Branch {
        DstBlock              "Scope_Interlocks"
        DstPort               1
      }
      Branch {
        DstBlock              "Save_Status"
        DstPort               1
      }
    }
  }
}
'''

with open(r'd:\matalb_;lam\lam_stage2_system.mdl', 'w', encoding='utf-8') as f:
    f.write(mdl_text)

print('Generated clean, professional engineering mdl file at d:\\matalb_;lam\\lam_stage2_system.mdl')
