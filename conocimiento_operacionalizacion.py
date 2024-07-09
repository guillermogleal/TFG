from metodos_utiles import get_n_fechas_con_juicios, get_total_juicios, es_div_decimal, get_tipo_restricciones, get_letrado_jefe, round_up, get_bloques_fuera
from restriccion import *


PORCENT_JEFE = 0.4
class Conocimiento_de_operacionalizacion():
    
    
    def regla_cuotas(requisitos):
        n_fechas = get_n_fechas_con_juicios(requisitos.list_bloques)
        n_juicios = get_total_juicios(requisitos.list_bloques)
        n_letrados = len(requisitos.list_letrados)
        media_juicios_ini = n_juicios//n_letrados
        if es_div_decimal(n_juicios, n_letrados):
            media_juicios_ini = media_juicios_ini + 1
        list_disponibilidad =  get_tipo_restricciones(requisitos.list_restricciones, DISPONIBILIDAD)

           
        list_juicios_descontados = []
        
        list_porcent = []

        letrad_con_baja = []

        list_cuotas = []

        for disponibilidad in list_disponibilidad:
            if not disponibilidad.parcial and len(disponibilidad.dias_de_baja) >= 5: 
                porcent_disp = (n_fechas-len(disponibilidad.dias_de_baja)) / n_fechas
                
                list_porcent.append(porcent_disp)
                letrad_con_baja.append(disponibilidad.letrado)

                juicios_descontados = round_up(media_juicios_ini - media_juicios_ini*porcent_disp)
                list_juicios_descontados.append(juicios_descontados)
        
        jefe = get_letrado_jefe(requisitos.list_letrados)
        
        if not jefe in letrad_con_baja:

            letrad_con_baja.append(jefe)
            list_porcent.append(PORCENT_JEFE)

            juicios_descontados = round_up(media_juicios_ini - media_juicios_ini*PORCENT_JEFE)
            list_juicios_descontados.append(juicios_descontados)
        else:
            index_jefe = letrad_con_baja.index(jefe)
            porcent_jefe = list_porcent[index_jefe] * PORCENT_JEFE
            list_porcent[index_jefe] = porcent_jefe

            juicios_descontados = round_up(media_juicios_ini - media_juicios_ini*porcent_jefe)
            list_juicios_descontados[index_jefe] = juicios_descontados

        num_letrados_sin_bajas = len(requisitos.list_letrados) - len(letrad_con_baja)

        media_juicios_fin = sum(list_juicios_descontados)/num_letrados_sin_bajas + media_juicios_ini

        if es_div_decimal(sum(list_juicios_descontados), num_letrados_sin_bajas):
            media_juicios_fin = round_up(media_juicios_fin)
        
        for letrado in requisitos.list_letrados:
            if letrado in letrad_con_baja:
                index = letrad_con_baja.index(letrado)
                cuota = media_juicios_fin * list_porcent[index]
                
                restric_cuota = MAX_CUOTA(letrado, round_up(cuota))

                list_cuotas.append(restric_cuota)
            else:
                restric_cuota = MAX_CUOTA(letrado, media_juicios_fin)
                list_cuotas.append(restric_cuota)
        
        return list_cuotas
    
    def regla_cuotas_fuera(requisitos):
        n_bloques_fuera= len(get_bloques_fuera(requisitos.list_bloques))
        n_letrados = len(requisitos.list_letrados)
        media_bloques_fuera = n_bloques_fuera/ n_letrados
        list_cuota_fuera = []

        if es_div_decimal(n_bloques_fuera, n_letrados):
            media_bloques_fuera = round_up(media_bloques_fuera)
        
        for letrado in requisitos.list_letrados:
            cuota_fuera = MAX_CUOTA_FUERA(letrado, media_bloques_fuera)
            list_cuota_fuera.append(cuota_fuera)

        return list_cuota_fuera

