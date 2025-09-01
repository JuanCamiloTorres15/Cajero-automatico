from Datos import capturar_datos
from Registros import registro

def estud():
    estudiantes = []
    while True:
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Capturar estudiante")
        print("2. Ver estudiantes registrados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = capturar_datos()
            estudiantes.append(estudiante)
            print("\n✅ Estudiante registrado correctamente.\n")
        elif opcion == "2":
            registro(estudiantes)
        elif opcion == "3":
            print("\n👋 Saliendo del programa.")
            break
        else:
            print("\n❌ Opción no válida. Inténtelo de nuevo.\n")

estud()
