# dungeons_and_trolls_client.DungeonsAndTrollsApi

All URIs are relative to *https://dt.garage-trip.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dungeons_and_trolls_assign_skill_points**](DungeonsAndTrollsApi.md#dungeons_and_trolls_assign_skill_points) | **POST** /v1/assign-skill-points | Send multiple commands to the Character bound to the logged user. The order of execution is defined in the message.
[**dungeons_and_trolls_buy**](DungeonsAndTrollsApi.md#dungeons_and_trolls_buy) | **POST** /v1/buy | Buy Items identified by the provided ID for the Character bound to the logged user.
[**dungeons_and_trolls_commands**](DungeonsAndTrollsApi.md#dungeons_and_trolls_commands) | **POST** /v1/commands | Send multiple commands to the Character bound to the logged user. The order of execution is defined in the message.
[**dungeons_and_trolls_game**](DungeonsAndTrollsApi.md#dungeons_and_trolls_game) | **GET** /v1/game | Sends all info about the game.
[**dungeons_and_trolls_monsters_commands**](DungeonsAndTrollsApi.md#dungeons_and_trolls_monsters_commands) | **POST** /v1/monsters-commands | Control monsters. Admin only.
[**dungeons_and_trolls_move**](DungeonsAndTrollsApi.md#dungeons_and_trolls_move) | **POST** /v1/move | Assign skill point to the attribute for the Character bound to the logged user.
[**dungeons_and_trolls_pick_up**](DungeonsAndTrollsApi.md#dungeons_and_trolls_pick_up) | **POST** /v1/pick-up | Equip the Item from the ground identified by the provided ID for the Character bound to the logged user (unused).
[**dungeons_and_trolls_register**](DungeonsAndTrollsApi.md#dungeons_and_trolls_register) | **POST** /v1/register | Register provided User to the Game and create a character.
[**dungeons_and_trolls_respawn**](DungeonsAndTrollsApi.md#dungeons_and_trolls_respawn) | **POST** /v1/respawn | Respawn the Character bound to the logged user.
[**dungeons_and_trolls_skill**](DungeonsAndTrollsApi.md#dungeons_and_trolls_skill) | **POST** /v1/skill | Use a skill (provided by an item) by the Character bound to the logged user.
[**dungeons_and_trolls_yell**](DungeonsAndTrollsApi.md#dungeons_and_trolls_yell) | **POST** /v1/yell | The Character bound to the logged user yells a messages (visible for everyone).


# **dungeons_and_trolls_assign_skill_points**
> object dungeons_and_trolls_assign_skill_points(attributes, blocking=blocking)

Send multiple commands to the Character bound to the logged user. The order of execution is defined in the message.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_attributes import DungeonsandtrollsAttributes
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    attributes = dungeons_and_trolls_client.DungeonsandtrollsAttributes() # DungeonsandtrollsAttributes | 
    blocking = True # bool | default true (optional)

    try:
        # Send multiple commands to the Character bound to the logged user. The order of execution is defined in the message.
        api_response = api_instance.dungeons_and_trolls_assign_skill_points(attributes, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_assign_skill_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_assign_skill_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_buy**
> object dungeons_and_trolls_buy(identifiers, blocking=blocking)

Buy Items identified by the provided ID for the Character bound to the logged user.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_identifiers import DungeonsandtrollsIdentifiers
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    identifiers = dungeons_and_trolls_client.DungeonsandtrollsIdentifiers() # DungeonsandtrollsIdentifiers | 
    blocking = True # bool | default true (optional)

    try:
        # Buy Items identified by the provided ID for the Character bound to the logged user.
        api_response = api_instance.dungeons_and_trolls_buy(identifiers, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_buy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_buy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifiers** | [**DungeonsandtrollsIdentifiers**](DungeonsandtrollsIdentifiers.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_commands**
> object dungeons_and_trolls_commands(commands_batch, blocking=blocking)

Send multiple commands to the Character bound to the logged user. The order of execution is defined in the message.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_commands_batch import DungeonsandtrollsCommandsBatch
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    commands_batch = dungeons_and_trolls_client.DungeonsandtrollsCommandsBatch() # DungeonsandtrollsCommandsBatch | 
    blocking = True # bool | default true (optional)

    try:
        # Send multiple commands to the Character bound to the logged user. The order of execution is defined in the message.
        api_response = api_instance.dungeons_and_trolls_commands(commands_batch, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_commands: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commands_batch** | [**DungeonsandtrollsCommandsBatch**](DungeonsandtrollsCommandsBatch.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_game**
> DungeonsandtrollsGameState dungeons_and_trolls_game(blocking=blocking)

Sends all info about the game.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_game_state import DungeonsandtrollsGameState
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    blocking = True # bool | default false (optional)

    try:
        # Sends all info about the game.
        api_response = api_instance.dungeons_and_trolls_game(blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocking** | **bool**| default false | [optional] 

### Return type

[**DungeonsandtrollsGameState**](DungeonsandtrollsGameState.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_monsters_commands**
> object dungeons_and_trolls_monsters_commands(commands_for_monsters, blocking=blocking)

Control monsters. Admin only.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_commands_for_monsters import DungeonsandtrollsCommandsForMonsters
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    commands_for_monsters = dungeons_and_trolls_client.DungeonsandtrollsCommandsForMonsters() # DungeonsandtrollsCommandsForMonsters | 
    blocking = True # bool | default true (optional)

    try:
        # Control monsters. Admin only.
        api_response = api_instance.dungeons_and_trolls_monsters_commands(commands_for_monsters, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_monsters_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_monsters_commands: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commands_for_monsters** | [**DungeonsandtrollsCommandsForMonsters**](DungeonsandtrollsCommandsForMonsters.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_move**
> object dungeons_and_trolls_move(position, blocking=blocking)

Assign skill point to the attribute for the Character bound to the logged user.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_position import DungeonsandtrollsPosition
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    position = dungeons_and_trolls_client.DungeonsandtrollsPosition() # DungeonsandtrollsPosition | 
    blocking = True # bool | default true (optional)

    try:
        # Assign skill point to the attribute for the Character bound to the logged user.
        api_response = api_instance.dungeons_and_trolls_move(position, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_move: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | [**DungeonsandtrollsPosition**](DungeonsandtrollsPosition.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_pick_up**
> object dungeons_and_trolls_pick_up(identifier, blocking=blocking)

Equip the Item from the ground identified by the provided ID for the Character bound to the logged user (unused).

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_identifier import DungeonsandtrollsIdentifier
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    identifier = dungeons_and_trolls_client.DungeonsandtrollsIdentifier() # DungeonsandtrollsIdentifier | 
    blocking = True # bool | default true (optional)

    try:
        # Equip the Item from the ground identified by the provided ID for the Character bound to the logged user (unused).
        api_response = api_instance.dungeons_and_trolls_pick_up(identifier, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_pick_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_pick_up: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | [**DungeonsandtrollsIdentifier**](DungeonsandtrollsIdentifier.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_register**
> DungeonsandtrollsRegistration dungeons_and_trolls_register(body)

Register provided User to the Game and create a character.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_registration import DungeonsandtrollsRegistration
from dungeons_and_trolls_client.models.dungeonsandtrolls_user import DungeonsandtrollsUser
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    body = dungeons_and_trolls_client.DungeonsandtrollsUser() # DungeonsandtrollsUser | 

    try:
        # Register provided User to the Game and create a character.
        api_response = api_instance.dungeons_and_trolls_register(body)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_register: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DungeonsandtrollsUser**](DungeonsandtrollsUser.md)|  | 

### Return type

[**DungeonsandtrollsRegistration**](DungeonsandtrollsRegistration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_respawn**
> object dungeons_and_trolls_respawn(respawn, blocking=blocking)

Respawn the Character bound to the logged user.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    respawn = None # object | 
    blocking = True # bool | default true (optional)

    try:
        # Respawn the Character bound to the logged user.
        api_response = api_instance.dungeons_and_trolls_respawn(respawn, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_respawn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_respawn: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respawn** | **object**|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_skill**
> object dungeons_and_trolls_skill(skill_use, blocking=blocking)

Use a skill (provided by an item) by the Character bound to the logged user.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_use import DungeonsandtrollsSkillUse
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    skill_use = dungeons_and_trolls_client.DungeonsandtrollsSkillUse() # DungeonsandtrollsSkillUse | 
    blocking = True # bool | default true (optional)

    try:
        # Use a skill (provided by an item) by the Character bound to the logged user.
        api_response = api_instance.dungeons_and_trolls_skill(skill_use, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_skill: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_use** | [**DungeonsandtrollsSkillUse**](DungeonsandtrollsSkillUse.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dungeons_and_trolls_yell**
> object dungeons_and_trolls_yell(message, blocking=blocking)

The Character bound to the logged user yells a messages (visible for everyone).

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import dungeons_and_trolls_client
from dungeons_and_trolls_client.models.dungeonsandtrolls_message import DungeonsandtrollsMessage
from dungeons_and_trolls_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dt.garage-trip.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = dungeons_and_trolls_client.Configuration(
    host = "https://dt.garage-trip.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with dungeons_and_trolls_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dungeons_and_trolls_client.DungeonsAndTrollsApi(api_client)
    message = dungeons_and_trolls_client.DungeonsandtrollsMessage() # DungeonsandtrollsMessage | 
    blocking = True # bool | default true (optional)

    try:
        # The Character bound to the logged user yells a messages (visible for everyone).
        api_response = api_instance.dungeons_and_trolls_yell(message, blocking=blocking)
        print("The response of DungeonsAndTrollsApi->dungeons_and_trolls_yell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DungeonsAndTrollsApi->dungeons_and_trolls_yell: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**DungeonsandtrollsMessage**](DungeonsandtrollsMessage.md)|  | 
 **blocking** | **bool**| default true | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

