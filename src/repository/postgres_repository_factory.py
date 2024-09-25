from .base import RepositoryFactory
from .statistics.postgres import PostgresStatisticsRepository
from .customer.postgres import PostgresCustomerRepository
from ..config import Config

class PostgresRepositoryFactory(RepositoryFactory):
    def __init__(self, config: Config):
        self.config = config

    def create_statistics_repository(self) -> PostgresStatisticsRepository:
        return PostgresStatisticsRepository(self.config)

    def create_customer_repository(self) -> PostgresCustomerRepository:
        return PostgresCustomerRepository(self.config)