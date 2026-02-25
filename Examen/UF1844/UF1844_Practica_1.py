#1.- Escribe un programa que:
#    1. Pida al usuario su nombre completo.
#    2. Muestre:
#       ○ El nombre en mayúsculas.
#       ○ El nombre en minúsculas.
#       ○ El número total de caracteres (incluyendo espacios).
#       ○ El nombre sin espacios al inicio ni al final.


################################################################

# 1. Pida al usuario su nombre completo.
nombre = input("Introduce tu nombre completo: ")

# 2. Muestre:

# 2. Realizar las transformaciones y mostrar resultados

print("\n--- Resultados ---")

#  ○ El nombre en mayúsculas.

print(f"Nombre en mayúsculas: {nombre.upper()}")

#   ○ El nombre en minúsculas.

print(f"Nombre en minúsculas: {nombre.lower()}")

#   ○ El número total de caracteres (incluyendo espacios).

print(f"Número total de caracteres: {len(nombre)}")

#   ○ El nombre sin espacios al inicio ni al final.

print(f"Nombre sin espacios extra: '{nombre.strip()}'")