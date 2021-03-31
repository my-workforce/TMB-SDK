# TpoDataDTOsClaimActivityDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of activity within a claim. | 
**start** | **str** | The date and time at which Activity started              Date Time format: DD/MM/YYYYY HH:MM. | 
**type** | **str** | The type of activity. 3 &#x3D; CPT; 4 &#x3D; HCPCS; 5 &#x3D; Drug; 6 &#x3D; Dental; 8 &#x3D; Service Code; 9 &#x3D; DRG; 10 &#x3D; Scientific Code. | 
**alternative_reason** | **str** | The reason for alternative dispensing. | [optional] 
**code** | **str** | ActivityCode is the code, specified by ActivityType, for the Activity performed. | 
**quantity** | **float** | Identifies the number of units (quantity) for a specific Activity. | 
**net** | **float** | The net charges billed by the provider to the Payer for this Activity. | 
**clinician** | **str** | License number of the Clinician who is providing the treatment or care for the patient. | 
**prior_authorization_id** | **str** | The Prior Authorization ID.              &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when there is an authorization for this claim              &lt;/p&gt;&lt;/div&gt; | [optional] 
**dispensed_activity_id** | **str** | Dispensed Activity ID.               Represents the activity Id from the transaction we want to dispense.              &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when submission type equals “Prescription-Dispense”              &lt;/p&gt;&lt;/div&gt; | [optional] 
**observation** | [**list[TpoDataDTOsSharedObservationDTO]**](TpoDataDTOsSharedObservationDTO.md) | Activity Observation. | [optional] 
**result** | [**list[TpoDataDTOsClaimActivityResultDTO]**](TpoDataDTOsClaimActivityResultDTO.md) | Activity Result. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

