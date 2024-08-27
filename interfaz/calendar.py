import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendario de Eventos")

        # Crear un calendario
        self.calendar = Calendar(root, selectmode='day', year=2024, month=8, day=1)
        self.calendar.pack(pady=20)

        # Crear un área de texto para mostrar eventos
        self.event_display = tk.Text(root, width=40, height=10)
        self.event_display.pack(pady=10)

        # Campo para entrada de nuevos eventos
        self.event_entry = tk.Entry(root, width=40)
        self.event_entry.pack(pady=10)
        self.event_entry.insert(0, "Descripción del Evento")

        # Botón para añadir un evento
        add_event_button = tk.Button(root, text="Añadir Evento", command=self.add_event)
        add_event_button.pack(pady=5)

        # Botón para mover un evento
        move_event_button = tk.Button(root, text="Mover Evento", command=self.move_event)
        move_event_button.pack(pady=5)

        # Diccionario para almacenar eventos {fecha: [eventos]}
        self.events = {}

    def add_event(self):
        date = self.calendar.get_date()
        event_desc = self.event_entry.get()
        if event_desc:
            if date not in self.events:
                self.events[date] = []
            self.events[date].append(event_desc)
            self.update_event_display()
            self.event_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, ingresa la descripción del evento.")

    def move_event(self):
        date = self.calendar.get_date()
        selected_event = self.get_selected_event()
        if selected_event:
            new_date = tk.simpledialog.askstring("Mover Evento", f"Mover evento '{selected_event}' a la nueva fecha (YYYY-MM-DD):")
            if new_date:
                if date in self.events and selected_event in self.events[date]:
                    self.events[date].remove(selected_event)
                    if new_date not in self.events:
                        self.events[new_date] = []
                    self.events[new_date].append(selected_event)
                    self.update_event_display()
                else:
                    messagebox.showwarning("Evento No Encontrado", "El evento seleccionado no existe en la fecha actual.")
            else:
                messagebox.showwarning("Entrada Vacía", "Por favor, ingresa una fecha válida.")
        else:
            messagebox.showwarning("Selección de Evento", "Por favor, selecciona un evento para mover.")

    def get_selected_event(self):
        try:
            selection_index = self.event_display.curselection()
            if selection_index:
                selected_text = self.event_display.get(selection_index)
                return selected_text.split(" - ", 1)[1]  # Obtiene solo la descripción del evento
            return None
        except:
            return None

    def update_event_display(self):
        self.event_display.delete(1.0, tk.END)
        date = self.calendar.get_date()
        events_for_date = self.events.get(date, [])
        for event in events_for_date:
            self.event_display.insert(tk.END, f"{date} - {event}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()