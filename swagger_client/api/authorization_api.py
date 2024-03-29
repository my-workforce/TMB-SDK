# coding: utf-8

"""
    Transaction Management Bus (TMB) API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V3.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AuthorizationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_authorization_get_new_get(self, **kwargs):  # noqa: E501
        """Get New Transactions  # noqa: E501

        This functions takes no parameters. Returns new transactions (not downloaded) up to 500 transaction.                Transactions returned according to user type. If user is Provider, the function will return the new PriorAuthorization transactions. If user is Payer, the function will return new PriorRequest transactions.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                             HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"Authorization/GetNew\");                // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_get_new_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_authorization_get_new_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_authorization_get_new_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_authorization_get_new_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get New Transactions  # noqa: E501

        This functions takes no parameters. Returns new transactions (not downloaded) up to 500 transaction.                Transactions returned according to user type. If user is Provider, the function will return the new PriorAuthorization transactions. If user is Payer, the function will return new PriorRequest transactions.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                             HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"Authorization/GetNew\");                // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_get_new_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'password', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_authorization_get_new_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'language' in params:
            header_params['language'] = params['language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Authorization/GetNew', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull',
            # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_authorization_post_request_post(self, **kwargs):  # noqa: E501
        """Upload Prior Request transaction  # noqa: E501

        Upload Prior Request transaction.            <br /><b class=\"ExampleColor\">C# Integration Example: </b>                          HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Accept.Clear();             client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(\"application/json\"));             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             PriorRequestParameter pr = new PriorRequestParameter() { ...... };             HttpResponseMessage response = await client.PostAsJsonAsync(\"Authorization/PostRequest\", pr);             // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_post_request_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TpoDataDTOsControllerParametersPriorRequestParameter body: The prior request Object.
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_authorization_post_request_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_authorization_post_request_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_authorization_post_request_post_with_http_info(self, **kwargs):  # noqa: E501
        """Upload Prior Request transaction  # noqa: E501

        Upload Prior Request transaction.            <br /><b class=\"ExampleColor\">C# Integration Example: </b>                          HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Accept.Clear();             client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(\"application/json\"));             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             PriorRequestParameter pr = new PriorRequestParameter() { ...... };             HttpResponseMessage response = await client.PostAsJsonAsync(\"Authorization/PostRequest\", pr);             // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_post_request_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TpoDataDTOsControllerParametersPriorRequestParameter body: The prior request Object.
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'username', 'password', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_authorization_post_request_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'language' in params:
            header_params['language'] = params['language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Authorization/PostRequest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpoSharedEntitiesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_authorization_search_get(self, **kwargs):  # noqa: E501
        """Search Authorization Transactions  # noqa: E501

        Search Post office authorizations. you can search new data or your data according to the filters provided. (up to 500 transactions)               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                              HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"Authorization/Search\");                // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_search_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license: Filter transactions according to sender license.  <b>If direction = 0 (received), license will be the SenderID license.  If direction = 1 (sent) , license will be the ReceiverID license.</b>
        :param int direction: Filter transactions user received or sent.  0 : Filter received transactions (<b>Default value</b>).  1 : Filter sent transactions.
        :param str from_date: Filter transactions greater than or equal to specific date.  <b>Date format : dd/MM/yyyy HH:mm</b>
        :param str to_date: Filter transactions less than or equal to specific date.  <b>Date format : dd/MM/yyyy HH:mm</b>
        :param int downloaded: Filter transactions according to downloaded indicator.  0 : Filter not downloaded transactions (<b>Default value</b>).  1 : Filter downloaded transactions.  2 : Filter all transactions.
        :param str id: Filter transactions according to Sub-Entity ID.
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_authorization_search_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_authorization_search_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_authorization_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """Search Authorization Transactions  # noqa: E501

        Search Post office authorizations. you can search new data or your data according to the filters provided. (up to 500 transactions)               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                              HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"Authorization/Search\");                // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str license: Filter transactions according to sender license.  <b>If direction = 0 (received), license will be the SenderID license.  If direction = 1 (sent) , license will be the ReceiverID license.</b>
        :param int direction: Filter transactions user received or sent.  0 : Filter received transactions (<b>Default value</b>).  1 : Filter sent transactions.
        :param str from_date: Filter transactions greater than or equal to specific date.  <b>Date format : dd/MM/yyyy HH:mm</b>
        :param str to_date: Filter transactions less than or equal to specific date.  <b>Date format : dd/MM/yyyy HH:mm</b>
        :param int downloaded: Filter transactions according to downloaded indicator.  0 : Filter not downloaded transactions (<b>Default value</b>).  1 : Filter downloaded transactions.  2 : Filter all transactions.
        :param str id: Filter transactions according to Sub-Entity ID.
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license', 'direction', 'from_date', 'to_date', 'downloaded', 'id', 'username', 'password',
                      'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_authorization_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'license' in params:
            query_params.append(('license', params['license']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'downloaded' in params:
            query_params.append(('downloaded', params['downloaded']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'language' in params:
            header_params['language'] = params['language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Authorization/Search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull',
            # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_authorization_set_downloaded_post(self, **kwargs):  # noqa: E501
        """Set transaction as downloaded  # noqa: E501

        Set transaction as downloaded. you can only do this action to new transactions assgined to you.              <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Accept.Clear();              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              var parameters = new Dictionary { { \"Id\", \"5b6ae93c28c75751aca5f3db\" } }; // Dictionary type string,string              var urlParams = new FormUrlEncodedContent(parameters);              HttpResponseMessage response = await client.PostAsync(\"Authorization/SetDownloaded\", urlParams);              // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_set_downloaded_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: transaction id
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_authorization_set_downloaded_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_authorization_set_downloaded_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_authorization_set_downloaded_post_with_http_info(self, **kwargs):  # noqa: E501
        """Set transaction as downloaded  # noqa: E501

        Set transaction as downloaded. you can only do this action to new transactions assgined to you.              <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Accept.Clear();              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              var parameters = new Dictionary { { \"Id\", \"5b6ae93c28c75751aca5f3db\" } }; // Dictionary type string,string              var urlParams = new FormUrlEncodedContent(parameters);              HttpResponseMessage response = await client.PostAsync(\"Authorization/SetDownloaded\", urlParams);              // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_set_downloaded_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: transaction id
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: TpoSharedEntitiesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'username', 'password', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_authorization_set_downloaded_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501

        header_params = {}
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'language' in params:
            header_params['language'] = params['language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Authorization/SetDownloaded', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpoSharedEntitiesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_authorization_view_get(self, **kwargs):  # noqa: E501
        """View the Authorization transaction  # noqa: E501

        View individual  claim from the post office. you can only view claims assigned to you or generated from you according to direction parameter.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"Authorization/View?id=5b6ae93c28c75751aca5f3db\");               // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_view_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: transaction id
        :param int direction: 0 for received, 1 for sent. default is 0
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_authorization_view_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_authorization_view_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_authorization_view_get_with_http_info(self, **kwargs):  # noqa: E501
        """View the Authorization transaction  # noqa: E501

        View individual  claim from the post office. you can only view claims assigned to you or generated from you according to direction parameter.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"Authorization/View?id=5b6ae93c28c75751aca5f3db\");               // Cast the response content to your object using the method response.Content.ReadAsAsync  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_authorization_view_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: transaction id
        :param int direction: 0 for received, 1 for sent. default is 0
        :param str username: username case sensitive
        :param str password: password case sensitive
        :param str language: 'en' for English(default), 'ar' for Arabic
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'direction', 'username', 'password', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_authorization_view_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501

        header_params = {}
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'language' in params:
            header_params['language'] = params['language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Authorization/View', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
