import tkinter as tk
from tkinter import ttk
from metodos_utiles import semanas_totales_en_mes
from datetime import datetime


class ProductTable(tk.Tk):
    def __init__(self, products, **kwargs):
        super().__init__(**kwargs)
        self.products = products
        self.tree = ttk.Treeview(self, columns=("Letrado", "Lunes", "cant0.", "Martes", "cant1.", "Miércoles", "cant2.", "Jueves", "cant3.", "Viernes", "cant4.", "Sábado", "cant5.", "Domingo", "Total sem."), show="headings")
        self.tree.heading("Letrado", text="Letrado")
        self.tree.heading("Lunes", text="Lunes")
        self.tree.heading("cant0.", text="cant.")
        self.tree.heading("Martes", text="Martes")
        self.tree.heading("cant1.", text="cant.")
        self.tree.heading("Miércoles", text="Miércoles")
        self.tree.heading("cant2.", text="cant.")
        self.tree.heading("Jueves", text="Jueves")
        self.tree.heading("cant3.", text="cant.")
        self.tree.heading("Viernes", text="Viernes")
        self.tree.heading("cant4.", text="cant.")
        self.tree.heading("Sábado", text="Sábado")
        self.tree.heading("cant5.", text="cant.")
        self.tree.heading("Domingo", text="Domingo")
        self.tree.heading("Total sem.", text="Total sem.")


        self.tree.column("Letrado", width=150, anchor= "center")
        self.tree.column("Lunes", width=50, anchor= "center")
        self.tree.column("cant0.", width=20, anchor= "center")
        self.tree.column("Martes", width=50, anchor= "center")
        self.tree.column("cant1.", width=20, anchor= "center")
        self.tree.column("Miércoles", width=50, anchor= "center")
        self.tree.column("cant2.", width=20, anchor= "center")
        self.tree.column("Jueves", width=50, anchor= "center")
        self.tree.column("cant3.", width=20, anchor= "center")
        self.tree.column("Viernes", width=50, anchor= "center")
        self.tree.column("cant4.", width=20, anchor= "center")
        self.tree.column("Sábado", width=50, anchor= "center")
        self.tree.column("cant5.", width=20, anchor= "center")
        self.tree.column("Domingo", width=50, anchor= "center")
        self.tree.column("Total sem.", width=30, anchor= "center")


        # Insert sample data into the Treeview
        for product in self.products:
            self.tree.insert("", "end", values=product)
        self.tree.pack(fill="both", expand=True)


def hacer_fila_de_semana(semana, primer_dia, n_columnas, ultimo_dia_registrado, ultimo_dia_mes):
    fila = []
    cont_colum = 1

    fila.append("") #el espacio encima de los letrados

    if semana == 0:
        espacios_hasta_primer_dia = primer_dia*2
        for i in range(espacios_hasta_primer_dia):
            fila.append("")
        cont_colum = espacios_hasta_primer_dia + 1

    while cont_colum < (n_columnas - 1) and ultimo_dia_registrado < ultimo_dia_mes:
        ultimo_dia_registrado = ultimo_dia_registrado + 1
        fila.append(ultimo_dia_registrado)
        fila.append("")
        cont_colum += 2
    
    while cont_colum < (n_columnas - 1): # para la ultima semana
        fila.append("")
        cont_colum += 1
    
    return fila, ultimo_dia_registrado
    
def hacer_fila_de_letrado(letrado, n_columnas, diseño, fila_semana, año, mes):
    fila_letrado = []
    juicios_semana = 0
    cont_juicios_semana = 2

    for n_columna in range(n_columnas):
        
        if n_columna == 0:
            fila_letrado.append(letrado.nombre)
        elif n_columna == (n_columnas-1):
            while cont_juicios_semana < (n_columnas-1):
                if fila_letrado[cont_juicios_semana] != "":
                    juicios_semana += fila_letrado[cont_juicios_semana]

                cont_juicios_semana += 2
            fila_letrado.append(juicios_semana)
        else:

            if fila_semana[n_columna] != "":
                dia = fila_semana[n_columna]
                list_bloque_asig = list(filter(lambda bloque: (bloque.fecha == datetime(año, mes, dia)) and bloque.asignado_a == letrado, diseño))
                
                if list_bloque_asig != []:
                    bloque_asig = list_bloque_asig[0]
                    fila_letrado.append(bloque_asig.juzgado)
                    fila_letrado.append(bloque_asig.cantidad)

                else:
                    fila_letrado.append("")
                    if n_columna != 13:
                        fila_letrado.append("")
            else:
                if len(fila_letrado)<= n_columna:
                    fila_letrado.append("")
    return fila_letrado
                


        

        
    



def main(diseño, letrados):
    filas = []
    
    bloque = diseño[0]                   #se obtiene un bloque cualquiera para conseguir una fecha y conocer el mes y año
    fecha = bloque.fecha

    ultimo_dia_registrado = 0
    n_semanas, primer_dia, dias_mes = semanas_totales_en_mes(fecha.year, fecha.month)
    n_letrados = len(letrados)

    n_filas = (n_letrados + 1) * n_semanas
    n_columnas = 15

    for semana in range(n_semanas) :
        fila_semana, ultimo_dia_registrado = hacer_fila_de_semana(semana, primer_dia, n_columnas, ultimo_dia_registrado, dias_mes)
        filas.append(tuple(fila_semana))

        for letrado in letrados:
            fila_letrado = hacer_fila_de_letrado(letrado, n_columnas, diseño, fila_semana, fecha.year, fecha.month)
            filas.append(tuple(fila_letrado))


    app = ProductTable(filas)
    app.mainloop()   

"""    products = [
            ("1001", "Product A", "Category 1", "$10.99"),
            ("1002", "Product B", "Category 2", "$15.49"),
            ("1003", "Product C", "Category 1", "$8.95"),
            ("1004", "Product D", "Category 3", "$12.99"),
            ("1005", "Product E", "Category 2", "$9.99"),
            ("1006", "Product F", "Category 1", "$7.50"),
            ("1007", "Product G", "Category 3", "$11.25"),
            ("1008", "Product H", "Category 2", "$14.99"),
            ("1009", "Product I", "Category 1", "$6.99"),
            ("1010", "Product J", "Category 3", "$10.00")
        ]"""

    