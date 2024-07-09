from conocimiento_de_proposicion import *
from bloque import *
class Proponer():
    def metodo(extensions, preferencias, diseño_esqueletal, diseño, let_probados, cuotas):
        index_sig_bloque = len(diseño)
        sig_bloque = diseño_esqueletal[index_sig_bloque]
        if sig_bloque.asignado_a != None:
            diseño.append(sig_bloque)
            return diseño
        else:
            bloque1 = Bloque(12, datetime(int(2024), int(6), int(6)), "juzgado_act", [])
            bloque1.asignado_a = extensions[0]
            diseño.append(bloque1)

            bloque2 = Bloque(12, datetime(int(2024), int(6), int(4)), "juzgado_act", [])
            

            bloque3 = Bloque(12, datetime(int(2024), int(6), int(5)), "juzgado_act", [])
            bloque3.asignado_a = extensions[0]
            diseño.append(bloque3)

            bloque4 = Bloque(12, datetime(int(2024), int(6), int(3)), "juzgado_act", [])
            bloque4.asignado_a = extensions[3]
            diseño.append(bloque4)

            max_criterios, letrados_que_cumplen = Conocimiento_de_proposicion.check_criteria(extensions, preferencias, diseño_esqueletal, diseño, let_probados, bloque2)

            if max_criterios == -1:
                return -1, diseño

            letrado_propuesto = Conocimiento_de_proposicion.elegir_letrado(max_criterios, letrados_que_cumplen, diseño, cuotas, bloque2)

            sig_bloque.asignado_a = letrado_propuesto

            diseño.append(sig_bloque)
            return sig_bloque, diseño