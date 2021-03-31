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


class TpoDataDTOsAuthorizationRequestResubmissionDTO(object):
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
        'comment': 'str',
        'attachment': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'comment': 'Comment',
        'attachment': 'Attachment'
    }

    def __init__(self, type=None, comment=None, attachment=None):  # noqa: E501
        """TpoDataDTOsAuthorizationRequestResubmissionDTO - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._comment = None
        self._attachment = None
        self.discriminator = None
        self.type = type
        self.comment = comment
        if attachment is not None:
            self.attachment = attachment

    @property
    def type(self):
        """Gets the type of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501

        Correction or internal complaint.  # noqa: E501

        :return: The type of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TpoDataDTOsAuthorizationRequestResubmissionDTO.

        Correction or internal complaint.  # noqa: E501

        :param type: The type of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501

        Comments entered by the provider during the resubmission transaction.  # noqa: E501

        :return: The comment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.

        Comments entered by the provider during the resubmission transaction.  # noqa: E501

        :param comment: The comment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def attachment(self):
        """Gets the attachment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501

        Attachment provided during the resubmission transaction if necessary.  # noqa: E501

        :return: The attachment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501
        :rtype: str
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.

        Attachment provided during the resubmission transaction if necessary.  # noqa: E501

        :param attachment: The attachment of this TpoDataDTOsAuthorizationRequestResubmissionDTO.  # noqa: E501
        :type: str
        """

        self._attachment = attachment

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
        if issubclass(TpoDataDTOsAuthorizationRequestResubmissionDTO, dict):
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
        if not isinstance(other, TpoDataDTOsAuthorizationRequestResubmissionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other