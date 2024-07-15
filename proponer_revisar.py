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
        restricciones = restricciones + requisitos.list_restricciones
       
        cuotas = get_tipo_restricciones(restricciones, MAX_CUOTA)
        cuotas = cuotas + get_tipo_restricciones(restricciones, MAX_CUOTA_FUERA)

        letrado_jefe = list(filter(lambda letrado: letrado.jefe == True, extensions))

        if letrado_jefe:
            extensions.remove(letrado_jefe[0])
            extensions.append(letrado_jefe[0])

        for bloque in diseño_esqueletal:
            if bloque.asignado_a != None:
                diseño.append(bloque)
                
        index_sig_bloque = 0
        while len(diseño) < len(diseño_esqueletal) and (len(let_probados) != len(extensions)) :
            
            extension, diseño = Proponer.metodo(extensions, preferencias, diseño_esqueletal, diseño, let_probados, cuotas, index_sig_bloque)
            
            if extension!= None and extension.cantidad == 4 and extension.juzgado == "R":
                llego =True

            if extension == -1:
                print("no se pudo proponer más letrados")
                return diseño
            
            elif extension == None:
                let_probados=[]
                index_sig_bloque+=1
            
            else:            
                valor, violacion = Verificar.metodo(extension, restricciones, diseño)

                if not valor:
                    diseño = Modificar.metodo(diseño, violacion)
                    let_probados.append(violacion.asignado_a)
                else:
                    let_probados=[]
                    index_sig_bloque+=1
           
        return diseño