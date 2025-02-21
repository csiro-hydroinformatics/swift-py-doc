extern char* GetLastStdExceptionMessage();
extern void RegisterExceptionCallback(const void* callback);
extern void DisposeSharedPointer( void* ptr);
extern void DeleteAnsiStringArray(char** values, int arrayLength);
extern void DeleteAnsiString(const char* value);
extern int GetNumRunoffModelIdentifiers();
extern int GetNumRunoffModelVarIdentifiers(const char* modelId);
extern char* GetRunoffModelIdentifier(int index);
extern char* GetRunoffModelVarIdentifier(const char* modelId, int index);
extern char** GetRunoffModelIdentifiers(int* size);
extern char** GetRunoffModelVarIdentifiers(const char* modelId, int* size);
extern void* CloneModel(void* simulation);
extern void* SubsetModel(void* simulation, const char* elementName, bool selectNetworkAboveElement, bool includeElementInSelection, bool invertSelection, char** terminationElements, int terminationElementsLength);
extern char** SortSimulationElementsByRunOrder(void* simulation, char** elementIds, int numElements, const char* orderingMethod, int* size);
extern void* SwapRunoffModel(void* simulation, const char* newModelId);
extern void SetChannelRoutingModel(void* simulation, const char* newModelId);
extern void SetErrorCorrectionModel(void* simulation, const char* newModelId, const char* elementId, int length, int seed);
extern void SetSeedForModel(void* simulation, const char* modelObjectIdentifier, int seed);
extern void SetReservoirModel(void* simulation, const char* newModelId, const char* elementId);
extern void SetRunoffPostProcessingModel(void* src, const char* newModelId, const char* elementId);
extern void SetReservoirGeometry(void* simulation, const char* elementId, int numEntries, double* level, double* storage, double* area);
extern void SetReservoirMinDischarge(void* simulation, const char* elementId, int numEntries, double* level, double* discharge);
extern void SetReservoirMaxDischarge(void* simulation, const char* elementId, int numEntries, double* level, double* discharge);
extern void SetReservoirOpsReleaseCurve(void* simulation, const char* elementId, int numEntries, double* level, double* discharge);
extern void RemoveStorageDischargeRelationship(void* simulation, const char* elementId, const char* relationshipType);
extern void SetSubareaInputsPreprocessorModel(void* simulation, const char* newModelId, const char* subAreaId);
extern void WireSubareaInputsPreprocessorModel(void* simulation, const char* fromOutput, const char* toInput, const char* subAreaId);
extern void RemoveModel(void* simulation, const char* fullModelId);
extern void* CreateCatchment(int numNodes, char** nodeIds, char** nodeNames, int numLinks, char** linkIds, char** linkNames, char** linkFromNode, char** linkToNode, const char* runoffModelName, double* areasKm2);
extern CatchmentStructure* GetCatchmentStructure(void* simulation);
extern void DisposeCatchmentStructure(CatchmentStructure* structure);
extern void* CreateNewFromNetworkInfo(void* nodes, int numNodes, void* links, int numLinks);
extern void Play(void* simulation, const char* variableIdentifier, double* values, void* geom);
extern void Record(void* simulation, const char* variableIdentifier);
extern void RemovePlayedTimeSeries(void* modelInstance, const char* variableIdentifier);
extern void RemoveRecorder(void* modelInstance, const char* variableIdentifier);
extern void SetSpan(void* simulation, MarshaledDateTime start, MarshaledDateTime end);
extern void* CreateSubarea(const char* modelId, double areaKm2);
extern void ExecuteSimulation(void* simulation, bool resetInitialStates);
extern void ResetModelStates(void* simulation);
extern char** CheckSimulationErrors(void* simulation, int* size);
extern void GetStart(void* simulation, void* start);
extern void GetEnd(void* simulation, void* end);
extern void SetTimeStep(void* simulation, const char* timeStepName);
extern char* GetTimeStepName(void* simulation);
extern int GetNumSteps(void* simulation);
extern int GetNumStepsForTimeSpan(void* modelSimulation, MarshaledDateTime start, MarshaledDateTime end);
extern int GetPlayedTimeSeriesLength(void* simulation, const char* variableIdentifier);
extern void GetPlayed(void* simulation, const char* variableIdentifier, double* values, int arrayLength);
extern void GetPlayedTsGeometry(void* simulation, const char* variableIdentifier, void* geom);
extern void GetRecorded(void* simulation, const char* variableIdentifier, double* values, int arrayLength);
extern void GetRecordedTsGeometry(void* simulation, const char* variableIdentifier, void* geom);
extern int GetNumRecordedVariables(void* simulation);
extern int GetNumPlayedVariables(void* simulation);
extern int GetNumLinks(void* simulation);
extern int GetNumNodes(void* simulation);
extern int GetNumSubareas(void* simulation);
extern int GetNumVarIdentifiers(void* simulation, const char* elementId);
extern bool IsValidVariableIdentifier(void* simulation, const char* varId);
extern char* GetCatchmentDOTGraph(void* simulation);
extern char** GetPlayedVariableNames(void* simulation, int* size);
extern char** GetRecordedVariableNames(void* simulation, int* size);
extern char** GetSubareaNames(void* simulation, int* size);
extern char** GetLinkNames(void* simulation, int* size);
extern char** GetNodeNames(void* simulation, int* size);
extern char** GetSubareaIdentifiers(void* simulation, int* size);
extern char** GetLinkIdentifiers(void* simulation, int* size);
extern char** GetNodeIdentifiers(void* simulation, int* size);
extern char** GetElementVarIdentifiers(void* simulation, const char* elementId, int* size);
extern void SetVariable(void* simulation, const char* variableIdentifier, double value);
extern void SetVariableInt(void* simulation, const char* variableIdentifier, int value);
extern void SetVariableBool(void* simulation, const char* variableIdentifier, bool value);
extern double GetVariable(void* simulation, const char* variableIdentifier);
extern string_string_map* GetModelConfigurationSwift(void* simulation, const char* elementIdentifier);
extern int GetVariableInt(void* simulation, const char* variableIdentifier);
extern bool GetVariableBool(void* simulation, const char* variableIdentifier);
extern bool VariableIsDouble(void* simulation, const char* variableIdentifier);
extern bool VariableIsInt(void* simulation, const char* variableIdentifier);
extern bool VariableIsBool(void* simulation, const char* variableIdentifier);
extern void* CreateEnsembleModelRunner(void* simulation, int ensembleSize);
extern void* PrepareEnsembleModelRunner(void* simulation, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd, double* obsTsValues, void* obsTsGeom, const char* errorModelElementId);
extern void SetupEnsembleModelRunner(void* emr, MarshaledDateTime forecastStart, int ensembleSize, int forecastHorizonLength);
extern void RecordEnsembleModelRunner(void* emr, const char* variableIdentifier);
extern void ApplyConfiguration(void* parameterizer, void* simulation);
extern bool SupportsThreadSafeCloning(void* parameterizer);
extern void* CloneHypercubeParameterizer(void* hypercubeParameterizer);
extern void* CreateHypercubeParameterizer(const char* strategy);
extern void* CreateSubcatchmentHypercubeParameterizer(void* parameterizer, void* subcatchment);
extern char** GetKnownParameterizationStrategies(int* size);
extern void* UntransformHypercubeParameterizer(void* hypercubeParameterizer);
extern void* HomotheticTransform(void* centre, void* point, double factor);
extern void* AggregateParameterizers(const char* strategy, void* parameterizers, int numParameterizers);
extern void TagParameterizer(void* p, const char* tag);
extern void* CreateCompositeParameterizer();
extern void* CreateFunctionsParameterizer(void* modelParameters, void* functionsParameters);
extern void* CreateFilteringParameterizer(void* p);
extern void HideParameters(void* p, character_vector* pnames, bool regex, bool startsWith, bool strict);
extern void ShowParameters(void* p, character_vector* pnames, bool regex, bool startsWith);
extern void* CreatePrefixingParameterizer(void* p, const char* prefix);
extern void AddToCompositeParameterizer(void* compositeParameterizer, void* parameterizer);
extern void* WrapObjectiveEvaluatorWila(void* objective, bool clone);
extern void* UnwrapObjectiveEvaluatorWila(void* objective);
extern char** GetKnownParameterizerAggregationStrategies(int* size);
extern void* CreateGr4ScaledParameterizer(double referenceAreaKm2, int tStepSeconds);
extern void* CreateStateInitParameterizer(void* hypercubeParameterizer);
extern void* CreateTransformParameterizer(void* hypercubeParameterizer);
extern void* CreateMuskingumConstraint(void* hypercubeParameterizer, double deltaTHours, const char* paramNameK, const char* paramNameX, void* simulation);
extern named_values_vector* GetFeasibleMuskingumBounds(void* simulation, double deltaTHours);
extern void DisposeNamedValuedVectorsSwift(named_values_vector* v);
extern void DisposeStringStringMapSwift(string_string_map* v);
extern void* CreateTargetScalingParameterizer(const char* selectorType);
extern char** GetKnownParameterizationTargetSelectorTypes(int* size);
extern void* CreateLinearFuncParameterizer(const char* paramName, const char* innerParamName, const char* observedState, double constant, double min, double max, double value, const char* selectorType);
extern void* CreateSqrtAreaRatioParameterizer(double referenceAreaKm2, const char* paramName, const char* innerParamName, double min, double max, double value);
extern double GetParameterMinValue(void* hypercubeParameterizer, const char* variableName);
extern double GetParameterMaxValue(void* hypercubeParameterizer, const char* variableName);
extern double GetParameterValue(void* hypercubeParameterizer, const char* variableName);
extern int GetNumParameters(void* hypercubeParameterizer);
extern char* GetParameterName(void* hypercubeParameterizer, int index);
extern bool IsWithinBounds(void* hypercubeParameterizer);
extern void SetParameterValue(void* hypercubeParameterizer, const char* variableName, double value);
extern void SetMaxParameterValue(void* hypercubeParameterizer, const char* variableName, double value);
extern void SetMinParameterValue(void* hypercubeParameterizer, const char* variableName, double value);
extern void AddParameterDefinition(void* hypercubeParameterizer, const char* variableName, double min, double max, double value);
extern void SetParameterDefinition(void* hypercubeParameterizer, const char* variableName, double min, double max, double value);
extern void SetDefaultParameters(void* hypercubeParameterizer, const char* modelId);
extern void AddLinearScalingParameterizer(void* scalingParameterizer, const char* paramName, const char* stateName, const char* scalingVarName, double constant, double min, double max, double value);
extern void AddParameterTransform(void* transformParameterizer, const char* paramName, const char* innerParamName, const char* transformId, double a, double b);
extern void* CreateSingleObservationObjectiveEvaluator(void* simulation, const char* obsVarId, double* observations, void* obsGeom, const char* statisticId);
extern void* CreateEmptyCompositeObjectiveEvaluator();
extern void AddSingleObservationObjectiveEvaluator(void* compositeObjective, void* singleObjective, double weight, const char* name);
extern void* CreateCompositeObservationObjectiveEvaluator(void* simulation, const char* obsVarId, double* observations, void* obsGeom, const char* yamlStatIdString);
extern void* CreateMultisiteObjectiveEvaluator(void* simulation, multi_statistic_definition* defn, named_values_vector* weights);
extern void* CloneObjectiveEvaluator(void* objectiveEvaluator, void* simulation);
extern double EvaluateScore(void* objectiveEvaluator);
extern double EvaluateScoreForParameters(void* objectiveEvaluator, void* parameterizer);
extern double EvaluateScoreForParametersInitState(void* objectiveEvaluator, void* parameterizer);
extern named_values_vector* EvaluateScoresForParametersWila(void* objectiveEvaluator, void* parameterizer);
extern char* GetNameObjectiveEvaluator(void* objectiveEvaluator);
extern bool ObjectiveEvaluatorIsMaximizable(void* objectiveEvaluator);
extern void* CreateSingleObservationObjectiveEvaluatorWila(void* simulation, const char* obsVarId, double* observations, void* obsGeom, const char* statisticId);
extern void* CreateShuffledComplexEvolutionWila(void* objective, void* terminationCriterion, SceParameters SCEpars, void* populationInitializer);
extern void* CreateOptimizerWila(void* objective, void* parameterizer, string_string_map* parameters);
extern void* CreateSceMarginalTerminationWila(double tolerance, int cutoffNoImprovement, double maxHours);
extern void* CreateSceMaxRuntimeTerminationWila(double maxHours);
extern void* CreateSceMaxIterationTerminationWila(int maxIterations);
extern void* CreateSceTerminationWila(const char* type, char** arguments, int numArguments);
extern void* CreateCandidateFactorySeedWila(void* hypercubeParameterizer, const char* type, int seed);
extern void* EvaluateScoreForParametersWila(void* objectiveEvaluator, void* hypercubeParameterizer);
extern void* EvaluateScoreForParametersWilaInitState(void* objectiveEvaluator, void* hypercubeParameterizer);
extern void* GetScoresAtIndex(void* vectorScores, int index);
extern void* SortSetOfScoresBy(void* vectorScores, const char* scoreName);
extern void* EstimateERRISParameters(void* simulation, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd, bool warmup, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, double censThr, double censOpt, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd, bool exclusion, void* terminationCondition, void* errisParams, void* hydroParams, bool restrictionOn, bool weightedLeastSquare);
extern void* CreateERRISParameterEstimator(void* mr, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, double censThr, double censOpt, void* terminationCondition, bool restrictionOn, bool weightedLeastSquare);
extern void SetERRISHydrologicParameterSpace(void* calibObject, void* hydroParams);
extern void SetERRISErrorCorrectionParameterSpace(void* calibObject, void* errisParams);
extern void SetERRISEstimationPeriod(void* calibObject, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd);
extern void SetERRISWarmupPeriod(void* calibObject, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd);
extern void SetERRISExclusionPeriod(void* calibObject, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd);
extern void RemoveERRISWarmupPeriod(void* calibObject);
extern void RemoveERRISExclusionPeriod(void* calibObject);
extern void SetERRISMaxObservation(void* calibObject, double maxObs);
extern void SetERRISCensOptions(void* calibObject, double censOpt);
extern void SetERRISVerboseCalibration(void* calibObject, bool verboseCalibrationLog);
extern void* CalibrateERRISStageOne(void* calibObject);
extern void* CalibrateERRISStageTwo(void* calibObject, void* previousStage);
extern void* CalibrateERRISStageThree(void* calibObject, void* previousStage);
extern void* CalibrateERRISStageFour(void* calibObject, void* previousStage, bool useRising);
extern void* CalibrateERRISStageThreeMS(void* calibObject, void* previousStage);
extern void* ConcatenateERRISStagesParameters(void* calibObject, void* hydroParams, void* stage1_result, void* stage2_result, void* stage3_result, void* stage4a_result, void* stage4b_result, bool toLongParameterName);
extern OptimizerLogData* GetERRISCalibrationLog(void* calibObject);
extern void* PrepareERRISForecasting(void* mr, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd);
extern void* EstimateMAERRISParameters(void* simulation, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd, bool warmup, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, double s2Window, double censThr, double censOpt, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd, bool exclusion, void* terminationCondition, void* maerrisParams, void* hydroParams, bool restrictionOn);
extern void* CreateMAERRISParameterEstimator(void* mr, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, double s2Window, double censThr, double censOpt, void* terminationCondition, bool restrictionOn);
extern void SetMAERRISHydrologicParameterSpace(void* calibObject, void* hydroParams);
extern void SetMAERRISErrorCorrectionParameterSpace(void* calibObject, void* maerrisParams);
extern void SetMAERRISEstimationPeriod(void* calibObject, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd);
extern void SetMAERRISWarmupPeriod(void* calibObject, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd);
extern void SetMAERRISExclusionPeriod(void* calibObject, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd);
extern void RemoveMAERRISWarmupPeriod(void* calibObject);
extern void RemoveMAERRISExclusionPeriod(void* calibObject);
extern void SetMAERRISS2Window(void* calibObject, double s2Window);
extern void SetMAERRISMaxObservation(void* calibObject, double maxObs);
extern void SetMAERRISRestrictionOn(void* calibObject, bool restrictionOn);
extern void SetMAERRISCensOptions(void* calibObject, double censOpt);
extern void SetMAERRISVerboseCalibration(void* calibObject, bool verboseCalibrationLog);
extern void* CalibrateMAERRISStageOne(void* calibObject);
extern void* CalibrateMAERRISStageTwo(void* calibObject, void* previousStage);
extern void* CalibrateMAERRISStageThree(void* calibObject, void* previousStage);
extern void* CalibrateMAERRISStageFour(void* calibObject, void* previousStage, bool useRising);
extern void* CalibrateMAERRISStageThreeMS(void* calibObject, void* previousStage);
extern void* ConcatenateMAERRISStagesParameters(void* calibObject, void* hydroParams, void* stage1_result, void* stage2_result, void* stage3_result, void* stage4a_result, void* stage4b_result, bool toLongParameterName);
extern OptimizerLogData* GetMAERRISCalibrationLog(void* calibObject);
extern void* EstimateDualPassParameters(void* simulation, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd, bool warmup, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, int windowL, int windowDecayL, int windowDecayS, bool useLongPass, char* objFuncDescYaml, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd, bool exclusion, void* terminationCondition);
extern void* PrepareDualPassForecasting(void* mr, double* obsValues, void* obsGeom, const char* errorModelElementId, MarshaledDateTime warmupStart, MarshaledDateTime warmupEnd, double requiredWindowPercentage);
extern void* EstimateTransformationParameters(double* obsValues, void* obsGeom, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, double censThr, double censOpt, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd, bool exclusion, void* terminationCondition);
extern void* EstimateTransformationParametersMS(double* obsValues, void* obsGeom, MarshaledDateTime estimationStart, MarshaledDateTime estimationEnd, MarshaledDateTime exclusionStart, MarshaledDateTime exclusionEnd, bool exclusion, void* terminationCondition, void* Params);
extern void* GetSystemConfigurationWila(void* scores);
extern int GetNumScoresWila(void* scores);
extern double GetScoreWila(void* scores, int index);
extern char* GetScoreNameWila(void* scores, int index);
extern int GetLengthSetOfScores(void* vectorScores);
extern void* ExecuteOptimizerWila(void* optimizer);
extern void SetMaxThreadsOptimizerWila(void* optimizer, int nThreads);
extern void SetDefaultMaxThreadsWila(int nThreads);
extern int GetDefaultMaxThreadsWila();
extern OptimizerLogData* GetOptimizerLogDataWila(void* optimizer);
extern void DisposeOptimizerLogDataWila(OptimizerLogData* logData);
extern void SetOptimizerLoggerWila(void* optimizer, const char* type);
extern void GetOptimizerLogDataWilaDims(OptimizerLogData* logData, int* logLength, int* stringDataCount, int* numericDataCount);
extern char* GetOptimizerLogDataWilaNumericDataNames(OptimizerLogData* logData, int numericDataIndex);
extern char* GetOptimizerLogDataWilaStringDataNames(OptimizerLogData* logData, int stringDataIndex);
extern void GetOptimizerLogDataWilaNumericData(OptimizerLogData* logData, int numericDataIndex, double* data);
extern char** GetOptimizerLogDataWilaStringData(OptimizerLogData* logData, int stringDataIndex);
extern void* CreateStateInitializer(const char* type);
extern void* CloneStateInitializer(void* stateInitializer);
extern bool IsDictionaryStateInitializer(void* stateInitializer);
extern double GetValueStateInitializer(void* stateInitializer, const char* identifier);
extern void SetValueStateInitializer(void* stateInitializer, const char* identifier, double value);
extern void UseStateInitializerModelRunner(void* simulation, void* stateInitializer);
extern void RemoveStateInitializerModelRunner(void* modelSimulation);
extern void AddStateInitializerModelRunner(void* modelSimulation, void* stateInit);
extern void* SnapshotMemoryStates(void* simulation);
extern void ApplyMemoryStates(void* simulation, void* memoryStates);
extern void SetMemoryStates(void* simulation, void* memoryStates);
extern void ClearMemoryStates(void* simulation);
extern void SaveParameterizer(void* parameterizer, const char* filepath);
extern void* LoadParameterizer(const char* filepath);
extern void SaveMemoryStatesToFile(void* memoryStates, const char* filePath, const char* format);
extern void* LoadMemoryStatesFromFile(const char* filePath, const char* format);
extern char* GetMemoryStates(void* memoryStates);
extern void* MemoryStatesFromString(const char* jsonString);
extern void SaveModelSimulationToJson(void* simulation, const char* jsonFilePath);
extern void* LoadModelSimulationFromJson(const char* jsonFilePath);
extern void PlayDatasetInputs(void* simulation, void* dataLibrary, char** identifiers, char** dataId, char** resampleMethod, int size);
extern void* CreateEnsembleForecastSimulation(void* simulation, MarshaledDateTime start, int leadTime, int ensembleSize, int simulationLength, int nTimeStepsBetweenForecasts);
extern void PlayDatasetSingleInput(void* efSimulation, void* dataLibrary, char** identifiers, char** dataId, int size);
extern void PlayDatasetEnsembleForecastInput(void* efSimulation, void* dataLibrary, char** identifiers, char** dataId, int size);
extern void ExecuteEnsembleForecastSimulation(void* efSimulation);
extern void GetEnsembleForecastSingleRecorded(void* efSimulation, const char* variableIdentifier, int leadTimeIndex, int ensembleIndex, double* values);
extern void GetEnsembleForecastEnsembleRecorded(void* efSimulation, const char* variableIdentifier, int leadTimeIndex, double** values);
extern int GetEnsembleForecastLeadLength(void* efSimulation);
extern int GetEnsembleForecastEnsembleSize(void* efSimulation);
extern void PlayEnsembleForecastTimeSeries(void* efSimulation, void* series, const char* variableIdentifier);
extern void RecordEnsembleForecastTimeSeries(void* efSimulation, const char* variableIdentifier);
extern void* GetRecordedEnsembleForecastTimeSeries(void* efSimulation, const char* variableIdentifier);
extern void RecordEnsembleForecastToRecorder(void* efSimulation, char** variableIdentifiers, void* dataLibrary, char** dataIdentifiers, int size);
extern int GetNumModelRunners();
extern int GetNumCatchments();
extern int GetNumRainfallRunoff();
extern int GetNumHyperCubes();
extern int GetNumHyperCubesWila();
extern int GetNumStateInitializers();
extern void SetLogLikelihoodVariableNames(const char* a, const char* b, const char* m, const char* s, const char* maxobs, const char* ct, const char* censopt);
extern void SetLogLikelihoodXVariableNames(const char* a, const char* b, const char* m, const char* s1, const char* s2, const char* w, const char* maxobs, const char* ct, const char* censopt);
extern void SetLogLikelihoodMixtureVariableNames(const char* a, const char* b, const char* m, const char* s1, const char* s2, const char* w, const char* maxobs, const char* ct, const char* censopt);
extern void* LoadVersionOneControlFile(const char* controlFileName, const char* rootDataDir);
extern void* LoadVersionOneTimeSeriesFile(const char* fileName);
extern bool RegisterAdditionalSwiftDataHandling(const char* type);
extern int GetNumMemTestCatchments();
extern int GetNumMemTestModelRunners();
extern void* CreateTestMemoryTrackedSimulation();
extern int GetNumMemTestParameterizers();
extern void* CreateTestMemoryTrackedParameterizer();
extern char* GetNodeName(void* simulation, int index);
extern char* GetLinkName(void* simulation, int index);
extern char* GetRecordedVariableName(void* simulation, int index);
extern char* GetPlayedVariableName(void* simulation, int index);
extern char* GetSubareaName(void* simulation, int index);
extern char* GetNodeIdentifier(void* simulation, int index);
extern char* GetLinkIdentifier(void* simulation, int index);
extern char* GetSubareaIdentifier(void* simulation, int index);
extern char* GetElementVarIdentifier(void* simulation, const char* elementId, int index);

