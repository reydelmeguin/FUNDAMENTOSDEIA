
import tkinter as tk
from Sumador import Sumador  

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma Acumulativa")  
        self.root.geometry("300x280")  
        self.sumador = Sumador()  

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz gráfica"""

        
        self.label = tk.Label(self.root, text="Ingrese un número o el0 para terminar:")
        self.label.pack(pady=10)

        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        
        self.button = tk.Button(self.root, text="Agregar", command=self.on_agregar)
        self.button.pack(pady=10)

        
        self.result_label = tk.Label(self.root, text="Suma total: 0", fg="blue")
        self.result_label.pack(pady=10)

    def on_agregar(self):
        """Función que se ejecuta al presionar el botón"""
        try:
            numero = int(self.entry.get())  
            total = self.sumador.agregar_numero(numero)  

            
            if numero == 0:
                self.label.config(text="Fin de la suma. Total final:")
                self.button.config(state=tk.DISABLED)
                self.entry.config(state=tk.DISABLED)

            self.result_label.config(text=f"Suma total: {total}")  
            self.entry.delete(0, tk.END)  

        except ValueError:
            self.result_label.config(text="Ingrese un número válido", fg="red")  
            self.entry.delete(0, tk.END)  
