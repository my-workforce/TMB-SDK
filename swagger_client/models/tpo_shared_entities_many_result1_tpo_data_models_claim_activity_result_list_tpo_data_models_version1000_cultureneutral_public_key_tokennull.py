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


class TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull(
    object):
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
        'entities': 'list[TpoDataModelsClaimActivityResultList]',
        'status_code': 'int',
        'message': 'str',
        'success': 'bool',
        'user_message': 'str',
        'entity_id': 'str',
        'reference_number': 'str',
        'error': 'list[TpoSharedEntitiesError]'
    }

    attribute_map = {
        'entities': 'Entities',
        'status_code': 'StatusCode',
        'message': 'Message',
        'success': 'Success',
        'user_message': 'UserMessage',
        'entity_id': 'EntityID',
        'reference_number': 'ReferenceNumber',
        'error': 'Error'
    }

    def __init__(self, entities=None, status_code=None, message=None, success=None, user_message=None, entity_id=None,
                 reference_number=None, error=None):  # noqa: E501
        """TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull - a model defined in Swagger"""  # noqa: E501
        self._entities = None
        self._status_code = None
        self._message = None
        self._success = None
        self._user_message = None
        self._entity_id = None
        self._reference_number = None
        self._error = None
        self.discriminator = None
        if entities is not None:
            self.entities = entities
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message
        if success is not None:
            self.success = success
        if user_message is not None:
            self.user_message = user_message
        if entity_id is not None:
            self.entity_id = entity_id
        if reference_number is not None:
            self.reference_number = reference_number
        if error is not None:
            self.error = error

    @property
    def entities(self):
        """Gets the entities of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        List of Result Entities.  # noqa: E501

        :return: The entities of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: list[TpoDataModelsClaimActivityResultList]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        List of Result Entities.  # noqa: E501

        :param entities: The entities of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: list[TpoDataModelsClaimActivityResultList]
        """

        self._entities = entities

    @property
    def status_code(self):
        """Gets the status_code of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        Result status code.  # noqa: E501

        :return: The status_code of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        Result status code.  # noqa: E501

        :param status_code: The status_code of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: int
        """
        allowed_values = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304,
                          305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414,
                          415, 416, 417, 421, 422, 423, 424, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506,
                          507, 508, 510, 511]  # noqa: E501
        if status_code not in allowed_values:
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                    .format(status_code, allowed_values)
            )

        self._status_code = status_code

    @property
    def message(self):
        """Gets the message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        Message.  # noqa: E501

        :return: The message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        Message.  # noqa: E501

        :param message: The message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def success(self):
        """Gets the success of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        Success indicator.  # noqa: E501

        :return: The success of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        Success indicator.  # noqa: E501

        :param success: The success of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def user_message(self):
        """Gets the user_message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        User Message.  # noqa: E501

        :return: The user_message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """Sets the user_message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        User Message.  # noqa: E501

        :param user_message: The user_message of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: str
        """

        self._user_message = user_message

    @property
    def entity_id(self):
        """Gets the entity_id of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        Entity ID.  # noqa: E501

        :return: The entity_id of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        Entity ID.  # noqa: E501

        :param entity_id: The entity_id of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def reference_number(self):
        """Gets the reference_number of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        Reference ID.              This will returend when posting ErxRequest, LabRequest, RadRequest  # noqa: E501

        :return: The reference_number of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        Reference ID.              This will returend when posting ErxRequest, LabRequest, RadRequest  # noqa: E501

        :param reference_number: The reference_number of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: str
        """

        self._reference_number = reference_number

    @property
    def error(self):
        """Gets the error of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501

        Error List.  # noqa: E501

        :return: The error of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :rtype: list[TpoSharedEntitiesError]
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.

        Error List.  # noqa: E501

        :param error: The error of this TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.  # noqa: E501
        :type: list[TpoSharedEntitiesError]
        """

        self._error = error

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
        if issubclass(
                TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull,
                dict):
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
        if not isinstance(other,
                          TpoSharedEntitiesManyResult1TpoDataModelsClaimActivityResultListTpoDataModelsVersion1000CultureneutralPublicKeyTokennull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
