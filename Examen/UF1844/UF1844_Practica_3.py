# 3.- Crea un programa que:
#     1. Solicite al usuario: Nombre, Edad y Ciudad.
#     2. Guarde los datos en un diccionario.
#     3. Muestre un mensaje como: "Juan tiene 25 años y vive en Madrid."

#########################################################################


# 3.- Crea un programa que:

#     1. Solicite al usuario: Nombre, Edad y Ciudad.

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
ciudad = input("Introduce tu ciudad: ")

#     2. Guarde los datos en un diccionario.

persona = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

#     3. Muestre un mensaje como: "Juan tiene 25 años y vive en Madrid."

print(f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['ciudad']}.")