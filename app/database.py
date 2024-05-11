import asyncpg

# Define your PostgreSQL database connection URL
DATABASE_URL = "postgresql://postgres:dharshan@localhost/my_project1_db"

# Create a global variable to hold the database connection pool
pool = None

# Function to create the database connection pool
async def create_pool():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

# Function to close the database connection pool
async def close_pool():
    await pool.close()

async def execute_query(query, *args):
    async with pool.acquire() as conn:
        if query.strip().lower().startswith('select'):
            # If the query is a SELECT query, fetch and return the rows
            result = await conn.fetch(query, *args)
            return result
        else:
            # For other types of queries, execute the query and return the execution status
            result = await conn.execute(query, *args)
            return result


# Function to fetch one row from the result of a query
async def fetch_one(query, *args):
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, *args)

# Function to fetch all rows from the result of a query
async def fetch_all(query, *args):
    async with pool.acquire() as conn:
        return await conn.fetch(query, *args)
