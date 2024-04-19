Register and Login App using FastAPI and PostgreSQL
This project is a register and login application built using FastAPI for the backend and PostgreSQL for database management.

FastAPI
Routes
Register Route
URL: /register
Method: POST
Description: Endpoint to register a new user.
Example Request:
register:
curl --location 'http://127.0.0.1:8000/register' \
--header 'Content-Type: application/json' \
--data-raw '{
  "username": "example_user",
  "password": "example_password"
}'
Response:
200 OK: Registration successful
400 Bad Request: Invalid request body or username already exists
Login Route
URL: /login
Method: POST
Description: Endpoint to log in a registered user.
Example Request:
login :
curl --location 'http://127.0.0.1:8000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
  "username": "example_user",
  "password": "example_password"
}'
Response:
200 OK: Login successful
401 Unauthorized: Incorrect username or password
Running the Application
To run the FastAPI application locally, use the following command:

FASTAPI COMMAND;
uvicorn main:app --reload

PostgreSQL
Database Setup
Create Database:
Create a PostgreSQL database named my_project1_db.
Database Tables:
Users table is created

Commands:
\l: View all databases.
\dt: View all tables in the current database.
\t <table_name>: View rows and columns of a specific table.

