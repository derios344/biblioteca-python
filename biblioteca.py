"SISTEMA DE BIBLIOTEA"
"POR:D3R1OS"

libros=[]

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

        libros.append({"nombre": nombre, "autor": autor,"año": año})
        seguir = input("Desea seguir? S/N")
        if seguir.lower() != "s":
            break

def eliminar_libros():
    global libros

    nombre_b = input("Introduzca el nombre exacto del libro a eliminar: ")
    
    print("")
    
    cantidad_antes = len(libros)
    
    libros = [libro for libro in libros if libro["nombre"] != nombre_b]
    
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
        print("Lista de libros")
        print("")
        for i, libro in enumerate(libros, start=1):
            print(f"{i}. {libro['nombre']}")
            print(f"    Autor: {libro['autor']} - Año: {libro['año']}")
            print("")


def buscar_por_nombre():
    nombre_buscado = input("Introduzca el nombre del libro que quiera enocontrar: ")
    resultado = [libro for libro in libros if libro["nombre"] == nombre_buscado]
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

while True:
    print("MENU DE BIBLIOTECA")
    print("1- Mostrar libros")
    print("2- Agregar libro")
    print("3- Eliminar libro")
    print("4- Buscar libro por nombre")
    print("5- Buscar libro por autor")
    print("6- Buscar libro por año")
    print("7- Salir")

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
        print("Adioos")
        break
    else:
        print("Opcion no valida")
