

import tkinter as tk
from tkinter import messagebox
from Empleado import Empleado

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Salario")
        self.root.geometry("350x400")

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz gráfica"""
        tk.Label(self.root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        tk.Label(self.root, text="Horas Normales:").pack()
        self.entry_horas_normales = tk.Entry(self.root)
        self.entry_horas_normales.pack()

        tk.Label(self.root, text="Horas Extras:").pack()
        self.entry_horas_extras = tk.Entry(self.root)
        self.entry_horas_extras.pack()

        tk.Label(self.root, text="Número de Hijos:").pack()
        self.entry_hijos = tk.Entry(self.root)
        self.entry_hijos.pack()

        tk.Label(self.root, text="Pago por Hora:").pack()
        self.entry_pago_hora = tk.Entry(self.root)
        self.entry_pago_hora.pack()

        tk.Button(self.root, text="Calcular", command=self.calcular_salario).pack(pady=10)

        self.result_label = tk.Label(self.root, text="", fg="blue")
        self.result_label.pack(pady=10)

    def calcular_salario(self):
        
        try:
            nombre = self.entry_nombre.get()
            horas_normales = int(self.entry_horas_normales.get())
            horas_extras = int(self.entry_horas_extras.get())
            hijos = int(self.entry_hijos.get())
            pago_hora = float(self.entry_pago_hora.get())

            empleado = Empleado(nombre, horas_normales, horas_extras, hijos, pago_hora)

            resultado = (
                f"Empleado: {empleado.nombre}\n"
                f"Pago Horas Normales: {empleado.calcular_monto_horas_normales():.2f}\n"
                f"Pago Horas Extras: {empleado.calcular_monto_horas_extras():.2f}\n"
                f"Bonificación por Hijos: {empleado.calcular_bonificacion():.2f}\n"
                f"Pago Total: {empleado.calcular_pago_total():.2f}"
            )

            self.result_label.config(text=resultado)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

