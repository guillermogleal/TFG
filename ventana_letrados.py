from tkinter import *
import tkinter as tk
from tkinter import messagebox

#se muestra una lista con los letrados almacenados y se puede modificar la lista como se requiera
class Ventana_letrados(tk.Frame):

    def __init__(self, controlador):
        super().__init__(controlador.root)

        self.controlador = controlador
        self.pack()
        

        self.message = tk.Message(self, text="Compruebe si es necesario hacer cambios a esta plantilla de letrados (añadir o eliminar letrados):", width=350)
        self.message.pack(side="top",pady=5)

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=50)
        self.listbox.pack(pady=10)

        self.jefe = tk.BooleanVar()

# Crear un widget Checkbutton
        checkbox = tk.Checkbutton(self, text="es jefe", variable=self.jefe)
        checkbox.pack(pady=10)

        self.entrada = Entry(self, width= 40)
        self.entrada.pack(side="left", padx=5)

        botonAdd = tk.Button(self, text="Añadir", command=self.añadir)
        botonAdd.pack(side= "left", pady=10)

        

       

        # Insertar ítems en el Listbox
        items = self.controlador.obtener_ultima_plantilla()
        
        if items != []:
            for item in items:
                if item.jefe:
                    self.listbox.insert(tk.END, item.nombre + ", jefe")
                else:
                    self.listbox.insert(tk.END, item.nombre)

        
        # Crear un botón para obtener la selección
        botonEliminar = tk.Button(self, text="Eliminar Selección", command=self.eliminar_seleccion)
        botonEliminar.pack(pady=10)

        botonPlantilla = tk.Button(self, text="Establecer plantilla", command= lambda: self.controlador.establecer_plantilla(self.listbox.get(0, tk.END)))
        botonPlantilla.pack(pady=10)

        self.botonNext = Button(self, text="Siguiente", command= lambda: self.controlador.ventana_letrados_but_siguiente(self.listbox.get(0, tk.END)))
        self.botonNext.pack(side= "right", padx= 5)



    def eliminar_seleccion(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            self.listbox.delete(index)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó un elemento.")

    def añadir(self):
        item = self.entrada.get()

        if self.jefe.get():
            item = item + ", jefe"

        self.listbox.insert(tk.END, item)





        

