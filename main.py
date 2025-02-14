import csv
import pandas as pd
import json
from models import eliminar_parentesis, eliminar_3, pasar_a_float, llenar_nan_moda, convertir_y_ordenar
from database import conexion

#Covierto mi  fichero json para manipulacion en Python y despues paso a Pandas
with open ("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2024", "r") as file:
    data_24= json.load(file)
    print(type(data_24))
    print(data_24)
    
df= pd.DataFrame(data_24)
print("-"*100)
print(f"la informacion del dataframe es: \n")
df.info()
df.head()

#Aplicar funcion applymap para aplicar a todas las celdas mi funcion creada
df = df.applymap(eliminar_parentesis)

#Elimiar los tres primeros caracteres de column w_racha
df["w_racha"] = eliminar_3(df['w_racha'])

#Covertir resultados string a float y comprobar 
for column in df.columns:
    df[column]= pasar_a_float(df[column])
   

print("-"*100)
print("La informacion del dataframe despues de la conversion es: \n")
df.info()

#Mostrar valores nulos por columna
print("\nLA SUMA DE NULOS POR COLUMNA ES: ")  
print(df.isnull().sum())
print("\tTOTAL: ",df.isnull().sum().sum())

#Calcular la moda de cada columna y sustituirlos los NaN
df["n_cub"]= llenar_nan_moda(df["n_cub"])
df["n_des"]= llenar_nan_moda(df["n_des"])
df["n_nub"]= llenar_nan_moda(df["n_nub"])
df= df.drop(columns= ["evap"])

#Eliminamos fila de media anual ya que no podemos hacer coversion a datetime y tampoco nos interesa
df= df.drop(index=12)
#Ordenar Fecha por indice anual
df= convertir_y_ordenar(df,"fecha")

print(f"\nLa suma de NAN en dataframe despues de aniadir modas es: ", df.isnull().sum().sum())
print(df)

df.to_sql('mi_tabla', conexion, if_exists='replace', index=False)

#Guardar Dataframe como archivo csv
df.to_csv("meteo_2024.csv", index=False)
