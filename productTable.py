import tkinter as tk
from tkinter import ttk
from metodos_utiles import semanas_totales_en_mes
from datetime import datetime


class ProductTable(tk.Frame):
    def __init__(self, controlador, products, **kwargs):
        super().__init__(controlador.root,**kwargs)
        
        self.controlador = controlador
        self.pack(fill="both", expand=True)

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

        self.tree.bind("<Double-1>", lambda event: self.onDoubleClick(event))

        self.tree.tag_configure("highlight", background="lightblue")

        # Insert sample data into the Treeview
        for product in self.products:
            if product[0] == "":
                self.tree.insert("", "end", values=product, tags=("highlight",))
            else:
                self.tree.insert("", "end", values=product)
        self.tree.pack(fill="both", expand=True)

        self.botonNext = tk.Button(self, text="Siguiente", command= lambda: self.controlador.productTable_pre_but_siguiente(self.tree))
        self.botonNext.pack(side= "right", padx= 5)

    def onDoubleClick(self, event):
            '''Executed, when a row is double-clicked'''
            # close previous popups
            try:  # in case there was no previous popup
                self.entryPopup.destroy()
            except AttributeError:
                pass

            # what row and column was clicked on
            rowid = self.tree.identify_row(event.y)
            column = self.tree.identify_column(event.x)

            # return if the header was double clicked
            if not rowid:
                return

            # get cell position and cell dimensions
            x, y, width, height = self.tree.bbox(rowid, column)
            

            # y-axis offset
            pady = height // 2

            # place Entry Widget
            text = self.tree.item(rowid, 'values')[int(column[1:])-1]
            self.entryPopup = EntryPopup(self, rowid, int(column[1:])-1, text)
            self.entryPopup.place(x=x, y=y+pady, width=width, height=height, anchor='w')
    
    def get_column(self, column_name):
        column_values = []
        for id in self.tree.get_children():
            column_values.append(self.tree.item(id, "values")[self.tree["columns"].index(column_name)])
        return column_values
    
    def get_row(self, row_index):
        print("get_children return value: ", self.tree.get_children())
        return self.tree.item(self.tree.get_children()[row_index], "values")

class EntryPopup(ttk.Entry):
    def __init__(self, parent, iid, column, text, **kw):
        super().__init__(parent, **kw)
        self.tv = parent.tree  # reference to parent window's treeview
        self.iid = iid  # row id
        self.column = column 

        self.insert(0, text) 
        self['exportselection'] = False  # Prevents selected text from being copied to  
                                         # clipboard when widget loses focus
        self.focus_force()  # Set focus to the Entry widget
        self.select_all()   # Highlight all text within the entry widget
        self.bind("<Return>", self.on_return) # Enter key bind
        self.bind("<Control-a>", self.select_all) # CTRL + A key bind
        self.bind("<Escape>", lambda *ignore: self.destroy()) # ESC key bind
        
    def on_return(self, event):
        '''Insert text into treeview, and delete the entry popup'''
        rowid = self.tv.focus()  # Find row id of the cell which was clicked
        vals = self.tv.item(rowid, 'values')  # Returns a tuple of all values from the row with id, "rowid"
        vals = list(vals)  # Convert the values to a list so it becomes mutable
        vals[self.column] = self.get()  # Update values with the new text from the entry widget
        self.tv.item(rowid, values=vals)  # Update the Treeview cell with updated row values
        self.destroy()  # Destroy the Entry Widget
        
    def select_all(self, *ignore):
        ''' Set selection on the whole text '''
        self.selection_range(0, 'end')
        return 'break'


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
                    
def main_product_table(diseño, letrados, mes, año):
    filas = []

    ultimo_dia_registrado = 0
    n_semanas, primer_dia, dias_mes = semanas_totales_en_mes(año, mes)
    n_letrados = len(letrados)

    n_filas = (n_letrados + 1) * n_semanas
    n_columnas = 15

    for semana in range(n_semanas) :
        fila_semana, ultimo_dia_registrado = hacer_fila_de_semana(semana, primer_dia, n_columnas, ultimo_dia_registrado, dias_mes)
        filas.append(tuple(fila_semana))

        for letrado in letrados:
            fila_letrado = hacer_fila_de_letrado(letrado, n_columnas, diseño, fila_semana, año, mes)
            filas.append(tuple(fila_letrado))

    return filas
      

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

    