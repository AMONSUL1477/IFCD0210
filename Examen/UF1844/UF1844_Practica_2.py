# 2.- Crea una lista con 5 números introducidos por el usuario.
#     1. Muestra:
#        ○ La lista completa.
#        ○ El número mayor.
#        ○ El número menor.
#        ○ La suma total de los números.

##################################################################


# 2.- Crea una lista con 5 números introducidos por el usuario.

numeros = []

for i in range(5):
    valor = float(input(f"Introduce el número {i+1}: "))
    numeros.append(valor)


#  1. Muestra:

#  ○ La lista completa.

print(f"Lista completa: {numeros}")

#  ○ El número mayor.

print(f"Número mayor: {max(numeros)}")

#    ○ El número menor.

print(f"Número menor: {min(numeros)}")

#    ○ La suma total de los números.

print(f"Suma total: {sum(numeros)}")