
class Costo:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad=edad
        self.precio= 50
        
    def calcular_precio(self):
        if self.edad < 10:
            return self.precio*0.25
        else:
            return 0
        
    def precio_nuevo(self):
        return self.precio-self.calcular_precio()
    