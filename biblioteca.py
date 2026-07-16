"""
Sistema de Biblioteca

Autor: D3R1OS

Descripción:
Programa de gestión de una biblioteca en consola.
Permite agregar, eliminar, editar, buscar y mostrar libros.
Los datos se almacenan de forma permanente en un archivo JSON.
"""

import json

libros = []


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
        nombre = input("Introduzca el nombre del libro: ").strip()
        autor = input("Introduzca el nombre del autor: ").strip()
        año_str = input("Introduzca el año de publicación: ").strip()
        print()

        if nombre == "":
            print("Introduzca un nombre válido.")
            continue

        if autor == "":
            print("Introduzca un nombre de autor válido.")
            continue

        try:
            año = int(año_str)
        except ValueError:
            print("Por favor, introduzca un número, no una letra. Inténtelo de nuevo.")
            continue

        if año < 0:
            print("Introduzca un número válido.")
            continue

        duplicado = any(
            libro["nombre"].lower() == nombre.lower()
            for libro in libros
        )

        if duplicado:
            print("El libro ya existe en la biblioteca.")
            continue

        libros.append({
            "nombre": nombre,
            "autor": autor,
            "año": año
        })

        guardar_libros()

        seguir = input("¿Desea agregar otro libro? (S/N): ")
        if seguir.lower() != "s":
            break


def eliminar_libros():
    global libros

    nombre_buscado = input(
        "Introduzca el nombre exacto del libro que desea eliminar: "
    )

    print()

    cantidad_antes = len(libros)

    libros = [
        libro
        for libro in libros
        if libro["nombre"].lower() != nombre_buscado.lower()
    ]

    guardar_libros()

    cantidad_despues = len(libros)

    if cantidad_antes == cantidad_despues:
        print("No se encontró ningún libro con ese nombre.")
        print()
    else:
        print("Se ha eliminado el libro con éxito.")
        print()


def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
        print()
        return

    libros_ordenados = sorted(libros, key=lambda libro: libro["nombre"].lower())

    print("Lista de libros:")
    print()

    for i, libro in enumerate(libros_ordenados, start=1):
        print(f"{i}. {libro['nombre']}")
        print(f"   Autor: {libro['autor']} - Año: {libro['año']}")
        print()


def buscar_por_nombre():
    nombre_buscado = input(
        "Introduzca el nombre del libro que desea encontrar: "
    )

    resultado = [
        libro
        for libro in libros
        if libro["nombre"].lower() == nombre_buscado.lower()
    ]

    if resultado:
        for i, libro in enumerate(resultado, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"   Autor: {libro['autor']} - Año: {libro['año']}")
            print()
    else:
        print("No existe un libro con ese nombre en la biblioteca.")
        print()


def buscar_por_autor():
    autor_buscado = input(
        "Introduzca el nombre del autor que desea encontrar: "
    )

    resultado = [
        libro
        for libro in libros
        if libro["autor"].lower() == autor_buscado.lower()
    ]

    if resultado:
        for i, libro in enumerate(resultado, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"   Autor: {libro['autor']} - Año: {libro['año']}")
            print()
    else:
        print("No existen libros de ese autor en la biblioteca.")
        print()


def buscar_por_año():
    año_buscado_str = input(
        "Introduzca el año del libro que desea encontrar: "
    )

    try:
        año_buscado = int(año_buscado_str)
    except ValueError:
        print("Por favor, introduzca un número, no una letra. Inténtelo de nuevo.")
        return

    resultado = [
        libro
        for libro in libros
        if libro["año"] == año_buscado
    ]

    if resultado:
        for i, libro in enumerate(resultado, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"   Autor: {libro['autor']} - Año: {libro['año']}")
            print()
    else:
        print("No existen libros publicados en ese año.")
        print()


def editar_libro():
    nombre_buscado = input(
        "Introduzca el nombre del libro que desea editar: "
    )

    indice_encontrado = None

    for i, libro in enumerate(libros):
        if libro["nombre"].lower() == nombre_buscado.lower():
            indice_encontrado = i
            break

    if indice_encontrado is None:
        print("No existe un libro con ese nombre en la biblioteca.")
        return

    print()
    print(f"Editando: {libros[indice_encontrado]['nombre']}")
    print("Deje el campo vacío si no desea modificar ese dato.")
    print()

    nuevo_nombre = input("Nuevo nombre: ").strip()
    nuevo_autor = input("Nuevo autor: ").strip()
    nuevo_año_str = input("Nuevo año de publicación: ").strip()

    if nuevo_nombre != "":
        duplicado = any(
            libro["nombre"].lower() == nuevo_nombre.lower()
            and i != indice_encontrado
            for i, libro in enumerate(libros)
        )

        if duplicado:
            print("Ya existe otro libro con ese nombre.")
            return

        libros[indice_encontrado]["nombre"] = nuevo_nombre

    if nuevo_autor != "":
        libros[indice_encontrado]["autor"] = nuevo_autor

    if nuevo_año_str != "":
        try:
            nuevo_año = int(nuevo_año_str)

            if nuevo_año < 0:
                print("El año debe ser un número positivo.")
            else:
                libros[indice_encontrado]["año"] = nuevo_año

        except ValueError:
            print("El año introducido no es válido. Se conservará el anterior.")

    guardar_libros()
    print("Libro actualizado con éxito.")
    print()


cargar_libros()

while True:
    print("MENÚ DE BIBLIOTECA")
    print("1 - Mostrar libros")
    print("2 - Agregar libro")
    print("3 - Eliminar libro")
    print("4 - Buscar libro por nombre")
    print("5 - Buscar libro por autor")
    print("6 - Buscar libro por año")
    print("7 - Editar libro")
    print("8 - Salir")

    opcion = input("Elija una opción: ")

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
        print("¡Adiós!")
        break
    else:
        print("Opción no válida.")
        print()