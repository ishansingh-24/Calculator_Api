from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API", description="Simple Calculator using FastAPI", version="1.0")


class Numbers(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {"message": "Calculator API is running successfully"}


@app.post("/add")
def add(numbers: Numbers):
    return {
        "operation": "addition",
        "result": numbers.a + numbers.b
    }


@app.post("/subtract")
def subtract(numbers: Numbers):
    return {
        "operation": "subtraction",
        "result": numbers.a - numbers.b
    }


@app.post("/multiply")
def multiply(numbers: Numbers):
    return {
        "operation": "multiplication",
        "result": numbers.a * numbers.b
    }


@app.post("/divide")
def divide(numbers: Numbers):
    if numbers.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    
    return {
        "operation": "division",
        "result": numbers.a / numbers.b
    }
