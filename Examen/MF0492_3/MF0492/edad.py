## 3. Dado este JSON:
## [
##{"nombre": "Ana", "edad": 25},
##{"nombre": "Luis", "edad": 17},
##{"nombre": "Carlos", "edad": 30}
## ]
## Crea un programa python que:
## 1. Filtre solo los mayores de edad
## 2. Muestre sus nombres
## 3. Calcule la edad media

## ---------------------------------------------------------------

import json

datos_json = '''
[
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 17},
    {"nombre": "Carlos", "edad": 30}
]
'''
personas = json.loads(datos_json)

## ---------------------------------------------------------------

# 1 y 2. Filtrar mayores de edad y mostrar nombres

mayores = [p for p in personas if p['edad'] >= 18]
print("Mayores de edad:")
for m in mayores:
    print(f"- {m['nombre']}")

## ---------------------------------------------------------------

# 3. Calcular la edad media

edades = [p['edad'] for p in personas]
media = sum(edades) / len(edades)
print(f"\nEdad media: {media:.2f}")