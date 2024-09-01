from conexion_BD import *
from bloque_BD import *
from letrado_BD import *
from datetime import datetime
from letrado import Letrado

from passer_reparto import obtener_reparto_de_excel

class Servicio_BD:

    def conexion_BD():
        Conexion_BD.conexion_BD()
    
    def eliminar_BD():
        Conexion_BD.eliminar_BD()

    def consultar_BD():
        session = Conexion_BD.obtener_sesion()
        bloques = session.query(Bloque_BD).all()
        letrados = session.query(Letrado_BD).all()
        session.close()
        return bloques, letrados
    
    def añadir_reparto_BD(list_bloques):
        list_bloques_BD = []
        for bloque in list_bloques:
            if isinstance(bloque.asignado_a, Letrado):
                bloque_BD = Bloque_BD(bloque.cantidad, bloque.fecha, bloque.juzgado, bloque.asignado_a.nombre)
            else:
                bloque_BD = Bloque_BD(bloque.cantidad, bloque.fecha, bloque.juzgado, bloque.asignado_a)
            list_bloques_BD.append(bloque_BD)

        session = Conexion_BD.obtener_sesion()
        session.add_all(list_bloques_BD)
        session.commit()
        session.close()
    
    def añadir_plantilla(list_letrados):
        list_letrados_BD = []
        for letrado in list_letrados:
            letrado_BD = Letrado_BD(letrado.nombre, letrado.jefe)
            list_letrados_BD.append(letrado_BD)

        session = Conexion_BD.obtener_sesion()
        session.add_all(list_letrados_BD)
        session.commit()
        session.close()

    
    def eliminar_reparto_BD():
        session = Conexion_BD.obtener_sesion()
        session.query(Bloque_BD).delete()
        session.commit()
        session.close()

    def eliminar_plantilla_BD():
        session = Conexion_BD.obtener_sesion()
        session.query(Letrado_BD).delete()
        session.commit()
        session.close()


