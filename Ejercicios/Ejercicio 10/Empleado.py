
class Empleado:
    def __init__(self, nombre, horas_normales, horas_extras, hijos, pago_hora):
        self.nombre = nombre
        self.horas_normales = horas_normales
        self.horas_extras = horas_extras
        self.hijos = hijos
        self.pago_hora = pago_hora

    def calcular_monto_horas_normales(self):
        
        return self.horas_normales * self.pago_hora

    def calcular_monto_horas_extras(self):
        
        pago_hora_extra = self.pago_hora * 1.5
        return self.horas_extras * pago_hora_extra

    def calcular_bonificacion(self):
        
        return self.hijos * 0.5

    def calcular_pago_total(self):
    
        return (
            self.calcular_monto_horas_normales()
            + self.calcular_monto_horas_extras()
            + self.calcular_bonificacion()
        )
