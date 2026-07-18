# Sistema de Gestión Multi-Biblioteca en Python

Aplicación de consola desarrollada en Python que utiliza el paradigma de **Programación Orientada a Objetos (POO)** para gestionar múltiples bibliotecas de forma independiente.

El programa permite organizar libros dentro de diferentes colecciones virtuales creadas por el usuario, controlando el total de páginas y el estado de lectura de cada volumen.

## Características

- **Gestión Multi-Biblioteca:** Creación y eliminación de múltiples bibliotecas personalizadas por nombre.
- **Modelado con Objetos:** Los libros y las bibliotecas están representados mediante clases independientes.
- **Control de Lectura:** Capacidad de marcar libros específicos como "Leídos" o "No leídos".
- **Estructura Detallada:** Registro de títulos, autores y contador físico de páginas por libro.
- **Visualización Limpia:** Listado ordenado de las bibliotecas disponibles y los libros contenidos en cada una.

## Tecnologías utilizadas

- Python 3 (Enfoque nativo en POO, sin dependencias externas).

## Modelos de Datos

El sistema se basa en dos entidades principales interconectadas:

### 1. Clase Libro
Representa un volumen individual con las propiedades:
- `titulo` (Texto)
- `autor` (Texto)
- `paginas` (Entero)
- `leido` (Booleano)

### 2. Clase Biblioteca
Actúa como contenedor y administrador, asociando un nombre único a una lista dinámica de objetos de tipo `Libro`.

> ⚠️ **Nota de Persistencia:** En esta versión, los datos se administran directamente en la memoria RAM. Al cerrar la aplicación, las bibliotecas creadas se reiniciarán.

## Instalación

Clonar el repositorio:

    git clone  https://github.com/derios344/biblioteca-python.git

Entrar en la carpeta del proyecto:

    cd biblioteca-python

Ejecutar el programa:

    python biblioteca.py

## Uso

Al iniciar el programa, interactuarás con el sistema a través del siguiente menú interactivo en consola:

    Opciones:
    1. Crear una biblioteca
    2. Mostrar todas las bibliotecas
    3. Crear un libro y agregarlo a la biblioteca
    4. Mostrar todos los libros de la biblioteca
    5. Marcar un libro como leído
    6. Eliminar un libro
    7. Eliminar una biblioteca
    8. Salir

## Conceptos practicados

Este rediseño fue ideal para profundizar en conceptos avanzados de desarrollo:

- **Programación Orientada a Objetos (POO):** Definición de clases, instanciación de objetos, encapsulamiento de estados y métodos de comportamiento.
- **Métodos Mágicos (Dunder Methods):** Implementación de `__str__` para representaciones en texto personalizadas y `__len__` para mapear el tamaño del libro a sus páginas.
- **Estructuras de Datos Avanzadas:** Uso de diccionarios globales donde las llaves son strings y los valores son instancias complejas de otras clases.
- **Lógica de Relaciones (1 a Muchos):** Asociación y paso de objetos (`Libro`) para ser almacenados dentro de los atributos de otra clase (`Biblioteca`).
- **Validaciones Básicas:** Control del flujo del menú y chequeo de existencia de elementos previos.

## Autor

D3R1OS

Proyecto enfocado en la transición hacia arquitecturas de software más escalables y limpias en Python.
