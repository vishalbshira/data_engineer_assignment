from abc import ABC, abstractmethod

class statisticsRepository(ABC):
    """
    This class represents abstract base class for handling statistical data.
    """
    
    @abstractmethod
    def get_number_of_rows(self, table_name: str) -> int:
        """Return the number of rows."""

    @abstractmethod
    def check_table_name(self, table_name: str) -> bool:
        """Return if table name exists"""

class customerRepository(ABC):
    """
    This class represents abstract base class for handling customer data.
    """
    
    @abstractmethod
    def check_customer_exist(self, customer_id: int) -> int:
        """Return if customer exists."""

    @abstractmethod
    def get_customer_interaction_count(self, customer_id: int) -> str:
        """Return customer interaction count"""

class RepositoryFactory(ABC):
    """
    Abstract base class for creating repository instances.
    This factory defines methods for creating repositories 
    that interact with the data layer.
    """
    @abstractmethod
    def create_statistics_repository(self) -> statisticsRepository:
        "Return an instance of a statistics repository."

    @abstractmethod
    def create_customer_repository(self) -> customerRepository:
        "Return an instance of a customer repository."