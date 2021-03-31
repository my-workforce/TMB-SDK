# swagger_client.AuthorizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authorization_get_new_get**](AuthorizationApi.md#api_authorization_get_new_get) | **GET** /api/Authorization/GetNew | Get New Transactions
[**api_authorization_post_request_post**](AuthorizationApi.md#api_authorization_post_request_post) | **POST** /api/Authorization/PostRequest | Upload Prior Request transaction
[**api_authorization_search_get**](AuthorizationApi.md#api_authorization_search_get) | **GET** /api/Authorization/Search | Search Authorization Transactions
[**api_authorization_set_downloaded_post**](AuthorizationApi.md#api_authorization_set_downloaded_post) | **POST** /api/Authorization/SetDownloaded | Set transaction as downloaded
[**api_authorization_view_get**](AuthorizationApi.md#api_authorization_view_get) | **GET** /api/Authorization/View | View the Authorization transaction

# **api_authorization_get_new_get**
> TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull api_authorization_get_new_get(username=username, password=password, language=language)

Get New Transactions

This functions takes no parameters. Returns new transactions (not downloaded) up to 500 transaction.                Transactions returned according to user type. If user is Provider, the function will return the new PriorAuthorization transactions. If user is Payer, the function will return new PriorRequest transactions.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                             HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"Authorization/GetNew\");                // Cast the response content to your object using the method response.Content.ReadAsAsync

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Get New Transactions
    api_response = api_instance.api_authorization_get_new_get(username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->api_authorization_get_new_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull**](TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_post_request_post**
> TpoSharedEntitiesResult api_authorization_post_request_post(body=body, username=username, password=password, language=language)

Upload Prior Request transaction

Upload Prior Request transaction.            <br /><b class=\"ExampleColor\">C# Integration Example: </b>                          HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Accept.Clear();             client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(\"application/json\"));             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             PriorRequestParameter pr = new PriorRequestParameter() { ...... };             HttpResponseMessage response = await client.PostAsJsonAsync(\"Authorization/PostRequest\", pr);             // Cast the response content to your object using the method response.Content.ReadAsAsync

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.TpoDataDTOsControllerParametersPriorRequestParameter() # TpoDataDTOsControllerParametersPriorRequestParameter | The prior request Object. (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Upload Prior Request transaction
    api_response = api_instance.api_authorization_post_request_post(body=body, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->api_authorization_post_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TpoDataDTOsControllerParametersPriorRequestParameter**](TpoDataDTOsControllerParametersPriorRequestParameter.md)| The prior request Object. | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesResult**](TpoSharedEntitiesResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_search_get**
> TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull api_authorization_search_get(license=license, direction=direction, from_date=from_date, to_date=to_date, downloaded=downloaded, id=id, username=username, password=password, language=language)

Search Authorization Transactions

Search Post office authorizations. you can search new data or your data according to the filters provided. (up to 500 transactions)               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                              HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"Authorization/Search\");                // Cast the response content to your object using the method response.Content.ReadAsAsync

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
license = 'license_example' # str | Filter transactions according to sender license.  <b>If direction = 0 (received), license will be the SenderID license.  If direction = 1 (sent) , license will be the ReceiverID license.</b> (optional)
direction = 56 # int | Filter transactions user received or sent.  0 : Filter received transactions (<b>Default value</b>).  1 : Filter sent transactions. (optional)
from_date = 'from_date_example' # str | Filter transactions greater than or equal to specific date.  <b>Date format : dd/MM/yyyy HH:mm</b> (optional)
to_date = 'to_date_example' # str | Filter transactions less than or equal to specific date.  <b>Date format : dd/MM/yyyy HH:mm</b> (optional)
downloaded = 56 # int | Filter transactions according to downloaded indicator.  0 : Filter not downloaded transactions (<b>Default value</b>).  1 : Filter downloaded transactions.  2 : Filter all transactions. (optional)
id = 'id_example' # str | Filter transactions according to Sub-Entity ID. (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Search Authorization Transactions
    api_response = api_instance.api_authorization_search_get(license=license, direction=direction, from_date=from_date, to_date=to_date, downloaded=downloaded, id=id, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->api_authorization_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**| Filter transactions according to sender license.  &lt;b&gt;If direction &#x3D; 0 (received), license will be the SenderID license.  If direction &#x3D; 1 (sent) , license will be the ReceiverID license.&lt;/b&gt; | [optional] 
 **direction** | **int**| Filter transactions user received or sent.  0 : Filter received transactions (&lt;b&gt;Default value&lt;/b&gt;).  1 : Filter sent transactions. | [optional] 
 **from_date** | **str**| Filter transactions greater than or equal to specific date.  &lt;b&gt;Date format : dd/MM/yyyy HH:mm&lt;/b&gt; | [optional] 
 **to_date** | **str**| Filter transactions less than or equal to specific date.  &lt;b&gt;Date format : dd/MM/yyyy HH:mm&lt;/b&gt; | [optional] 
 **downloaded** | **int**| Filter transactions according to downloaded indicator.  0 : Filter not downloaded transactions (&lt;b&gt;Default value&lt;/b&gt;).  1 : Filter downloaded transactions.  2 : Filter all transactions. | [optional] 
 **id** | **str**| Filter transactions according to Sub-Entity ID. | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull**](TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_set_downloaded_post**
> TpoSharedEntitiesResult api_authorization_set_downloaded_post(id=id, username=username, password=password, language=language)

Set transaction as downloaded

Set transaction as downloaded. you can only do this action to new transactions assgined to you.              <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Accept.Clear();              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              var parameters = new Dictionary { { \"Id\", \"5b6ae93c28c75751aca5f3db\" } }; // Dictionary type string,string              var urlParams = new FormUrlEncodedContent(parameters);              HttpResponseMessage response = await client.PostAsync(\"Authorization/SetDownloaded\", urlParams);              // Cast the response content to your object using the method response.Content.ReadAsAsync

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | transaction id (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Set transaction as downloaded
    api_response = api_instance.api_authorization_set_downloaded_post(id=id, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->api_authorization_set_downloaded_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| transaction id | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesResult**](TpoSharedEntitiesResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorization_view_get**
> api_authorization_view_get(id=id, direction=direction, username=username, password=password, language=language)

View the Authorization transaction

View individual  claim from the post office. you can only view claims assigned to you or generated from you according to direction parameter.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"Authorization/View?id=5b6ae93c28c75751aca5f3db\");               // Cast the response content to your object using the method response.Content.ReadAsAsync

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | transaction id (optional)
direction = 56 # int | 0 for received, 1 for sent. default is 0 (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # View the Authorization transaction
    api_instance.api_authorization_view_get(id=id, direction=direction, username=username, password=password, language=language)
except ApiException as e:
    print("Exception when calling AuthorizationApi->api_authorization_view_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| transaction id | [optional] 
 **direction** | **int**| 0 for received, 1 for sent. default is 0 | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

