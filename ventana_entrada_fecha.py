from tkinter import *
import tkinter as tk


class Ventana_Entrada_Fecha(tk.Frame):
    
    def __init__(self, controlador):
        super().__init__(controlador.root)

        self.controlador = controlador
        self.pack()

        

        self.message = tk.Message(self, text="Introduzca el número mes y el año del que se desea hacer el reparto en las siguientes entradas respectivamente:", width=350)
        self.message.pack(side="top",pady=5)

        self.message = tk.Message(self, text="Mes (nº del 1 al 12):", width=350)
        self.message.pack(side="top",pady=5)

        self.entrada1 = Entry(self, width= 40)
        self.entrada1.pack(side="left", padx=5)

        self.message = tk.Message(self, text="Año:", width=350)
        self.message.pack(side="top",pady=5)

        self.entrada2 = Entry(self, width= 40)
        self.entrada2.pack(side="left", padx=5)
                                                                #si no se pone el lambda te hace varias ventanas en una
        self.botonNext = Button(self, text="Siguiente", command= lambda: self.controlador.ventana_entrada_fecha_but_siguiente(int(self.entrada1.get()), int(self.entrada2.get())))
        self.botonNext.pack(side= "right", padx= 5)
    