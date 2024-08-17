from datetime import datetime
from restriccion import *
import calendar

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

def get_n_fechas_con_juicios(list_bloques):
    list_fechas = []
    cont = 0

    for bloque in list_bloques:
        if not (bloque.fecha in list_fechas):

            list_fechas.append(bloque.fecha)
            cont = cont + 1

    return cont

def get_total_juicios(list_bloques):
    cont = 0
    
    for bloque in list_bloques:
        cont = cont + len(bloque.lista_de_juicios)
    
    return cont

def es_div_decimal(numero1, numero2):
    if numero1 % numero2 == 0:
        return False
    else:
        return True
    
def get_letrados_con_baja(list_restricciones, list_letrados):
    letrados_con_baja = []
    for restric in list_restricciones:
        if isinstance(restric, DISPONIBILIDAD):
            letrados_con_baja.append(restric.letrado)
    return letrados_con_baja

def get_tipo_restricciones(list_restricciones, tipo):
    list = []

    for restric in list_restricciones:
        if isinstance(restric, tipo):
            list.append(restric)
    return list 

def get_letrado_jefe(list_letrados):
    for letrado in list_letrados:
        if letrado.jefe == True:
            break
    return letrado

def round_up (num):
    redondeo = round(num)
    if redondeo < num:
        redondeo = redondeo+1
    
    return redondeo

def is_bloque_fuera(bloque):
    return bloque.juzgado[0] == 'F' or bloque.juzgado[0] == 'S'
            

def get_bloques_fuera(list_bloques):
    list_bloques_fuera = []
    

    for bloque in list_bloques:
        if bloque.juzgado[0] == 'F' or bloque.juzgado[0] == 'S':
            list_bloques_fuera.append(bloque)

    return list_bloques_fuera

def get_n_bloques_asignados_semana(bloque, letrado, diseño): #cambiar lista a contador si no hace falta los bloques
    cont = 0

    week_target = bloque.fecha.isocalendar()[1]

    for bloque_dis in diseño:
        if bloque_dis.asignado_a == letrado:
            week_dis = bloque_dis.fecha.isocalendar()[1]

            if week_dis == week_target:
                cont = cont + 1

    return cont

def get_bloques_asignados_semana(bloque, letrado, diseño): 
    list_bloques = []

    week_target = bloque.fecha.isocalendar()[1]

    for bloque_dis in diseño:
        if bloque_dis.asignado_a == letrado:
            week_dis = bloque_dis.fecha.isocalendar()[1]

            if week_dis == week_target:
                list_bloques.append(bloque_dis)

    return list_bloques

def semanas_totales_en_mes(anio, mes):
    # Obtener el primer día del mes (0=Lunes, 1=Martes, ..., 6=Domingo)
    primer_dia_semana, dias_mes = calendar.monthrange(anio, mes)
    
    # Calcular el número de semanas que cubren el mes
    semanas_totales = (dias_mes + primer_dia_semana + 6) // 7
    return semanas_totales, primer_dia_semana, dias_mes