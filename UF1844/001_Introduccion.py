# calcular el precio con IVA de un producto
 
precio_producto = 32.18
porcetanje_iva  = 0.21
precio_total = precio_producto * (1 + porcetanje_iva)
print('El precio total es: ' + str(precio_total))

# Convertir de grados Celsius a Fahrenheit

grados_celsius = 49
grados_fh = grados_celsius * 1.8 + 32
# print(grados_celsius, '-->', grados_fh)
mensaje = str(grados_celsius) + " Grados Celsius son " + str(grados_fh) + " Grados Fh"
print(mensaje)

#Calcular el índice de la masa corporal
#Imc < 18 : bajo; < 25 normal; > 25 Sobrepeso

peso = 70
altura = 1.70
imc = peso / altura ** 2
print(imc)














