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


class TpoDataDTOsPatientPatientVitalSignsDTO(object):
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
        'vital_signs_type': 'str',
        'vital_signs_value_type': 'str',
        'vital_signs_value': 'str'
    }

    attribute_map = {
        'vital_signs_type': 'VitalSignsType',
        'vital_signs_value_type': 'VitalSignsValueType',
        'vital_signs_value': 'VitalSignsValue'
    }

    def __init__(self, vital_signs_type=None, vital_signs_value_type=None, vital_signs_value=None):  # noqa: E501
        """TpoDataDTOsPatientPatientVitalSignsDTO - a model defined in Swagger"""  # noqa: E501
        self._vital_signs_type = None
        self._vital_signs_value_type = None
        self._vital_signs_value = None
        self.discriminator = None
        self.vital_signs_type = vital_signs_type
        self.vital_signs_value_type = vital_signs_value_type
        self.vital_signs_value = vital_signs_value

    @property
    def vital_signs_type(self):
        """Gets the vital_signs_type of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501

        Patient vital sign type   Values:  BP  Temp  Pulse  RR  Oxygen Saturation)  # noqa: E501

        :return: The vital_signs_type of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501
        :rtype: str
        """
        return self._vital_signs_type

    @vital_signs_type.setter
    def vital_signs_type(self, vital_signs_type):
        """Sets the vital_signs_type of this TpoDataDTOsPatientPatientVitalSignsDTO.

        Patient vital sign type   Values:  BP  Temp  Pulse  RR  Oxygen Saturation)  # noqa: E501

        :param vital_signs_type: The vital_signs_type of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501
        :type: str
        """
        if vital_signs_type is None:
            raise ValueError("Invalid value for `vital_signs_type`, must not be `None`")  # noqa: E501

        self._vital_signs_type = vital_signs_type

    @property
    def vital_signs_value_type(self):
        """Gets the vital_signs_value_type of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501

        Patient vital sign value type   Values:  mmHg  C  F  BPM  %  # noqa: E501

        :return: The vital_signs_value_type of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501
        :rtype: str
        """
        return self._vital_signs_value_type

    @vital_signs_value_type.setter
    def vital_signs_value_type(self, vital_signs_value_type):
        """Sets the vital_signs_value_type of this TpoDataDTOsPatientPatientVitalSignsDTO.

        Patient vital sign value type   Values:  mmHg  C  F  BPM  %  # noqa: E501

        :param vital_signs_value_type: The vital_signs_value_type of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501
        :type: str
        """
        if vital_signs_value_type is None:
            raise ValueError("Invalid value for `vital_signs_value_type`, must not be `None`")  # noqa: E501

        self._vital_signs_value_type = vital_signs_value_type

    @property
    def vital_signs_value(self):
        """Gets the vital_signs_value of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501

        Patient vital sign value  # noqa: E501

        :return: The vital_signs_value of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501
        :rtype: str
        """
        return self._vital_signs_value

    @vital_signs_value.setter
    def vital_signs_value(self, vital_signs_value):
        """Sets the vital_signs_value of this TpoDataDTOsPatientPatientVitalSignsDTO.

        Patient vital sign value  # noqa: E501

        :param vital_signs_value: The vital_signs_value of this TpoDataDTOsPatientPatientVitalSignsDTO.  # noqa: E501
        :type: str
        """
        if vital_signs_value is None:
            raise ValueError("Invalid value for `vital_signs_value`, must not be `None`")  # noqa: E501

        self._vital_signs_value = vital_signs_value

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
        if issubclass(TpoDataDTOsPatientPatientVitalSignsDTO, dict):
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
        if not isinstance(other, TpoDataDTOsPatientPatientVitalSignsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
