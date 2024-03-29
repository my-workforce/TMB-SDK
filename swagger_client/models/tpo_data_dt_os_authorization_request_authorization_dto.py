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


class TpoDataDTOsAuthorizationRequestAuthorizationDTO(object):
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
        'type': 'str',
        'id': 'str',
        'request_type': 'str',
        'request_reference_number': 'str',
        'id_payer': 'str',
        'member_id': 'str',
        'weight': 'float',
        'height': 'float',
        'patient_name': 'str',
        'contact_number': 'str',
        'national_id_number': 'str',
        'date_ordered': 'str',
        'encounter': 'TpoDataDTOsAuthorizationRequestEncounterDTO',
        'diagnosis': 'list[TpoDataDTOsSharedDiagnosisDTO]',
        'activity': 'list[TpoDataDTOsAuthorizationRequestActivityDTO]',
        'resubmission': 'TpoDataDTOsAuthorizationRequestResubmissionDTO'
    }

    attribute_map = {
        'type': 'Type',
        'id': 'ID',
        'request_type': 'RequestType',
        'request_reference_number': 'RequestReferenceNumber',
        'id_payer': 'IDPayer',
        'member_id': 'MemberID',
        'weight': 'Weight',
        'height': 'Height',
        'patient_name': 'PatientName',
        'contact_number': 'ContactNumber',
        'national_id_number': 'NationalIDNumber',
        'date_ordered': 'DateOrdered',
        'encounter': 'Encounter',
        'diagnosis': 'Diagnosis',
        'activity': 'Activity',
        'resubmission': 'Resubmission'
    }

    def __init__(self, type=None, id=None, request_type=None, request_reference_number=None, id_payer=None,
                 member_id=None, weight=None, height=None, patient_name=None, contact_number=None,
                 national_id_number=None, date_ordered=None, encounter=None, diagnosis=None, activity=None,
                 resubmission=None):  # noqa: E501
        """TpoDataDTOsAuthorizationRequestAuthorizationDTO - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._request_type = None
        self._request_reference_number = None
        self._id_payer = None
        self._member_id = None
        self._weight = None
        self._height = None
        self._patient_name = None
        self._contact_number = None
        self._national_id_number = None
        self._date_ordered = None
        self._encounter = None
        self._diagnosis = None
        self._activity = None
        self._resubmission = None
        self.discriminator = None
        self.type = type
        self.id = id
        if request_type is not None:
            self.request_type = request_type
        if request_reference_number is not None:
            self.request_reference_number = request_reference_number
        if id_payer is not None:
            self.id_payer = id_payer
        self.member_id = member_id
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height
        if patient_name is not None:
            self.patient_name = patient_name
        if contact_number is not None:
            self.contact_number = contact_number
        self.national_id_number = national_id_number
        self.date_ordered = date_ordered
        if encounter is not None:
            self.encounter = encounter
        if diagnosis is not None:
            self.diagnosis = diagnosis
        if activity is not None:
            self.activity = activity
        if resubmission is not None:
            self.resubmission = resubmission

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Specifies Type using Values: Eligibility, Authorization, Cancellation.  # noqa: E501

        :return: The type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Specifies Type using Values: Eligibility, Authorization, Cancellation.  # noqa: E501

        :param type: The type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Authorization ID.  # noqa: E501

        :return: The id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Authorization ID.  # noqa: E501

        :param id: The id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def request_type(self):
        """Gets the request_type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

         What transaction user want to authorize.   New = Stand-alone Request   Prescription = Request Authorization for Prescription dispense  <div><p><strong style=\"border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\"> Conditional required</strong> required when authorization type equals “Authorization”  </p></div>  # noqa: E501

        :return: The request_type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

         What transaction user want to authorize.   New = Stand-alone Request   Prescription = Request Authorization for Prescription dispense  <div><p><strong style=\"border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\"> Conditional required</strong> required when authorization type equals “Authorization”  </p></div>  # noqa: E501

        :param request_type: The request_type of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """

        self._request_type = request_type

    @property
    def request_reference_number(self):
        """Gets the request_reference_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

         The Request Reference Number user wants to authorize.  <div><p><strong style=\"border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\"> Conditional required</strong> required when request type equals “Prescription”  </p></div>  # noqa: E501

        :return: The request_reference_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._request_reference_number

    @request_reference_number.setter
    def request_reference_number(self, request_reference_number):
        """Sets the request_reference_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

         The Request Reference Number user wants to authorize.  <div><p><strong style=\"border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\"> Conditional required</strong> required when request type equals “Prescription”  </p></div>  # noqa: E501

        :param request_reference_number: The request_reference_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """

        self._request_reference_number = request_reference_number

    @property
    def id_payer(self):
        """Gets the id_payer of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        The unique number assigned by an insurer to identify the Claim.  # noqa: E501

        :return: The id_payer of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._id_payer

    @id_payer.setter
    def id_payer(self, id_payer):
        """Sets the id_payer of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        The unique number assigned by an insurer to identify the Claim.  # noqa: E501

        :param id_payer: The id_payer of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """

        self._id_payer = id_payer

    @property
    def member_id(self):
        """Gets the member_id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        The patient's insurance member number, if the patient is claiming insurance.  # noqa: E501

        :return: The member_id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        The patient's insurance member number, if the patient is claiming insurance.  # noqa: E501

        :param member_id: The member_id of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """
        if member_id is None:
            raise ValueError("Invalid value for `member_id`, must not be `None`")  # noqa: E501

        self._member_id = member_id

    @property
    def weight(self):
        """Gets the weight of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        The patient's weight.  # noqa: E501

        :return: The weight of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        The patient's weight.  # noqa: E501

        :param weight: The weight of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def height(self):
        """Gets the height of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        The patient's height in cm  # noqa: E501

        :return: The height of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        The patient's height in cm  # noqa: E501

        :param height: The height of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def patient_name(self):
        """Gets the patient_name of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Patient name  # noqa: E501

        :return: The patient_name of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._patient_name

    @patient_name.setter
    def patient_name(self, patient_name):
        """Sets the patient_name of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Patient name  # noqa: E501

        :param patient_name: The patient_name of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """

        self._patient_name = patient_name

    @property
    def contact_number(self):
        """Gets the contact_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Patient contact number  # noqa: E501

        :return: The contact_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """Sets the contact_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Patient contact number  # noqa: E501

        :param contact_number: The contact_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """

        self._contact_number = contact_number

    @property
    def national_id_number(self):
        """Gets the national_id_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Gets or sets the national identifier number.  # noqa: E501

        :return: The national_id_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._national_id_number

    @national_id_number.setter
    def national_id_number(self, national_id_number):
        """Sets the national_id_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Gets or sets the national identifier number.  # noqa: E501

        :param national_id_number: The national_id_number of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """
        if national_id_number is None:
            raise ValueError("Invalid value for `national_id_number`, must not be `None`")  # noqa: E501

        self._national_id_number = national_id_number

    @property
    def date_ordered(self):
        """Gets the date_ordered of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        The date on which the prescription/order is ordered/prescribed.             Date format: DD/MM/YYYYY  # noqa: E501

        :return: The date_ordered of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: str
        """
        return self._date_ordered

    @date_ordered.setter
    def date_ordered(self, date_ordered):
        """Sets the date_ordered of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        The date on which the prescription/order is ordered/prescribed.             Date format: DD/MM/YYYYY  # noqa: E501

        :param date_ordered: The date_ordered of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: str
        """
        if date_ordered is None:
            raise ValueError("Invalid value for `date_ordered`, must not be `None`")  # noqa: E501

        self._date_ordered = date_ordered

    @property
    def encounter(self):
        """Gets the encounter of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501


        :return: The encounter of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: TpoDataDTOsAuthorizationRequestEncounterDTO
        """
        return self._encounter

    @encounter.setter
    def encounter(self, encounter):
        """Sets the encounter of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.


        :param encounter: The encounter of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: TpoDataDTOsAuthorizationRequestEncounterDTO
        """

        self._encounter = encounter

    @property
    def diagnosis(self):
        """Gets the diagnosis of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Authorization Diagnosis.  # noqa: E501

        :return: The diagnosis of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsSharedDiagnosisDTO]
        """
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        """Sets the diagnosis of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Authorization Diagnosis.  # noqa: E501

        :param diagnosis: The diagnosis of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: list[TpoDataDTOsSharedDiagnosisDTO]
        """

        self._diagnosis = diagnosis

    @property
    def activity(self):
        """Gets the activity of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501

        Authorization Activity.  # noqa: E501

        :return: The activity of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsAuthorizationRequestActivityDTO]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.

        Authorization Activity.  # noqa: E501

        :param activity: The activity of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: list[TpoDataDTOsAuthorizationRequestActivityDTO]
        """

        self._activity = activity

    @property
    def resubmission(self):
        """Gets the resubmission of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501


        :return: The resubmission of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :rtype: TpoDataDTOsAuthorizationRequestResubmissionDTO
        """
        return self._resubmission

    @resubmission.setter
    def resubmission(self, resubmission):
        """Sets the resubmission of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.


        :param resubmission: The resubmission of this TpoDataDTOsAuthorizationRequestAuthorizationDTO.  # noqa: E501
        :type: TpoDataDTOsAuthorizationRequestResubmissionDTO
        """

        self._resubmission = resubmission

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
        if issubclass(TpoDataDTOsAuthorizationRequestAuthorizationDTO, dict):
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
        if not isinstance(other, TpoDataDTOsAuthorizationRequestAuthorizationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
