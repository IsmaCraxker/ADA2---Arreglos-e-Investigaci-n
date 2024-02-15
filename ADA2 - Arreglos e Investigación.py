# Definir la matriz de calificaciones
calificaciones = [
    [85, 70, 90, 80, 75],
    [95, 85, 90, 95, 80],
    [75, 65, 80, 70, 65],
    # ... (se omiten las demás filas para abreviar)
]
alumno = 95
materia = 5
calificacion_encontrada = False

for fila in calificaciones:
    for i in range(len(fila)):
        if i == materia and fila[i] == alumno:
            calificacion_encontrada = True
            calificacion = fila[i]
            break
    if calificacion_encontrada:
        break

try:
    indice_alumno = calificaciones.index([alumno])
    calificacion = calificaciones[indice_alumno][materia]
except ValueError:
    calificacion = None

if calificacion is not None:
    print(f"Calificación del alumno {alumno} en la materia {materia}: {calificacion}")
else:
    print(f"Alumno {alumno} no encontrado.")
