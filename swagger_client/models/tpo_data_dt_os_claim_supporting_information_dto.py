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


class TpoDataDTOsClaimSupportingInformationDTO(object):
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
        'procedure_code': 'str',
        'reference_number': 'str',
        'attachment_id': 'str'
    }

    attribute_map = {
        'procedure_code': 'ProcedureCode',
        'reference_number': 'ReferenceNumber',
        'attachment_id': 'AttachmentId'
    }

    def __init__(self, procedure_code=None, reference_number=None, attachment_id=None):  # noqa: E501
        """TpoDataDTOsClaimSupportingInformationDTO - a model defined in Swagger"""  # noqa: E501
        self._procedure_code = None
        self._reference_number = None
        self._attachment_id = None
        self.discriminator = None
        self.procedure_code = procedure_code
        self.reference_number = reference_number
        if attachment_id is not None:
            self.attachment_id = attachment_id

    @property
    def procedure_code(self):
        """Gets the procedure_code of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501

        Gets or sets the ProcedureCode.  # noqa: E501

        :return: The procedure_code of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501
        :rtype: str
        """
        return self._procedure_code

    @procedure_code.setter
    def procedure_code(self, procedure_code):
        """Sets the procedure_code of this TpoDataDTOsClaimSupportingInformationDTO.

        Gets or sets the ProcedureCode.  # noqa: E501

        :param procedure_code: The procedure_code of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501
        :type: str
        """
        if procedure_code is None:
            raise ValueError("Invalid value for `procedure_code`, must not be `None`")  # noqa: E501

        self._procedure_code = procedure_code

    @property
    def reference_number(self):
        """Gets the reference_number of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501

        Gets or sets the ReferenceNumber.  # noqa: E501

        :return: The reference_number of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this TpoDataDTOsClaimSupportingInformationDTO.

        Gets or sets the ReferenceNumber.  # noqa: E501

        :param reference_number: The reference_number of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501
        :type: str
        """
        if reference_number is None:
            raise ValueError("Invalid value for `reference_number`, must not be `None`")  # noqa: E501

        self._reference_number = reference_number

    @property
    def attachment_id(self):
        """Gets the attachment_id of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501

        Gets or sets the AttachmentId.  # noqa: E501

        :return: The attachment_id of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this TpoDataDTOsClaimSupportingInformationDTO.

        Gets or sets the AttachmentId.  # noqa: E501

        :param attachment_id: The attachment_id of this TpoDataDTOsClaimSupportingInformationDTO.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

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
        if issubclass(TpoDataDTOsClaimSupportingInformationDTO, dict):
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
        if not isinstance(other, TpoDataDTOsClaimSupportingInformationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other