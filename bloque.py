class Bloque():
    def __init__(self, cantidad, fecha, juzgado, lista_de_juicios):
        self.cantidad = cantidad
        self.fecha = fecha
        self.juzgado = juzgado
        self.lista_de_juicios = lista_de_juicios
        self.asignado_a = None
        self.partido = 0
        #self.probado = [] #si hay una restriccion que no se cumpla al asignar un letrado a este bloque
                            #se añade el letrado a esta lista en los bloques del diseño
