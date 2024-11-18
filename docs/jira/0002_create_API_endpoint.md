Title: Create API endpoint to return interaction count per customer for a specific channel

- Design GET request schema strucutre
    http://<base_url>/api/v1/customer/interactions/<customer_id>
- Design response schema strucutre
```json
{
    "data": {
        "customer_id": 3,
        "interactions": [
            {
                "channel": "Email",
                "count": 1
            }
        ]
    }
}
```

- Implment business logic
- Validate and test API implmentation

Definition of Done:
- The API endpoint returns the count of interactions for a given customer.
- Validation and test cases are implemented for the customer_id.
