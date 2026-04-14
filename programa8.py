def sumar(numero1, numero2): return numero1 + numero2
def restar(numero1, numero2): return numero1 - numero2
def multiplicar(numero1, numero2): return numero1 * numero2

def dividir(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return "Error, no se puede dividir entre cero"

def capturar_datos():
    while True:
        try:
            numero1 = int(input("Ingrese el primero número: "))
            numero2 = int(input("Ingrese el segundo número: "))
            # devuelvo los datos como una tupla
            return numero1, numero2
        except ValueError:
            print("Error, debe ingresar números enteros !")

def capturar_operacion():
    while True:
        print("Operaciones permitidas: Sumar (S), Restar (R), Multiplicar (M), Dividir (D)")
        operacion = input("Ingrese la operación a realizar: ").strip().upper()
        if operacion in ['S', 'R', 'M', 'D']:
            return operacion
        print("Error, operación no permitida !")

# programa principal
numero1, numero2 = capturar_datos()
operaciones = {'S': sumar, 'R': restar, 'M': multiplicar, 'D': dividir}
operacion = capturar_operacion()
resultado = operaciones[operacion](numero1, numero2)
print(f"Resultado: {resultado}")
