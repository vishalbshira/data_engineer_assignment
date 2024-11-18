Title: Implement Authentication Method for API Using HTTP Basic Authentication

Develop an authentication method using HTTP Basic Authentication (HTTPBasicAuth) to secure API endpoints.

- Install and configure Flask-HTTPAuth to handle HTTP Basic Authentication
- Create a separate authentication module to handle user verification and password validation.
- Validate the username and password for incoming API requests.
- Modify existing API endpoints to require authentication using the @auth.login_required decorator.

Definition of Done:
- HTTP Basic Authentication is implemented and integrated with the API.
- All protected API endpoints require valid credentials to access.
- Unit tests authenticates valid and invalid APIs.