from conexion_BD import *
from bloque_BD import *
from datetime import datetime
from letrado import Letrado

class Servicio_BD:

    def conexion_BD():
        Conexion_BD.conexion_BD()
    
    def eliminar_BD():
        Conexion_BD.eliminar_BD()

    def consultar_BD():
        session = Conexion_BD.obtener_sesion()
        bloques = session.query(Bloque_BD).all()
        session.close()
        return bloques
    
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
    
    def eliminar_reparto_BD():
        session = Conexion_BD.obtener_sesion()
        session.query(Bloque_BD).delete()
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
BD_reparto =Servicio_BD.consultar_BD()

llega = True

