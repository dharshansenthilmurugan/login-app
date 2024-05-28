from fastapi import APIRouter, HTTPException, Depends
from app.models import User
from app.database import execute_query, fetch_one

router = APIRouter()

@router.post("/register")
async def register(user: User):
    query = """
        INSERT INTO users (username, password)
        VALUES ($1, $2)
    """
    try:
        await execute_query(query, user.username, user.password)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/login")
async def login(user: User):
    query = """
        SELECT * FROM users
        WHERE username = $1 AND password = $2
    """
    result = await fetch_one(query, user.username, user.password)
    if result:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@router.post("/forgot-password")
async def forgot_password(user: User):
    query = """
        SELECT * FROM users
        WHERE username = $1
    """
    result = await fetch_one(query, user.username)
    if result:
        # Update password for the existing user
        update_query = """
            UPDATE users
            SET password = $1
            WHERE username = $2
        """
        await execute_query(update_query, user.password, user.username)
        return {"message": "Password updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")