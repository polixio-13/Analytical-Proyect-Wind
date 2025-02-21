import sqlite3
import pandas as pd

conexion= sqlite3.connect("meteo.db")

df_combi= pd.read_sql_query("SELECT w_racha, tm_mes, año, hr, q_med  FROM meteo", conexion)
w_racha_combi= pd.read_sql_query("SELECT w_racha, año, mes FROM meteo", conexion)
hr_combi= pd.read_sql_query("SELECT hr, año, mes FROM meteo", conexion)
tm_mes_combi= pd.read_sql_query("SELECT tm_mes, año, mes FROM meteo", conexion)

conexion.close()















