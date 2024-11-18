import requests
import pytest

class BaseApiTest:
    """
    Base class for API testing using pytest fixtures and helper methods.
    """

    # Default header for API requests
    headers = {
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ='  # Base64-encoded 'admin:password'
    }

    # Fixture to provide a base_url to the test function
    @pytest.fixture(autouse=True)
    def setup_class(self, base_url):
        """
        Pytest fixture to set up the base URL for API tests.
        The fixture is automatically applied before each test.
        
        :param base_url: The base URL for API testing.
        """
        self.base_url = base_url

    def get(self, endpoint):
        """
        A helper method to perform GET requests on the provided endpoint.
        
        :param endpoint: The API endpoint to be appended to the base URL.
        :return: The response object from the GET request.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def assert_status_code(self, response, expected_status_code):
        """
        A helper method to assert the HTTP status code of the response.
        
        :param response: The response object returned by the API request.
        :param expected_status_code: The expected HTTP status code (e.g., 200).
        :raises AssertionError: If the status code does not match the expectation.
        """
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, "
            f"but got {response.status_code}. Response: {response.text}"
        )

    def assert_json_key_count(self, response, key):
        """
        Asserts that a specific key exists in the JSON response and contains data.
        
        :param response: The response object containing a JSON body.
        :param key: The key to look for in the JSON body.
        :raises AssertionError: If the key is missing or contains no data.
        """
        json_data = response.json()
        assert key in json_data, f"Key '{key}' not found in response"
        assert json_data[key] > 0, f"No data in key '{key}': {response.text}"

    def assert_json_key_has_data(self, response, key):
        """
        Asserts that a specific key exists in the JSON response and has non-empty data.
        
        :param response: The response object containing a JSON body.
        :param key: The key to check for non-empty data in the JSON body.
        :raises AssertionError: If the key is missing or its value is empty.
        """
        json_data = response.json()
        assert key in json_data, f"Key '{key}' not found in response"
        assert len(json_data[key]) > 0, f"No data in key '{key}': {response.text}"