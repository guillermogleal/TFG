class Restriccion():
    def __init__(self, letrado):
        self.letrado = letrado
    
class DISPONIBILIDAD(Restriccion):
    def __init__(self, letrado, dias_de_baja, parcial):
        super().__init__(letrado)
        self.dias_de_baja = dias_de_baja 
        self.parcial = parcial       

class MAX_CUOTA(Restriccion):
    def __init__(self, letrado, cuota):
        super().__init__(letrado)
        self.cuota = cuota

class MAX_CUOTA_FUERA(Restriccion):
    def __init__(self, letrado, cuota):
        super().__init__(letrado)
        self.cuota = cuota