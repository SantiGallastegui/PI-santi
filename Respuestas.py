import json
import requests
from PIL import Image
import io
import csv
import pandas as pd


constructors= pd.read_json('http://127.0.0.1:8000/constructors')
drivers= pd.read_json('http://127.0.0.1:8000/drivers')

def Respuesta1():
    races = pd.read_json('http://127.0.0.1:8000/races')
    resultado= races.groupby('year').count().sort_values('raceId',ascending=False).max(axis=1).head(5)
    print('Los anios con mas carreras son : ')
    print( resultado)
    

def Respuesta2():
    results = pd.read_json('http://127.0.0.1:8000/results')
    mask = (results['position'] == 1)
    mask2 = results[mask]
    mask3 = mask2[['raceId','driverId']]
    #valor = mask3.groupby('driverId').count().sort_values('raceId',ascending=False).max(axis=1).head(1)
    piloto = drivers.loc[drivers['driverId'] == 1].name
    print( ' EL piloto con mas carreras ganadas es' + piloto )
    print( piloto )



Respuesta1()

Respuesta2()




# def Respuesta2():
