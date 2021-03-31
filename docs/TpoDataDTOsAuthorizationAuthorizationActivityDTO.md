# TpoDataDTOsAuthorizationAuthorizationActivityDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of activity within an authorization. | 
**type** | **str** | The type of activity. 3 &#x3D; CPT; 4 &#x3D; HCPCS; 5 &#x3D; Drug; 6 &#x3D; Dental; 8 &#x3D; Service Code; 9 &#x3D; DRG; 10 &#x3D; Scientific Code. | 
**code** | **str** | ActivityCode is the code, specified by ActivityType, for the Activity performed. | 
**quantity** | **float** | Identifies the number of units (quantity) for a specific Activity. | [optional] 
**net** | **float** | The net charges billed by the provider to the Payer for this Activity. | 
**list** | **float** | ActivityList describes the list price before any adjustments of discounts. | [optional] 
**patient_share** | **float** | Any fee the provider have effectively collected from the patient. | [optional] 
**payment_amount** | **float** | Amount Approved to be paid by the payer for the activity. | 
**denial_code** | **str** | The denial code if the Activity is denied by the payer. | [optional] 
**observation** | [**list[TpoDataDTOsSharedObservationDTO]**](TpoDataDTOsSharedObservationDTO.md) | Activity Observations. | [optional] 
**comments** | **str** | Optional comments by the payer (2000 max chars). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

