import tkinter as tk

class Controlador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana Principal")
        self.ventana_actual = None
        self.mostrar_ventana_principal()

    def mostrar_ventana_principal(self):
        # Si ya hay una ventana abierta, la destruimos
        if self.ventana_actual:
            self.ventana_actual.destroy()

        # Crear la ventana principal
        self.ventana_actual = VentanaPrincipal(self)

    def mostrar_ventana_secundaria(self, argumento):
        if self.ventana_actual is not None:
            self.ventana_actual.destroy()

        self.ventana_actual = VentanaSecundaria(self, argumento)
        self.ventana_actual.pack(fill="both", expand=True)
    def iniciar(self):
        self.root.mainloop()

#### 2. **Ventana Principal (`VentanaPrincipal`)**

class VentanaPrincipal(tk.Frame):
    def __init__(self, controlador):
        super().__init__(controlador.root)
        self.controlador = controlador
        self.pack()

        label = tk.Label(self, text="Esta es la Ventana Principal")
        label.pack(pady=20)

        boton = tk.Button(self, text="Ir a la Ventana Secundaria", command=lambda: self.controlador.mostrar_ventana_secundaria("¡Hola!"))
        boton.pack()

#### 3. **Ventana Secundaria (`VentanaSecundaria`)**

class VentanaSecundaria(tk.Frame):
    def __init__(self, controlador, argumento):
        super().__init__(controlador.root)
        self.controlador = controlador

        label = tk.Label(self, text=f"Ventana Secundaria - Recibido: {argumento}")
        label.pack(pady=20)

        boton = tk.Button(self, text="Volver a la Ventana Principal", command=self.controlador.mostrar_ventana_principal)
        boton.pack()

#### 4. **Ejecución de la Aplicación**


if __name__ == "__main__":
    app = Controlador()
    app.iniciar()