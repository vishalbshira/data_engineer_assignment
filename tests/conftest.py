import pytest

# Fixture that provides the base URL for the API endpoints.
@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000"

# Fixture that provides the test database configuration.
@pytest.fixture
def test_config():
    return {
        "DB_NAME": "business",
        "DB_USER": "postgres",
        "DB_HOST": "localhost",
        "DB_PASSWORD": "thepassword",
        "DB_PORT": 5432,
    }