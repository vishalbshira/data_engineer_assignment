from .config import Config
from .repository.statistics.postgres import PostgresStatisticsRepository
from .repository.customer.postgres import PostgresCustomerRepository

def get_statistics_repository(config: Config) -> PostgresStatisticsRepository:
    # Factory function to create an instance of PostgresStatisticsRepository.
    return PostgresStatisticsRepository(config)

def get_customer_repository(config: Config) -> PostgresCustomerRepository:
    # Factory function to create an instance of PostgresCustomerRepository.
    return PostgresCustomerRepository(config)