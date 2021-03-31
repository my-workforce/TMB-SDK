# TpoDataDTOsClaimClaimDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Claim ID. | 
**id_payer** | **str** | The unique number assigned by an insurer to identify the Claim. | [optional] 
**member_id** | **str** | The patient&#x27;s insurance member number, if the patient is claiming insurance. | 
**manual_claim** | **bool** | Manual claim. | [optional] 
**date_ordered** | **str** |  The date and time at which prescription ordered   Date Time format: DD/MM/YYYYY HH:MM  &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when submission type equals “Submission” and ManualClaim equal true  &lt;/p&gt;&lt;/div&gt; | [optional] 
**provider_id** | **str** | ID of the provider claiming from the Payer. | 
**weight** | **float** | The patient&#x27;s weight. | 
**national_id_number** | **str** | The unique number the government assigns to a citizen. | 
**height** | **float** | The patient&#x27;s height in cm | [optional] 
**gross** | **float** | The total amount of the charges included on the Claim. | 
**patient_share** | **float** | The amount a patient owes a provider according to the terms of their insurance plan/product. | 
**net** | **float** | The net charges included on the Claim. This is the amount the provider is expected to be paid. | 
**dispense_reference_id** | **str** | The unique number assigned to the request dispense. This is the Reference Number for Erx              &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when submission type equals “Prescription-Dispense”              &lt;/p&gt;&lt;/div&gt; | [optional] 
**encounter** | [**TpoDataDTOsClaimEncounterDTO**](TpoDataDTOsClaimEncounterDTO.md) |  | 
**diagnosis** | [**list[TpoDataDTOsSharedDiagnosisDTO]**](TpoDataDTOsSharedDiagnosisDTO.md) | Claim Diagnosis. | [optional] 
**activity** | [**list[TpoDataDTOsClaimActivityDTO]**](TpoDataDTOsClaimActivityDTO.md) | Claim Activities. | [optional] 
**resubmission** | [**TpoDataDTOsClaimResubmissionDTO**](TpoDataDTOsClaimResubmissionDTO.md) |  | [optional] 
**supporting_information** | [**TpoDataDTOsClaimSupportingInformationDTO**](TpoDataDTOsClaimSupportingInformationDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

