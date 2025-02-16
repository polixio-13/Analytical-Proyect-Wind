import csv
import pandas as pd
import json
import sqlite3
from models import eliminar_parentesis, eliminar_3, pasar_a_float, llenar_nan_moda, convertir_y_ordenar

#Covierto mi  fichero json para manipulacion en Python y despues paso a Pandas
with open ("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2024", "r") as file:
    data_24= json.load(file)
with open("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2023", "r") as file:
    data_23= json.load(file)
with open("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2022", "r") as file:
    data_22= json.load(file)
    
df= pd.DataFrame(data_24)
df_23= pd.DataFrame(data_23)
df_22= pd.DataFrame(data_22)
print("-"*100)
print(f"la informacion del dataframe es: \n")
df_22.info()
df_22.head()

#Aplicar funcion applymap para aplicar a todas las celdas mi funcion creada
df = df.applymap(eliminar_parentesis)
df_23= df_23.applymap(eliminar_parentesis)
df_22= df_22.applymap(eliminar_parentesis)

#Elimiar los tres primeros caracteres de column w_racha
df["w_racha"] = eliminar_3(df['w_racha'])
df_23["w_racha"]= eliminar_3(df_23["w_racha"])
df_22["w_racha"]= eliminar_3(df_22["w_racha"])

#Covertir resultados string a float y comprobar 
for column in df.columns:
    df[column]= pasar_a_float(df[column])
for column in df_23.columns:
    df_23[column]= pasar_a_float(df_23[column]) 
for column in df_22.columns:
    df_22[column]= pasar_a_float(df_22[column]) 
    
print("-"*100)
print("La informacion del dataframe despues de la conversion es: \n")
df_22.info()

#Mostrar valores nulos por columna
print("\nLA SUMA DE NULOS POR COLUMNA ES: ")  
print(df_22.isnull().sum())
print("\tTOTAL: ",df_22.isnull().sum().sum())

#Calcular la moda de cada columna y sustituirlos los NaN
df["n_cub"]= llenar_nan_moda(df["n_cub"])
df["n_des"]= llenar_nan_moda(df["n_des"])
df["n_nub"]= llenar_nan_moda(df["n_nub"])
df_22["inso"]= llenar_nan_moda(df_22["inso"])

#Eliminamos fila de media anual y columnas que no se repiten en todos los dataframes
df= df.drop(index=12)
df_23= df_23.drop(index=3)
df_22= df_22.drop(index=3)
df= df.drop(columns= ["indicativo"])
df_23= df_23.drop(columns= ["indicativo"])
df_22= df_22.drop(columns= ["indicativo"])
df= df.drop(columns= ["evap"])
df_23= df_23.drop(columns= ["evap"])
df_22= df_22.iloc[:, :-3]
df_22= df_22.rename(columns={"hora":"hr"})

#Ordenar Fecha por indice anual
df= convertir_y_ordenar(df,"fecha")
df_23= convertir_y_ordenar(df_23,"fecha")
df_22= convertir_y_ordenar(df_22, "fecha")

#Crear nueva column con año a traves de fecha
df["año"]= df["fecha"].dt.year
df_23["año"]= df_23["fecha"].dt.year
df_22["año"]= df_22["fecha"].dt.year

print(f"\nLa suma de NAN en dataframe despues de aniadir modas es: ", df_22.isnull().sum().sum())
print(df_22)

#Guardar Dataframe como archivo csv
df.to_csv("meteo_2024.csv", index=False)
df_23.to_csv("meteo_2023.csv", index=False)
df_22.to_csv("meteo_2022.csv", index=False)

conexion= sqlite3.connect("meteo.db")
df.to_sql('meteo', conexion, if_exists='append', index=False)
df_23.to_sql('meteo', conexion, if_exists='append', index=False)
df_22.to_sql('meteo', conexion, if_exists='append', index=False)
conexion.commit()
conexion.close()
