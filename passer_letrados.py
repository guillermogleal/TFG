from letrado import Letrado
from restriccion import *

from datetime import datetime

def introducir_letrados_y_disp():
    lista_letrados = []
    lista_restricciones = []

    letrado1 = Letrado("Angel", True)
    lista_letrados.append(letrado1)

    letrado2 = Letrado("Pepa", False)
    lista_letrados.append(letrado2)

    letrado3 = Letrado("Ana", False)
    lista_letrados.append(letrado3)
    disp3 = DISPONIBILIDAD(letrado3, [datetime(2024, 6, 6), datetime(2024, 6, 7), datetime(2024, 6, 19)]) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp3)

    letrado4 = Letrado("Natalia", False)
    lista_letrados.append(letrado4)

    letrado5 = Letrado("Belen", False)
    lista_letrados.append(letrado5)

    letrado6 = Letrado("Marta G.", False)
    lista_letrados.append(letrado6)

    letrado7 = Letrado("Mª Jesus", False)
    lista_letrados.append(letrado7)

    letrado8 = Letrado("Fuencisla", False)
    lista_letrados.append(letrado8)
    disp8 = DISPONIBILIDAD(letrado8, [datetime(2024, 6, 6), datetime(2024, 6, 7), datetime(2024, 6, 10)]) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp8)

    letrado9 = Letrado("Conchita", False)
    lista_letrados.append(letrado9)

    letrado10 = Letrado("Marta C.", False)
    lista_letrados.append(letrado10)
    disp10 = DISPONIBILIDAD(letrado10, [datetime(2024, 6, 5)]) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp10)

    return lista_letrados, lista_restricciones


