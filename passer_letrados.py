from letrado import Letrado
from restriccion import *

from datetime import datetime

def introducir_letrados_y_disp():
    lista_letrados = []
    lista_restricciones = []

    letrado1 = Letrado("ANGEL GONZALEZ QUINTAS", True)
    lista_letrados.append(letrado1)
    disp1 = DISPONIBILIDAD(letrado1, [datetime(2024, 6, 10), datetime(2024, 6, 11), datetime(2024, 6, 12),  datetime(2024, 6, 13),  datetime(2024, 6, 14)], False) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp1)


    letrado2 = Letrado("MARIA JOSE GOYANES VIVIANI", False)
    lista_letrados.append(letrado2)

    letrado3 = Letrado("ANA MARIA PARDO COSTAS", False)
    lista_letrados.append(letrado3)
    disp3 = DISPONIBILIDAD(letrado3, [datetime(2024, 6, 6), datetime(2024, 6, 7), datetime(2024, 6, 19)], False) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp3)

    letrado4 = Letrado("NATALIA SUAREZ HERVA", False)
    lista_letrados.append(letrado4)

    letrado5 = Letrado("MARIA BELEN GUERRA PAZ", False)
    lista_letrados.append(letrado5)

    letrado6 = Letrado("MARTA GARCIA LOPEZ", False)
    lista_letrados.append(letrado6)

    letrado7 = Letrado("MARIA JESUS LEDO MOURE", False)
    lista_letrados.append(letrado7)

    letrado8 = Letrado("M. FUENCISLA SUAREZ BEREA", False)
    lista_letrados.append(letrado8)
    disp8 = DISPONIBILIDAD(letrado8, [datetime(2024, 6, 6), datetime(2024, 6, 7), datetime(2024, 6, 10),  datetime(2024, 6, 25),  datetime(2024, 6, 26) ], False) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp8)

    letrado9 = Letrado("CONCEPCION NIETO ROIG", False)
    lista_letrados.append(letrado9)

    letrado10 = Letrado("MARTA CALVO TRAVIESO", False)
    lista_letrados.append(letrado10)
    disp10 = DISPONIBILIDAD(letrado10, [datetime(2024, 6, 5)], False) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp10)

    return lista_letrados, lista_restricciones


