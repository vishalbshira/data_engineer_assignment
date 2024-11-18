from ..base import customerRepository
from ...utils.db.postgres import QueryRunner
from ...config import Config

# SQL Queries for fetching the data from database
TABLE_CUSTOMER_EXIST_SQL = """SELECT COUNT(1) FROM customers where customer_id = {customer_Id}; """

TABLE_CUSTOMER_ID_PER_CHANNEL_SQL = """
SELECT c.Customer_Id, ei.event AS Channel, COUNT(ei.event) AS Interaction_Count
FROM 
    Customers c JOIN interactions ei ON c.Customer_Id = ei.Customers
WHERE c.Customer_Id = {customer_Id}
GROUP BY 
    ei.event, c.Customer_Id
ORDER BY c.Customer_Id;"""

class PostgresCustomerRepository(customerRepository):
    def __init__(self, config: Config):
        # initialize database connection
        self.runner = QueryRunner(config)
    
    def get_customer_interaction_count(self, customer_Id: int) -> int:
        """Retrieves the interaction count for a specific customer per channel.

        Args:
            customer_Id (int): The ID of the customer.

        Returns:
            int: interaction count for the customer
        """
        try:            
            # run the SQL query to get the interaction count
            result = self.runner.execute_query(TABLE_CUSTOMER_ID_PER_CHANNEL_SQL.format(customer_Id=customer_Id), return_dict=False)
            return result
        
        except Exception as e:
            raise e
        
    
    def check_customer_exist(self, customer_Id: int) -> int:
        """
        Checks if a customer exists in the database.

        Args:
            customer_Id (int): The ID of the customer to check.

        Returns:
            int: 1 if the customer exists, 0 otherwise.
        """
        try:
            # run SQL query to check for customer existence
            result = self.runner.execute_query(TABLE_CUSTOMER_EXIST_SQL.format(customer_Id=customer_Id), return_dict=False)
            
            # Return the count if the result is not empty
            return result[0][0] if result else 0
        
        except Exception as e:
            raise e