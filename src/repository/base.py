from abc import ABC, abstractmethod

class statisticsRepository(ABC):
    """
    This class represents abstract base class for handling statistical data.
    """
    
    @abstractmethod
    def get_number_of_rows(self, table_name: str) -> int:
        """Return the number of rows."""

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