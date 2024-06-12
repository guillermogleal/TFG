from Passer_from_excel import obtenerBloques
from passer_letrados import introducir_letrados_y_disp
from requisitos import Requisitos
from configuracion import Configuracion

bloques = obtenerBloques()
letrados, restricciones = introducir_letrados_y_disp()

requisitos = Requisitos(bloques, letrados, restricciones)

obj_conf = Configuracion(requisitos, letrados)

diseño = obj_conf.execute()

print("llega al final")