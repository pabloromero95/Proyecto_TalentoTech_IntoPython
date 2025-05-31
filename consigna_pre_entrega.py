# C25011 - Pre-entrega PFI
# Fecha de publicación: Clase 8 - el lunes 19 de mayo
# Fecha de entrega: hasta el domingo 1 de junio a la medianoche
# Modalidad de entrega: archivo py en un repositorio en la nube (Google Drive)

# Consigna: Ver debajo del código

# A continuación se presenta un bloque de código que pueden utilizar
# para la estructura inicial de su proyecto.
# La idea es luego, ir completando cada opción de menú con lo que aprendimos en clases

lista_productos = [] # Inicializo la lista de productos fuera del while

while True: # Condicion siempre True que maneja el flujo normal del menú

    print("""
    Menú de opciones:
    1. Alta de producto
    2. Motrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
        """)
    
    opcion = input("Ingrese su opción: ") # Solicito al usuario que ingresa su opción

    # Procesamiento de la opción ingresada
    match opcion:
        case "1":
            # Alta de producto 
            # Validando que el nombre del producto no esté vacío
            while True:
                nombre = input("Ingrese el nombre del producto: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío.")
            # Validando que la categoría no esté vacía
            while True:
                categoria = input("Ingrese la categoría del producto: ").strip()
                if categoria:
                    break
                print("La categoría no puede estar vacía.")
            # Validando que el precio sea un número entero positivo
            while True:
                precio = input("Ingrese el precio del producto (entero positivo): ").strip()
                try:
                    # Validando que el precio sea un número entero positivo
                    precio = int(precio)
                    if precio > 0:
                        break
                    else:
                        print("El precio debe ser mayor que cero.")
                    # Validando que el precio sea un número.
                except ValueError:
                    print("El precio debe ser un número entero.")
            # Agregando los datos a la sublista y luego a la lista de productos
            producto = [nombre, categoria, precio]
            # Almacenando el producto como una sublista en la lista de productos
            lista_productos.append(producto)
            print(f"Producto '{nombre}' agregado correctamente.")

        case "2":
            # Mostrar productos
            # Validando que la lista de productos no esté vacía
            if len(lista_productos) == 0:
                print("No hay productos cargados en el sistema.")
            else:
            #Recorriendo la lista de productos y mostrando cada uno con el índice y el nombre del producto
                print("\nProductos disponibles:")
                for i, producto in enumerate(lista_productos):
                    print(f"{i + 1}. {producto[0]}")
                    

        case "3":
            # Buscar producto por nombre
            # Validando que la lista de productos no esté vacía
            if len(lista_productos) == 0:
                print("No hay productos cargados para buscar.")
                continue
            # Solicito al usuario que ingrese el nombre del producto a buscar
            # y lo convierto a minúsculas para hacer la búsqueda insensible a mayúsculas
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            #Recorriendo la lista de productos y buscando coincidencias
            encontrados = [p for p in lista_productos if p[0].lower() == nombre_buscar]
            # Si se encuentran coincidencias, las muestro
            if encontrados:
                for p in encontrados:
                    print(f"Producto encontrado: Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")
            # Si no se encuentran coincidencias, informo al usuario que no se encontraron resultados
            else:
                print("Producto no encontrado.")

        case "4":
            # Eliminar producto
            # Validando que la lista de productos no esté vacía
            if len(lista_productos) == 0:
                print("No hay productos para eliminar.")
                continue
            
            # Mostrando los productos disponibles para eliminar  
            print("\nProductos disponibles:")
            for i, producto in enumerate(lista_productos):
                print(f"{i + 1}. {producto[0]}")
                
            # Solicito al usuario que ingrese el número del producto a eliminar y lo convierto a entero
            opcion_eliminar = int(input(f"Ingrese el número del producto a eliminar (1 - {len(lista_productos)}): "))
            # Validando que la opción ingresada sea un número entero y que esté dentro del rango de productos disponibles
            if opcion_eliminar < 0:
                print("Error: Debe ingresar un número entero positivo.")
                continue
            # Validando que la opción ingresada esté dentro del rango de productos disponibles
            if 1 <= opcion_eliminar <= len(lista_productos):
                producto_eliminado = lista_productos.pop(opcion_eliminar - 1)
                print(f"Producto '{producto_eliminado[0]}' eliminado correctamente.")
            # Si la opción ingresada no está dentro del rango de productos disponibles, informo al usuario
            else:
                print(f"Error: Número fuera de rango. Debe ser entre 1 y {len(lista_productos)}.")

        case "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        case _:
            print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
    

# Consigna
"""
1. Ingreso de datos de productos
El sistema debe permitir ingresar datos básicos de los productos: 
nombre, categoría, y precio (sin centavos). 
Estos datos deben almacenarse en una lista, donde cada producto sea representado
como una sublista de tres elementos (nombre, categoría, y precio).

Nota_JP: 
Menú de opciones: Alta de productos
Solicitar y validar ingresos: nombre (str), categoría (str o lista), precio (int)
Almacenar estos valores en una lista, y esta lista en otra lista general llamada lista_productos

----------------------------------------------------------------------------------------

2. Visualización de productos registrados
El programa debe incluir una funcionalidad para mostrar en pantalla
todos los productos ingresados. La información debe presentarse de manera ordenada y legible, 
con cada producto numerado.

Nota_JP: 
Menú de opciones: Mostrar productos
Iteramos lista_productos y mostramos cada elemento
Podemos usar el índice de la lista para obtener la numeración

----------------------------------------------------------------------------------------

3. Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. 
Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. 
Si no hay coincidencias, debe informar que no se encontraron resultados.

Nota_JP:
Menú de opciones: Buscar productos
Solicitar al usuario que ingrese el nombre del producto a mostrar
Iteramos lista_productos y buscamos coincidencia en cada iteración
A medida que haya coincidencia mostramos en pantalla

----------------------------------------------------------------------------------------

4. Eliminación de productos
El sistema debe permitir eliminar un producto de la lista, 
identificándolo por su posición (número) en la lista.

Nota_JP:
Menú de opciones: Eliminar productos
Solicitar al usuario que ingrese la posición que ocupa en la lista_productos para eliminar

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

Requisitos

A. Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.
B. Usar listas para almacenar y gestionar los datos. 
C. Presentar un menú que permita elegir entre las funcionalidades disponibles: 
agregar productos, visualizar productos, buscar productos y eliminar productos.
D. Incorporar bucles while y for según corresponda. 
E. Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.
F. El programa debe continuar funcionando hasta que se elija una opción para salir.


Consejos

I. Usá lo aprendido sobre listas y bucles para gestionar los datos y recorrerlos.
II .Recordá validar las entradas utilizando condicionales.
III. Utilizá las herramientas vistas para organizar y presentar la información de manera clara.
"""