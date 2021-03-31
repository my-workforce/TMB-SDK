# TpoDataDTOsAuthorizationRequestAuthorizationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specifies Type using Values: Eligibility, Authorization, Cancellation. | 
**id** | **str** | Authorization ID. | 
**request_type** | **str** |  What transaction user want to authorize.   New &#x3D; Stand-alone Request   Prescription &#x3D; Request Authorization for Prescription dispense  &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when authorization type equals “Authorization”  &lt;/p&gt;&lt;/div&gt; | [optional] 
**request_reference_number** | **str** |  The Request Reference Number user wants to authorize.  &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when request type equals “Prescription”  &lt;/p&gt;&lt;/div&gt; | [optional] 
**id_payer** | **str** | The unique number assigned by an insurer to identify the Claim. | [optional] 
**member_id** | **str** | The patient&#x27;s insurance member number, if the patient is claiming insurance. | 
**weight** | **float** | The patient&#x27;s weight. | [optional] 
**height** | **float** | The patient&#x27;s height in cm | [optional] 
**patient_name** | **str** | Patient name | [optional] 
**contact_number** | **str** | Patient contact number | [optional] 
**national_id_number** | **str** | Gets or sets the national identifier number. | 
**date_ordered** | **str** | The date on which the prescription/order is ordered/prescribed.             Date format: DD/MM/YYYYY | 
**encounter** | [**TpoDataDTOsAuthorizationRequestEncounterDTO**](TpoDataDTOsAuthorizationRequestEncounterDTO.md) |  | [optional] 
**diagnosis** | [**list[TpoDataDTOsSharedDiagnosisDTO]**](TpoDataDTOsSharedDiagnosisDTO.md) | Authorization Diagnosis. | [optional] 
**activity** | [**list[TpoDataDTOsAuthorizationRequestActivityDTO]**](TpoDataDTOsAuthorizationRequestActivityDTO.md) | Authorization Activity. | [optional] 
**resubmission** | [**TpoDataDTOsAuthorizationRequestResubmissionDTO**](TpoDataDTOsAuthorizationRequestResubmissionDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

