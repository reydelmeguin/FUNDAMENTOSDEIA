import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def graficar_funcion():
    try:
        m = float(entry_m.get())
        b = float(entry_b.get())
        
        # Crear la figura de matplotlib
        fig, ax = plt.subplots(figsize=(5, 4))
        x = np.linspace(-10, 10, 400)
        y = m * x + b
        
        ax.plot(x, y, label=f"f(x) = {m}x + {b}", color='blue')
        ax.set_title("Gráfica de la función lineal")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.legend()
        
        # Limpiar el área anterior (si existe)
        for widget in frame_grafica.winfo_children():
            widget.destroy()
        
        # Integrar la gráfica en la interfaz de tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos para m y b.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Funciones Lineales")
root.geometry("600x500")

# Frame para controles (m, b, botón)
frame_controles = tk.Frame(root)
frame_controles.pack(pady=10)

tk.Label(frame_controles, text="Pendiente (m):").grid(row=0, column=0, padx=5, pady=5)
entry_m = tk.Entry(frame_controles)
entry_m.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_controles, text="Término (b):").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_controles)
entry_b.grid(row=1, column=1, padx=5, pady=5)

boton_graficar = tk.Button(frame_controles, text="Generar Gráfica", command=graficar_funcion)
boton_graficar.grid(row=2, columnspan=2, pady=10)

# Frame para la gráfica
frame_grafica = tk.Frame(root)
frame_grafica.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()