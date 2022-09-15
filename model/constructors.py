from decimal import Decimal
from unicodedata import decimal
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL
from config.db import engine, meta_data, BaseModel

constructors = Table("constructors",meta_data,
            Column("constructorId",Integer,primary_key=True),
            Column("constructorRef", String(255), nullable=False),
            Column("name", String(255), nullable=False),
            Column("nationality",String(255), nullable=False),
            Column("url", String(255), nullable=False))

class constructors(BaseModel):
    constructorId: int
    constructorRef: str
    name: str
    nationality :str
    url: str
    
circuits = Table("circuits",meta_data,
            Column("circuitId",Integer,primary_key=True),
            Column("circuitRef", String(255), nullable=False),
            Column("name", String(255), nullable=False),
            Column("location",String(255), nullable=False),
            Column("country", String(255), nullable=False),
            Column("lat",DECIMAL, nullable=False),
            Column("lng",DECIMAL, nullable=False),
            Column("alt",Integer, nullable=False),
            Column("url",String, nullable=False))

drivers = Table("drivers",meta_data,
            Column("driverId",Integer,primary_key=True),
            Column("driverRef", String(255), nullable=False),
            Column("number", String(255), nullable=False),
            Column("code",String(255), nullable=False),
            Column("name", String(255), nullable=False),
            Column("dob",String(255), nullable=False),
            Column("nationality",String(255), nullable=False),
            Column("url",String(255), nullable=False))

pit_stoprs = Table("pit_stoprs",meta_data,
            Column("raceId",Integer,primary_key=True),
            Column("driverId", Integer, nullable=False),
            Column("stop", Integer, nullable=False),
            Column("lap",Integer, nullable=False),
            Column("time", String(255), nullable=False),
            Column("duration",DECIMAL, nullable=False),
            Column("milliseconds",Integer, nullable=False))

races = Table("races",meta_data,
            Column("raceId",Integer,primary_key=True),
            Column("year", Integer, nullable=False),
            Column("round", Integer, nullable=False),
            Column("circuitId",Integer, nullable=False),
            Column("name", String(255), nullable=False),
            Column("date",String(255), nullable=False),
            Column("time",String(255), nullable=False),
            Column("url",String(255), nullable=False))

results = Table("results_filt",meta_data,
            Column("resultId",Integer,primary_key=True),
            Column("raceId", Integer, nullable=False),
            Column("driverId", Integer, nullable=False),
            Column("constructorId",Integer, nullable=False),
            Column("number", Integer, nullable=False),
            Column("grid",Integer, nullable=False),
            Column("position",Integer, nullable=False),
            Column("positionText",Integer, nullable=False),
            Column("positionOrder",Integer, nullable=False),
            Column("points",DECIMAL, nullable=False),
            Column("laps",Integer, nullable=False),
            Column("time",String(255), nullable=False),
            Column("milliseconds",Integer, nullable=False),
            Column("fastestLap",Integer, nullable=False),
            Column("rank",Integer, nullable=False),
            Column("fastestLapTime",String(255), nullable=False),
            Column("fastestLapSpeed",DECIMAL, nullable=False),
            Column("statusId",Integer, nullable=False),)



meta_data.create_all(engine) 
