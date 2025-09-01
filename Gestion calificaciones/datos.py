def capturar_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese la asignatura: ")
    notas = []
    cantidad = int(input("¿Cuántas notas desea ingresar? "))
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    return nombre, asignatura, notas