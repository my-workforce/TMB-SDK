# TpoDataDTOsRadActivityDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of activity within an Order | 
**type** | **str** | ActivityType classifies the type of activity. (must have the value 3, CPT) | 
**code** | **str** | ActivityCode is the code, specified by ActivityType, for the Activity performed. | 
**quantity** | **float** | Identifies the number of units (quantity) for a specific Activity. | 
**instructions** | **str** | Identifies the instructions for a given activity as provided by the prescribing clinician | [optional] 
**observation** | [**list[TpoDataDTOsSharedObservationDTO]**](TpoDataDTOsSharedObservationDTO.md) | Actvity Observations | [optional] 
**start** | **str** | The date and time at which Activity started  Date Time format: DD/MM/YYYYY HH:MM | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

