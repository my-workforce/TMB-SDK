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


class TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO(object):
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
        'code': 'str',
        'quantity': 'float',
        'duration': 'float',
        'unit_id': 'int',
        'refills': 'int',
        'rout_of_admin': 'str',
        'instructions': 'str',
        'arabic_instructions': 'str',
        'start': 'str',
        'frequency': 'TpoDataDTOsERXFrequencyDTO',
        'observation': 'list[TpoDataDTOsSharedObservationDTO]',
        'status': 'str',
        'remaining_refills': 'int',
        'dispense_track': 'list[TpoDataDTOsERXPatientPrescriptionsActivityDispenseTrackDTO]'
    }

    attribute_map = {
        'id': 'ID',
        'type': 'Type',
        'code': 'Code',
        'quantity': 'Quantity',
        'duration': 'Duration',
        'unit_id': 'UnitId',
        'refills': 'Refills',
        'rout_of_admin': 'RoutOfAdmin',
        'instructions': 'Instructions',
        'arabic_instructions': 'ArabicInstructions',
        'start': 'Start',
        'frequency': 'Frequency',
        'observation': 'Observation',
        'status': 'Status',
        'remaining_refills': 'RemainingRefills',
        'dispense_track': 'DispenseTrack'
    }

    def __init__(self, id=None, type=None, code=None, quantity=None, duration=None, unit_id=None, refills=None,
                 rout_of_admin=None, instructions=None, arabic_instructions=None, start=None, frequency=None,
                 observation=None, status=None, remaining_refills=None, dispense_track=None):  # noqa: E501
        """TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._code = None
        self._quantity = None
        self._duration = None
        self._unit_id = None
        self._refills = None
        self._rout_of_admin = None
        self._instructions = None
        self._arabic_instructions = None
        self._start = None
        self._frequency = None
        self._observation = None
        self._status = None
        self._remaining_refills = None
        self._dispense_track = None
        self.discriminator = None
        self.id = id
        self.type = type
        self.code = code
        self.quantity = quantity
        self.duration = duration
        self.unit_id = unit_id
        if refills is not None:
            self.refills = refills
        self.rout_of_admin = rout_of_admin
        self.instructions = instructions
        if arabic_instructions is not None:
            self.arabic_instructions = arabic_instructions
        self.start = start
        if frequency is not None:
            self.frequency = frequency
        if observation is not None:
            self.observation = observation
        if status is not None:
            self.status = status
        if remaining_refills is not None:
            self.remaining_refills = remaining_refills
        if dispense_track is not None:
            self.dispense_track = dispense_track

    @property
    def id(self):
        """Gets the id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Unique identifier of activity within a Prescription.  # noqa: E501

        :return: The id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Unique identifier of activity within a Prescription.  # noqa: E501

        :param id: The id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        ActivityType classifies the type of activity. (Should have the value 5 for Drug or the value 10 for scientific code)  # noqa: E501

        :return: The type of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        ActivityType classifies the type of activity. (Should have the value 5 for Drug or the value 10 for scientific code)  # noqa: E501

        :param type: The type of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def code(self):
        """Gets the code of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        ActivityCode is the code, specified by ActivityType, for the Activity performed.  # noqa: E501

        :return: The code of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        ActivityCode is the code, specified by ActivityType, for the Activity performed.  # noqa: E501

        :param code: The code of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def quantity(self):
        """Gets the quantity of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the number of units (quantity) for a specific Activity.  # noqa: E501

        :return: The quantity of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the number of units (quantity) for a specific Activity.  # noqa: E501

        :param quantity: The quantity of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def duration(self):
        """Gets the duration of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the duration in days for the prescribed activity.  # noqa: E501

        :return: The duration of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the duration in days for the prescribed activity.  # noqa: E501

        :param duration: The duration of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: float
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def unit_id(self):
        """Gets the unit_id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the type of units  for a specific Activity.  # noqa: E501

        :return: The unit_id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the type of units  for a specific Activity.  # noqa: E501

        :param unit_id: The unit_id of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: int
        """
        if unit_id is None:
            raise ValueError("Invalid value for `unit_id`, must not be `None`")  # noqa: E501

        self._unit_id = unit_id

    @property
    def refills(self):
        """Gets the refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the number of refills for a given activity.  # noqa: E501

        :return: The refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: int
        """
        return self._refills

    @refills.setter
    def refills(self, refills):
        """Sets the refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the number of refills for a given activity.  # noqa: E501

        :param refills: The refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: int
        """

        self._refills = refills

    @property
    def rout_of_admin(self):
        """Gets the rout_of_admin of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the rout of admin for a given activity.  # noqa: E501

        :return: The rout_of_admin of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._rout_of_admin

    @rout_of_admin.setter
    def rout_of_admin(self, rout_of_admin):
        """Sets the rout_of_admin of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the rout of admin for a given activity.  # noqa: E501

        :param rout_of_admin: The rout_of_admin of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """
        if rout_of_admin is None:
            raise ValueError("Invalid value for `rout_of_admin`, must not be `None`")  # noqa: E501

        self._rout_of_admin = rout_of_admin

    @property
    def instructions(self):
        """Gets the instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the instructions for a given activity as provided by the prescribing clinician.  # noqa: E501

        :return: The instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the instructions for a given activity as provided by the prescribing clinician.  # noqa: E501

        :param instructions: The instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """
        if instructions is None:
            raise ValueError("Invalid value for `instructions`, must not be `None`")  # noqa: E501

        self._instructions = instructions

    @property
    def arabic_instructions(self):
        """Gets the arabic_instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Identifies the Arabic instructions for a given activity as provided by the prescribing clinician.              <div><p><strong style=\"border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\"> Conditional required</strong> required when normal instructions are being sent              </p></div>  # noqa: E501

        :return: The arabic_instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._arabic_instructions

    @arabic_instructions.setter
    def arabic_instructions(self, arabic_instructions):
        """Sets the arabic_instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Identifies the Arabic instructions for a given activity as provided by the prescribing clinician.              <div><p><strong style=\"border: 5% solid #584c7e;padding:1px;border-radius: 5%;background: #584c7e;color:white;\"> Conditional required</strong> required when normal instructions are being sent              </p></div>  # noqa: E501

        :param arabic_instructions: The arabic_instructions of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """

        self._arabic_instructions = arabic_instructions

    @property
    def start(self):
        """Gets the start of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        The date and time at which Activity started  Date Time format: DD/MM/YYYYY HH:MM  # noqa: E501

        :return: The start of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        The date and time at which Activity started  Date Time format: DD/MM/YYYYY HH:MM  # noqa: E501

        :param start: The start of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def frequency(self):
        """Gets the frequency of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501


        :return: The frequency of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: TpoDataDTOsERXFrequencyDTO
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.


        :param frequency: The frequency of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: TpoDataDTOsERXFrequencyDTO
        """

        self._frequency = frequency

    @property
    def observation(self):
        """Gets the observation of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501

        Activity Observations.  # noqa: E501

        :return: The observation of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsSharedObservationDTO]
        """
        return self._observation

    @observation.setter
    def observation(self, observation):
        """Sets the observation of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.

        Activity Observations.  # noqa: E501

        :param observation: The observation of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: list[TpoDataDTOsSharedObservationDTO]
        """

        self._observation = observation

    @property
    def status(self):
        """Gets the status of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501


        :return: The status of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.


        :param status: The status of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def remaining_refills(self):
        """Gets the remaining_refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501


        :return: The remaining_refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: int
        """
        return self._remaining_refills

    @remaining_refills.setter
    def remaining_refills(self, remaining_refills):
        """Sets the remaining_refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.


        :param remaining_refills: The remaining_refills of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: int
        """

        self._remaining_refills = remaining_refills

    @property
    def dispense_track(self):
        """Gets the dispense_track of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501


        :return: The dispense_track of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsERXPatientPrescriptionsActivityDispenseTrackDTO]
        """
        return self._dispense_track

    @dispense_track.setter
    def dispense_track(self, dispense_track):
        """Sets the dispense_track of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.


        :param dispense_track: The dispense_track of this TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO.  # noqa: E501
        :type: list[TpoDataDTOsERXPatientPrescriptionsActivityDispenseTrackDTO]
        """

        self._dispense_track = dispense_track

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
        if issubclass(TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO, dict):
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
        if not isinstance(other, TpoDataDTOsERXPatientPrescriptionsPrescriptionActivityDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
