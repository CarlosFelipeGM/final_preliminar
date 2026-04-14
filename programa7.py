def funcion():
    try:
        num1 = int(input("Ingrese el primero número: "))
        num2 = int(input("Ingrese el segundo número: "))
        
        resultado = num1 / num2
    except ValueError:
        print("Error, debe ingresar números enteros")
    except ZeroDivisionError:
        print("Error, no se puede dividir entre cero")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Finalizó la aplicación")
    
funcion()
