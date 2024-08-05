from datetime import datetime, timedelta
from metodos_utiles import get_n_bloques_asignados_semana, get_bloques_asignados_semana, get_bloques_fuera, is_bloque_fuera

class Conocimiento_de_proposicion():

    def check_criteria(extensions, preferencias, diseño_esqueletal, diseño, let_probados, sig_bloque):
        max_criteria = -1
        letrados_que_cumplen = []
        
        letrados_no_probados = list(filter(lambda letrado: letrado not in let_probados, extensions))
        
        if letrados_no_probados == []:
            return -1, []

        for letrado in letrados_no_probados:
            if Conocimiento_de_proposicion.cond_tres_seguidos(diseño,sig_bloque, letrado):
                if max_criteria < 0:
                    max_criteria = 0
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 0:
                    letrados_que_cumplen.append(letrado)                    
                    
            elif Conocimiento_de_proposicion.cond_tres_no_todos_seguidos(diseño,sig_bloque, letrado):
                if max_criteria < 1:
                    max_criteria = 1
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 1:
                    letrados_que_cumplen.append(letrado)
            
            elif Conocimiento_de_proposicion.cond_tres(diseño,sig_bloque, letrado):
                if max_criteria < 2:
                    max_criteria = 2
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 2:
                    letrados_que_cumplen.append(letrado)
            
            elif Conocimiento_de_proposicion.cond_seguidos(diseño,sig_bloque, letrado):
                if max_criteria < 3:
                    max_criteria = 3
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 3:
                    letrados_que_cumplen.append(letrado)
            elif Conocimiento_de_proposicion.cond_rep_juzgado_fuera(diseño,sig_bloque, letrado):
                if max_criteria < 4:
                    max_criteria = 4
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 4:
                    letrados_que_cumplen.append(letrado)
            elif Conocimiento_de_proposicion.cond_rep_juzgado(diseño,sig_bloque, letrado):
                if max_criteria < 5:
                    max_criteria = 5
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 5:
                    letrados_que_cumplen.append(letrado)
            elif Conocimiento_de_proposicion.cond_rep_juzgado_fuera_mes(sig_bloque, letrado, preferencias):
                if max_criteria < 6:
                    max_criteria = 6
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 6:
                    letrados_que_cumplen.append(letrado)
            elif Conocimiento_de_proposicion.cond_rep_juzgado_mes(preferencias,sig_bloque, letrado):
                if max_criteria < 7:
                    max_criteria = 7
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 7:
                    letrados_que_cumplen.append(letrado)
            else:
                if max_criteria < 8:
                    max_criteria = 8
                    letrados_que_cumplen = []
                    letrados_que_cumplen.append(letrado)
                elif max_criteria == 8:
                    letrados_que_cumplen.append(letrado)
        return max_criteria, letrados_que_cumplen
    
    def cond_tres_seguidos(diseño, sig_bloque, letrado):    #devuelve true si serían 3 seguidos

        fecha = sig_bloque.fecha
        dia_sem = fecha.weekday()
        
        if dia_sem == 0:
            b_asignados_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            if b_asignados_dia_sig != []:
                b_asignados_2_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=2))) and bloque.asignado_a == letrado, diseño))
                return b_asignados_2_dia_sig != []
            return False
        
        elif dia_sem == 1:
            b_asignados_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            b_asignados_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            if b_asignados_dia_sig != [] and b_asignados_dia_ant != []:
                return True
            else:
                b_asignados_2_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=2))) and bloque.asignado_a == letrado, diseño))
                
                if b_asignados_dia_sig != [] and b_asignados_2_dia_sig != []:
                    return True
            return False
        
        elif dia_sem == 2 or dia_sem == 3:
            b_asignados_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            b_asignados_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            b_asignados_2_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=2))) and bloque.asignado_a == letrado, diseño))
            b_asignados_2_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=2))) and bloque.asignado_a == letrado, diseño))

            if (b_asignados_dia_ant != [] and b_asignados_dia_sig != []) or  (b_asignados_dia_ant != [] and b_asignados_2_dia_ant != []) or  (b_asignados_dia_sig != [] and b_asignados_2_dia_sig != []):
                return True
            return False
        
        elif dia_sem == 4:
            b_asignados_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            b_asignados_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            if b_asignados_dia_sig != [] and b_asignados_dia_ant != []:
                return True
            else:
                b_asignados_2_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=2))) and bloque.asignado_a == letrado, diseño))
                
                if b_asignados_dia_ant != [] and b_asignados_2_dia_ant != []:
                    return True
            return False
        
        elif dia_sem == 5:
            b_asignados_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
            if b_asignados_dia_ant != []:
                b_asignados_2_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=2))) and bloque.asignado_a == letrado, diseño))
                return b_asignados_2_dia_ant != []
            return False
        else:
            print("algo fue mal con dia de semana")
    
    def cond_tres_no_todos_seguidos(diseño, sig_bloque, letrado):
        if Conocimiento_de_proposicion.cond_tres(diseño, sig_bloque, letrado):
            bloques_semana = get_bloques_asignados_semana(sig_bloque, letrado, diseño)
            
            seguidos1_2 = ((sig_bloque.fecha + timedelta(days=1)) == bloques_semana[0].fecha) or ((sig_bloque.fecha - timedelta(days=1)) == bloques_semana[0].fecha) #comprueba si el bloque nuevo y el primero de los dos semanales van seguidos
            seguidos1_3 = ((sig_bloque.fecha + timedelta(days=1)) == bloques_semana[1].fecha) or ((sig_bloque.fecha - timedelta(days=1)) == bloques_semana[1].fecha) #comprueba si el bloque nuevo y el primero de los dos semanales van seguidos
            seguidos2_3 = ((bloques_semana[0].fecha + timedelta(days=1)) == bloques_semana[1].fecha) or ((bloques_semana[0].fecha - timedelta(days=1)) == bloques_semana[1].fecha) #comprueba si el bloque nuevo y el primero de los dos semanales van seguidos

            return seguidos1_2 or seguidos1_3 or seguidos2_3
    
    def cond_tres(diseño, sig_bloque, letrado):
        
        n_dias_semana = get_n_bloques_asignados_semana(sig_bloque, letrado, diseño)

        return n_dias_semana >= 2
    
    def cond_seguidos(diseño, sig_bloque, letrado):
        fecha = sig_bloque.fecha

        b_asignados_dia_sig = list(filter(lambda bloque: (bloque.fecha == (fecha + timedelta(days=1))) and bloque.asignado_a == letrado, diseño))
        b_asignados_dia_ant = list(filter(lambda bloque: (bloque.fecha == (fecha - timedelta(days=1))) and bloque.asignado_a == letrado, diseño))

        return b_asignados_dia_ant != [] or b_asignados_dia_sig != []
    
    def cond_rep_juzgado_fuera(diseño, sig_bloque, letrado):
        if is_bloque_fuera(sig_bloque) and sig_bloque.juzgado[0] == "F":
            bloques_fuera = get_bloques_fuera(diseño)
            bloques_fuera = list(filter(lambda bloque: (bloque.juzgado[0] == "F"), bloques_fuera))
            bloques_fuera_asign = list(filter(lambda bloque: (bloque.asignado_a == letrado), bloques_fuera))
            return bloques_fuera_asign != []

        else:
            
            return False
    
    def cond_rep_juzgado_semana(diseño, sig_bloque, letrado):
        target_juzgado = sig_bloque.juzgado
        b_asignados_juzgado_sem = list(filter(lambda bloque: (bloque.juzgado == target_juzgado) and bloque.fecha.isocalendar()[1] == sig_bloque.fecha.isocalendar()[1] and bloque.asignado_a == letrado, diseño))
        return b_asignados_juzgado_sem != []


    def cond_rep_juzgado(diseño, sig_bloque, letrado):
        target_juzgado = sig_bloque.juzgado
        b_asignados_juzgado = list(filter(lambda bloque: (bloque.juzgado == target_juzgado) and bloque.asignado_a == letrado, diseño))
        return b_asignados_juzgado != []
    
    def cond_rep_juzgado_fuera_mes(sig_bloque, letrado, preferencias):
        
        if sig_bloque.juzgado[0] == "F":
            bloques_fuera = list(filter(lambda pref: (pref.juzgado[0] == "F"), preferencias))
            bloques_fuera_asign = list(filter(lambda pref: (pref.letrado == letrado.nombre) and (pref.juzgado == sig_bloque.juzgado), bloques_fuera))
            return bloques_fuera_asign != []

        else:
            
            return False                                                          #si se repite un juzgado de un mes a otro
        
    def cond_rep_juzgado_mes(preferencias, sig_bloque, letrado):
        target_juzgado = sig_bloque.juzgado
        b_asignados_juzgado = list(filter(lambda pref: (pref.juzgado == target_juzgado) and pref.letrado == letrado.nombre, preferencias))
        return b_asignados_juzgado != []
