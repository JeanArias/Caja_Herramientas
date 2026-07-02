import random

def generar_codigo_estudiante(nombre):
    numero = random.randint(1000,9999)
    return f'{nombre[:3].upper()}-{numero}'