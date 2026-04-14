def ingresar_numero_entero(texto):
    numero = 0
    while True:
        try:
            numero = int(input(texto))
            break
        except:
            print("¡Error, no se ingresó correctamente el número entero!")
    return numero
