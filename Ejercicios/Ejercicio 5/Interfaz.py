

import tkinter as tk
from Validador import Validador

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Número") 
        self.root.geometry("300x200") 
        self.app = Validador()  
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Ingrese un valor entre 0 y 20")
        self.label.pack(pady=10)

       
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

       
        self.button = tk.Button(self.root, text="Validar", command=self.on_validar)
        self.button.pack(pady=10)

    def on_validar(self):
        try:
            
            numero = int(self.entry.get())
            if self.app.validar_numero(numero):
               
                self.label.config(text=f"Número válido ingresado: {numero}", fg="green")
                self.entry.delete(0, tk.END)  
            else:
                
                self.entry.delete(0, tk.END)  
        except ValueError:
            
            self.entry.delete(0, tk.END)  
