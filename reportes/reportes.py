from datetime import datetime
from reportes.calculos import calcular_promedio
from codigos import generar_codigo_estudiante

def obtener_fecha_actual():
    return datetime.now().strftime('%Y-%m-%d')

def crear_reporte_estudiante(nombre,notas):
    codigo = generar_codigo_estudiante(nombre)
    promedio = calcular_promedio(notas)
    fecha = obtener_fecha_actual()
    return {'nombre':nombre,
            'codigo':codigo,
            'notas':notas,
            'promedio': round(promedio,2),
            'fecha':fecha}


