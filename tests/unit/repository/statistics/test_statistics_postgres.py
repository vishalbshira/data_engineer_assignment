from src.repository.statistics.postgres import PostgresStatisticsRepository

# Test case for checking if the table name is valid
def test_check_table_name(test_config, base_url):
    stats_repo = PostgresStatisticsRepository(test_config)
    table_name = "business"
    assert stats_repo.check_table_name(table_name) == False, f"Expected 'False' for non-existent table {table_name}"

# Test case for counting number of rows in the table
def test_get_row_count(test_config):
    stats_repo = PostgresStatisticsRepository(test_config)
    table_name = "customers"
    assert stats_repo.get_number_of_rows(table_name) > 0, f"Row count for {table_name} should be greater than 0"

# Test case for verifying interaction count
def test_get_interaction_count(test_config):
    stats_repo = PostgresStatisticsRepository(test_config)
    table_name = "customers"
    assert len(stats_repo.get_interaction_count(table_name)) > 0, f"Expected atleast 1 interaction"
