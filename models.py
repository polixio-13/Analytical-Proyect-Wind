import re

#Funcion para eliminar parentesis con informacion
def eliminar_parentesis(text):
    return re.sub(r'\(.*?\)', '', str(text))

#Funcion para elimar 3 primeros caracteres
def eliminar_3(serie):
    return serie.apply(lambda x: x[3:])

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
    return dataframe.drop(columns= [columna_a_eliminar])
