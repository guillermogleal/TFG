import tkinter as tk

def agregar_item():
    """Función para agregar un ítem al Listbox desde el Entry."""
    item = entrada.get()
    if item:  # Verifica que el Entry no esté vacío
        listbox.insert(tk.END, item)  # Añade el ítem al final del Listbox
        entrada.delete(0, tk.END)  # Limpia el Entry después de agregar el ítem

# Crear la ventana principal
root = tk.Tk()
root.title("Agregar Ítems al Listbox")

# Crear un widget Entry para ingresar texto
entrada = tk.Entry(root, width=50)
entrada.pack(pady=10)

# Crear un widget Listbox para mostrar los ítems
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Crear un botón para agregar el texto del Entry al Listbox
boton = tk.Button(root, text="Agregar Ítem", command=agregar_item)
boton.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()