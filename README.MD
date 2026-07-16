# Sistema de Biblioteca en Python

Aplicación de consola desarrollada en Python para gestionar una biblioteca de libros.

El programa permite agregar, modificar, eliminar y buscar libros, manteniendo los datos guardados de forma persistente mediante un archivo JSON.

## Características

- Agregar libros.
- Mostrar todos los libros registrados.
- Buscar libros por nombre.
- Buscar libros por autor.
- Buscar libros por año de publicación.
- Editar información de libros.
- Eliminar libros.
- Evitar libros duplicados.
- Ordenar la lista de libros.
- Validar entradas del usuario.
- Guardar los datos automáticamente.
- Cargar los libros al iniciar el programa.

## Tecnologías utilizadas

- Python 3.
- JSON para almacenamiento de datos.

## Estructura de un libro

Cada libro se almacena con la siguiente información:

```json
{
    "nombre": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año": 1943
}
```

## Instalación

Clonar el repositorio:

```bash
git clone git@github.com:derios344/biblioteca-python.git
```

Entrar en la carpeta del proyecto:

```bash
cd biblioteca-python
```

Ejecutar el programa:

```bash
python biblioteca.py
```

## Uso

Al iniciar el programa aparecerá un menú con las siguientes opciones:

```text
1. Mostrar libros
2. Agregar libro
3. Eliminar libro
4. Buscar libro por nombre
5. Buscar libro por autor
6. Buscar libro por año
7. Editar libro
8. Salir
```

Los libros se guardan automáticamente en:

```text
libros.json
```

Esto permite conservar la información aunque el programa sea cerrado.

## Conceptos practicados

Este proyecto fue realizado para practicar:

- Funciones.
- Listas.
- Diccionarios.
- Manejo de archivos.
- Persistencia de datos con JSON.
- Manejo de errores (`try/except`).
- Comprensiones de listas.
- Validación de datos.
- Manipulación de estructuras de datos.


## Autor

D3R1OS

Proyecto realizado como práctica de aprendizaje de Python y desarrollo de software.