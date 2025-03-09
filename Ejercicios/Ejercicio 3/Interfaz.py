
import tkinter as tk
from tkinter import messagebox
from tienda import Descuento


class Interfaz:
    def __init__(self, root, enviar_callback):
        self.root = root
        self.root.title("Ingreso de Datos")
        
        tk.Label(root, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        self.fecha_entry = tk.Entry(root)
        self.fecha_entry.pack(pady=5)
        
        tk.Label(root, text="Monto:").pack(pady=5)
        self.monto_entry = tk.Entry(root)
        self.monto_entry.pack(pady=5)
        
        tk.Button(root, text="Enviar", command=self.enviar).pack(pady=20)
        self.enviar_callback = enviar_callback

    def enviar(self):
        fecha = self.fecha_entry.get()
        monto = self.monto_entry.get()
        self.enviar_callback(fecha, monto)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Resultado", mensaje)