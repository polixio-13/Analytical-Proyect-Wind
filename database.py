import sqlite3

conexion= sqlite3.connect("meteo.db")
cursor= conexion.cursor()
conexion.close()



