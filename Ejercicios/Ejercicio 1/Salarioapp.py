
import tkinter as tk
from tkinter import messagebox
from Empleado import Empleado

class Salarioapp:
    
    def __init__(self, root):
        self.root=root
        self.root.title("Calculo incremento de salario")
        
        self.nombre_label=tk.Label(root,text="Nombre")
        self.nombre_label.pack()
        self.nombre_entry=tk.Entry(root)
        self.nombre_entry.pack()
        
        self.salario_label=tk.Label(root,text="Salario base")
        self.salario_label.pack()
        self.salario_entry=tk.Entry(root)
        self.salario_entry.pack()
        
        self.Calcular_button=tk.Button(root,text="Calcular incremento",command=self.Calcular_incremento)
        self.Calcular_button.pack()
    
    def Calcular_incremento(self):
        nombre=self.nombre_entry.get()
        salario_base=float(self.salario_entry.get())
        empleado=Empleado(nombre,salario_base)
        incremento=empleado.calcular_salario()
        nuevo_salario=empleado.nuevo_salario()
        messagebox.showinfo("Incremento de Salario",f"Incremento:${incremento:.2f}\nNuevo Salario:${nuevo_salario:.2f}")

if __name__=="__main__":
        root=tk.Tk()
        Salarioapp = Salarioapp(root)
        root.mainloop()
        
        
        
        
        
        
        
        