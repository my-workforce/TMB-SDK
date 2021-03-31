# TpoDataDTOsClaimEncounterDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_id** | **str** | Gets or sets the identifier of the facility. | 
**type** | **str** | Type of the encounter should be one of the following:    1 &#x3D; No Bed + No emergency room    2 &#x3D; No Bed + Emergency room    3 &#x3D; Inpatient Bed + No emergency room    4 &#x3D; Inpatient Bed + Emergency room    5 &#x3D; Daycase Bed + No emergency room    6 &#x3D; Daycase Bed + Emergency room    7 &#x3D; Nationals Screening    8 &#x3D; New Visa Screening    9 &#x3D; Renewal Visa Screening    12 &#x3D; Home    13 &#x3D; Assisted Living Facility    15 &#x3D; Mobile Unit    41 &#x3D; Ambulance - Land    42 &#x3D; Ambulance - Air or Water | 
**patient_id** | **str** | The unique number a healthcare provider assigns to a patient. | 
**start** | **str** | EncounterStart is the date and time at which the patient comes under the care of a responsible clinician             Date Time format: DD/MM/YYYYY HH:MM. | 
**end** | **str** | The time the patient ceases to be under the direct care of a responsible clinician, discharge date and time for inpatients              Date Time format: DD/MM/YYYYY HH:MM. | [optional] 
**start_type** | **str** | Encounter Start Type:    1 &#x3D; Elective, i.e., an Encounter is scheduled in advance   2 &#x3D; Emergency   3 &#x3D; Transfer, i.e., primarily inter-hospital transfers, not between wards within a hospital   4 &#x3D; Live birth   5 &#x3D; Still birth   6 &#x3D; Dead On Arrival   7 &#x3D; Continuing Encounter | [optional] 
**end_type** | **str** | How the patient was discharged.              1 &#x3D; Discharged with approval              2 &#x3D; Discharged against advice              3 &#x3D; Discharged absent without leave              4 &#x3D; Discharge transfer to acute care              5 &#x3D; Deceased              6 &#x3D; Not discharged              7 &#x3D; Discharge transfer to non-acute care(Transfer to long term care). | [optional] 
**transfer_source** | **str** | EncounterTransferSource is the healthcare facility from where a hospital transfer originated (EncounterStartType &#x3D; 3 Transfer). | [optional] 
**transfer_destination** | **str** | Transfer Destination is the healthcare facility to which a hospital transfer is made at the end of an Encounter (EncounterEndType &#x3D; 4 Transfer). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

