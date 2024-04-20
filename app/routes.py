from fastapi import APIRouter, HTTPException
from .database import conn
from .models import User
import psycopg2
import logging
logging.basicConfig(level=logging.ERROR, filename="error.log", format="%(asctime)s - %(levelname)s - %(message)s")


router = APIRouter()

@router.post("/register")
async def register(user: User):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (user.username, user.password)
        )
        conn.commit()
        return {"message": "User registered successfully"}
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        cursor.close()



@router.post("/login")
async def login(user: User):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (user.username, user.password)
        )
        result = cursor.fetchone()
        cursor.close()
        if result:
            print("inside if")
            return {"message": "Login successful"}
        else:
            print("inside else")
            return{"message":"Invalid username or password"}
    except psycopg2.Error as e:
        print("inside exception 1")
        logging.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        print("inside exception 2")
        logging.error(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


        import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




@router.post("/forgot-password")
async def forgot_password(user: User):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (user.username,)
        )
        result = cursor.fetchone()
        if result:
            # Update the password for the existing user
            cursor.execute(
                "UPDATE users SET password = %s WHERE username = %s",
                (user.password, user.username)
            )
            conn.commit()
            cursor.close()
            return {"message": "Password updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except psycopg2.Error as e:
        logging.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
