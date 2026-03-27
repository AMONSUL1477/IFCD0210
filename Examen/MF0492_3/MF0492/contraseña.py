## 1. Crea una función python que valide una contraseña:
## La contraseña debe cumplir:
## ● Mínimo 8 caracteres
## ● Al menos una mayúscula
## ● Al menos un número
## ● Al menos un carácter especial
## Devuelve:
## ● "Válida"
## ● o el motivo del error

## ----------------------------------------------------------------------------------------

def validar_contrasena(password):
    if len(password) < 8:
        return "Error: Mínimo 8 caracteres"

    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False

    especiales = "!@#$%^&*(),.?\":{}|<>+-_"

    for c in password:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_numero = True
        if c in especiales:
            tiene_especial = True

    if not tiene_mayuscula:
        return "Error: Al menos una mayúscula"
    if not tiene_numero:
        return "Error: Al menos un número"
    if not tiene_especial:
        return "Error: Al menos un carácter especial"

    return "Válida"