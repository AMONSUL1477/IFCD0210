#  5.- Sistema Básico de Gestión de Inventario
#      Desarrollar un programa que permita gestionar un inventario utilizando:
#      ● Diccionarios
#      ● Bucles
#      ● Condicionales
#  Crea un programa que gestione un inventario de una tienda.
#  El inventario debe almacenarse en un diccionario con la siguiente estructura:
#       inventario = {
#         "manzanas": 10,
#         "peras": 5,
#         "naranjas": 8 }
#  El programa debe mostrar el siguiente menú repetidamente hasta que el usuario decida salir:
#     1. Mostrar inventario
#     2. Añadir producto
#     3. Actualizar cantidad
#     4. Eliminar producto
#     5. Salir

#####################################################################################################

#  El inventario debe almacenarse en un diccionario con la siguiente estructura:
#      inventario = {
#        "manzanas": 10,
#        "peras": 5,
#        "naranjas": 8 }

inventario = {"manzanas": 10, "peras": 5, "naranjas": 8}


#  El programa debe mostrar el siguiente menú repetidamente hasta que el usuario decida salir:
#     1. Mostrar inventario
#     2. Añadir producto
#     3. Actualizar cantidad
#     4. Eliminar producto
#     5. Salir

while True:
    print("1.Ver - 2.Añadir - 3.Borrar - 4.Salir")
    op = input("Opción: ")

    if op == "4": break

    if op == "1":
        print(inventario)

    if op == "2":
        nombre = input("Producto: ")
        inventario[nombre] = int(input("Cantidad: "))

    if op == "3":
        nombre = input("Nombre a borrar: ")
        inventario.pop(nombre, "No encontrado")
        print("Operación realizada.")