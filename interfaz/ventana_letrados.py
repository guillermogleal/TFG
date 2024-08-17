from tkinter import *
import tkinter as tk
from tkinter import messagebox

#se muestra una lista con los letrados almacenados y se puede modificar la lista como se requiera
class Ventana_letrados():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.geometry("400x200")

        self.message = tk.Message(self.ventana, text="Compruebe si es necesario hacer cambios a esta plantilla de letrados (añadir o eliminar letrados):", width=350)
        self.message.pack(side="top",pady=5)

        self.listbox = tk.Listbox(self.ventana, selectmode=tk.SINGLE, height=10, width=50)
        self.listbox.pack(pady=10)

        self.entrada = Entry(self.ventana, width= 40)
        self.entrada.pack(side="left", padx=5)

        botonAdd = tk.Button(self.ventana, text="Añadir", command=self.añadir)
        botonAdd.pack(side= "left", pady=10)

        

       

        # Insertar ítems en el Listbox
        items = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
        for item in items:
            self.listbox.insert(tk.END, item)
        valores = self.listbox.get(0, tk.END)
        # Crear un botón para obtener la selección
        boton = tk.Button(self.ventana, text="Eliminar Selección", command=self.eliminar_seleccion)
        boton.pack(pady=10)

    def eliminar_seleccion(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            self.listbox.delete(index)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó un elemento.")

    def añadir(self):
        item = self.entrada.get()
        self.listbox.insert(tk.END, item)

    def main(self):
        self.ventana.mainloop()


ventanaLetrados= Ventana_letrados()
ventanaLetrados.main()

        

