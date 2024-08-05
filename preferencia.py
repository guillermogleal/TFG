class Preferencia():
    def __init__(self, letrado):
        self.letrado = letrado
    
class NO_JUZGADO(Preferencia):
    def __init__(self, letrado, juzgado):
        super().__init__(letrado)
        self.juzgado = juzgado  