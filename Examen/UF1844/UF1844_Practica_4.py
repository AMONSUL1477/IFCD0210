# 4.- Define una función llamada area_rectangulo(base, altura) que devuelva el área.
#     1. Pide al usuario base y altura.
#     2. Muestra el resultado llamando a la función.
#   NOTA: Validar que los valores sean positivos.

########################################################################################


# 4.- Define una función llamada area_rectangulo(base, altura) que devuelva el área.

def area_rectangulo(base, altura):
    return base * altura

#     1. Pide al usuario base y altura.

b = float(input("Introduce la base: "))
h = float(input("Introduce la altura: "))

#     2. Muestra el resultado llamando a la función.
#   NOTA: Validar que los valores sean positivos.

if b > 0 and h > 0:
    resultado = area_rectangulo(b, h)
    print("El área es:", resultado)
else:
    print("Los números deben ser positivos.")
