#ventana que pide los datos de entrada del programa

from tkinter import *
import tkinter as tk
from tkinter import filedialog

class Ventana_Entrada(tk.Frame):
    
    def __init__(self, controlador):
        super().__init__(controlador.root)

        self.controlador = controlador
        self.pack()

        

        self.message = tk.Message(self, text="Introduzca la ruta del archivo con el listado de juicios, puede usar examinar y seleccionar directamente el archivo:", width=350)
        self.message.pack(side="top",pady=5)

        self.entrada = Entry(self, width= 40)
        self.entrada.pack(side="left", padx=5)

        self.boton = Button(self, text="Examinar", command=self.obtener_ruta_archivo)
        self.boton.pack(side= "left", padx= 5)
                                                                #si no se pone el lambda te hace varias ventanas en una
        self.botonNext = Button(self, text="Siguiente", command= lambda: self.controlador.ventana_entrada_but_siguiente(self.entrada.get()))
        self.botonNext.pack(side= "right", padx= 5)
    
    def obtener_ruta_archivo(self):
            ruta = filedialog.askopenfilename()
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0,ruta)
            


        
    

