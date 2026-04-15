def capturar_validar_edad():
    while True:
        try:
            numero = int(input("Ingrese la edad del animal (número entero): "))
            if numero >= 0:
                return numero
            else:
                print("¡Error, La edad no puede ser negativa!")
        except ValueError:
            print("¡Error, solo se permiten números enteros!")
    
def capturar_validar_estado_salud():
    while True:
        print("Estados de salud permitidos: SANO / ENFERMO")
        estado_salud = input("Ingrese el estado de salud del animal: ").strip().upper()
        if estado_salud in ['SANO', 'ENFERMO']:
            return estado_salud
        print("¡Error, estado de salud no contemplado!")