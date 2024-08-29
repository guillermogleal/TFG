from datetime import datetime
from bloque_BD import Bloque_BD

import pandas as pd
import pandas_read_xml as pdx
import numpy as np

def obtener_mes(content_celda):

    if content_celda == "ENERO":
        return 1
    if content_celda == "FEBRERO":
        return 2
    if content_celda == "MARZO":
        return 3
    if content_celda == "ABRIL":
        return 4
    if content_celda == "MAYO":
        return 5
    if content_celda == "JUNIO":
        return 6
    if content_celda == "JULIO":
        return 7
    if content_celda == "AGOSTO":
        return 8
    if content_celda == "SEPTIEMBRE":
        return 9
    if content_celda == "OCTUBRE":
        return 10
    if content_celda == "NOVIEMBRE":
        return 11
    if content_celda == "DICIEMBRE":
        return 12
    
    print("No se reconoció el mes, asegurese de que no tiene espacios, está en español y está en mayúsculas.")
    return 0

def obtener_primera_fila(datos_excel):
    cont=0
    while type(datos_excel.iloc[cont, 0])==float  and cont!=datos_excel.shape[0]:
        cont=cont+1
        
    
    return cont

def traducir_letrado(mote_letrado):

    if mote_letrado == "ANGEL":
        letrado = "ANGEL GONZALEZ QUINTAS"
    elif mote_letrado == "PEPA":
        letrado = "MARIA JOSE GOYANES VIVIANI"
    elif mote_letrado == "ANA":
        letrado = "ANA MARIA PARDO COSTAS"
    elif mote_letrado == "NATALIA":
        letrado = "NATALIA SUAREZ HERVA"
    elif mote_letrado == "BELEN":
        letrado = "MARIA BELEN GUERRA DIAZ"
    elif mote_letrado == "MARTA G":
        letrado = "MARTA GARCIA LOPEZ"
    elif mote_letrado == "Mª JESUS":
        letrado = "MARIA JESUS LEDO MOURE"
    elif mote_letrado == "FUENCISLA": 
        letrado = "M. FUENCISLA SUAREZ BEREA"
    elif mote_letrado == "CONCHITA":
        letrado = "CONCEPCION NIETO ROIG"
    elif mote_letrado == "MARTA":
        letrado = "MARTA CALVO TRAVIESO"
    else:
        letrado = mote_letrado
    return letrado

def crear_bloque(cont_fila, cont_column, datos_excel, fila_con_dias, mes, año):
    letrado_asignado = datos_excel.iloc[cont_fila, 0]

    letrado_asignado = traducir_letrado(letrado_asignado)

    fecha = datetime(año, mes, int(datos_excel.iloc[fila_con_dias, cont_column]))
    juzgado = datos_excel.iloc[cont_fila, cont_column]
    cantidad = datos_excel.iloc[cont_fila, cont_column + 1]

    bloque_BD = Bloque_BD(cantidad, fecha, juzgado, letrado_asignado)
    return bloque_BD


def recorrer_semana(cont_fila, cont_column, datos_excel, mes, año):
    list_bloques_sem = []
    fila_con_dias = cont_fila - 1

    while isinstance(datos_excel.iloc[cont_fila, cont_column-1], str) :             #mientras la primera columna no esté vacía en esa fila, será una fila con bloques y no días

        while cont_column < 13:

            if isinstance(datos_excel.iloc[cont_fila, cont_column], str):
                bloque_sem = crear_bloque(cont_fila, cont_column, datos_excel, fila_con_dias, mes, año)
                list_bloques_sem.append(bloque_sem)

            cont_column+=2

        cont_column = 1
        cont_fila += 1
    
    cont_fila+=1

    return list_bloques_sem, cont_fila, cont_column



def obtener_list_bloques_de_reparto(datos_excel):

    diseño_BD = []                                              #lista de bloques para meter en la base de datos

    filas, columnas = datos_excel.shape

    #primera_fila = obtener_primera_fila(datos_excel)

    año = 2024                                                  #obtener año

    fila_con_numeros = 0
    serie_mes = datos_excel.iloc[:,0]                           #obtener mes a partir del nombre de la columna
    mes_name = serie_mes.name
    mes = obtener_mes(mes_name)                                    

    cont_fila = 2                                               #fila y columna iniciales
    cont_column = 1

    
    while isinstance(datos_excel.iloc[cont_fila, cont_column-1], str):
        list_bloques_sem, cont_fila, cont_column = recorrer_semana(cont_fila, cont_column, datos_excel, mes, año)
        diseño_BD.extend(list_bloques_sem)


    return diseño_BD
    """
    while datos_excel.iloc[cont_fila+1, 0] != "final" and cont_fila+1!=datos_excel.shape[0]:
        while type(datos_excel.iloc[cont_fila, 0]) == float and cont_fila!=datos_excel.shape[0]:
            cont_fila+=1
        
        cont_fila-=1

        while np.isnan(datos_excel.iloc[cont_fila, cont_column]) and cont_fila!=datos_excel.shape[0] and cont_column!=datos_excel.shape[1]:
            cont_column +=1
        fila_con_numeros = cont_fila
        while type(datos_excel.iloc[cont_fila, cont_column]) == int or type(datos_excel.iloc[cont_fila, cont_column]) == np.float64 and not np.isnan(datos_excel.iloc[cont_fila, cont_column]) and cont_fila!=datos_excel.shape[0] and cont_column!=datos_excel.shape[1]:
            dia = datos_excel.iloc[cont_fila, cont_column]
            
            cont_fila += 1
            while type(datos_excel.iloc[cont_fila, cont_column]) != int and type(datos_excel.iloc[cont_fila, cont_column]) != np.float64 and not np.isnan(datos_excel.iloc[cont_fila, cont_column]) and cont_fila!=datos_excel.shape[0] and cont_column!=datos_excel.shape[1]:
            
                while type(datos_excel.iloc[cont_fila, cont_column]) != (str or int or np.float64)and np.isnan(datos_excel.iloc[cont_fila, cont_column])  and cont_fila!=datos_excel.shape[0] and cont_column!=datos_excel.shape[1]:
                    cont_fila += 1
                if isinstance(datos_excel.iloc[cont_fila, cont_column], (int , float , np.float64)) or datos_excel.iloc[cont_fila, cont_column] == "**********":
                    cont_fila = cont_fila
                else:
                    juzgado = datos_excel.iloc[cont_fila, cont_column]
                    cantidad = datos_excel.iloc[cont_fila, cont_column+1]
                    letrado = datos_excel.iloc[cont_fila, 0]
                    fecha = datetime(int(datos_excel.iloc[0, 0]), mes, int(dia))

                    bloque_BD = Bloque_BD(cantidad, fecha, juzgado, letrado)
                    diseño_BD.append(bloque_BD)

                    cont_fila+=1
            
            cont_column+=2
            cont_fila = fila_con_numeros
        cont_fila += 1
        cont_column = 0
        while type(datos_excel.iloc[cont_fila, cont_column]) != float and cont_fila!=datos_excel.shape[0] and cont_column!=datos_excel.shape[1]:
            cont_fila += 1
    return diseño_BD
    """


def obtener_reparto_de_excel(ruta_archivo):
#ruta_archivo = 'C:/Users/gonza/Desktop/uni/TFG/junio/Reparto JUNIO 2024.xlsx'

        # Leer el archivo Excel en un DataFrame de pandas
    datos_excel = pd.read_excel(ruta_archivo)
    diseño_BD = obtener_list_bloques_de_reparto(datos_excel)
    return diseño_BD

#print(type(datos_excel.iloc[13,13]) == np.float64)


    


