from conocimiento_de_verificacion import *

class Verificar():

    def metodo(extension, restricciones, diseño):

        valid = not Conocimiento_de_verificacion.check_criteria(extension, restricciones, diseño)
        return valid, extension