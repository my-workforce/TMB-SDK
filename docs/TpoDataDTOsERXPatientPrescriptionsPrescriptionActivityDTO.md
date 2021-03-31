# TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of activity within a Prescription. | 
**type** | **str** | ActivityType classifies the type of activity. (Should have the value 5 for Drug or the value 10 for scientific code) | 
**code** | **str** | ActivityCode is the code, specified by ActivityType, for the Activity performed. | 
**quantity** | **float** | Identifies the number of units (quantity) for a specific Activity. | 
**duration** | **float** | Identifies the duration in days for the prescribed activity. | 
**unit_id** | **int** | Identifies the type of units  for a specific Activity. | 
**refills** | **int** | Identifies the number of refills for a given activity. | [optional] 
**rout_of_admin** | **str** | Identifies the rout of admin for a given activity. | 
**instructions** | **str** | Identifies the instructions for a given activity as provided by the prescribing clinician. | 
**arabic_instructions** | **str** | Identifies the Arabic instructions for a given activity as provided by the prescribing clinician.              &lt;div&gt;&lt;p&gt;&lt;strong style&#x3D;\&quot;border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\&quot;&gt; Conditional required&lt;/strong&gt; required when normal instructions are being sent              &lt;/p&gt;&lt;/div&gt; | [optional] 
**start** | **str** | The date and time at which Activity started  Date Time format: DD/MM/YYYYY HH:MM | 
**frequency** | [**TpoDataDTOsERXFrequencyDTO**](TpoDataDTOsERXFrequencyDTO.md) |  | [optional] 
**observation** | [**list[TpoDataDTOsSharedObservationDTO]**](TpoDataDTOsSharedObservationDTO.md) | Activity Observations. | [optional] 
**status** | **str** |  | [optional] 
**remaining_refills** | **int** |  | [optional] 
**dispense_track** | [**list[TpoDataDTOsERXPatientPrescriptionsActivityDispenseTrackDTO]**](TpoDataDTOsERXPatientPrescriptionsActivityDispenseTrackDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

