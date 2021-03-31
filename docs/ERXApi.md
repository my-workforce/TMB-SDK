# swagger_client.ERXApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_erx_check_activity_status_get**](ERXApi.md#api_erx_check_activity_status_get) | **GET** /api/ERX/CheckActivityStatus | Check prescription activity status
[**api_erx_get_new_get**](ERXApi.md#api_erx_get_new_get) | **GET** /api/ERX/GetNew | Get New Transactions
[**api_erx_patient_prescriptions_get**](ERXApi.md#api_erx_patient_prescriptions_get) | **GET** /api/ERX/PatientPrescriptions | View Patient Prescriptions.
[**api_erx_post_request_post**](ERXApi.md#api_erx_post_request_post) | **POST** /api/ERX/PostRequest | Upload Erx Request transaction
[**api_erx_search_get**](ERXApi.md#api_erx_search_get) | **GET** /api/ERX/Search | Search ERX Transactions
[**api_erx_set_downloaded_post**](ERXApi.md#api_erx_set_downloaded_post) | **POST** /api/ERX/SetDownloaded | Set transaction as downloaded
[**api_erx_view_get**](ERXApi.md#api_erx_view_get) | **GET** /api/ERX/View | download the ERX transaction
[**api_erx_view_pharmacy_prescription_get**](ERXApi.md#api_erx_view_pharmacy_prescription_get) | **GET** /api/ERX/ViewPharmacyPrescription | View Prescription (Pharmacy Use only)

# **api_erx_check_activity_status_get**
> TpoSharedEntitiesManyResult1TpoDataModelsERXPrescriptionActivityStatusTpoDataModelsVersion1000CultureneutralPublicKeyTokennull api_erx_check_activity_status_get(id=id, activity_id=activity_id, username=username, password=password, language=language)

Check prescription activity status

return the activity status related to the prescription              <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"ERX/CheckActivityStatus?id=5b6ae93c28c75751aca5f3db\");               // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Transaction Id (optional)
activity_id = 'activity_id_example' # str | Activity Id (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Check prescription activity status
    api_response = api_instance.api_erx_check_activity_status_get(id=id, activity_id=activity_id, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_check_activity_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Transaction Id | [optional] 
 **activity_id** | **str**| Activity Id | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesManyResult1TpoDataModelsERXPrescriptionActivityStatusTpoDataModelsVersion1000CultureneutralPublicKeyTokennull**](TpoSharedEntitiesManyResult1TpoDataModelsERXPrescriptionActivityStatusTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_erx_get_new_get**
> TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull api_erx_get_new_get(username=username, password=password, language=language)

Get New Transactions

This functions takes no parameters. Returns new transactions (not downloaded) up to 500 transaction.                Transactions returned according to user type. If user is Provider, the function will return the new eRxAuthorization transactions. If user is Payer, the function will return new eRxRequest transactions.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                              HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"ERX/GetNew\");                // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Get New Transactions
    api_response = api_instance.api_erx_get_new_get(username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_get_new_get: %s\n" % e)
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

# **api_erx_patient_prescriptions_get**
> TpoSharedEntitiesManyResult1TpoDataDTOsERXPatientPrescriptionsPatientPrescriptionDTOTpoDataDTOsVersion1000CultureneutralPublicKeyTokennull api_erx_patient_prescriptions_get(national_id=national_id, username=username, password=password, language=language)

View Patient Prescriptions.

Return available prescription list for the patient to dispense               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"ERX/PatientPrescriptions?nationalId=123123\");               // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
national_id = 'national_id_example' # str | National Id (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # View Patient Prescriptions.
    api_response = api_instance.api_erx_patient_prescriptions_get(national_id=national_id, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_patient_prescriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **national_id** | **str**| National Id | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesManyResult1TpoDataDTOsERXPatientPrescriptionsPatientPrescriptionDTOTpoDataDTOsVersion1000CultureneutralPublicKeyTokennull**](TpoSharedEntitiesManyResult1TpoDataDTOsERXPatientPrescriptionsPatientPrescriptionDTOTpoDataDTOsVersion1000CultureneutralPublicKeyTokennull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_erx_post_request_post**
> TpoSharedEntitiesResult api_erx_post_request_post(body=body, username=username, password=password, language=language)

Upload Erx Request transaction

Upload Erx Request transaction.              <br /><b class=\"ExampleColor\">C# Integration Example: </b>                              HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };               client.DefaultRequestHeaders.Accept.Clear();               client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(\"application/json\"));               client.DefaultRequestHeaders.Add(\"Username\", \"User\");               client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");               ErxRequestParameter pr = new ErxRequestParameter() { ...... };               HttpResponseMessage response = await client.PostAsJsonAsync(\"ERX/PostRequest\", pr);               // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
body = swagger_client.TpoDataDTOsControllerParametersErxRequestParameter() # TpoDataDTOsControllerParametersErxRequestParameter | The erx request object. (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Upload Erx Request transaction
    api_response = api_instance.api_erx_post_request_post(body=body, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_post_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TpoDataDTOsControllerParametersErxRequestParameter**](TpoDataDTOsControllerParametersErxRequestParameter.md)| The erx request object. | [optional] 
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

# **api_erx_search_get**
> TpoSharedEntitiesManyResult1TpoDataModelsSharedSearchItemTpoDataModelsVersion1000CultureneutralPublicKeyTokennull api_erx_search_get(license=license, direction=direction, from_date=from_date, to_date=to_date, downloaded=downloaded, id=id, username=username, password=password, language=language)

Search ERX Transactions

Search Post office erx. you can search new data or your data according to the filters provided. (up to 500 transactions)               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                              HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              HttpResponseMessage response = await client.GetAsync(\"ERX/Search\");                // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
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
    # Search ERX Transactions
    api_response = api_instance.api_erx_search_get(license=license, direction=direction, from_date=from_date, to_date=to_date, downloaded=downloaded, id=id, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_search_get: %s\n" % e)
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

# **api_erx_set_downloaded_post**
> TpoSharedEntitiesResult api_erx_set_downloaded_post(id=id, username=username, password=password, language=language)

Set transaction as downloaded

Set transaction as downloaded. you can only do this action to new transactions assgined to you.              <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };              client.DefaultRequestHeaders.Accept.Clear();              client.DefaultRequestHeaders.Add(\"Username\", \"User\");              client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");              var parameters = new Dictionary { { \"Id\", \"5b6ae93c28c75751aca5f3db\" } }; // Dictionary type string,string              var urlParams = new FormUrlEncodedContent(parameters);              HttpResponseMessage response = await client.PostAsync(\"ERX/SetDownloaded\", urlParams);              // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | transaction id (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Set transaction as downloaded
    api_response = api_instance.api_erx_set_downloaded_post(id=id, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_set_downloaded_post: %s\n" % e)
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

# **api_erx_view_get**
> api_erx_view_get(id=id, direction=direction, username=username, password=password, language=language)

download the ERX transaction

View individual  erx transaction from the post office. you can only view ERX assigned to you or generated from you according to direction parameter.               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"ERX/View?id=5b6ae93c28c75751aca5f3db\");               // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | transaction id (optional)
direction = 56 # int | 0 for received, 1 for sent. default is 0 (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # download the ERX transaction
    api_instance.api_erx_view_get(id=id, direction=direction, username=username, password=password, language=language)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_view_get: %s\n" % e)
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

# **api_erx_view_pharmacy_prescription_get**
> TpoSharedEntitiesOneResult1TpoDataModelsERXERxRequestTpoDataModelsVersion1000CultureneutralPublicKeyTokennull api_erx_view_pharmacy_prescription_get(reference=reference, patient_identity=patient_identity, username=username, password=password, language=language)

View Prescription (Pharmacy Use only)

Return available prescription to dispense               <br /><b class=\"ExampleColor\">C# Integration Example: </b>                            HttpClient client = new HttpClient{ BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             HttpResponseMessage response = await client.GetAsync(\"ERX/ViewPharmacyPrescription?reference=1111\");               // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ERXApi(swagger_client.ApiClient(configuration))
reference = 'reference_example' # str | prescription reference number (optional)
patient_identity = 'patient_identity_example' # str | patient Identity (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # View Prescription (Pharmacy Use only)
    api_response = api_instance.api_erx_view_pharmacy_prescription_get(reference=reference, patient_identity=patient_identity, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERXApi->api_erx_view_pharmacy_prescription_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**| prescription reference number | [optional] 
 **patient_identity** | **str**| patient Identity | [optional] 
 **username** | **str**| username case sensitive | [optional] 
 **password** | **str**| password case sensitive | [optional] 
 **language** | **str**| &#x27;en&#x27; for English(default), &#x27;ar&#x27; for Arabic | [optional] [default to en]

### Return type

[**TpoSharedEntitiesOneResult1TpoDataModelsERXERxRequestTpoDataModelsVersion1000CultureneutralPublicKeyTokennull**](TpoSharedEntitiesOneResult1TpoDataModelsERXERxRequestTpoDataModelsVersion1000CultureneutralPublicKeyTokennull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

