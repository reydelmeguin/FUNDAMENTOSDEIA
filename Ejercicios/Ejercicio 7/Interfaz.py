
import tkinter as tk
from Suma import Suma  

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Sumador de Números")
        self.root.geometry("300x280")  

        self.setup_ui()  

    def setup_ui(self):
        """Configura la interfaz gráfica."""

        
        self.label = tk.Label(self.root, text="Ingrese un número entero positivo:")
        self.label.pack(pady=10)

        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        
        self.button = tk.Button(self.root, text="Calcular", command=self.on_calcular)
        self.button.pack(pady=10)

        
        self.result_label = tk.Label(self.root, text="Suma: ", fg="blue")
        self.result_label.pack(pady=10)

    def on_calcular(self):
        """Función que se ejecuta al presionar el botón."""
        try:
            numero = int(self.entry.get())
            sumador = Suma(numero)
            resultado = sumador.calcular_suma()  

            if resultado is not None:
                self.result_label.config(text=f"Suma: {resultado}", fg="green")
            else:
                self.result_label.config(text="Ingrese un número válido", fg="red")  

            self.entry.delete(0, tk.END)  

        except ValueError:
            self.result_label.config(text="Ingrese un número válido", fg="red")  
            self.entry.delete(0, tk.END)