"""
lista_bloques_BD = []

lista_bloques_BD.append(Bloque_BD(11, datetime(2024, 7, 4), 'F1', "ANA MARIA PARDO COSTAS"))

lista_bloques_BD.append(Bloque_BD(11, datetime(2024, 7, 3), 'C5', "CONCEPCION NIETO ROIG"))

lista_bloques_BD.append(Bloque_BD(11, datetime(2024, 7, 9), 'C5', "MARIA JESUS LEDO MOURE"))

lista_bloques_BD.append(Bloque_BD(11, datetime(2024, 7, 19), 'C4', "ANGEL GONZALEZ QUINTAS"))

lista_bloques_BD.append(Bloque_BD(10, datetime(2024, 7, 9), 'C6', "M. FUENCISLA SUAREZ BEREA"))

lista_bloques_BD.append(Bloque_BD(10, datetime(2024, 7, 11), 'S2', "ANGEL GONZALEZ QUINTAS"))

lista_bloques_BD.append(Bloque_BD(9, datetime(2024, 7, 2), 'F2', "MARIA JOSE GOYANES VIVIANI"))

lista_bloques_BD.append(Bloque_BD(9, datetime(2024, 7, 10), 'C3', "MARIA BELEN GUERRA PAZ"))

lista_bloques_BD.append(Bloque_BD(9, datetime(2024, 7, 16), 'C5', "M. FUENCISLA SUAREZ BEREA"))

lista_bloques_BD.append(Bloque_BD(9, datetime(2024, 7, 17), 'S4', "MARIA JOSE GOYANES VIVIANI"))

lista_bloques_BD.append(Bloque_BD(8, datetime(2024, 7, 1), 'C4', "NATALIA SUAREZ HERVA"))

lista_bloques_BD.append(Bloque_BD(8, datetime(2024, 7, 2), 'C6', "MARTA GARCIA LOPEZ"))

lista_bloques_BD.append(Bloque_BD(8, datetime(2024, 7, 8), 'C4', "MARTA CALVO TRAVIESO"))

lista_bloques_BD.append(Bloque_BD(8, datetime(2024, 7, 16), 'S3', "ANGEL GONZALEZ QUINTAS"))

lista_bloques_BD.append(Bloque_BD(7, datetime(2024, 7, 3), 'S4', "MARTA GARCIA LOPEZ"))

lista_bloques_BD.append(Bloque_BD(7, datetime(2024, 7, 8), 'C6', "MARTA GARCIA LOPEZ"))

lista_bloques_BD.append(Bloque_BD(7, datetime(2024, 7, 8), 'S3', "M. FUENCISLA SUAREZ BEREA"))

lista_bloques_BD.append(Bloque_BD(7, datetime(2024, 7, 15), 'C4', "MARIA BELEN GUERRA PAZ"))

lista_bloques_BD.append(Bloque_BD(7, datetime(2024, 7, 15), 'C6', "MARTA CALVO TRAVIESO"))

lista_bloques_BD.append(Bloque_BD(7, datetime(2024, 7, 16), 'C6', "MARIA BELEN GUERRA PAZ"))

lista_bloques_BD.append(Bloque_BD(6, datetime(2024, 7, 8), 'S1', "NATALIA SUAREZ HERVA"))

lista_bloques_BD.append(Bloque_BD(6, datetime(2024, 7, 15), 'C4', "ANA MARIA PARDO COSTAS"))

lista_bloques_BD.append(Bloque_BD(6, datetime(2024, 7, 17), 'C3', "MARTA GARCIA LOPEZ"))

lista_bloques_BD.append(Bloque_BD(6, datetime(2024, 7, 23), 'R', "CONCEPCION NIETO ROIG"))

lista_bloques_BD.append(Bloque_BD(6, datetime(2024, 7, 30), 'R', "MARIA BELEN GUERRA PAZ"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 2), 'C1', "MARTA CALVO TRAVIESO"))


lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 3), 'C3', "NATALIA SUAREZ HERVA"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 3), 'C2', "M. FUENCISLA SUAREZ BEREA"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 4), 'C7', "CONCEPCION NIETO ROIG"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 9), 'C1', "ANA MARIA PARDO COSTAS"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 9), 'C7', "MARTA CALVO TRAVIESO"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 16), 'C7', "ANA MARIA PARDO COSTAS"))

lista_bloques_BD.append(Bloque_BD(5, datetime(2024, 7, 17), 'R', "M. FUENCISLA SUAREZ BEREA"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 1), 'C1', "ANA MARIA PARDO COSTAS"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 2), 'C7', "MARIA JESUS LEDO MOURE"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 4), 'C2', "MARIA JOSE GOYANES VIVIANI"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 9), 'R', "NATALIA SUAREZ HERVA"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 9), 'S3', "MARTA GARCIA LOPEZ"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 10), 'R', "ANGEL GONZALEZ QUINTAS"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 10), 'C2', "ANA MARIA PARDO COSTAS"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 11), 'C2', "MARIA BELEN GUERRA PAZ"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 11), 'C7', "MARIA JESUS LEDO MOURE"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 12), 'R', "MARTA CALVO TRAVIESO"))

lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 24), 'R', "MARIA JOSE GOYANES VIVIANI"))
lista_bloques_BD.append(Bloque_BD(4, datetime(2024, 7, 31), 'R', "NATALIA SUAREZ HERVA"))
lista_bloques_BD.append(Bloque_BD(3, datetime(2024, 7, 11), 'C3', "M. FUENCISLA SUAREZ BEREA"))
lista_bloques_BD.append(Bloque_BD(3, datetime(2024, 7, 16), 'C1', "MARTA GARCIA LOPEZ"))
lista_bloques_BD.append(Bloque_BD(3, datetime(2024, 7, 16), 'R', "MARTA CALVO TRAVIESO"))

lista_bloques_BD.append(Bloque_BD(3, datetime(2024, 7, 19), 'R', "MARIA JOSE GOYANES VIVIANI"))
lista_bloques_BD.append(Bloque_BD(1, datetime(2024, 7, 2), 'R', "ANGEL GONZALEZ QUINTAS"))
lista_bloques_BD.append(Bloque_BD(1, datetime(2024, 7, 4), 'C3', "MARIA JESUS LEDO MOURE"))
lista_bloques_BD.append(Bloque_BD(1, datetime(2024, 7, 17), 'C6', "ANGEL GONZALEZ QUINTAS"))
lista_bloques_BD.append(Bloque_BD(1, datetime(2024, 7, 18), 'C3', "ANA MARIA PARDO COSTAS"))

"""


