# TpoDataDTOsAuthorizationAuthorizationAuthorizationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | The answer of the inquiry can be one of the following (Yes, No or Pending). | [optional] 
**id** | **str** | Authorization ID. | 
**id_payer** | **str** | The unique number assigned by an insurer to identify the Claim. | [optional] 
**denial_code** | **str** | The denial code if the claim is denied by the payer. | [optional] 
**start** | **str** | The date and time at started  Date Time format: DD/MM/YYYYY HH:MM | 
**end** | **str** | The date and time at ended  Date Time format: DD/MM/YYYYY HH:MM | 
**limit** | **float** | Identifies the Authorization Limit. | [optional] 
**comments** | **str** | The comments given to add more details on the Authorization. | [optional] 
**activity** | [**list[TpoDataDTOsAuthorizationAuthorizationActivityDTO]**](TpoDataDTOsAuthorizationAuthorizationActivityDTO.md) | Authorization Activity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

