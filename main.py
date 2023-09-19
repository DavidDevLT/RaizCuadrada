from logica.RaizCuadrada import OperacionMatematica

if __name__ == '__main__':
    print("BIENVENIDO\n")
    operacion = OperacionMatematica(0)
    operacion.ingresar_datos()
    result = operacion.calcular()
    operacion.imprimir_resultado(result)
