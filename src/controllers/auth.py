from flask_httpauth import HTTPBasicAuth
from flask import jsonify

# Create a basic auth instance
auth = HTTPBasicAuth()

# user credentials
users = {
    "admin": "password",
    "user": "password"
}

# Verify password
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

# Error handler for authentication failure
@auth.error_handler
def auth_error():
    return jsonify({"message": "Unauthorized access, invalid credentials"}), 401
