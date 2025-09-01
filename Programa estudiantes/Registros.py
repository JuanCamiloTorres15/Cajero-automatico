def registro(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return
    
    print("\n--- Lista de Estudiantes ---")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"\nEstudiante #{i}")
        print(f" Nombre   : {estudiante['nombre']}")
        print(f" Contacto : {estudiante['contacto']}")
        print(f" Promedio : {estudiante['promedio']}")
        print(f" Municipio: {estudiante['municipio']}")
