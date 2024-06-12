class Restriccion():
    def __init__(self, letrado):
        self.letrado = letrado
    
class DISPONIBILIDAD(Restriccion):
    def __init__(self, letrado, dias_de_baja):
        super().__init__(letrado)
        self.dias_de_baja = dias_de_baja        
    
    