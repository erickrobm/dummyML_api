# Erick Eduardo Robledo Montes
import logging
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, PositiveInt
from pydantic import constr
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("miarchivo1.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

app = FastAPI()

class Gender(str, Enum):
    male = "male"
    female = "female"
    undisclosed = "undisclosed"

class Model(BaseModel):
    active: bool
    balance: float = 0
    email: EmailStr = None
    age: PositiveInt
    name: constr(min_length=4)
    gender: Gender

@app.post("/validate_data")
async def validate_data(data: Model):
    logger.info(f"Data validated for user: {data.name}.")
    return {"message": "Data was validated. All good!", "valid": True}

@app.post("/make_prediction")
async def make_prediction(data: Model):
    prediction_list = ["a high balance", "an average balance", "a normal balance"]
    result = random.choice(prediction_list)
    logger.info(f"User {data.name} has {result} of ${data.balance}.")
    return {"message": result, "prediction": True}

@app.get("/get_info")
async def get_info():
    logger.info(f"User asked for information.")
    return {"message": "This API blablabla..."}