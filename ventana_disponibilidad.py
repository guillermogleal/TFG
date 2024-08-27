from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class Ventana_disponibilidad(tk.Frame):

    def __init__(self, controlador):
        super().__init__(controlador.root)

        self.controlador = controlador
        self.pack()

        self.message = tk.Message(self, text="Añada los periodos de no disponibilidad para los letrados que correspondan:", width=350)
        self.message.pack(side="top",pady=5)

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=50)
        self.listbox.pack(pady=10)

        self.message = tk.Message(self, text="Fecha de inicio de la baja:", width=350)
        self.message.pack(pady=5)

        self.calendarioIn = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
        self.calendarioIn.pack(pady=10)

        self.message = tk.Message(self, text="Fecha fin de la baja:", width=350)
        self.message.pack(pady=5)

        self.calendarioFin = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
        self.calendarioFin.pack(pady=10)

        self.parcial = tk.BooleanVar()

# Crear un widget Checkbutton
        checkbox = tk.Checkbutton(self, text="baja parcial", variable=self.parcial)
        checkbox.pack(pady=10)

        self.listboxBajas = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=50)
        self.listboxBajas.pack(pady=10)

        botonAdd = tk.Button(self, text="Añadir", command=self.añadir_baja)
        botonAdd.pack(side= "left", pady=10)

        self.calendarioIn.bind("<<DateEntrySelected>>", self.actualizar_fecha_fin)

        # Insertar ítems en el Listbox
        items = self.controlador.plantilla
        for item in items:
            self.listbox.insert(tk.END, item)
        valores = self.listbox.get(0, tk.END)
        # Crear un botón para obtener la selección
        boton = tk.Button(self, text="Eliminar Selección", command=self.eliminar_seleccion)
        boton.pack(pady=10)

        botonNext = tk.Button(self, text="Siguiente", command= lambda: self.controlador.ventana_disponibilidad_but_siguiente(self.listboxBajas.get(0, tk.END)))
        botonNext.pack(pady=10)

    def actualizar_fecha_fin(self, event):
        fecha_in = self.calendarioIn.get_date()
        self.calendarioFin.set_date(fecha_in)


    def eliminar_seleccion(self):
        seleccion = self.listboxBajas.curselection()
        if seleccion:
            index = seleccion[0]
            self.listboxBajas.delete(index)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó un elemento.")

    def añadir(self):
        item = self.entrada.get()
        self.listbox.insert(tk.END, item)
    
    def añadir_baja(self):
        seleccionletrado = self.listbox.curselection()
        if seleccionletrado:
            index = seleccionletrado[0]
            letrado = self.listbox.get(index)

            fecha_in = self.calendarioIn.get_date()
            fecha_fin = self.calendarioFin.get_date()

            if fecha_fin > fecha_in:
                if self.parcial.get():
                    isParcial = "Parcial"
                else:
                    isParcial = "No Parcial"

                self.listboxBajas.insert(tk.END, letrado.split(',')[0] + ", " + fecha_in.strftime("%d/%m/%Y") + " - " + fecha_fin.strftime("%d/%m/%Y") + ", " + isParcial)
            elif fecha_fin == fecha_in:
                if self.parcial.get():
                    isParcial = "Parcial"
                else:
                    isParcial = "No Parcial"
                self.listboxBajas.insert(tk.END, letrado.split(',')[0] + ", " + fecha_in.strftime("%d/%m/%Y") + ", " + isParcial)
            else:
                messagebox.showwarning("Advertencia", "la fecha final es anterior a la inicial")

        else:
            messagebox.showwarning("Advertencia", "No se seleccionó un letrado.")

        


