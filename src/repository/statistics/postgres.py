from ..base import statisticsRepository
from ...utils.db.postgres import QueryRunner
from ...config import Config

TABLES = ["customers", "products", "interactions"]

TABLE_COUNT_SQL = """SELECT COUNT(*) FROM {table_name}; """

TABLE_CUSTOMER_EXIST_SQL = """SELECT COUNT(1) FROM customers where customer_id = {customer_Id}; """

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
    
    def check_table_name(self, table_name: str) -> bool:
        """Checl if table is present in the database

        Args:
            table_name (str): The name of the table to find.

        Returns:
            bool: True if table exists
        """
        return table_name in TABLES