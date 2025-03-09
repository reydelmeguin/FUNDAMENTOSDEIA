
class Validador:
    def __init__(self):
        self.contador = 0  

    def registrar_numero(self, numero):
        """Cada vez que mete un número correcto, incrementa el contador."""
        self.contador += 1  
        return self.contador  