"""
from letrado import Letrado
from restriccion import *

from datetime import datetime

def introducir_letrados_y_disp():
    lista_letrados = []
    lista_restricciones = []

    letrado1 = Letrado("ANGEL GONZALEZ QUINTAS", True)
    lista_letrados.append(letrado1)
    disp1 = DISPONIBILIDAD(letrado1, [datetime(2024, 9, 2), datetime(2024, 9, 3), datetime(2024, 7, 4), datetime(2024, 7, 5), datetime(2024, 7, 6), datetime(2024, 7, 9)], False)
    lista_restricciones.append(disp1)
    


    letrado2 = Letrado("MARIA JOSE GOYANES VIVIANI", False)
    lista_letrados.append(letrado2)
    disp2 = DISPONIBILIDAD(letrado2, [datetime(2024, 9, 2), datetime(2024, 9, 17)], False)
    lista_restricciones.append(disp2)

    letrado3 = Letrado("ANA MARIA PARDO COSTAS", False)
    lista_letrados.append(letrado3)
    disp3 = DISPONIBILIDAD(letrado3, [datetime(2024, 6, 6), datetime(2024, 6, 7), datetime(2024, 6, 19)], False) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp3)

    letrado4 = Letrado("NATALIA SUAREZ HERVA", False)
    lista_letrados.append(letrado4)
    disp4 = DISPONIBILIDAD(letrado4, [datetime(2024, 9, 2)], False)
    lista_restricciones.append(disp4)


    letrado5 = Letrado("MARIA BELEN GUERRA DIAZ", False)
    lista_letrados.append(letrado5)
    disp5 = DISPONIBILIDAD(letrado5, [datetime(2024, 9, 2), datetime(2024, 9, 5), datetime(2024, 9, 9)], False)
    lista_restricciones.append(disp5)


    letrado6 = Letrado("MARTA GARCIA LOPEZ", False)
    lista_letrados.append(letrado6)
    disp6 = DISPONIBILIDAD(letrado6, [datetime(2024, 9, 5), datetime(2024, 9, 6), datetime(2024, 9, 9), datetime(2024, 9, 10)], False)
    lista_restricciones.append(disp6)

    letrado7 = Letrado("MARIA JESUS LEDO MOURE", False)
    lista_letrados.append(letrado7)
    disp7 = DISPONIBILIDAD(letrado7, [datetime(2024, 9, 2), datetime(2024, 9, 3)], False)
    lista_restricciones.append(disp7)


    letrado8 = Letrado("M. FUENCISLA SUAREZ BEREA", False)
    lista_letrados.append(letrado8)
    disp8 = DISPONIBILIDAD(letrado8, [datetime(2024, 9, 6)], False) #Habrá que hacer una funcion para pasar de str a datetime
    lista_restricciones.append(disp8)

    letrado9 = Letrado("CONCEPCION NIETO ROIG", False)
    lista_letrados.append(letrado9)
    disp9 = DISPONIBILIDAD(letrado9, [datetime(2024, 9, 2)], False)
    lista_restricciones.append(disp9)

    #letrado10 = Letrado("MARTA CALVO TRAVIESO", False)
    #lista_letrados.append(letrado10)
    #disp10 = DISPONIBILIDAD(letrado10, [datetime(2024, 6, 5)], False) #Habrá que hacer una funcion para pasar de str a datetime
    #lista_restricciones.append(disp10)

    return lista_letrados



list_letrados = introducir_letrados_y_disp()

Servicio_BD.añadir_plantilla(list_letrados)

list_bloques_BD = obtener_reparto_de_excel("C:/Users/gonza/Desktop/uni/TFG/septiembre/Reparto SEPTIEMBRE 2024.xlsx")

Servicio_BD.eliminar_reparto_BD()

Servicio_BD.añadir_reparto_BD(list_bloques_BD)

BD_reparto, BD_plantilla =Servicio_BD.consultar_BD()

llega = True
"""

