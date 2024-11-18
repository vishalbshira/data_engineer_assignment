from src.repository.customer.postgres import PostgresCustomerRepository

# Test case for fetching customer interaction count from the repository
def test_get_customer_interaction_count(test_config):
    stats_repo = PostgresCustomerRepository(test_config)
    customer_id = 4
    interaction_count = stats_repo.get_customer_interaction_count(customer_id)
    assert len(interaction_count) > 0, f"No interactions found for customer ID {customer_id}"


# Test case for checking if a customer exists in the repository
def test_check_customer_exist(test_config):
    stats_repo = PostgresCustomerRepository(test_config)
    customer_id = "1"
    customer_exists = stats_repo.check_customer_exist(customer_id)
    assert customer_exists > 0, f"Customer ID {customer_id} does not exist"
