
import tkinter as tk
from Validador import Validador  

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Números")  
        self.root.geometry("300x250") 
        self.app = Validador()  
        self.setup_ui()

    def setup_ui(self):
       
        self.label = tk.Label(self.root, text="Ingrese cualquier número")
        self.label.pack(pady=10)

        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

      
        self.button = tk.Button(self.root, text="Ingresar", command=self.on_validar)
        self.button.pack(pady=10)

       
        self.contador_label = tk.Label(self.root, text="Números ingresados: 0", fg="blue")
        self.contador_label.pack(pady=10)

    def on_validar(self):
        try:
            numero = float(self.entry.get())  
            total_numeros = self.app.registrar_numero(numero)  

         
            self.label.config(text=f"Número ingresado: {numero}", fg="green")
            self.contador_label.config(text=f"Números ingresados: {total_numeros}")  
            self.entry.delete(0, tk.END)  
        except ValueError:
           
            self.entry.delete(0, tk.END)  
