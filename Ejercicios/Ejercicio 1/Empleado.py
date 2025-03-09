
class Empleado:
    def __init__(self,nombre,salario_base):
        self.nombre=nombre
        self.salario_base=salario_base
        
    def calcular_salario(self):
        if self.salario_base<4000:
            return self.salario_base*0.15
        
        else:
            return self.salario_base*0.08
    
    def nuevo_salario(self):
        return self.salario_base+self.calcular_salario()
        
        
        
