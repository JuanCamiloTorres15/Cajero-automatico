def capturar_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    contacto = input("Ingrese el número de contacto: ")
    promedio = input("Ingrese el promedio del estudiante: ")
    municipio = input("Ingrese el municipio del estudiante: ")
    return {
        "nombre": nombre,
        "contacto": contacto,
        "promedio": promedio,
        "municipio": municipio
    }
