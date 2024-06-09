class Bloque():
    def __init__(self, cantidad, fecha, juzgado, lista_de_juicios):
        self.cantidad = cantidad
        self.fecha = fecha
        self.juzgado = juzgado
        self.lista_de_juicios = lista_de_juicios
        self.asignado_a = None

bloque1 = Bloque(2, "02/3", "e2", [1,2])
