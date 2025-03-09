
from datetime import datetime

class Descuento:
    def __init__(self, fecha, monto):
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        self.monto = float(monto)

    def calcular_descuento(self):
        if self.fecha.month == 10: 
            return self.monto * 0.85  
        return self.monto   