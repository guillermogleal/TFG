import pandas as pd
import pandas_read_xml as pdx
from hermetrics.levenshtein import Levenshtein 
import math

def buscar_primera_fila(datos_excel, lev):
    cont=0
    while lev.similarity(str(datos_excel.iloc[cont, 0]), "Fecha") < 0.55  and cont!=datos_excel.shape[0]:
        cont=cont+1
        
    
    return cont

def identificar_juzgado(juzgado, lev):
    if juzgado == 'J SOC. 3 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'C3'
    elif juzgado == 'J SOC. 7 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C7'
    elif juzgado == 'J SOC. 1 A CORUÑA FERROL (CAPITAL)':
        return 'F1'
    elif juzgado == 'J SOC. 1 FERROL (CAPITAL) CORUÑA, A':
        return 'F1'
    elif juzgado == 'J SOC. 2 A CORUÑA SANTIAGO DE COMPOSTELA (CAPITAL)':
        return 'S2'
    elif juzgado == 'J SOC. 1 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C1'
    elif juzgado == 'J SOC. 4 CORUÑA (A) (CAPITAL) A CORUÑA':
        return 'C4'
    elif juzgado == 'J SOC. 4 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C4'
    elif juzgado == 'J SOC. 6 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C6'
    elif juzgado == 'J SOC. 94 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'R'
    elif juzgado == 'J SOC. 94 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'R'
    elif juzgado == 'J SOC. 2 A CORUÑA FERROL (CAPITAL)':
        return 'F2'
    elif juzgado == 'J SOC. 3 A CORUÑA SANTIAGO DE COMPOSTELA (CAPITAL)':
        return 'S3'
    elif juzgado == 'J SOC. 2 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C2'
    elif juzgado == 'J SOC. 3 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C3'
    elif juzgado == 'J SOC. 93 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'R'
    elif juzgado == 'J SOC. 5 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'C5'
    elif juzgado == 'J SOC. 1 A CORUÑA SANTIAGO DE COMPOSTELA (CAPITAL)':
        return 'S1'
    elif juzgado == 'J SOC. 4 A CORUÑA SANTIAGO DE COMPOSTELA (CAPITAL)':
        return 'S4'
    elif juzgado == 'J SOC. 4 CORUÑA, A CORUÑA (A) (CAPITAL)':
        return 'C4'
    elif juzgado == 'J SOC. 93 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'R'
    elif juzgado == 'J SOC. 4 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'C4'
    elif juzgado == 'J SOC. 2 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'C2'
    elif juzgado == 'J SOC. 1 FERROL (CAPITAL) A CORUÑA':
        return 'F1'
    elif juzgado == 'J SOC. 2 FERROL (CAPITAL) CORUÑA, A':
        return 'F2'
    elif juzgado == 'J SOC. 992 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'R'
    elif juzgado == 'J SOC. 92 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'R'
    elif juzgado == 'J SOC. 1 CORUÑA (A) (CAPITAL) CORUÑA, A':
        return 'C1'
    elif juzgado == 'J CA 1 A CORUÑA CORUÑA (A) (CAPITAL)':
        return 'CA1C'
    elif juzgado == 'J SOC. 1 SANTIAGO DE COMPOSTELA (CAPITAL) CORUÑA, A':
        return 'S1'
    return 'juzgado desconocido'

#instancias
lev=Levenshtein()
# Ruta al archivo Excel
ruta_archivo = 'C:/Users/gonza/Desktop/uni/TFG/junio/Listado juicios JUNIO.xlsx'

# Leer el archivo Excel en un DataFrame de pandas
datos_excel = pd.read_excel(ruta_archivo)
filas, columnas = datos_excel.shape
cont_fila= 0
cont_col= 0
# Mostrar los primeros registros del DataFrame

#lista_de_fechas = datos_excel['Unnamed: 0']
#lista_de_juzgados = datos_excel['Unnamed: 1']

cont_fila = buscar_primera_fila(datos_excel,lev)
cont_fila = cont_fila + 1
fecha_act = datos_excel.iloc[cont_fila, 0]
celda_act = fecha_act
juzgado_act = ''
num_juicios = 0
letrados_con_juicios = []
n_juicios = []
num_juicios_total = 0
while cont_fila < filas-1:
    print(fecha_act+":")

    while  celda_act == fecha_act or type(celda_act) == float:
        if type(celda_act) == str:
                 

            juzgado=identificar_juzgado(datos_excel.iloc[cont_fila, 1], lev)
            if juzgado != juzgado_act:
                if num_juicios != 0:
                    print(str(num_juicios),end="")
                    print("   ",end="")
                    print(letrados_con_juicios, end="")
                    print(n_juicios)
                juzgado_act = juzgado
                print(juzgado_act+"|", end='')
                num_juicios_total=num_juicios_total+num_juicios
                num_juicios = 0
                letrados_con_juicios = []
                n_juicios = []
            
            letrado = datos_excel.iloc[cont_fila, 18]
            if type(letrado) == str:
                if letrado in letrados_con_juicios:
                    num_letrado=letrados_con_juicios.index(letrado)
                    n_juicios[num_letrado]= n_juicios[num_letrado] + 1
                else:
                    letrados_con_juicios.append(letrado)
                    n_juicios.append(1)

            
            num_juicios=num_juicios+1
            

        cont_fila = cont_fila + 1
        celda_act = datos_excel.iloc[cont_fila, 0]
    print(str(num_juicios), end="")
    print("   ", end='')
    print(letrados_con_juicios,end="")
    print(n_juicios)
    juzgado_act = ''
    fecha_act = celda_act
    num_juicios_total = num_juicios_total + num_juicios
    num_juicios = 0
print("Juicios totales: "+str(num_juicios_total))

#print(buscar_primera_fila(datos_excel,lev))