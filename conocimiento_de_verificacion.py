from metodos_utiles import get_tipo_restricciones, is_bloque_fuera, get_n_bloques_asignados_semana, get_bloques_asignados_semana, get_total_juicios
from restriccion import *

class Conocimiento_de_verificacion():

    def check_criteria(extension, restricciones, diseño):
        fecha_sin_bloque = Conocimiento_de_verificacion.cond_fecha_sin_bloque(extension, diseño)
        fecha_disponible = Conocimiento_de_verificacion.cond_fecha_disponible(extension, restricciones)
        dias_semanales = Conocimiento_de_verificacion.cond_dias_semanales(extension, diseño)
        dias_semanales_fuera = Conocimiento_de_verificacion.cond_dias_semanales_fuera(extension, diseño)
        juicios_semanales = Conocimiento_de_verificacion.cond_juicios_semanales(extension, diseño)
        max_cuota_fuera = Conocimiento_de_verificacion.cond_max_cuota_fuera(extension, restricciones, diseño)
        max_cuotas = Conocimiento_de_verificacion.cond_max_cuotas(extension, restricciones, diseño)

        return fecha_sin_bloque or fecha_disponible or dias_semanales or dias_semanales_fuera or juicios_semanales or max_cuota_fuera or max_cuotas
    
    def cond_fecha_sin_bloque(extension, diseño):  #comprobar que el letrado no tiene un bloque asignado en esa fecha 
        diseño_copia = diseño.copy()
        diseño_copia.remove(extension)
        return [] != list(filter(lambda bloque: (bloque.fecha == extension.fecha) and bloque.asignado_a == extension.asignado_a, diseño_copia))
    
    def cond_fecha_disponible(extension, restricciones):
        no_disponible = False
        disponibilidades = get_tipo_restricciones(restricciones, DISPONIBILIDAD)

        if is_bloque_fuera(extension):
            bajas_de_asignado = list(filter(lambda restriccion: restriccion.letrado == extension.asignado_a, disponibilidades))
            if bajas_de_asignado != []:

                for list_bajas in bajas_de_asignado:
                    dias_de_baja = list_bajas.dias_de_baja
            
                    if extension.fecha in dias_de_baja:
                        no_disponible= True
                
                
            return no_disponible

        else:

            bajas_de_asignado = list(filter(lambda restriccion: (restriccion.letrado == extension.asignado_a) and restriccion.parcial == False, disponibilidades))
            if bajas_de_asignado != []:

                for list_bajas in bajas_de_asignado:
                    dias_de_baja = list_bajas.dias_de_baja
            
                    if extension.fecha in dias_de_baja:
                        no_disponible= True
                
                
            return no_disponible
        
    def cond_dias_semanales(extension, diseño):

        n_bloques_asignados_semana = get_n_bloques_asignados_semana(extension, extension.asignado_a, diseño)

        return n_bloques_asignados_semana > 3
    
    def cond_dias_semanales_fuera(extension, diseño):
        bloques_asignados_semana = get_bloques_asignados_semana(extension, extension.asignado_a, diseño)
        bloques_fuera_asignados_semana = list(filter(lambda bloque: is_bloque_fuera(bloque), bloques_asignados_semana))
        return len(bloques_fuera_asignados_semana) > 1
    
    def cond_juicios_semanales(extension, diseño):

        bloques_asignados_semana = get_bloques_asignados_semana(extension, extension.asignado_a, diseño)
        juicios_semana = get_total_juicios(bloques_asignados_semana)

        return juicios_semana >= 20
    
    def cond_max_cuota_fuera(extension, restricciones, diseño):

        list_cuota_fuera = get_tipo_restricciones(restricciones, MAX_CUOTA_FUERA)
        list_bloques_fuera = list(filter(lambda bloque: (bloque.asignado_a == extension.asignado_a) and is_bloque_fuera(bloque), diseño))
        list_cuota_fuera_de_letrado = list(filter(lambda restriccion: (restriccion.letrado == extension.asignado_a), list_cuota_fuera))

        n_bloques_fuera = len(list_bloques_fuera)

        return n_bloques_fuera > list_cuota_fuera_de_letrado[0].cuota
    
    def cond_max_cuotas(extension, restricciones, diseño):
        list_cuotas = get_tipo_restricciones(restricciones, MAX_CUOTA)
        list_cuota_letrado = list(filter(lambda restriccion: (restriccion.letrado == extension.asignado_a), list_cuotas))


        list_bloques_asignados= list(filter(lambda bloque: (bloque.asignado_a == extension.asignado_a), diseño))
        n_juicios = get_total_juicios(list_bloques_asignados)

        return n_juicios > list_cuota_letrado[0].cuota


                                 
       



