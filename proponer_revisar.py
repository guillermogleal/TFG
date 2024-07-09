from especificar import *
from operacionalizar import *
from proponer import *
from verificar import *
from metodos_utiles import get_bajas, get_tipo_restricciones
from modificar import *

class Proponer_revisar():
    def execute( requisitos, extensions):
        let_probados = []
        diseño = []


        requisitos.list_bloques.sort(key= lambda bloque: bloque.cantidad, reverse= True)

        diseño_esqueletal = Especificar.metodo(requisitos)
        
        restricciones, preferencias = Operacionalizar.metodo(requisitos)

        cuotas = get_tipo_restricciones(restricciones, MAX_CUOTA)

        letrado_jefe = list(filter(lambda letrado: letrado.jefe == True, extensions))

        if letrado_jefe:
            extensions.remove(letrado_jefe[0])
            extensions.append(letrado_jefe[0])
            
        
        while len(diseño) < len(diseño_esqueletal) and (len(let_probados) != len(extensions)) :

            extension, diseño = Proponer.metodo(extensions, preferencias, diseño_esqueletal, diseño, let_probados, cuotas)
            
            if extension == -1:
                print("no se pudo proponer más letrados")
                return diseño
            
            valor, violacion = Verificar.metodo(extension, restricciones, diseño)

            if not valor:
                diseño = Modificar.metodo(diseño, violacion)
       
        return diseño