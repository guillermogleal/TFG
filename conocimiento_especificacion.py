from bloque import Bloque
from juicio import Juicio
from metodos_utiles import *

class Conocimiento_de_especificacion():
    def regla_preparados(bloque : Bloque, list_letrados, list_restricciones, list_bloques):
        fecha_datetime = bloque.fecha
        list_con_juicios = []
        list_cantidad = []
        n_mitad_bloque = round(len(bloque.lista_de_juicios) / 2)
        list_nombres_letrado = get_nombres_letrado(list_letrados) 
        list_nombres_restriccion = get_nombres_restriccion(list_restricciones)
        asignable=True

        for juicio in bloque.lista_de_juicios:
            
            
            preparado_por = juicio.preparado_por
            if juicio.demanda == "INSS":
               letrado = get_letrado_por_nombre(preparado_por, list_letrados)
               bloques_asignados_ese_dia = list(filter(lambda bloque_lista: bloque.fecha == bloque_lista.fecha and letrado == bloque_lista.asignado_a, list_bloques))

               bloque.asignado_a = letrado
               if bloques_asignados_ese_dia != []:
                   for bloque_asignado in bloques_asignados_ese_dia:
                       bloque_asignado.asignado_a = None

               return bloque
      

            if preparado_por != None and preparado_por in list_nombres_letrado:
                
                if preparado_por in list_con_juicios:
                    num_letrado=list_con_juicios.index(preparado_por)
                    list_cantidad[num_letrado]= list_cantidad[num_letrado] + 1
                else:
                    list_con_juicios.append(preparado_por)
                    list_cantidad.append(1)
        
        
        for n_preparados in list_cantidad:
            
            if n_preparados >= n_mitad_bloque:
                index_letrado = list_cantidad.index(n_preparados)
                nombre_de_preparador = list_con_juicios[index_letrado]
                if nombre_de_preparador in list_nombres_restriccion:
                    #n_restriccion = list_nombres_restriccion.index(nombre_de_preparador)
                    n_letrado = get_letrado_por_nombre(nombre_de_preparador, list_letrados)
                    list_bajas = get_bajas(list_restricciones, n_letrado)
                    
                    if fecha_datetime in list_bajas:
                        asignable = False
                if asignable:
                    letrado = get_letrado_por_nombre(nombre_de_preparador, list_letrados)

                    bloques_asignados_ese_dia = list(filter(lambda bloque_lista: bloque.fecha == bloque_lista.fecha and letrado == bloque_lista.asignado_a, list_bloques))                    
                    
                    if bloques_asignados_ese_dia != []:

                        bloque.asignado_a = None
                    else: 
                    
                        bloque.asignado_a = letrado
                    break
                else:
                    asignable = True
        return bloque