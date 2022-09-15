CREATE DATABASE proyecto;

USE proyecto; 

SELECT * FROM circuits;
SELECT * FROM circuits;


SELECT * FROM results_filt
WHERE raceId=3;

SELECT * FROM pit_stoprs;

# año con mas carrera
SELECT count(*), YEAR FROM races
GROUP BY YEAR
ORDER BY 2 DESC;

# piloto con mayor cantidad de puestos

SELECT raceId,driverId,count(*) as gano FROM results_filt
WHERE position=1
group by driverId
ORDER BY gano DESC;

SELECT * FROM drivers 
WHERE driverId=1;

# nombre del circuito mas corrido

SELECT * , count(*) as cant FROM races
group by circuitId
ORDER BY cant DESC
LIMIT 2;

SELECT * FROM circuits 
WHERE circuitId = 14;

# piloto con mayor cantidad de puntos

CREATE VIEW puntoTotal AS
SELECT * , sum(points) as puntototal FROM results_filt
WHERE constructorID 
group by driverId;

SELECT * FROM puntoTotal;

CREATE VIEW AmeBri AS
SELECT * FROM constructors
WHERE nationality='American' OR nationality='British';

SELECT *, sum(points) as puntaje FROM AmeBri
INNER JOIN results_filt
ON AmeBri.constructorId = results_filt.constructorId
GROUP BY driverId
ORDER BY puntaje DESC;

SELECT * FROM drivers
WHERE driverId = 18;

# 1 2021 con 23 carreras
# 2 hamilton
# 3 Autodromo Nazionale di Monza
# 4 button


