import requests
from tests.intergration.base_integration import BaseApiTest

# TestApi class extends BaseApiTest to handle API tests for specific endpoints
class TestApi(BaseApiTest):

    # Test case: Verify API returns a 404 error for an invalid table
    def test_get_wrong_table(self):
        table_name = "wrong_table"
        response = self.get(f"/api/v1/stats/{table_name}")
        self.assert_status_code(response, 404)  # Expect 404 Not Found for incorrect table

    # Test case: Verify API returns correct number of customers in the "customers" table
    def test_number_of_customers(self):
        table_name = "customers"
        response = self.get(f"/api/v1/stats/{table_name}")
        self.assert_status_code(response, 200)  # Expect 200 OK for valid table
        self.assert_json_key_count(response, "rows")  # Validate the presence of "rows" in response

    # Test case: Verify API returns the correct number of interactions from "customers_interactions" table
    def test_number_of_interactions(self):
        choose_classifiers = "customers_interactions"
        response = self.get(f"/api/v1/stats/get_interactions/{choose_classifiers}")
        self.assert_status_code(response, 200)  # Expect 200 OK for valid interaction request
        self.assert_json_key_has_data(response, "rows")  # Validate "rows" contain data

    # Test case: Verify API returns interactions for a specific customer ID
    def test_number_of_customer_interactions(self):
        customer_id = 1
        response = self.get(f"/api/v1/customer/interactions/{customer_id}")
        self.assert_status_code(response, 200)  # Expect 200 OK for valid customer interaction request
        self.assert_json_key_has_data(response, "data")  # Validate "data" contains interaction data

    # Test case: Verify API returns 200 OK for successful authentication
    def test_successful_authentication(self):
        table_name = "customers"
        response = self.get(f"/api/v1/stats/{table_name}")
        self.assert_status_code(response, 200)  # Expect 200 OK for authenticated request

    # Test case: Verify API returns 401 Unauthorized for missing authentication
    def test_missing_authentication(self):
        table_name = "customers"
        # Using requests library directly to simulate a missing authentication scenario
        response = requests.get(f"{self.base_url}/api/v1/stats/{table_name}")
        self.assert_status_code(response, 401)  # Expect 401 Unauthorized when authentication is missing
