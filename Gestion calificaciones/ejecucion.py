from datos import capturar_datos
from calculos import calcular_aprobacion, calcular_promedio

def ejecutar():
    nombre, asignatura, notas = capturar_datos()
    promedio = calcular_promedio(notas)
    aprobado = calcular_aprobacion(promedio)
    
    if aprobado:
        print(f"{nombre} ha aprobado la asignatura {asignatura} con un promedio de {promedio:.2f}.")
    else:
        print(f"{nombre} no ha aprobado la asignatura {asignatura}. El promedio fue {promedio:.2f}.")

if __name__ == "__main__":
    ejecutar()