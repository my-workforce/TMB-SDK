# TpoDataDTOsSharedSubmissionHeaderDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **str** | Unique identifier of the Provider, Payer or TPA receiving information, as provided by the regulator. | 
**receiver_id** | **str** | Unique identifier of the Provider, Payer or TPA receiving information, as provided by the regulator. | 
**transaction_date** | **str** | System generated date and time specifying when the transaction was generated             Date Time format: DD/MM/YYYYY HH:MM | 
**record_count** | **int** | Number of sub objects in the file. The file may contain at least 1 record, and may contain more than one depending on the business and validation rules related to that specific transaction. | 
**disposition_flag** | **str** | Flag to determine if the transaction file is either a “TEST” or production “PRODUCTION” file based on the selected reserved word. | 
**payer_id** | **str** | PayerID is the Insurer License if the ReceiverID is TPA. If ReceiverID is Insurance, PayerID must be equal to ReceiverID. | 
**transaction_type** | **str** | Indicating Submission type: “Submission”, “Resubmission”, “Prescription-Dispense”, “Radiology-Dispense”, “Laboratory-Dispense”. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

