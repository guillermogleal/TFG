#ventana que pide los datos de entrada del programa

from tkinter import *
import tkinter as tk
from tkinter import filedialog

class Ventana_Entrada():
    
    def __init__(self) -> None:
        self.ventana = Tk()

        self.ventana.geometry("400x100")

        self.message = tk.Message(self.ventana, text="Introduzca la ruta del archivo con el listado de juicios, puede usar examinar y seleccionar directamente el archivo:", width=350)
        self.message.pack(side="top",pady=5)

        self.entrada = Entry(self.ventana, width= 40)
        self.entrada.pack(side="left", padx=5)

        self.boton = Button(self.ventana, text="Examinar", command=self.obtener_ruta_archivo)
        self.boton.pack(side= "left", padx= 5)

        self.botonNext = Button(self.ventana, text="Siguiente")
        self.botonNext.pack(side= "right", padx= 5)
    
    def obtener_ruta_archivo(self):
        ruta = filedialog.askopenfilename()
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0,ruta)

    def main(self):
        self.ventana.mainloop()
    

ventanaEntrada = Ventana_Entrada()
ventanaEntrada.main()