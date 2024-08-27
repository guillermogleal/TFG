import ventana_entrada
import ventana_letrados
import ventana_disponibilidad
import productTable
import ventana_entrada_fecha
from servicio_BD import Servicio_BD
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from letrado_BD import Letrado_BD
from letrado import Letrado
from restriccion import *
from metodos_utiles import str_to_datetime
from datetime import datetime
from productTable import main_product_table



class Controlador():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Ventana Principal")
        self.ventanaActual= None
        
        if self.ventanaActual:
            self.ventanaActual.destroy()

        self.ventanaActual = ventana_entrada.Ventana_Entrada(self)
        self.ruta = None
        self.plantilla = None                             #letrados para la tabla
        self.restricciones = None
        self.filas = None
        self.mes = None
        self.año = None

    def ventana_entrada_but_siguiente(self, ruta):
        if ruta != "":
            self.ruta = ruta
            if self.ventanaActual:
                self.ventanaActual.destroy()
            
            self.ventanaActual = ventana_letrados.Ventana_letrados(self)
        else:
            messagebox.showwarning("Advertencia", "No se introdujo ninguna ruta de archivo.")

    def ventana_letrados_but_siguiente(self, valores):
        self.plantilla = valores
        if self.ventanaActual:
            self.ventanaActual.destroy()
            
        self.ventanaActual = ventana_disponibilidad.Ventana_disponibilidad(self)

    def ventana_disponibilidad_but_siguiente(self, valores):
        list_letrados = []
        list_restricciones = []
        self.restricciones = list(valores)
        
        
        for letrado in self.plantilla:
            index = letrado.find(",")
            if index != -1:
                letrado = Letrado(letrado[:index], True)
            else:
                letrado = Letrado(letrado, False)
            list_letrados.append(letrado)

            #son las disponibilidades añadidas por el usuario de un letrado concreto
            restricciones_letrado = list(filter(lambda restric: (restric.split(',')[0] == letrado.nombre) , self.restricciones))

            if restricciones_letrado != []:
                restricciones_letrado_parcial = list(filter(lambda restric: (restric.split(',')[2] == ' Parcial') , restricciones_letrado))
                restricciones_letrado_no_parcial = list(filter(lambda restric: (restric.split(',')[2] == ' No Parcial') , restricciones_letrado))
                list_fechas_parcial = []
                list_fechas_no_parcial = []


                for restriccion in restricciones_letrado_parcial:
                    nombre, fecha, isparcial = restriccion.split(',')
                    if fecha.find("-") == -1:
                        fecha = fecha.strip()
                        dia, mes, año = fecha.split('/')
                        fecha = datetime(int(año), int(mes), int(dia))
                        if fecha not in list_fechas_parcial and fecha.weekday() != 5 and fecha.weekday() != 6:
                            list_fechas_parcial.append(fecha)
                    else:
                        fechaIn, fechaFin = fecha.split('-')
                        fechaIn = fechaIn.strip()
                        
                        diaIn, mes, año = fechaIn.split('/')
                        diaFin = int(fechaFin.split('/')[0])
                        contDia = int(diaIn)
                        while contDia <= diaFin:
                            fecha = datetime(int(año), int(mes), contDia)
                            if fecha not in list_fechas_parcial and fecha.weekday() != 5 and fecha.weekday() != 6:
                                list_fechas_parcial.append(fecha)
                            contDia+=1
                if list_fechas_parcial != []:
                    list_restricciones.append(DISPONIBILIDAD(letrado, list_fechas_parcial, True))

                for restriccion in restricciones_letrado_no_parcial:
                    nombre, fecha, isparcial = restriccion.split(',')
                    if fecha.find("-") == -1:
                        fecha = fecha.strip()
                        dia, mes, año = fecha.split('/')
                        fecha = datetime(int(año), int(mes), int(dia))
                        if fecha not in list_fechas_no_parcial and fecha.weekday() != 5 and fecha.weekday() != 6:
                            list_fechas_no_parcial.append(fecha)
                    else:
                        fechaIn, fechaFin = fecha.split('-')
                        fechaIn = fechaIn.strip()
                        
                        diaIn, mes, año = fechaIn.split('/')
                        diaFin = int(fechaFin.split('/')[0])
                        contDia = int(diaIn)
                        while contDia <= diaFin:
                            fecha = datetime(int(año), int(mes), int(contDia))
                            if fecha not in list_fechas_no_parcial and fecha.weekday() != 5 and fecha.weekday() != 6:
                                list_fechas_no_parcial.append(fecha)
                            contDia+=1
                if list_fechas_no_parcial != []:
                    list_restricciones.append(DISPONIBILIDAD(letrado, list_fechas_no_parcial, False))

        self.restricciones = list_restricciones
        self.plantilla = list_letrados
        if self.ventanaActual:
            self.ventanaActual.destroy()
            
        self.ventanaActual = ventana_entrada_fecha.Ventana_Entrada_Fecha(self)

    
    def ventana_entrada_fecha_but_siguiente(self, mes, año):

        self.mes = mes
        self.año = año

        if controlador.es_fecha_valida(año, mes):
            self.filas = main_product_table([], self.plantilla, self.mes, self.año)

            if self.ventanaActual:
                self.ventanaActual.destroy()
                
            self.ventanaActual = productTable.ProductTable(self, self.filas)
        else:
            messagebox.showwarning("Advertencia", "El mes o año introducidos no son válidos.")
        
     

    
    def es_fecha_valida(self, anio, mes, dia=1):
        try:
            datetime(anio, mes, dia)
            return True
        except ValueError:
            return False

    def obtener_ultima_plantilla(self):
        return Servicio_BD.consultar_BD()[1]
    
    def establecer_plantilla(self, valores):
        list_letrados = []
        for valor in valores:
            index = valor.find(",")
            if index != -1:
                letrado = Letrado_BD(valor[:index], True)
            else:
                letrado = Letrado_BD(valor, False)
            list_letrados.append(letrado)

        Servicio_BD.eliminar_plantilla_BD()
        Servicio_BD.añadir_plantilla(list_letrados)
        let_BD = Servicio_BD.consultar_BD()[1]
        print("")

    def main(self):
        self.root.mainloop()
             
if __name__ == "__main__":
    controlador = Controlador()
    controlador.main()