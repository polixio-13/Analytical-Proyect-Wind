import csv
import pandas as pd
import json
from models import eliminar_parentesis

#Covierto mi  fichero json para manipulacion en Python y despues paso a Pandas
with open ("C:\\Users\\clios\\OneDrive\\Escritorio\\my_proyect\\meteo_data\\meteo_2024", "r") as file:
    data_24= json.load(file)
    print(type(data_24))
    print(data_24)
    
df= pd.DataFrame(data_24)
print("-"*100)
print(f"la informacion del dataframe es: \n")
df.info()


#Aplicar funcion applymap para aplicar a todas las celdas mi funcion creada
df = df.applymap(eliminar_parentesis)

#Elimiar los tres primeros caracteres de column w_racha
df["w_racha"] = df['w_racha'].apply(lambda x: x[3:])

#Covertir resultados string a float y comprobar 
for column in df.columns:
    df[column]= df[column].str.replace(",", ".")
    try:
        df[column]= df[column].astype(float)
    except ValueError:
        pass

print("-"*100)
print("La informacion del dataframe despues de la conversion es: \n")
df.info()

#Mostrar valores nulos por columna
print("\nLA SUMA DE NULOS POR COLUMNA ES: ")  
print(df.isnull().sum())

#Calcular la moda de cada columna y sustituirlos los NaN
moda_n_cub= df["n_cub"].mode()[0]
moda_n_des= df["n_des"].mode()[0]
moda_n_nub= df["n_nub"].mode()[0]
print(f"\nLa moda de n_cub es {moda_n_cub}")
print(f"La moda de n_des {moda_n_des}")
print(f"La moda de n_nub {moda_n_nub}\n")
df["n_cub"]= df["n_cub"].fillna(moda_n_cub)
df["n_des"]= df["n_des"].fillna(moda_n_des)
df["n_nub"]= df["n_nub"].fillna(moda_n_nub)
df= df.drop(columns= ["evap"])



print(df.head())
df.info()
#Guardar Dataframe como archivo csv
df.to_csv("meteo_2024.csv", index=False)
