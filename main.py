from reportes.reportes import crear_reporte_estudiante

nombre = "Estudiante Python"
notas = [90,98,98,95]
reporte = crear_reporte_estudiante(nombre,notas)

print("Reporte del estudiante")
print("Nombre: ", reporte['nombre'])
print("Codigo: ", reporte['codigo'])
print("Notas: ", reporte['notas'])
print("Promedio: ", reporte['promedio'])
print("Fecha: ", reporte['fecha'])