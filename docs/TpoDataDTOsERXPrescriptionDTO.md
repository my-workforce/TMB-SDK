# TpoDataDTOsERXPrescriptionDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Prescription ID | 
**type** | **str** | Specifies the e-Prescription (Erx) transaction type using Values: eRxRequest, eRxCancellation | 
**reference_number** | **str** | Transaction Reference Number | [optional] 
**clinician** | **str** | In general the Clinician is the person providing the referral for the patient | 
**patient** | [**TpoDataDTOsSharedPatientDTO**](TpoDataDTOsSharedPatientDTO.md) |  | 
**encounter** | [**TpoDataDTOsERXEncounterDTO**](TpoDataDTOsERXEncounterDTO.md) |  | [optional] 
**diagnosis** | [**list[TpoDataDTOsSharedDiagnosisDTO]**](TpoDataDTOsSharedDiagnosisDTO.md) | Prescription Diagnosis | [optional] 
**activity** | [**list[TpoDataDTOsERXActivityDTO]**](TpoDataDTOsERXActivityDTO.md) | Prescription Activities | [optional] 
**comments** | **str** | Physician Comments | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

