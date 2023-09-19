class OperacionMatematica:
    def __init__(self, numero):
        self.numero = numero

    def ingresar_datos(self):
        self.numero = float(input("Ingrese número: "))
        return self.numero

    def calcular(self):
        x = self.numero
        a = 1  # inicio de la iteración
        for i in range(1, 10):
            a = (a + (x / a)) / 2
            print(f'La raíz después de {i} iteraciones es: {a} \n')

        return a

    def imprimir_resultado(self, resultado):
        print(f'La raíz cuadrada de {self.numero} es: {resultado}')
