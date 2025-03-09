
class suma100:
    def __init__(self):
        self.total = 0  

    def agregar_numero(self, numero):
        
        self.total += numero  
        return self.total  

    def ha_superado_limite(self):
        
        return self.total > 100
