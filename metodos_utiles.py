from datetime import datetime
from restriccion import *

def obtener_campo_aux(str, i):
    campo = ""
    length = len(str)
    letra_act = str[i]
    while (i<length) and (str[i] != '/'):
        campo = campo + str[i]        
        i = i + 1
    i = i + 1
    return campo, i 

def str_to_datetime(str):
    i = 0
    lengt = len(str)
    dia, i = obtener_campo_aux(str, i)
    mes, i = obtener_campo_aux(str, i)
    año, i = obtener_campo_aux(str, i)

    if len(año) == 2 :
        str_año = "20"
        año = str_año+año
    return datetime(int(año), int(mes), int(dia))

def get_nombres_letrado(list_letrados):
    list_nombres = []
    for i in list_letrados:
        list_nombres.append(i.nombre)
    return list_nombres

def get_nombres_restriccion(list_restricciones):
    list_nombres = []
    for i in list_restricciones:
        list_nombres.append(i.letrado.nombre)
    return list_nombres

def get_bajas(list_restricciones, letrado):
    i = 0 
    while i < len(list_restricciones) and not isinstance(list_restricciones[i], DISPONIBILIDAD) and list_restricciones[i].letrado != letrado:
        i = i + 1
    return list_restricciones[i].dias_de_baja

def get_letrado_por_nombre(nombre_letrado, list_letrados):
    i = 0
    while list_letrados[i].nombre != nombre_letrado:
        i = i+1
    return list_letrados[i]