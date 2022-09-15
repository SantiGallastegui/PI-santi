
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text , Optional, Union
from datetime import datetime



app= FastAPI()

# Post Model

@app.get("/")
async def index():
    return {'Message': 'Easter Science'}