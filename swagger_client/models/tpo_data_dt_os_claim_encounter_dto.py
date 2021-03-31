# coding: utf-8

"""
    Transaction Management Bus (TMB) API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V3.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class TpoDataDTOsClaimEncounterDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'facility_id': 'str',
        'type': 'str',
        'patient_id': 'str',
        'start': 'str',
        'end': 'str',
        'start_type': 'str',
        'end_type': 'str',
        'transfer_source': 'str',
        'transfer_destination': 'str'
    }

    attribute_map = {
        'facility_id': 'FacilityID',
        'type': 'Type',
        'patient_id': 'PatientID',
        'start': 'Start',
        'end': 'End',
        'start_type': 'StartType',
        'end_type': 'EndType',
        'transfer_source': 'TransferSource',
        'transfer_destination': 'TransferDestination'
    }

    def __init__(self, facility_id=None, type=None, patient_id=None, start=None, end=None, start_type=None,
                 end_type=None, transfer_source=None, transfer_destination=None):  # noqa: E501
        """TpoDataDTOsClaimEncounterDTO - a model defined in Swagger"""  # noqa: E501
        self._facility_id = None
        self._type = None
        self._patient_id = None
        self._start = None
        self._end = None
        self._start_type = None
        self._end_type = None
        self._transfer_source = None
        self._transfer_destination = None
        self.discriminator = None
        self.facility_id = facility_id
        self.type = type
        self.patient_id = patient_id
        self.start = start
        if end is not None:
            self.end = end
        if start_type is not None:
            self.start_type = start_type
        if end_type is not None:
            self.end_type = end_type
        if transfer_source is not None:
            self.transfer_source = transfer_source
        if transfer_destination is not None:
            self.transfer_destination = transfer_destination

    @property
    def facility_id(self):
        """Gets the facility_id of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        Gets or sets the identifier of the facility.  # noqa: E501

        :return: The facility_id of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this TpoDataDTOsClaimEncounterDTO.

        Gets or sets the identifier of the facility.  # noqa: E501

        :param facility_id: The facility_id of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")  # noqa: E501

        self._facility_id = facility_id

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        Type of the encounter should be one of the following:    1 = No Bed + No emergency room    2 = No Bed + Emergency room    3 = Inpatient Bed + No emergency room    4 = Inpatient Bed + Emergency room    5 = Daycase Bed + No emergency room    6 = Daycase Bed + Emergency room    7 = Nationals Screening    8 = New Visa Screening    9 = Renewal Visa Screening    12 = Home    13 = Assisted Living Facility    15 = Mobile Unit    41 = Ambulance - Land    42 = Ambulance - Air or Water  # noqa: E501

        :return: The type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsClaimEncounterDTO.

        Type of the encounter should be one of the following:    1 = No Bed + No emergency room    2 = No Bed + Emergency room    3 = Inpatient Bed + No emergency room    4 = Inpatient Bed + Emergency room    5 = Daycase Bed + No emergency room    6 = Daycase Bed + Emergency room    7 = Nationals Screening    8 = New Visa Screening    9 = Renewal Visa Screening    12 = Home    13 = Assisted Living Facility    15 = Mobile Unit    41 = Ambulance - Land    42 = Ambulance - Air or Water  # noqa: E501

        :param type: The type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def patient_id(self):
        """Gets the patient_id of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        The unique number a healthcare provider assigns to a patient.  # noqa: E501

        :return: The patient_id of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """Sets the patient_id of this TpoDataDTOsClaimEncounterDTO.

        The unique number a healthcare provider assigns to a patient.  # noqa: E501

        :param patient_id: The patient_id of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """
        if patient_id is None:
            raise ValueError("Invalid value for `patient_id`, must not be `None`")  # noqa: E501

        self._patient_id = patient_id

    @property
    def start(self):
        """Gets the start of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        EncounterStart is the date and time at which the patient comes under the care of a responsible clinician             Date Time format: DD/MM/YYYYY HH:MM.  # noqa: E501

        :return: The start of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TpoDataDTOsClaimEncounterDTO.

        EncounterStart is the date and time at which the patient comes under the care of a responsible clinician             Date Time format: DD/MM/YYYYY HH:MM.  # noqa: E501

        :param start: The start of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        The time the patient ceases to be under the direct care of a responsible clinician, discharge date and time for inpatients              Date Time format: DD/MM/YYYYY HH:MM.  # noqa: E501

        :return: The end of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TpoDataDTOsClaimEncounterDTO.

        The time the patient ceases to be under the direct care of a responsible clinician, discharge date and time for inpatients              Date Time format: DD/MM/YYYYY HH:MM.  # noqa: E501

        :param end: The end of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def start_type(self):
        """Gets the start_type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        Encounter Start Type:    1 = Elective, i.e., an Encounter is scheduled in advance   2 = Emergency   3 = Transfer, i.e., primarily inter-hospital transfers, not between wards within a hospital   4 = Live birth   5 = Still birth   6 = Dead On Arrival   7 = Continuing Encounter  # noqa: E501

        :return: The start_type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        """Sets the start_type of this TpoDataDTOsClaimEncounterDTO.

        Encounter Start Type:    1 = Elective, i.e., an Encounter is scheduled in advance   2 = Emergency   3 = Transfer, i.e., primarily inter-hospital transfers, not between wards within a hospital   4 = Live birth   5 = Still birth   6 = Dead On Arrival   7 = Continuing Encounter  # noqa: E501

        :param start_type: The start_type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """

        self._start_type = start_type

    @property
    def end_type(self):
        """Gets the end_type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        How the patient was discharged.              1 = Discharged with approval              2 = Discharged against advice              3 = Discharged absent without leave              4 = Discharge transfer to acute care              5 = Deceased              6 = Not discharged              7 = Discharge transfer to non-acute care(Transfer to long term care).  # noqa: E501

        :return: The end_type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_type

    @end_type.setter
    def end_type(self, end_type):
        """Sets the end_type of this TpoDataDTOsClaimEncounterDTO.

        How the patient was discharged.              1 = Discharged with approval              2 = Discharged against advice              3 = Discharged absent without leave              4 = Discharge transfer to acute care              5 = Deceased              6 = Not discharged              7 = Discharge transfer to non-acute care(Transfer to long term care).  # noqa: E501

        :param end_type: The end_type of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """

        self._end_type = end_type

    @property
    def transfer_source(self):
        """Gets the transfer_source of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        EncounterTransferSource is the healthcare facility from where a hospital transfer originated (EncounterStartType = 3 Transfer).  # noqa: E501

        :return: The transfer_source of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._transfer_source

    @transfer_source.setter
    def transfer_source(self, transfer_source):
        """Sets the transfer_source of this TpoDataDTOsClaimEncounterDTO.

        EncounterTransferSource is the healthcare facility from where a hospital transfer originated (EncounterStartType = 3 Transfer).  # noqa: E501

        :param transfer_source: The transfer_source of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """

        self._transfer_source = transfer_source

    @property
    def transfer_destination(self):
        """Gets the transfer_destination of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501

        Transfer Destination is the healthcare facility to which a hospital transfer is made at the end of an Encounter (EncounterEndType = 4 Transfer).  # noqa: E501

        :return: The transfer_destination of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._transfer_destination

    @transfer_destination.setter
    def transfer_destination(self, transfer_destination):
        """Sets the transfer_destination of this TpoDataDTOsClaimEncounterDTO.

        Transfer Destination is the healthcare facility to which a hospital transfer is made at the end of an Encounter (EncounterEndType = 4 Transfer).  # noqa: E501

        :param transfer_destination: The transfer_destination of this TpoDataDTOsClaimEncounterDTO.  # noqa: E501
        :type: str
        """

        self._transfer_destination = transfer_destination

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TpoDataDTOsClaimEncounterDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TpoDataDTOsClaimEncounterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other