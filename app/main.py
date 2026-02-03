from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "environment": os.getenv("ENV"),
        "message": "FastAPI runningxccf cfxvfdvd"
    }