import sqlite3
from helper import ingresar_numero_entero

def menu():
    """
    Muestra el menú principal del sistema y gestiona la navegación entre opciones.
    Opciones disponibles:
        1 - Registrar un nuevo animal.
        2 - Filtrar y mostrar animales con estado de salud 'ENFERMO'.
        3 - Consultar un animal por nombre.
        4 - Listar todos los animales registrados.
        5 - Salir del sistema.
    No retorna ningún valor. El bucle finaliza cuando el usuario elige la opción 5.
    """
    while True:
        print("******************************************")
        print("BIENVENIDOS AL SISTEMA REFUGIO DE ANIMALES")
        print("******************************************")
        print("[1] Registrar animal ...!!!")
        print("[2] Filtrar animales enfermos ...!!!")
        print("[3] Consulta animal por nombre ...!!!")
        print("[4] Listar todos los animales registrados ...!!!")
        print("[5] Salir ...!!!")
        
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
            break
        else:
            print("La opción ingresada es incorrecta ...!!!")
        
        print()
        input("\nPresione ENTER para continuar...")
            

def registrar_animal():
    """
    Solicita al usuario los datos de un animal y los registra en la base de datos.
    Parámetros solicitados:
        - nombre      : Nombre del animal (se convierte a mayúsculas).
        - especie     : Especie del animal (se convierte a mayúsculas).
        - edad        : Edad en años (número entero validado).
        - estado_salud: Estado de salud del animal (se convierte a mayúsculas).
    No retorna ningún valor.
    """
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()
    # capturamos datos
    nombre = input("Ingrese el nombre del animal: ").upper()
    especie = input("Ingrese la especie del animal: ").upper()
    # edad = int(input("Ingrese la edad del animal (número entero en años): "))
    edad = ingresar_numero_entero("Ingrese la edad del animal (número entero en años): ")
    estado_salud = input("Ingrese el estado de salud del animal: ").upper()
    #ejecutamos el registro
    sql = "insert into animal (nombre, especie, edad, estado_salud) values (?, ?, ?, ?)"
    cursor.execute(sql, (nombre, especie, edad, estado_salud))
    conexion.commit()
    # cerramos
    conexion.close()

def filtrar_animales_enfermos():
    """
    Consulta y muestra todos los animales con estado de salud 'ENFERMO'.
    Los resultados se ordenan por especie y luego por nombre, ambos de forma ascendente.
    La información se imprime en formato de tabla con las columnas:
        CODIGO, NOMBRE, ESPECIE, EDAD, ESTADO DE SALUD.
    No retorna ningún valor.
    """
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()
    # armamos la consulta
    cursor.execute("select * from animal where estado_salud='ENFERMO' order by especie asc, nombre asc")
    # cabecera
    print("--------|-----------|-----------|--------|------------------")
    print(" CODIGO |  NOMBRE   |  ESPECIE  |  EDAD  |  ESTADO DE SALUD ")
    print("--------|-----------|-----------|--------|------------------")
    # datos
    for animales in cursor:
        print(f"{animales[0]:^8}|{animales[1]:^11}|{animales[2]:^11}|{animales[3]:^8}|{animales[4]:^12}")
    # cerramos
    conexion.close()

def consultar_animal():
    """
    Solicita un nombre al usuario y muestra los animales que coincidan en la base de datos.
    Parámetros solicitados:
        - nombre: Nombre del animal a buscar (se convierte a mayúsculas).
    La información se imprime en formato de tabla con las columnas:
        CODIGO, NOMBRE, ESPECIE, EDAD, ESTADO DE SALUD.
    No retorna ningún valor.
    """
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del animal a consultar: ").upper()
    sql = "select * from animal where nombre=?"
    cursor.execute(sql, (nombre,))
    resultado = cursor.fetchall()
    # cabecera
    print("--------|-----------|-----------|--------|------------------")
    print(" CODIGO |  NOMBRE   |  ESPECIE  |  EDAD  |  ESTADO DE SALUD ")
    print("--------|-----------|-----------|--------|------------------")
    # datos
    for animales in resultado:
        print(f"{animales[0]:^8}|{animales[1]:^11}|{animales[2]:^11}|{animales[3]:^8}|{animales[4]:^12}")
    # cerramos
    conexion.close()

def listar_animales():
    """
    Consulta y muestra todos los animales registrados en la base de datos.
    La información se imprime en formato de tabla con las columnas:
        CODIGO, NOMBRE, ESPECIE, EDAD, ESTADO DE SALUD.
    No retorna ningún valor.
    """
    conexion = sqlite3.connect("refugio.db")
    cursor = conexion.cursor()
    # armamos la consulta
    sql = "select * from animal"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    # cabecera
    print("--------|-----------|-----------|--------|------------------")
    print(" CODIGO |  NOMBRE   |  ESPECIE  |  EDAD  |  ESTADO DE SALUD ")
    print("--------|-----------|-----------|--------|------------------")
    # datos
    for animales in resultado:
        print(f"{animales[0]:^8}|{animales[1]:^11}|{animales[2]:^11}|{animales[3]:^8}|{animales[4]:^12}")
    # cerramos
    conexion.close()

menu()
