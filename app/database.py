import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="my_project1_db",
    user="postgres",
    password="dharshan",
    host="localhost"
)

