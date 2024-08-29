from proponer_revisar import *
class Configuracion():
    def __init__(self, requisitos, extensions):
        self.requisitos = requisitos
        self.extensions = extensions
    
    def execute(self):
        diseño, bloques_sin_asignar, restricciones = Proponer_revisar.execute(self.requisitos, self.extensions)
        return diseño, bloques_sin_asignar, restricciones
    
        