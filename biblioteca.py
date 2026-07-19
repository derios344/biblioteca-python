"""
Sistema de bibloteca

Autor: D3R1OS

Descripción:
    Este programa permite crear y gestionar una biblioteca de libros. 
    Se pueden crear bibliotecas, agregar libros a ellas, mostrar los libros disponibles, marcar libros como leídos, eliminar libros y eliminar bibliotecas completas.
"""

import json
import os

ARCHIVO_DATOS = "biblioteca.json"


def guardar_datos(nombre_archivo, bibliotecas):
    datos = {nombre: biblioteca.to_dict() for nombre, biblioteca in bibliotecas.items()}
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return {}

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    bibliotecas = {}
    for nombre, biblioteca_data in datos.items():
        bibliotecas[nombre] = Biblioteca.from_dict(biblioteca_data)
    return bibliotecas


def mostrar_bibliotecas(bibliotecas):
    if not bibliotecas:
        print("No hay bibliotecas creadas.")
        return False

    print("Bibliotecas disponibles:")
    for nombre in bibliotecas.keys():
        print(f'- {nombre}')
    return True


def seleccionar_biblioteca(bibliotecas, mensaje="Ingrese el nombre de la biblioteca: "):
    if not mostrar_bibliotecas(bibliotecas):
        return None

    nombre = input(mensaje)
    if nombre in bibliotecas:
        return nombre

    print("La biblioteca especificada no existe.")
    return None


def mostrar_libros_de_biblioteca(bibliotecas, nombre):
    if nombre in bibliotecas:
        bibliotecas[nombre].mostrar_libros()
    else:
        print("La biblioteca especificada no existe.")


class Libro:
    def __init__(self, titulo, autor, paginas, leido=False):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.leido = leido

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "paginas": self.paginas,
            "leido": self.leido,
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["titulo"],
            datos["autor"],
            datos["paginas"],
            datos.get("leido", False),
        )
    
    def mostrar(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Paginas: {self.paginas}')
        if self.leido:
            print('Leído')
        else:
            print('No leído')
    
    def marcar_como_leido(self):
        self.leido = True
        print(f'El libro "{self.titulo}" ha sido marcado como leído.')
    
    def cambiar_nombre(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        print(f'El título del libro ha sido cambiado a "{self.titulo}".')
    
    def __str__(self):
        return f'"{self.titulo}" por {self.autor}, {self.paginas} páginas'
    
    def __len__(self):
        return self.paginas

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def crear_biblioteca(self, nombre):
        self.nombre = nombre
        self.libros = []
        print(f'Se ha creado la biblioteca "{self.nombre}".')

    def mostrar_nombre(self):
        return self.nombre

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'El libro "{libro.titulo}" ha sido agregado a la biblioteca.')
    
    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print(f"Libros en '{self.nombre}':")
            for libro in self.libros:
                libro.mostrar()
                print()  

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f'El libro "{titulo}" ha sido eliminado de la biblioteca.')
                return
        print(f'No se encontró el libro "{titulo}" en la biblioteca.')

    def eliminar_biblioteca(self):
        self.libros = []
        print(f'La biblioteca "{self.nombre}" ha sido eliminada.')

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "libros": [libro.to_dict() for libro in self.libros],
        }

    @classmethod
    def from_dict(cls, datos):
        biblioteca = cls(datos["nombre"])
        biblioteca.libros = [Libro.from_dict(libro_data) for libro_data in datos.get("libros", [])]
        return biblioteca


bibliotecas = cargar_datos(ARCHIVO_DATOS)

while True:
    print("\nOpciones:")
    print("1. Crear una biblioteca")
    print("2. Mostrar todas las bibliotecas")
    print("3. Crear un libro y agregarlo a la biblioteca")
    print("4. Mostrar todos los libros de la biblioteca")
    print("5. Marcar un libro como leído")
    print("6. Eliminar un libro")
    print("7. Eliminar una biblioteca")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_biblioteca = input("Ingrese el nombre de la biblioteca: ")
        if nombre_biblioteca in bibliotecas:
            print(f"La biblioteca '{nombre_biblioteca}' ya existe.")
        else:
            bibliotecas[nombre_biblioteca] = Biblioteca(nombre_biblioteca)
            guardar_datos(ARCHIVO_DATOS, bibliotecas)
            print(f'Se ha creado la biblioteca "{nombre_biblioteca}".')
    
    elif opcion == "2":
        mostrar_bibliotecas(bibliotecas)
    
    elif opcion == "3":
        if not bibliotecas:
            print("No hay bibliotecas creadas. Cree una primero.")
        else:
            biblioteca_elegida = seleccionar_biblioteca(bibliotecas)
            if biblioteca_elegida:
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                try:
                    paginas = int(input("Ingrese el número de páginas del libro: "))
                except ValueError:
                    print("Número de páginas inválido. Debe ser un número entero.")
                    continue
                leido_input = input("¿Ha leído el libro? (s/n): ")
                leido = leido_input.lower() == 's'
                
                nuevo_libro = Libro(titulo, autor, paginas, leido)
                bibliotecas[biblioteca_elegida].agregar_libro(nuevo_libro)
                guardar_datos(ARCHIVO_DATOS, bibliotecas)

    elif opcion == "4":
        biblioteca_elegida = seleccionar_biblioteca(bibliotecas, "Ingrese el nombre de la biblioteca que desea mostrar: ")
        if biblioteca_elegida:
            mostrar_libros_de_biblioteca(bibliotecas, biblioteca_elegida)

    elif opcion == "5":
        if not bibliotecas:
            print("No hay bibliotecas creadas.")
        else:
            biblioteca_elegida = seleccionar_biblioteca(bibliotecas)
            if biblioteca_elegida:
                print("Libros disponibles:")
                bibliotecas[biblioteca_elegida].mostrar_libros()
                titulo_libro = input("Ingrese el título del libro que desea marcar como leído: ")
                libro_encontrado = bibliotecas[biblioteca_elegida].buscar_libro(titulo_libro)
                if libro_encontrado:
                    libro_encontrado.marcar_como_leido()
                    guardar_datos(ARCHIVO_DATOS, bibliotecas)
                else:
                    print("El libro especificado no se encuentra en la biblioteca.")
    
    elif opcion == "6":
        if not bibliotecas:
            print("No hay bibliotecas creadas.")
        else:
            biblioteca_elegida = seleccionar_biblioteca(bibliotecas)
            if biblioteca_elegida:
                bibliotecas[biblioteca_elegida].mostrar_libros()
                titulo_libro = input("Ingrese el título del libro que desea eliminar: ")
                bibliotecas[biblioteca_elegida].eliminar_libro(titulo_libro)
                guardar_datos(ARCHIVO_DATOS, bibliotecas)
    
    elif opcion == "7":
        if not bibliotecas:
            print("No hay bibliotecas creadas.")
        else:
            biblioteca_elegida = seleccionar_biblioteca(bibliotecas, "Ingrese el nombre de la biblioteca que desea eliminar: ")
            if biblioteca_elegida:
                confirmacion = input(f"¿Está seguro de que desea eliminar la biblioteca '{biblioteca_elegida}'? (s/n): ")
                if confirmacion.lower() == 's':
                    bibliotecas[biblioteca_elegida].eliminar_biblioteca()
                    del bibliotecas[biblioteca_elegida]
                    guardar_datos(ARCHIVO_DATOS, bibliotecas)
                else:
                    print("Eliminación cancelada.")
    
    elif opcion == "8":
        guardar_datos(ARCHIVO_DATOS, bibliotecas)
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")