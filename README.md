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

## PostgreSQL
### Database Setup
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
```

```bash
curl --location --request PUT 'http://localhost:8000/customers/update/1' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customer_name": "saipranav",
  "customer_email": "saipranav@gmail.com",
  "customer_phone": "8888833333",
  "customer_address":"madurai"
}'
```

```bash
curl --location --request DELETE 'http://localhost:8000/customers/delete/3'
```




MACHINE ENDPOINTS
 
 ### Create a Machine:
```bash
curl --location 'http://localhost:8000/machines/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "machine_id": 1,
    "status": "active"
}'
```

### Read All Machines:

```bash
curl --location 'http://localhost:8000/machines/read_all'
```

### Read One Machine:
```bash
curl --location 'http://localhost:8000/machines/1'
```

### Update a Machine:

```bash
curl --location --request PUT 'http://localhost:8000/machines/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "status": "inactive"
}'
```

### Delete a Machine
```bash
curl --location --request DELETE 'http://localhost:8000/machines/delete/1'
```

## Inventory Endpoints
### Create an Inventory Item

```bash
curl --location 'http://localhost:8000/inventoryItem/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item_id": 1,
    "name": "widget",
    "quantity": 100
}'
```

### Read All Inventory Items
```bash
curl --location 'http://localhost:8000/inventory/read_all'
```

### Read One Inventory Item
```bash
curl --location 'http://localhost:8000/inventory/1'
```

###  Update an Inventory Item
```bash
curl --location --request PUT 'http://localhost:8000/inventory/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "widget",
    "quantity": 150
}'
```

### Delete an Inventory Item
```bash
curl --location --request DELETE 'http://localhost:8000/inventory/delete/1'
```

## Production Data Endpoints
### Create Production Data
```bash
curl --location 'http://localhost:8000/productiondata/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 1,
    "machine_id": 1,
    "product_id": 1,
    "quantity": 1000,
    "timestamp": "2024-05-21T12:00:00Z"
}'
```

### Read All Production Data
```bash
curl --location 'http://localhost:8000/productiondata/read_all'
```

### Read One Production Data
```bash
curl --location 'http://localhost:8000/productiondata/1'
```

### Update Production Data
```bash
curl --location --request PUT 'http://localhost:8000/productiondata/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "machine_id": 1,
    "product_id": 2,
    "quantity": 1200,
    "timestamp": "2024-05-21T12:30:00Z"
}'
```

### Delete Production Data
```bash
curl --location --request DELETE 'http://localhost:8000/productiondata/delete/1'
```

## Quality Report Endpoints
### Create a Quality Report
```bash
curl --location 'http://localhost:8000/qualityreport/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "report_id": 1,
    "machine_id": 1,
    "issues_found": "None",
    "timestamp": "2024-05-21T12:00:00Z"
}'
```

### Read All Quality Reports
```bash
curl --location 'http://localhost:8000/qualityreport/read_all'
```

### Read One Quality Report
```bash
curl --location 'http://localhost:8000/qualityreport/1'
```

### Update a Quality Report
```bash
curl --location --request PUT 'http://localhost:8000/qualityreport/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "machine_id": 2,
    "issues_found": "Minor scratches",
    "timestamp": "2024-05-21T12:30:00Z"
}'
```

### Delete a Quality Report
```bash
curl --location --request DELETE 'http://localhost:8000/qualityreport/delete/1'
```

## Maintenance Schedule Endpoints
### Create a Maintenance Schedule
```bash
curl --location 'http://localhost:8000/maintenanceschedule/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 1,
    "machine_id": 1,
    "scheduled_date": "2024-06-01T09:00:00Z",
    "description": "Quarterly maintenance"
}'
```

### Read All Maintenance Schedules
```bash
curl --location 'http://localhost:8000/maintenanceschedule/read_all'
```

### Read One Maintenance Schedule
```bash
curl --location 'http://localhost:8000/maintenanceschedule/1'
```

### Update a Maintenance Schedule
```bash
curl --location --request PUT 'http://localhost:8000/maintenanceschedule/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "machine_id": 1,
    "scheduled_date": "2024-06-02T09:00:00Z",
    "description": "Updated quarterly maintenance"
}'
```

### Delete a Maintenance Schedule
```bash
curl --location --request DELETE 'http://localhost:8000/maintenanceschedule/delete/1'
```

## SUPPLIERS ROUTES

```bash
curl --location 'http://localhost:8000/suppliers/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "supplier_id": 1,
    "supplier_name": "Supplier A",
    "supplier_email": "supplierA@example.com",
    "supplier_phone": "1234567890",
    "supplier_address": "123 Supplier St."
}'

curl --location 'http://localhost:8000/suppliers/read_all' \
--header 'Content-Type: application/json'

curl --location 'http://localhost:8000/suppliers/1' \
--header 'Content-Type: application/json'

curl --location --request PUT 'http://localhost:8000/suppliers/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "supplier_name": "Supplier A Updated",
    "supplier_email": "supplierA_updated@example.com",
    "supplier_phone": "0987654321",
    "supplier_address": "456 Supplier Ave."
}'

curl --location --request DELETE 'http://localhost:8000/suppliers/delete/1' \
--header 'Content-Type: application/json'
```

## Supplier Products Management

```bash
curl --location 'http://localhost:8000/suppliers_product/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "product_id": 1,
    "supplier_id": 1,
    "product_name": "Product A",
    "product_description": "Description of Product A",
    "price": 100.0
}'

curl --location 'http://localhost:8000/suppliers_product/read_all' \
--header 'Content-Type: application/json'


curl --location 'http://localhost:8000/supplier_product/1' \
--header 'Content-Type: application/json'


curl --location --request PUT 'http://localhost:8000/supplier_product/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "product_name": "Product A Updated",
    "product_description": "Updated description of Product A",
    "price": 150.0
}'


curl --location --request DELETE 'http://localhost:8000/supplier_product/delete/1' \
--header 'Content-Type: application/json'
```

## Orders Management
```bash
curl --location 'http://localhost:8000/orders/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "order_id": 1,
    "supplier_id": 1,
    "product_id": 1,
    "quantity": 10,
    "order_date": "2024-05-21",
    "delivery_date": "2024-05-28"
}'

curl --location 'http://localhost:8000/orders/read_all' \
--header 'Content-Type: application/json'

curl --location 'http://localhost:8000/orders/1' \
--header 'Content-Type: application/json'

curl --location --request PUT 'http://localhost:8000/order/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "supplier_id": 1,
    "product_id": 1,
    "quantity": 20,
    "order_date": "2024-05-21",
    "delivery_date": "2024-05-29"
}'

curl --location --request DELETE 'http://localhost:8000/orders/delete/1' \
--header 'Content-Type: application/json'
```

## Delivery Schedule Management
```bash
curl --location 'http://localhost:8000/deliveryschedule/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "delivery_id": 1,
    "order_id": 1,
    "supplier_id": 1,
    "delivery_date": "2024-05-28",
    "status": "Scheduled"
}'


curl --location 'http://localhost:8000/deliveryschedule/read_all' \
--header 'Content-Type: application/json'


curl --location 'http://localhost:8000/deliveryschedule/1' \
--header 'Content-Type: application/json'

curl --location --request PUT 'http://localhost:8000/deliveryschedule/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "order_id": 1,
    "supplier_id": 1,
    "delivery_date": "2024-05-30",
    "status": "Completed"
}'

curl --location --request DELETE 'http://localhost:8000/deliveryschedule/delete/1' \
--header 'Content-Type: application/json'
```

