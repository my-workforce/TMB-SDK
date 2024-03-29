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


class TpoDataDTOsERXEncounterDTO(object):
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
        'type': 'int',
        'vital_signs': 'list[TpoDataDTOsPatientPatientVitalSignsDTO]',
        'patient_observation': 'TpoDataDTOsPatientPatientObservationDTO',
        'allergy_codes': 'list[str]'
    }

    attribute_map = {
        'facility_id': 'FacilityID',
        'type': 'Type',
        'vital_signs': 'VitalSigns',
        'patient_observation': 'PatientObservation',
        'allergy_codes': 'AllergyCodes'
    }

    def __init__(self, facility_id=None, type=None, vital_signs=None, patient_observation=None,
                 allergy_codes=None):  # noqa: E501
        """TpoDataDTOsERXEncounterDTO - a model defined in Swagger"""  # noqa: E501
        self._facility_id = None
        self._type = None
        self._vital_signs = None
        self._patient_observation = None
        self._allergy_codes = None
        self.discriminator = None
        self.facility_id = facility_id
        self.type = type
        if vital_signs is not None:
            self.vital_signs = vital_signs
        self.patient_observation = patient_observation
        if allergy_codes is not None:
            self.allergy_codes = allergy_codes

    @property
    def facility_id(self):
        """Gets the facility_id of this TpoDataDTOsERXEncounterDTO.  # noqa: E501

        ID  of the facility responsible for the Encounter  # noqa: E501

        :return: The facility_id of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :rtype: str
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this TpoDataDTOsERXEncounterDTO.

        ID  of the facility responsible for the Encounter  # noqa: E501

        :param facility_id: The facility_id of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :type: str
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")  # noqa: E501

        self._facility_id = facility_id

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsERXEncounterDTO.  # noqa: E501

        Type of the encounter:  1 = No Bed + No emergency room  2 = No Bed + Emergency room  3 = Inpatient Bed + No emergency room  4 = Inpatient Bed + Emergency room  5 = Daycase Bed + No emergency room  6 = Daycase Bed + Emergency room  7 = Nationals Screening  8 = New Visa Screening  9 = Renewal Visa Screening  12 = Home  13 = Assisted Living Facility  15 = Mobile Unit  41 = Ambulance - Land  42 = Ambulance - Air or Water  # noqa: E501

        :return: The type of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsERXEncounterDTO.

        Type of the encounter:  1 = No Bed + No emergency room  2 = No Bed + Emergency room  3 = Inpatient Bed + No emergency room  4 = Inpatient Bed + Emergency room  5 = Daycase Bed + No emergency room  6 = Daycase Bed + Emergency room  7 = Nationals Screening  8 = New Visa Screening  9 = Renewal Visa Screening  12 = Home  13 = Assisted Living Facility  15 = Mobile Unit  41 = Ambulance - Land  42 = Ambulance - Air or Water  # noqa: E501

        :param type: The type of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def vital_signs(self):
        """Gets the vital_signs of this TpoDataDTOsERXEncounterDTO.  # noqa: E501

        Patient vital signs  # noqa: E501

        :return: The vital_signs of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsPatientPatientVitalSignsDTO]
        """
        return self._vital_signs

    @vital_signs.setter
    def vital_signs(self, vital_signs):
        """Sets the vital_signs of this TpoDataDTOsERXEncounterDTO.

        Patient vital signs  # noqa: E501

        :param vital_signs: The vital_signs of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :type: list[TpoDataDTOsPatientPatientVitalSignsDTO]
        """

        self._vital_signs = vital_signs

    @property
    def patient_observation(self):
        """Gets the patient_observation of this TpoDataDTOsERXEncounterDTO.  # noqa: E501


        :return: The patient_observation of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :rtype: TpoDataDTOsPatientPatientObservationDTO
        """
        return self._patient_observation

    @patient_observation.setter
    def patient_observation(self, patient_observation):
        """Sets the patient_observation of this TpoDataDTOsERXEncounterDTO.


        :param patient_observation: The patient_observation of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :type: TpoDataDTOsPatientPatientObservationDTO
        """
        if patient_observation is None:
            raise ValueError("Invalid value for `patient_observation`, must not be `None`")  # noqa: E501

        self._patient_observation = patient_observation

    @property
    def allergy_codes(self):
        """Gets the allergy_codes of this TpoDataDTOsERXEncounterDTO.  # noqa: E501

        Patient allergies  # noqa: E501

        :return: The allergy_codes of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._allergy_codes

    @allergy_codes.setter
    def allergy_codes(self, allergy_codes):
        """Sets the allergy_codes of this TpoDataDTOsERXEncounterDTO.

        Patient allergies  # noqa: E501

        :param allergy_codes: The allergy_codes of this TpoDataDTOsERXEncounterDTO.  # noqa: E501
        :type: list[str]
        """

        self._allergy_codes = allergy_codes

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
        if issubclass(TpoDataDTOsERXEncounterDTO, dict):
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
        if not isinstance(other, TpoDataDTOsERXEncounterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
