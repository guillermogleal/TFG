from especificar import *

class Proponer_revisar():
    def execute( requisitos, extensions):
        diseño_esqueletal = especificar.metodo(requisitos)
        """
        restricciones, preferencias = operacionalizar(requisitos)
        
        #while
        extension, diseño = proponer.metodo(extensions, preferencias, diseño)
        valor, violacion = verificar.metodo(extension, restricciones, diseño)
        list_acciones = criticar.metodo(violacion, diseño)
        accion = seleccionar.metodo(list_acciones)
        diseño = modificar.metodo(diseño, accion)"""
        return diseño_esqueletal