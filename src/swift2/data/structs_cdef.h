typedef unsigned long int size_t;
typedef struct _SceParameters
{
int Alpha;
int Beta;
int P;
int Pmin;
int M;
int Q;
int NumShuffle;
double TrapezoidalDensityParameter;
double ReflectionRatio;
double ContractionRatio;
} SceParameters;
typedef struct _parameter_interval
{
char* name;
double value;
double minimum;
double maximum;
} parameter_interval;
typedef struct _hypercube_parameter_set
{
size_t size;
parameter_interval* parameters;
} hypercube_parameter_set;
typedef struct _OptimizerLogData
{
int LogLength;
int StringDataCount;
int NumericDataCount;
char** NamesNumericData;
char** NamesStringData;
double** NumericData;
char*** StringData;
} OptimizerLogData;
typedef struct _date_time_to_second
{
int year;
int month;
int day;
int hour;
int minute;
int second;
} date_time_to_second;
typedef struct _named_values_vector
{
size_t size;
double* values;
char** names;
} named_values_vector;
typedef struct _values_vector
{
size_t size;
double* values;
} values_vector;
typedef struct _character_vector
{
size_t size;
char** values;
} character_vector;
typedef struct _string_string_map
{
size_t size;
char** keys;
char** values;
} string_string_map;
typedef enum _time_step_code
{
strictly_regular = 0,
monthly_step = 1
} time_step_code;
typedef struct _regular_time_series_geometry
{
date_time_to_second start;
int time_step_seconds;
int length;
time_step_code time_step_code;
} regular_time_series_geometry;
typedef struct _multi_regular_time_series_data
{
regular_time_series_geometry time_series_geometry;
int ensemble_size;
double** numeric_data;
} multi_regular_time_series_data;
typedef struct _time_series_dimension_description
{
char* dimension_type;
size_t size;
} time_series_dimension_description;
typedef struct _time_series_dimensions_description
{
time_series_dimension_description* dimensions;
int num_dimensions;
} time_series_dimensions_description;
typedef struct _statistic_definition
{
char* model_variable_id;
char* objective_identifier;
char* objective_name;
char* statistic_identifier;
date_time_to_second start;
date_time_to_second end;
multi_regular_time_series_data* observations;
} statistic_definition;
typedef struct _multi_statistic_definition
{
int size;
statistic_definition** statistics;
char* mix_statistics_id;
} multi_statistic_definition;
typedef date_time_to_second MarshaledDateTime ;
typedef regular_time_series_geometry MarshaledTsGeometry;
typedef multi_regular_time_series_data MultiTimeSeriesData;
typedef struct _NodeInfo
{
char* Id;
char* Name;
} NodeInfo;
typedef struct _LinkInfo
{
char* Id;
char* Name;
double LengthMetres;
double f;
double ManningsN;
double Slope;
} LinkInfo;
typedef struct _SubareaInfo
{
char* Id;
char* Name;
double SubareaSurfaceKm2;
} SubareaInfo;
typedef struct _NodeLinkConnection
{
char* LinkId;
char* UpstreamNodeId;
char* DownstreamNodeId;
} NodeLinkConnection;
typedef struct _SubareaLinkConnection
{
char* SubareaId;
char* LinkId;
} SubareaLinkConnection;
typedef struct _CatchmentStructure
{
int NumNodes;
int NumLinks;
int NumSubareas;
int NumNodeLinkConnections;
int NumSubareaLinkConnections;
NodeInfo* Nodes;
LinkInfo* Links;
SubareaInfo* Subareas;
NodeLinkConnection* NodeLinkConnections;
SubareaLinkConnection* SubareaLinkConnections;
} CatchmentStructure;