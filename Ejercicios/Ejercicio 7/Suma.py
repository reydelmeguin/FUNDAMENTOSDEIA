
class Suma:
    def __init__(self, numero):
        self.numero = numero  

    def calcular_suma(self):
        """Calcula la suma de los primeros 'n' números enteros positivos."""
        suma = 0
        for i in range(1, self.numero + 1):  
            suma += i
        return suma  

    def numero_nuevo(self):
        """Llama a la función de suma y devuelve el resultado."""
        return self.calcular_suma()
