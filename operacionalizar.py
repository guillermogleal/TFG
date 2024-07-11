from conocimiento_operacionalizacion import *

class Operacionalizar():

    def metodo(requisitos):
                
        list_cuotas = Conocimiento_de_operacionalizacion.regla_cuotas(requisitos)
        
        list_cuotas_fuera = Conocimiento_de_operacionalizacion.regla_cuotas_fuera(requisitos)
        
        return list_cuotas + list_cuotas_fuera, []