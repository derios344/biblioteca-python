"SISTEMA DE BIBLIOTEA"
"POR:D3R1OS"

import json

libros=[]

def guardar_libros():
    with open("libros.json", "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)

def cargar_libros():
    global libros
    try:
        with open("libros.json", "r", encoding="utf-8") as archivo:
            libros = json.load(archivo)
    except FileNotFoundError:
        libros = []

def agregar_libros():
    while True:
        nombre = input("Introduzca el nombre del libro: ")
        autor = input("Introduzca el nombre del autor: ")
        año_str = input("introduzca el año de publicaciòn: ")
        print("")

        if nombre == "":
            print("Introduzca un nombre valido")
            continue
        
        if autor == "":
            print ("Introduza el nombre del autor valido")
            continue

        try:
            año = int(año_str)
        except ValueError:
            print("Porfavor introduzca un numero no uan letra intentelo de nuevo")
            continue

        if año < 0:
            print("Intorduzca un número valido")
            continue

        duplicado = any(libro["nombre"].lower() == nombre.lower() for libro in libros)
        if duplicado:
            print("El libro ya existe en la biblioteca")
            continue

        libros.append({"nombre": nombre, "autor": autor, "año": año})
        guardar_libros()
        seguir = input("Desea seguir? S/N")
        if seguir.lower() != "s":
            break


def eliminar_libros():
    global libros

    nombre_b = input("Introduzca el nombre exacto del libro a eliminar: ")
    
    print("")
    
    cantidad_antes = len(libros)
    
    libros = [libro for libro in libros if libro["nombre"].lower() != nombre_b.lower()]
    guardar_libros() 
    
    cantidad_despues = len(libros)

    

    if cantidad_antes == cantidad_despues:
        print("No se encontro ninugn libro con ese nombre")
        print("")
    else:
        print("Se ha borrado con exito el libro")
    


def mostrar_libros():
    if not libros:
        print("No hay libros")
        print("")
    else:
        libros_ordenados = sorted(libros, key=lambda libro: libro["nombre"])

        print("Lista de libros:")
        for i, libro in enumerate(libros_ordenados, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"    Autor: {libro['autor']} - Año: {libro['año']}")
            print("")

def buscar_por_nombre():
    nombre_buscado = input("Introduzca el nombre del libro que quiera enocontrar: ")
    resultado = [libro for libro in libros if libro["nombre"].lower() == nombre_buscado.lower()]
    if resultado:
        for i, libro in enumerate(resultado, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"    Autor: {libro['autor']} - Año: {libro['año']}")
    else:
        print("No existe el libro que buscas en la biblioteca")


def buscar_por_autor():
    autor_buscado = input("Introduzca el nombre del autor que quiera enocontrar: ")
    resultado = [libro for libro in libros if libro["autor"] == autor_buscado]
    if resultado:
        for i, libro in enumerate(resultado, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"    Autor: {libro['autor']} - Año: {libro['año']}")
    else:
        print("No existe el libro que buscas en la biblioteca")

def buscar_por_año():
    año_buscado_str = input("Introduzca el año del libro que quiera enocontrar: ")

    try:
        año_buscado = int(año_buscado_str)
    except ValueError:
        print("Porfavor introduzca un numero no uan letra intentelo de nuevo")
        return
            

    resultado = [libro for libro in libros if libro["año"] == año_buscado]
    if resultado:
        for i, libro in enumerate(resultado, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"    Autor: {libro['autor']} - Año: {libro['año']}")
    else:
        print("No existe el libro que buscas en la biblioteca")

def editar_libro():
    nombre_buscado = input("Introduzca el nombre del libro que quiere editar: ")
    
    indice_encontrado = None
    
    for i, libro in enumerate(libros):
        if libro["nombre"].lower() == nombre_buscado.lower():
            indice_encontrado = i
            break

    if indice_encontrado is None:
        print("No existe el libro que buscas en la biblioteca")
        return

    print(f"Editando: {libros[indice_encontrado]['nombre']}")
    print("Dejá el campo vacío si no querés cambiarlo")
    print("")

    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_año_str = input("Nuevo año: ")

    if nuevo_nombre != "":
        libros[indice_encontrado]["nombre"] = nuevo_nombre

    if nuevo_autor != "":
        libros[indice_encontrado]["autor"] = nuevo_autor

    if nuevo_año_str != "":
        try:
            libros[indice_encontrado]["año"] = int(nuevo_año_str)
        except ValueError:
            print("El año no era válido, se mantuvo el anterior")

    guardar_libros()
    print("Libro actualizado con éxito")

cargar_libros()

while True:
    print("MENU DE BIBLIOTECA")
    print("1- Mostrar libros")
    print("2- Agregar libro")
    print("3- Eliminar libro")
    print("4- Buscar libro por nombre")
    print("5- Buscar libro por autor")
    print("6- Buscar libro por año")
    print("7- Editar libro")
    print("8- Salir")

    opcion = input("Elije una opcion: ")

    if opcion == "1":
        mostrar_libros()
    elif opcion == "2":
        agregar_libros()
    elif opcion == "3":
        eliminar_libros()
    elif opcion == "4":
        buscar_por_nombre()
    elif opcion == "5":
        buscar_por_autor()
    elif opcion == "6":
        buscar_por_año()
    elif opcion == "7":
        editar_libro()
    elif opcion == "8":
        print("Adioos")
        break
    else:
        print("Opcion no valida")
