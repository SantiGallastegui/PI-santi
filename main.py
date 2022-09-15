
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Text , Optional, Union
from datetime import datetime
import databases
from sqlalchemy import Column,Integer,String, FLOAT, Table
import sqlalchemy
from urllib import response

DATABASE_URL= "postgresql://aoboqevtajtyzv:061501012291955f1da70705a26b469eb9871c88622ee5aadba159adb46c66ee@ec2-54-160-109-68.compute-1.amazonaws.com:5432/d756kc2sop1go7"
database= databases.Database(DATABASE_URL)
metadata= sqlalchemy.MetaData()


constructors = Table("constructors",metadata,
            Column("constructorId",Integer,primary_key=True),
            Column("constructorRef", String(255), nullable=False),
            Column("name", String(255), nullable=False),
            Column("nationality",String(255), nullable=False),
            Column("url", String(255), nullable=False))

class constructor(BaseModel):
    constructorId: int
    constructorRef: str
    name: str
    nationality :str
    url: str

engine= sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)

app= FastAPI()

# Post Model
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/constructors/', response_model=List[constructor])
async def read_notes():
    query= constructors.select()
    return await database.fetch_all(query)


@app.get("/")
async def index():
    return {'Message': 'Easter Science'}