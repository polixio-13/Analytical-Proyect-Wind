import csv
import pandas as pd
import json
import sqlite3
from models import eliminar_parentesis, eliminar_3, pasar_a_float, llenar_nan_moda, convertir_y_ordenar, eliminar_columna, elimim_media_anual

#Covierto mi  fichero json para manipulacion en Python y despues paso a Pandas
with open ("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2024", "r") as file:
    data_24= json.load(file)
with open("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2023", "r") as file:
    data_23= json.load(file)
with open("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2022", "r") as file:
    data_22= json.load(file)
with open("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2021", "r") as file:
    data_21= json.load(file)
with open("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2020", "r") as file:
    data_20= json.load(file)
            
df= pd.DataFrame(data_24)
df_23= pd.DataFrame(data_23)
df_22= pd.DataFrame(data_22)
df_21= pd.DataFrame(data_21)
df_20= pd.DataFrame(data_20)

print("-"*100)
print(f"la informacion del dataframe es: \n")
df_20.info()
print(df_20)
#Aplicar funcion applymap para aplicar a todas las celdas mi funcion creada
df = df.applymap(eliminar_parentesis)
df_23= df_23.applymap(eliminar_parentesis)
df_22= df_22.applymap(eliminar_parentesis)
df_21= df_21.applymap(eliminar_parentesis)
df_20= df_20.applymap(eliminar_parentesis)

#Elimiar los tres primeros caracteres de column w_racha
df["w_racha"] = eliminar_3(df['w_racha'])
df_23["w_racha"]= eliminar_3(df_23["w_racha"])
df_22["w_racha"]= eliminar_3(df_22["w_racha"])
df_21["w_racha"]= eliminar_3(df_21["w_racha"])
df_20["w_racha"]= eliminar_3(df_20["w_racha"])

#Covertir resultados string a float y comprobar 
for column in df.columns:
    df[column]= pasar_a_float(df[column])
for column in df_23.columns:
    df_23[column]= pasar_a_float(df_23[column]) 
for column in df_22.columns:
    df_22[column]= pasar_a_float(df_22[column]) 
for column in df_21.columns:
    df_21[column]= pasar_a_float(df_21[column]) 
for column in df_20.columns:
    df_20[column]= pasar_a_float(df_20[column]) 
       
print("-"*100)
print("La informacion del dataframe despues de la conversion es: \n")
df_20.info()

#Mostrar valores nulos por columna
print("\nLA SUMA DE NULOS POR COLUMNA ES: ")  
print(df_20.isnull().sum())
print("\tTOTAL: ",df_20.isnull().sum().sum())

#Calcular la moda de cada columna y sustituirlos los NaN
df["n_cub"]= llenar_nan_moda(df["n_cub"])
df["n_des"]= llenar_nan_moda(df["n_des"])
df["n_nub"]= llenar_nan_moda(df["n_nub"])
df_22["inso"]= llenar_nan_moda(df_22["inso"])
df_21["inso"]= llenar_nan_moda(df_21["inso"])
df_21["hora"]= llenar_nan_moda(df_21["hora"])
df_20["n_gra"]= llenar_nan_moda(df_20["n_gra"])
df_20["n_fog"]= llenar_nan_moda(df_20["n_fog"])
df_20["inso"]= llenar_nan_moda(df_20["inso"])
df_20["n_llu"]= llenar_nan_moda(df_20["n_llu"])
df_20["n_tor"]= llenar_nan_moda(df_20["n_tor"])
df_20["n_nie"]= llenar_nan_moda(df_20["n_nie"])

#Eliminamos fila de media anual y columnas que no se repiten en todos los dataframes
df= elimim_media_anual(df, 12)
df_23= elimim_media_anual(df_23, 3)
df_22= elimim_media_anual(df_22, 3)
df_21= elimim_media_anual(df_21, 3)
df_20= elimim_media_anual(df_20, 3)

df= eliminar_columna(df, "evap")
df_23= eliminar_columna(df_23, "evap")
df_21= eliminar_columna(df_21, "evaporar")
df_20= eliminar_columna(df_20, "evaporar")


df_22= df_22.iloc[:, :-3]
df_21= df_21.iloc[:, :-2]
df_20= df_20.iloc[:, :-2]
df_22= df_22.rename(columns={"hora":"hr"})
df_21= df_21.rename(columns={"hora":"hr"})
df_20= df_20.rename(columns={"hora":"hr"})

#Ordenar Fecha por indice anual
df= convertir_y_ordenar(df,"fecha")
df_23= convertir_y_ordenar(df_23,"fecha")
df_22= convertir_y_ordenar(df_22, "fecha")
df_21= convertir_y_ordenar(df_21, "fecha")
df_20= convertir_y_ordenar(df_20, "fecha")

#Crear nueva column con año a traves de fecha para poder filtrar en BBDD
df["año"]= df["fecha"].dt.year
df_23["año"]= df_23["fecha"].dt.year
df_22["año"]= df_22["fecha"].dt.year
df_21["año"]= df_21["fecha"].dt.year
df_20["año"]= df_20["fecha"].dt.year

print(f"\nLa suma de NAN en dataframe despues de aniadir modas es: ", df_20.isnull().sum().sum())
print(df_20)

#Guardar Dataframe como archivo csv
df.to_csv("meteo_2024.csv", index=False)
df_23.to_csv("meteo_2023.csv", index=False)
df_22.to_csv("meteo_2022.csv", index=False)
df_21.to_csv("meteo_2021.csv", index=False)
df_20.to_csv("meteo_2020.csv", index=False)

conexion= sqlite3.connect("meteo.db")
df.to_sql('meteo', conexion, if_exists='append', index=False)
df_23.to_sql('meteo', conexion, if_exists='append', index=False)
df_22.to_sql('meteo', conexion, if_exists='append', index=False)
df_21.to_sql('meteo', conexion, if_exists='append', index=False)
df_20.to_sql('meteo', conexion, if_exists='append', index=False)
conexion.commit()
conexion.close()
