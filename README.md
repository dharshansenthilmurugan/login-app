### Register and Login App using FastAPI and PostgreSQL

#### Description
This project is a register and login application built using FastAPI for the backend and PostgreSQL for database management.

#### FastAPI
##### Routes
- **Register Route**
  - **URL**: `/register`
  - **Method**: POST
  - **Description**: Endpoint to register a new user.
  - **Example Request**:
    ```bash
    curl --location 'http://127.0.0.1:8000/register' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "username": "example_user",
      "password": "example_password"
    }'
    ```
  - **Response**:
    - *200 OK*: Registration successful
    - *400 Bad Request*: Invalid request body or username already exists

- **Login Route**
  - **URL**: `/login`
  - **Method**: POST
  - **Description**: Endpoint to log in a registered user.
  - **Example Request**:
    ```bash
    curl --location 'http://127.0.0.1:8000/login' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "username": "example_user",
      "password": "example_password"
    }'
    ```
  - **Response**:
    - *200 OK*: Login successful
    - *401 Unauthorized*: Incorrect username or password

##### Running the Application
To run the FastAPI application locally, use the following command:
```bash
uvicorn main:app --reload
```

#### PostgreSQL
##### Database Setup
- **Create Database**: Create a PostgreSQL database named my_project1_db.

##### Database Tables
- **Users Table**: This table is created.

##### Commands
- `\l`: View all databases.
- `\dt`: View all tables in the current database.
- `\t <table_name>`: View rows and columns of a specific table.

---

### Customer Management API

#### Overview
The purpose of this API is to manage customer records in a database.

#### Endpoints
- `/create`: Creates a new customer record in the database.
- `/update/{customer_id}`: Updates an existing customer record identified by `{customer_id}`.
- `/delete/{customer_id}`: Deletes a customer record identified by `{customer_id}`.

#### Creating a Customer Record
```bash
curl --location 'http://localhost:8000/customers/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_name": "check",
    "customer_email": "check@gmail.com",
    "customer_phone": "9999944444",
    "customer_address":"coimbatore"
}'

curl --location --request PUT 'http://localhost:8000/customers/update/1' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customer_name": "saipranav",
  "customer_email": "saipranav@gmail.com",
  "customer_phone": "8888833333",
  "customer_address":"madurai"
}'

curl --location --request DELETE 'http://localhost:8000/customers/delete/3'
```

This structure makes it easier to follow the organization of the readme, separating the sections clearly and providing clear instructions for each part of the application.