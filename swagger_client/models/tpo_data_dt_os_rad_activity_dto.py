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


class TpoDataDTOsRadActivityDTO(object):
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
        'instructions': 'str',
        'observation': 'list[TpoDataDTOsSharedObservationDTO]',
        'start': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'type': 'Type',
        'code': 'Code',
        'quantity': 'Quantity',
        'instructions': 'Instructions',
        'observation': 'Observation',
        'start': 'Start'
    }

    def __init__(self, id=None, type=None, code=None, quantity=None, instructions=None, observation=None,
                 start=None):  # noqa: E501
        """TpoDataDTOsRadActivityDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._code = None
        self._quantity = None
        self._instructions = None
        self._observation = None
        self._start = None
        self.discriminator = None
        self.id = id
        self.type = type
        self.code = code
        self.quantity = quantity
        if instructions is not None:
            self.instructions = instructions
        if observation is not None:
            self.observation = observation
        self.start = start

    @property
    def id(self):
        """Gets the id of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        Unique identifier of activity within an Order  # noqa: E501

        :return: The id of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TpoDataDTOsRadActivityDTO.

        Unique identifier of activity within an Order  # noqa: E501

        :param id: The id of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        ActivityType classifies the type of activity. (must have the value 3, CPT)  # noqa: E501

        :return: The type of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsRadActivityDTO.

        ActivityType classifies the type of activity. (must have the value 3, CPT)  # noqa: E501

        :param type: The type of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def code(self):
        """Gets the code of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        ActivityCode is the code, specified by ActivityType, for the Activity performed.  # noqa: E501

        :return: The code of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TpoDataDTOsRadActivityDTO.

        ActivityCode is the code, specified by ActivityType, for the Activity performed.  # noqa: E501

        :param code: The code of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def quantity(self):
        """Gets the quantity of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        Identifies the number of units (quantity) for a specific Activity.  # noqa: E501

        :return: The quantity of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this TpoDataDTOsRadActivityDTO.

        Identifies the number of units (quantity) for a specific Activity.  # noqa: E501

        :param quantity: The quantity of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def instructions(self):
        """Gets the instructions of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        Identifies the instructions for a given activity as provided by the prescribing clinician  # noqa: E501

        :return: The instructions of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this TpoDataDTOsRadActivityDTO.

        Identifies the instructions for a given activity as provided by the prescribing clinician  # noqa: E501

        :param instructions: The instructions of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: str
        """

        self._instructions = instructions

    @property
    def observation(self):
        """Gets the observation of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        Actvity Observations  # noqa: E501

        :return: The observation of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: list[TpoDataDTOsSharedObservationDTO]
        """
        return self._observation

    @observation.setter
    def observation(self, observation):
        """Sets the observation of this TpoDataDTOsRadActivityDTO.

        Actvity Observations  # noqa: E501

        :param observation: The observation of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: list[TpoDataDTOsSharedObservationDTO]
        """

        self._observation = observation

    @property
    def start(self):
        """Gets the start of this TpoDataDTOsRadActivityDTO.  # noqa: E501

        The date and time at which Activity started  Date Time format: DD/MM/YYYYY HH:MM  # noqa: E501

        :return: The start of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TpoDataDTOsRadActivityDTO.

        The date and time at which Activity started  Date Time format: DD/MM/YYYYY HH:MM  # noqa: E501

        :param start: The start of this TpoDataDTOsRadActivityDTO.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

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
        if issubclass(TpoDataDTOsRadActivityDTO, dict):
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
        if not isinstance(other, TpoDataDTOsRadActivityDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
