Title: Add base test classes to reduce repetitive code

Refactor the test cases by adding base test classes to handle repetitive setup and teardown logic. Child test classes will inherit from these base classes, as a result we can leverage code reusability, simplifying test maintenance, and ensuring consistent test patterns across the project.

- Identify any repetitive logic shared across multiple test classes, such as database connections, API client configurations, or environment setups.
- Ensure base classes are generic and can be extended for multiple test scenarios.
- Use base classes to handle common test utilities, such as custom assertions or reusable helper methods.
- Ensure child classes can extend or override setup logic when needed for specific test cases.

Definition of Done
- Base test classes are created to handle repetitive logic for setup, teardown, and common utilities.
- Child test classes successfully inherit from base classes, reducing redundant code and improving maintainability.