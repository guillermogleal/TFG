from requisitos import Requisitos
from conocimiento_especificacion import Conocimiento_de_especificacion
class especificar():
    def metodo(requisitos : Requisitos):
        for i in requisitos.list_bloques:

            i = Conocimiento_de_especificacion.regla_preparados(i, requisitos.list_letrados, requisitos.list_restricciones)

        return requisitos.list_bloques