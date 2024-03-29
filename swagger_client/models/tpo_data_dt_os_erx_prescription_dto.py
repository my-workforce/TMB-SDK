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


class TpoDataDTOsERXPrescriptionDTO(object):
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
        'id': 'str',
        'type': 'str',
        'reference_number': 'str',
        'clinician': 'str',
        'patient': 'TpoDataDTOsSharedPatientDTO',
        'encounter': 'TpoDataDTOsERXEncounterDTO',
        'diagnosis': 'list[TpoDataDTOsSharedDiagnosisDTO]',
        'activity': 'list[TpoDataDTOsERXActivityDTO]',
        'comments': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'type': 'Type',
        'reference_number': 'ReferenceNumber',
        'clinician': 'Clinician',
        'patient': 'Patient',
        'encounter': 'Encounter',
        'diagnosis': 'Diagnosis',
        'activity': 'Activity',
        'comments': 'Comments'
    }

    def __init__(self, id=None, type=None, reference_number=None, clinician=None, patient=None, encounter=None,
                 diagnosis=None, activity=None, comments=None):  # noqa: E501
        """TpoDataDTOsERXPrescriptionDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._reference_number = None
        self._clinician = None
        self._patient = None
        self._encounter = None
        self._diagnosis = None
        self._activity = None
        self._comments = None
        self.discriminator = None
        self.id = id
        self.type = type
        if reference_number is not None:
            self.reference_number = reference_number
        self.clinician = clinician
        self.patient = patient
        if encounter is not None:
            self.encounter = encounter
        if diagnosis is not None:
            self.diagnosis = diagnosis
        if activity is not None:
            self.activity = activity
        if comments is not None:
            self.comments = comments

    @property
    def id(self):
        """Gets the id of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        Prescription ID  # noqa: E501

        :return: The id of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpoDataDTOsERXPrescriptionDTO.

        Prescription ID  # noqa: E501

        :param id: The id of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        Specifies the e-Prescription (Erx) transaction type using Values: eRxRequest, eRxCancellation  # noqa: E501

        :return: The type of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsERXPrescriptionDTO.

        Specifies the e-Prescription (Erx) transaction type using Values: eRxRequest, eRxCancellation  # noqa: E501

        :param type: The type of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def reference_number(self):
        """Gets the reference_number of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        Transaction Reference Number  # noqa: E501

        :return: The reference_number of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this TpoDataDTOsERXPrescriptionDTO.

        Transaction Reference Number  # noqa: E501

        :param reference_number: The reference_number of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: str
        """

        self._reference_number = reference_number

    @property
    def clinician(self):
        """Gets the clinician of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        In general the Clinician is the person providing the referral for the patient  # noqa: E501

        :return: The clinician of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: str
        """
        return self._clinician

    @clinician.setter
    def clinician(self, clinician):
        """Sets the clinician of this TpoDataDTOsERXPrescriptionDTO.

        In general the Clinician is the person providing the referral for the patient  # noqa: E501

        :param clinician: The clinician of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: str
        """
        if clinician is None:
            raise ValueError("Invalid value for `clinician`, must not be `None`")  # noqa: E501

        self._clinician = clinician

    @property
    def patient(self):
        """Gets the patient of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501


        :return: The patient of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: TpoDataDTOsSharedPatientDTO
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this TpoDataDTOsERXPrescriptionDTO.


        :param patient: The patient of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: TpoDataDTOsSharedPatientDTO
        """
        if patient is None:
            raise ValueError("Invalid value for `patient`, must not be `None`")  # noqa: E501

        self._patient = patient

    @property
    def encounter(self):
        """Gets the encounter of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501


        :return: The encounter of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: TpoDataDTOsERXEncounterDTO
        """
        return self._encounter

    @encounter.setter
    def encounter(self, encounter):
        """Sets the encounter of this TpoDataDTOsERXPrescriptionDTO.


        :param encounter: The encounter of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: TpoDataDTOsERXEncounterDTO
        """

        self._encounter = encounter

    @property
    def diagnosis(self):
        """Gets the diagnosis of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        Prescription Diagnosis  # noqa: E501

        :return: The diagnosis of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsSharedDiagnosisDTO]
        """
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        """Sets the diagnosis of this TpoDataDTOsERXPrescriptionDTO.

        Prescription Diagnosis  # noqa: E501

        :param diagnosis: The diagnosis of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: list[TpoDataDTOsSharedDiagnosisDTO]
        """

        self._diagnosis = diagnosis

    @property
    def activity(self):
        """Gets the activity of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        Prescription Activities  # noqa: E501

        :return: The activity of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsERXActivityDTO]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this TpoDataDTOsERXPrescriptionDTO.

        Prescription Activities  # noqa: E501

        :param activity: The activity of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: list[TpoDataDTOsERXActivityDTO]
        """

        self._activity = activity

    @property
    def comments(self):
        """Gets the comments of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501

        Physician Comments  # noqa: E501

        :return: The comments of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TpoDataDTOsERXPrescriptionDTO.

        Physician Comments  # noqa: E501

        :param comments: The comments of this TpoDataDTOsERXPrescriptionDTO.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if issubclass(TpoDataDTOsERXPrescriptionDTO, dict):
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
        if not isinstance(other, TpoDataDTOsERXPrescriptionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
