import pytest
from src.repository.postgres_repository_factory import PostgresRepositoryFactory, PostgresStatisticsRepository, PostgresCustomerRepository

@pytest.fixture
def factory(test_config):
    # Return an instance of the concrete factory
    return PostgresRepositoryFactory(test_config)

# Test that the factory creates a statistics repository instance
def test_create_statistics_repository(factory):
    repo = factory.create_statistics_repository()
    assert isinstance(repo, PostgresStatisticsRepository), "Factory did not return a PostgresStatisticsRepository instance"

# Test that the factory creates a customer repository instance
def test_create_customer_repository(factory):
    repo = factory.create_customer_repository()
    assert isinstance(repo, PostgresCustomerRepository), "Factory did not return a PostgresCustomerRepository instance"