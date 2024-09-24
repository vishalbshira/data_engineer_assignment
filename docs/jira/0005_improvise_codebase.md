Title: Improve Codebase by Adding Connection Pool and Fixing Transaction Management

#### Add Connection Pool
- Implement a connection pool using psycopg2.pool.SimpleConnectionPool or an equivalent method.
- Ensure that connections are returned to the pool after use to prevent leaks.
#### Fix Transaction Management
- Verify that the context manager used for database transactions closes connections appropriately, not just transactions.
- Implement proper error handling and rollback procedures in case of transaction failures.
#### Manage Configuration Secrets:
- Review current configuration management and identify sensitive information (e.g., database passwords).
- Implement a secure method for managing configuration secrets, such as using environment variables or a secrets management tool (e.g., Azure Key Vaults).


