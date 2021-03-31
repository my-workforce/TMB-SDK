# TpoDataDTOsLabOrderDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID | 
**type** | **str** | Specifies the order type using Values: Request, Cancellation | 
**reference_number** | **str** | Transaction Reference Number | [optional] 
**clinician** | **str** | In general the Clinician is the person providing the referral for the patient | 
**patient** | [**TpoDataDTOsSharedPatientDTO**](TpoDataDTOsSharedPatientDTO.md) |  | 
**encounter** | [**TpoDataDTOsLabEncounterDTO**](TpoDataDTOsLabEncounterDTO.md) |  | [optional] 
**diagnosis** | [**list[TpoDataDTOsLabDiagnosisDTO]**](TpoDataDTOsLabDiagnosisDTO.md) | Order Diagnosis | [optional] 
**activity** | [**list[TpoDataDTOsLabActivityDTO]**](TpoDataDTOsLabActivityDTO.md) | Order Activities | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

