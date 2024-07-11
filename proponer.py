from conocimiento_de_proposicion import *
from bloque import *
class Proponer():
    def metodo(extensions, preferencias, diseño_esqueletal, diseño, let_probados, cuotas, index_sig_bloque):
        
        sig_bloque = diseño_esqueletal[index_sig_bloque]
        if sig_bloque.asignado_a != None:
            return None, diseño
        else:

            max_criterios, letrados_que_cumplen = Conocimiento_de_proposicion.check_criteria(extensions, preferencias, diseño_esqueletal, diseño, let_probados, sig_bloque)

            if max_criterios == -1:
                return -1, diseño

            letrado_propuesto = Conocimiento_de_proposicion.elegir_letrado(max_criterios, letrados_que_cumplen, diseño, cuotas, sig_bloque)

            new_bloque = Bloque(sig_bloque.cantidad, sig_bloque.fecha, sig_bloque.juzgado, sig_bloque.lista_de_juicios)
            new_bloque.asignado_a = letrado_propuesto
            

            diseño.append(new_bloque)

            return new_bloque, diseño