#######################################################################################################

    #elige de entre los letrados que cumplen los mismo criterios según heurísticas
    def elegir_letrado(max_criteria, list_letrados, diseño, cuotas, bloque): 
        
        if len(list_letrados)>1:            

            if not is_bloque_fuera(bloque):            
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_menos_juicios(list_letrados, diseño)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_mas_bloques_fuera(list_letrados, diseño)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_mas_separacion(list_letrados, diseño, bloque)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                list_letrados =  Conocimiento_de_proposicion.get_letrados_con_menos_juicios_semana(list_letrados, diseño, bloque)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_menos_cuota(list_letrados, cuotas)
                
                return list_letrados[0]
                
                
            else:
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_menos_juicios(list_letrados, diseño)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_mas_bloques_coru(list_letrados, diseño)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                list_letrados = Conocimiento_de_proposicion.get_letrados_con_mas_separacion(list_letrados, diseño, bloque)
                if len(list_letrados) == 1:
                    return list_letrados[0]
                
                list_letrados =  Conocimiento_de_proposicion.get_letrados_con_menos_juicios_semana(list_letrados, diseño, bloque)
                if len(list_letrados) == 1:
                    return list_letrados[0]

                list_letrados = Conocimiento_de_proposicion.get_letrados_con_menos_cuota(list_letrados, cuotas)
                
                
                
                return list_letrados[0]
                    
        elif len(list_letrados)==1:
            return list_letrados[0]
        
        else:
            return 0
        
    def get_letrados_con_mas_bloques_fuera(list_letrados, diseño):
        max_bloques = 0
        output_letrados = []

        for letrado in list_letrados:
            letr_bloques_fuera =list(filter(lambda bloque: (is_bloque_fuera(bloque)) and bloque.asignado_a == letrado, diseño))
            n_bloques_fuera =len(letr_bloques_fuera)
            if n_bloques_fuera > max_bloques:
                max_bloques = n_bloques_fuera
                output_letrados = []
                output_letrados.append(letrado)
            elif n_bloques_fuera == max_bloques:
                output_letrados.append(letrado)
        
        return output_letrados
    
    def get_letrados_con_mas_bloques_coru(list_letrados, diseño):
        max_bloques = 0
        output_letrados = []

        for letrado in list_letrados:
            letr_bloques_coru =list(filter(lambda bloque: (not is_bloque_fuera(bloque)) and bloque.asignado_a == letrado, diseño))
            n_bloques_coru =len(letr_bloques_coru)
            if n_bloques_coru > max_bloques:
                max_bloques = n_bloques_coru
                output_letrados = []
                output_letrados.append(letrado)
            elif n_bloques_coru == max_bloques:
                output_letrados.append(letrado)
        
        return output_letrados

    def get_letrados_con_menos_juicios(list_letrados, diseño):
        min_juicios = 50     #valor inicial arbitrario muy alto
        output_letrados = []

        for letrado in list_letrados:
            bloques_asignados =list(filter(lambda bloque: bloque.asignado_a == letrado, diseño))
            n_juicios = 0

            for bloque in bloques_asignados:
                n_juicios+= bloque.cantidad
            
            if n_juicios < min_juicios:
                min_juicios = n_juicios
                output_letrados = []
                output_letrados.append(letrado)
            elif n_juicios == min_juicios:
                output_letrados.append(letrado)
            
        return output_letrados
        
    def get_letrados_con_menos_cuota(list_letrados, cuotas):

        min_cuota = 500     #valor inicial arbitrario muy alto
        output_letrados = []

        for letrado in list_letrados:
            cuota_de_let =list(filter(lambda restriccion: restriccion.letrado == letrado, cuotas))
            n_cuota = cuota_de_let[0].cuota
            
            if n_cuota < min_cuota:
                min_cuota = n_cuota
                output_letrados = []
                output_letrados.append(letrado)
            elif n_cuota == min_cuota:
                output_letrados.append(letrado)
            
        return output_letrados

    def get_letrados_con_menos_juicios_semana(list_letrados, diseño, bloque):
        
        min_juicios = 50     #valor inicial arbitrario muy alto
        output_letrados = []

        for letrado in list_letrados:
            bloques_asignados = get_bloques_asignados_semana(bloque, letrado, diseño)
            n_juicios = 0

            for bloque in bloques_asignados:
                n_juicios+= bloque.cantidad
            
            if n_juicios < min_juicios:
                min_juicios = n_juicios
                output_letrados = []
                output_letrados.append(letrado)
            elif n_juicios == min_juicios:
                output_letrados.append(letrado)
            
        return output_letrados
    
    def get_letrados_con_mas_separacion(list_letrados, diseño, bloque):           #letrados que tengan más días de margen entre el bloque y el más cercano en cuanto fecha
        margen_max = 0
        list_margen_letrados = list_letrados.copy()
        
        for letrado in list_letrados:
            list_b_let_semana = get_bloques_asignados_semana(bloque, letrado, diseño)

            if list_b_let_semana != []:
                list_margenes = []
                for bloque_sem in list_b_let_semana:
                    margen = bloque_sem.fecha - bloque.fecha
                    diferencia_dias = margen.days
                    list_margenes.append(diferencia_dias)
                
                min_margen = min(list_margenes)
                if min_margen != 0:
                    if min_margen > margen_max:
                        margen_max = min_margen
                        list_margen_letrados = []
                        list_margen_letrados.append(letrado)
                    elif min_margen == margen_max:
                        list_margen_letrados.append(letrado)
        
        return list_margen_letrados
