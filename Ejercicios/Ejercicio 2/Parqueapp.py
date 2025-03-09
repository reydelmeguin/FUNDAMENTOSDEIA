
import tkinter as tk
from tkinter import messagebox
from costo import Costo

class Parqueapp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calcular precio parque")
        
        self.nombre_label = tk.Label(root, text="Nombre")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()
        
        self.edad_label = tk.Label(root, text="Edad")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(root)
        self.edad_entry.pack()
        
        self.costo_button = tk.Button(root, text="Calcular precio", command=self.precio_boleto)
        self.costo_button.pack()
        
    def precio_boleto(self):
        nombre = self.nombre_entry.get()
        
        try:
            edad = float(self.edad_entry.get())
            costo = Costo(nombre, edad)  # Aquí solo pasamos nombre y edad
            
            precio_final = costo.precio_nuevo()  # Calculamos el precio con el descuento
            messagebox.showinfo("Precio del boleto", f"El costo del boleto es: ${precio_final:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa una edad válida")

if __name__ == "__main__":
    root = tk.Tk()
    app = Parqueapp(root)
    root.mainloop()
        
        
