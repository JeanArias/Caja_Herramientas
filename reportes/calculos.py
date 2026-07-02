import math

def calcular_area_circulo(radio):
    return math.pi*radio**2

def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas)/len(notas)