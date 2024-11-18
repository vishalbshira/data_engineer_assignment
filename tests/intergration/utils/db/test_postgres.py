from src.utils.db.postgres import QueryRunner
import pytest

# Fixture to provide a QueryRunner instance to the test function
@pytest.fixture(autouse=True)
def query_runner(test_config):
    """
    Fixture that provides a QueryRunner instance with the test configuration.
    This fixture runs automatically before each test.
        
    Returns:
        QueryRunner: An instance of QueryRunner initialized with test_config.
    """
    return QueryRunner(test_config)

# Test case for validating query execution
def test_query_runner_execute_query(query_runner):
    query = "SELECT 1 as Value;"
    result = query_runner.execute_query(query)
    assert result[0]['value'] == 1