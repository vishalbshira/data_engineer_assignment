from ..base import statisticsRepository
from ...utils.db.postgres import QueryRunner
from ...config import Config

TABLES = ["customers", "products", "interactions"]

TABLE_COUNT_SQL = """SELECT COUNT(*) FROM {table_name}; """

TABLE_CUSTOMER_EXIST_SQL = """SELECT COUNT(1) FROM customers where customer_id = {customer_Id}; """

TABLE_PER_CUSTOMER_PER_CHANNEL_CERTAIN_TOPIC_SQL = """
SELECT c.Customer_Id, ei.event AS Channel, pd.Product, COUNT(ei.event) AS Interaction_Count
FROM 
    Customers c JOIN interactions ei ON c.Customer_Id = ei.Customers
    LEFT JOIN products pd ON TO_CHAR(ei.Date_Start, 'MM-YYYY') = pd.Date
GROUP BY 
    c.Customer_Id, ei.event, pd.Product
ORDER BY c.Customer_Id; """

TABLE_PER_CUSTOMER_PER_CHANNEL_SQL = """
SELECT c.Customer_Id, ei.event AS Channel, -- pd.Product,
    COUNT(ei.event) AS Interaction_Count
FROM 
    Customers c JOIN interactions ei ON c.Customer_Id = ei.Customers
-- LEFT JOIN 
--     products pd 
--     ON TO_CHAR(ei.Date_Start, 'MM-YYYY') = pd.Date
GROUP BY 
    c.Customer_Id, 
    ei.event
    -- pd.Product
ORDER BY c.Customer_Id; """

TABLE_INTERACTION_PER_TYPE_SQL = """
SELECT c.Type AS Customer_Type, ei.event AS Channel, COUNT(ei.event) AS Interaction_Count
FROM 
    Customers c JOIN interactions ei ON c.Customer_Id = ei.Customers
GROUP BY 
    c.Type, ei.event
ORDER BY c.Type, Interaction_Count DESC;
"""

TABLE_CUSTOMER_ID_PER_CHANNEL_SQL = """
SELECT c.Customer_Id, ei.event AS Channel, COUNT(ei.event) AS Interaction_Count
FROM 
    Customers c JOIN interactions ei ON c.Customer_Id = ei.Customers
WHERE c.Customer_Id = {customer_Id}
GROUP BY 
    ei.event, c.Customer_Id
ORDER BY c.Customer_Id;"""

class PostgresStatisticsRepository(statisticsRepository):
    def __init__(self, config: Config):
        # initialize database connection
        self.runner = QueryRunner(config)

    def get_number_of_rows(self, table_name) -> int:
        """Retrieves the number of rows in the specified table.

        Args:
            table_name (str): The name of the table to count rows in.

        Returns:
            int: The number of rows in the table.
        """
        try:
            # run SQL query to count the number of rows
            result = self.runner.execute_query(TABLE_COUNT_SQL.format(table_name = table_name), return_dict=False)

            # return the count of rows
            return result[0][0]
        except Exception as e:
            raise e
    
    def get_customer_interaction_count(self, customer_Id) -> int:
        """
        Return the number of content entries in the database.

        Returns:
            Tuple with the number of content entries.
        """

        result = self.runner.execute_query(TABLE_CUSTOMER_ID_PER_CHANNEL_SQL.format(customer_Id = customer_Id), return_dict=False)
        return result
    
    def get_interaction_count(self, classifier) -> int:
        """
        Return the number of content entries in the database.

        Returns:
            Tuple with the number of content entries.
        """

        result = self.runner.execute_query(TABLE_PER_CUSTOMER_PER_CHANNEL_SQL, return_dict=False)
        return result
    
    def check_table_name(self, table_name: str) -> bool:
        return table_name in TABLES
    
    def check_table_name(self, table_names: list) -> bool:
        return set(table_names.split("_")).issubset(set(TABLES))
    
    def check_customer_exist(self, customer_Id) -> int:
        result = self.runner.execute_query(TABLE_CUSTOMER_EXIST_SQL.format(customer_Id = customer_Id), return_dict=False)
        return result[0][0]