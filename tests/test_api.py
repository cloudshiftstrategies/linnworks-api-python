import pytest
from unittest.mock import patch, Mock
from linnworks_api.generated.auth.api import AuthApi
from linnworks_api.generated.auth.models.authorize_by_application_request import AuthorizeByApplicationRequest
from linnworks_api.generated.inventory.api import InventoryApi
from linnworks_api.generated.inventory.base_client import LinnworksConfig, LinnworksClient as InventoryClient


@pytest.fixture
def mock_response():
    def _create_mock_response(data, content_length=None):
        mock = Mock()
        mock.status = 200
        mock.data = data.encode("utf-8")
        mock.getheader.return_value = "application/json; charset=utf-8"
        mock.getheaders.return_value = {
            "content-type": "application/json; charset=utf-8",
            "content-length": str(content_length or len(data)),
        }
        return mock

    return _create_mock_response


@pytest.fixture
def mock_auth_response(mock_response):
    return mock_response('{"Token": "mock_session_token", "Server": "mock_server"}')


@pytest.fixture
def auth_request():
    return AuthorizeByApplicationRequest(ApplicationId="fake_id", ApplicationSecret="fake_secret", Token="fake_token")


@pytest.fixture
def linnworks_config():
    return LinnworksConfig(client_id="fake_id", client_secret="fake_secret", token="fake_token")


@patch("linnworks_api.generated.auth.api_client.ApiClient.call_api")
def test_auth(mock_call_api, mock_auth_response, auth_request):
    mock_call_api.return_value = mock_auth_response

    auth_api = AuthApi()
    response = auth_api.authorize_by_application(auth_request)

    assert response.token == "mock_session_token"
    mock_call_api.assert_called_once()


@patch("linnworks_api.generated.auth.api_client.ApiClient.call_api")
@patch("linnworks_api.generated.inventory.api_client.ApiClient.call_api")
def test_inventory(mock_inventory_call, mock_auth_call, mock_response, mock_auth_response, linnworks_config):
    # Setup mock responses
    mock_auth_call.return_value = mock_auth_response
    mock_inventory_call.return_value = mock_response("1", content_length=1)

    # Test
    inventory_api = InventoryApi(InventoryClient(linnworks_config=linnworks_config))
    response = inventory_api.get_inventory_items_count()

    assert response == 1
    mock_auth_call.assert_called_once()
    mock_inventory_call.assert_called_once()
