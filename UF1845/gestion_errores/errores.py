def escribe(numero):
    try:
        n=int(numero)
        z=4/n
        print(f'El número es {n}')
    except ValueError:
        print('Número no valido')
    except ZeroDivisionError as z:
        print('No se puede dividir entre cero ', z)
    except

escribe('0')











        print("División")

        print("Tírate por el barranco")


#lista_error()

def archivo():
    try:
        arch = open("basura.txt", "r")
    except FileNotFoundError:
        arch
