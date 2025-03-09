import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Ejercicios")
        self.root.geometry("400x500")

        tk.Label(self.root, text="Seleccione un ejercicio", font=("Arial", 14)).pack(pady=10)

        for i in range(1, 11):
            tk.Button(self.root, text=f"Ejercicio {i}", width=20, command=lambda i=i: self.abrir_ejercicio(i)).pack(pady=5)

    def abrir_ejercicio(self, numero):
        """Ejecuta el script 'main.py' dentro de la carpeta correspondiente usando ruta absoluta y manejando espacios."""
        carpeta = os.path.abspath(f"Ejercicio {numero}")  
        script = os.path.join(carpeta, "main.py")  

        if os.path.exists(script):
            try:
                subprocess.run([sys.executable, script], check=True)  
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"No se pudo ejecutar {script}\n\nError: {str(e)}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()
