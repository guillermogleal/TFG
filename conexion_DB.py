from bloque_BD import *

class Conexion_BD:

    engine = None
    Session = None

    def inicializar(database_name):
        Conexion_BD.engine = create_engine(f'sqlite:///{database_name}')
        Base.metadata.create_all(Conexion_BD.engine)
        Conexion_BD.Session = scoped_session(sessionmaker(bind=Conexion_BD.engine))

    def conexion_BD():
        #la crea en caso de que no exista
        Base.metadata.create_all(Conexion_BD.engine)
    
    def eliminar_BD():
        Base.metadata.tables['bloque_BD'].drop(Conexion_BD.engine, checkfirst= True)
    
    def obtener_sesion():
        Conexion_BD.inicializar('base_de_datos')
        return Conexion_BD.Session()

#Conexion_BD.obtener_sesion()