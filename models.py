import re
import pandas as pd

#Funcion para eliminar parentesis con informacion
def eliminar_parentesis(text):
    return re.sub(r'\(.*?\)', '', str(text))

#Funcion para elimar 3 primeros caracteres
def eliminar_3(serie):
    return serie.apply(lambda x: x[3:]if isinstance(x, str) and len(x) > 3 else x)

def pasar_a_float(serie):
    serie = serie.str.replace(",", ".")
    try:
        serie = serie.astype(float)
    except ValueError:
        pass
    return serie

#Funcion para sustituir los Nan por sus modas correspondientes
def llenar_nan_moda(serie):
    moda= serie.mode()[0]
    return serie.fillna(moda)

#Funcion para eliminar columna
def eliminar_columna(dataframe, columna_a_eliminar):
    if isinstance(columna_a_eliminar, int):
        columna_a_eliminar = dataframe.columns[columna_a_eliminar]
    
    return dataframe.drop(columns=[columna_a_eliminar])

#Eliminar fila
def elimim_media_anual(dataframe, indice):
    return dataframe.drop(index= indice)
    
#Funcion para ordenar fechas
def convertir_y_ordenar(data, nombre_column):
    data[nombre_column]= pd.to_datetime(data[nombre_column], format= "%Y-%m", errors= "coerce")
    data= data.sort_values(by= [nombre_column])
    return data