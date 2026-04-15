from helper import capturar_validar_edad
from helper import capturar_validar_estado_salud

def menu():
    while True:
        print("******************************************")
        print("BIENVENIDOS AL SISTEMA REFUGIO DE ANIMALES")
        print("******************************************")
        print("[1] Registrar animal ...!!!")
        print("[2] Filtrar animales enfermos ...!!!")
        print("[3] Consulta animal por nombre ...!!!")
        print("[4] Listar todos los animales registrados ...!!!")
        print("[5] Salir ...!!!")
        
        # se puede reducir con un diccionario de opciones

        print()
        opcion = input("Ingrese una opción: ")
        print()

        if opcion == "1":
            print("Registrando un animal ...!!!\n")
            registrar_animal()
            print("")
            print("Animal registrado correctamente ...!!!\n")
        elif opcion == "2":
            print("Filtrando animales enfermos ...!!!\n")
            filtrar_animales_enfermos()
            print("")
        elif opcion == "3":
            print("Consultado un animal ...!!!\n")
            consultar_animal()
            print("")
        elif opcion == "4":
            print("Listando animales ...!!!\n")
            listar_animales()
            print("")
        elif opcion == "5":
            print("Saliendo ...!!!\n")
            return
            #break
        else:
            print("La opción ingresada es incorrecta ...!!!")
        
        print()
        input("\nPresione ENTER para continuar...")
            
# simulacion de la base de datos
animales = [
    {
        "nombre" : "FIRULAIS",
        "especie" : "PERRO",
        "edad" : 5,
        "estado_salud" : "SANO"

    },
    {
        "nombre" : "MICHIFUZ",
        "especie" : "GATO",
        "edad" : 3,
        "estado_salud" : "ENFERMO"

    },
]


def registrar_animal():
    # capturamos y validamos datos
    nombre = input("Ingrese el nombre del animal: ").strip().upper()
    especie = input("Ingrese la especie del animal: ").strip().upper()
    edad = capturar_validar_edad()
    estado_salud = capturar_validar_estado_salud()
    #formamos y ejecutamos el registro
    animal = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "estado_salud": estado_salud
    }
    animales.append(animal)

def filtrar_animales_enfermos():
    hay_animales_enfermos = False
    for animal in animales:
        if animal['estado_salud'] == "ENFERMO":
            print(f"Nombre: {animal['nombre']} | Especie: {animal['especie']}")
            hay_animales_enfermos = True
    # Por si no se encuentra ninguno
    if not hay_animales_enfermos:
        print("¡ No existen animales enfermos registrados !")

def consultar_animal():
    encontrado = False
    nombre = input("Ingrese el nombre del animal: ").upper()
    for animal in animales:
        if animal['nombre'] == nombre:
            print(f"Nombre: {animal['nombre']} | Especie: {animal['especie']} | Edad: {animal['edad']} | Estado de salud: {animal['estado_salud']}")
            encontrado = True
    # Por si no se encuentra ninguno
    if not encontrado:
        print(f"¡ No existen animales registrados con el nombre: {nombre}!")

def listar_animales():
    if len(animales) == 0:
        print("No existen animales registrados !")
    else:
        for animal in animales:
            print(f"Nombre: {animal['nombre']} | Especie: {animal['especie']} | Edad: {animal['edad']} | Estado de salud: {animal['estado_salud']}")

menu()
