from Passer_from_excel import obtenerBloques
from passer_letrados import introducir_letrados_y_disp
from requisitos import Requisitos
from configuracion import Configuracion

def print_diseño(diseño, letrados, dias_mes):
    i = 0
    list_n_juicios_letrado = []
    matriz_diseño = []
    num_letrado = 0

    for i in range(len(letrados)):
        fila = []
        for j in range(dias_mes+1): #el +1 para que no haya dia 0
            fila.append(0)
        matriz_diseño.append(fila)
    
    for letrado in letrados:
        n_juicios_letrado = 0

        bloques_de_letrado = list(filter(lambda bloque: bloque.asignado_a == letrado, diseño))
        for bloque in bloques_de_letrado:
            fecha_bloque = bloque.fecha
            n_juicios_letrado += bloque.cantidad
            dia_fecha_bloque = fecha_bloque.day

            matriz_diseño[num_letrado][dia_fecha_bloque] = bloque.juzgado + "|" + bloque.cantidad
        list_n_juicios_letrado.append(n_juicios_letrado)
        num_letrado += 1
    
    for fila in matriz_diseño:
        print(fila)





bloques = obtenerBloques()
letrados, restricciones = introducir_letrados_y_disp()

requisitos = Requisitos(bloques, letrados, restricciones)

obj_conf = Configuracion(requisitos, letrados)

diseño = obj_conf.execute()

print_diseño(diseño, letrados, 31)

print("llega al final")