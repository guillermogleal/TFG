from Passer_from_excel import obtenerBloques
from passer_letrados import introducir_letrados_y_disp
from passer_reparto import *
from requisitos import Requisitos
from configuracion import Configuracion
from servicio_BD import *
from productTable import main_product_table

def print_diseño(diseño, letrados, dias_mes):
    i = 0
    list_n_juicios_letrado = []
    matriz_diseño = []
    num_letrado = 0
    list_nombres = []

    for i in range(len(letrados)):
        fila = []
        for j in range(dias_mes + 1): #el +1 para que no haya dia 0
            fila.append("    "+ str(0))
        matriz_diseño.append(fila)
    
    for letrado in letrados:
        n_juicios_letrado = 0

        list_nombres.append(letrado.nombre)

        bloques_de_letrado = list(filter(lambda bloque: bloque.asignado_a == letrado, diseño))
        for bloque in bloques_de_letrado:
            fecha_bloque = bloque.fecha
            n_juicios_letrado += bloque.cantidad
            dia_fecha_bloque = fecha_bloque.day

            str_bloque = bloque.juzgado + "|" + str(bloque.cantidad)
            n_espacio = 5 - len(str_bloque)
            espacio = ""

            for n in range(n_espacio):
                espacio = espacio + " "

            matriz_diseño[num_letrado][dia_fecha_bloque] =  espacio + str(dia_fecha_bloque)+"|"+str_bloque
        list_n_juicios_letrado.append(n_juicios_letrado)
        num_letrado += 1
    cont_letrado = 0
    for fila in matriz_diseño:
        fila[0] = letrados[cont_letrado].nombre
        print(fila)
        print("\n")
        cont_letrado+=1
    
    print(list_nombres)


    print(list_n_juicios_letrado)




####################################################################

def iniciar_modelo(bloques, plantilla, disponibilidades, list_bloques_directos):

    
    letrados = plantilla
    restricciones = disponibilidades
#    meter_reparto_manual = True

#    if meter_reparto_manual:
#        Servicio_BD.eliminar_reparto_BD()

#        reparto_BD = obtener_reparto_de_excel('C:/Users/gonza/Desktop/uni/TFG/junio/Reparto JUNIO 2024.xlsx')

#        Servicio_BD.añadir_reparto_BD(reparto_BD)

    bloques_BD = Servicio_BD.consultar_BD()[0]

    requisitos = Requisitos(bloques, letrados, restricciones, bloques_BD, list_bloques_directos)

    obj_conf = Configuracion(requisitos, letrados)

    diseño, bloques_sin_asignar, restricciones = obj_conf.execute()



    

#    print_diseño(diseño, letrados, 30)

#    main_product_table(diseño, letrados)                #el main de productTable

    print("llega al final")

    return diseño, bloques_sin_asignar, restricciones