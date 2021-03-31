# swagger_client.ClaimApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_claim_post_submission_post**](ClaimApi.md#api_claim_post_submission_post) | **POST** /api/Claim/PostSubmission | Upload submission transaction

# **api_claim_post_submission_post**
> TpoSharedEntitiesResult api_claim_post_submission_post(body=body, username=username, password=password, language=language)

Upload submission transaction

Upload submission transaction.            <br /><b class=\"ExampleColor\">C# Integration Example: </b>                          HttpClient client = new HttpClient { BaseAddress = new Uri(\"http://TPO_URL/api/\") };             client.DefaultRequestHeaders.Accept.Clear();             client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue(\"application/json\"));             client.DefaultRequestHeaders.Add(\"Username\", \"User\");             client.DefaultRequestHeaders.Add(\"Password\", \"Pass\");             SubmissionParameter pr = new SubmissionParameter() { ...... };             HttpResponseMessage response = await client.PostAsJsonAsync(\"Claim/PostSubmission\", pr);             // Cast the response content to your object using the method response.Content.ReadAsAsync

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
api_instance = swagger_client.ClaimApi(swagger_client.ApiClient(configuration))
body = swagger_client.TpoDataDTOsControllerParametersSubmissionParameter() # TpoDataDTOsControllerParametersSubmissionParameter | The submission object (optional)
username = 'username_example' # str | username case sensitive (optional)
password = 'password_example' # str | password case sensitive (optional)
language = 'en' # str | 'en' for English(default), 'ar' for Arabic (optional) (default to en)

try:
    # Upload submission transaction
    api_response = api_instance.api_claim_post_submission_post(body=body, username=username, password=password, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->api_claim_post_submission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TpoDataDTOsControllerParametersSubmissionParameter**](TpoDataDTOsControllerParametersSubmissionParameter.md)| The submission object | [optional] 
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

