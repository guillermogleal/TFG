#ventana que pide los datos de entrada del programa

from tkinter import *
import tkinter as tk
from tkinter import filedialog

class Ventana_Entrada(tk.Frame):
    
    def __init__(self, controlador):
        super().__init__(controlador.root)

        self.controlador = controlador
        self.pack()

        

        self.message = tk.Message(self, text="Introduzca la ruta del archivo con el LISTADO de juicios, puede usar examinar y seleccionar directamente el archivo:", width=350)
        self.message.grid(row=0, column=0, columnspan=3, pady=10)

        self.entrada = Entry(self, width= 40)
        self.entrada.grid(row=1, column=0,  padx=10,pady=5)

        self.boton = Button(self, text="Examinar", command= lambda: self.obtener_ruta_archivo(self.entrada))
        self.boton.grid(row=1, column=1,  padx=10,pady=5)
                                                                #si no se pone el lambda te hace varias ventanas en una
        self.botonNext = Button(self, text="Siguiente", command= lambda: self.controlador.ventana_entrada_but_siguiente(self.entrada.get()))
        self.botonNext.grid(row=1, column=2,  padx=10,pady=5)

        self.message2 = tk.Message(self, text="Introduzca la ruta del archivo con el REPARTO de juicios que quiera insertar en la base de datos:", width=350)
        self.message2.grid(row=2, column=0, columnspan=3, pady=10)

        self.entrada2 = Entry(self, width= 40)
        self.entrada2.grid(row=3, column=0,  padx=10,pady=5)

        self.boton2 = Button(self, text="Examinar", command= lambda: self.obtener_ruta_archivo(self.entrada2))
        self.boton2.grid(row=3, column=1,  padx=10,pady=5)
                                                                #si no se pone el lambda te hace varias ventanas en una
        self.botonInsertar = Button(self, text="Insertar", command= lambda: self.controlador.ventana_entrada_but_insertar(self.entrada2.get()))
        self.botonInsertar.grid(row=3, column=2,  padx=10,pady=5)
    
    def obtener_ruta_archivo(self, entrada):
            ruta = filedialog.askopenfilename()
            entrada.delete(0, tk.END)
            entrada.insert(0,ruta)
            


        
    

