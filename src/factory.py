from .config import Config
from .repository.postgres_repository_factory import PostgresRepositoryFactory

def get_repository_factory(config: Config) -> PostgresRepositoryFactory:
    """
    Factory function to create an instance of PostgresRepositoryFactory.

    Args:
        config (Config): The configuration object containing database connection details.

    Returns:
        PostgresRepositoryFactory: An instance of PostgresRepositoryFactory.
    """
    # create and return a new instance of PostgresRepositoryFactory
    return PostgresRepositoryFactory(config)