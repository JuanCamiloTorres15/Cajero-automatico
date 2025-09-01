from productos import Producto
from total import calcular_total

productos = [
    Producto("Café", 3000, 1),
    Producto("Té", 2500, 1),
    Producto("Sandwich", 5000, 1),
    Producto("Galleta", 1500, 1)
]

for i, p in enumerate(productos, 1):
    print(f"{i}. {p.nombre} - ${p.precio} - con IVA: ${int(p.precio * 1.19)}")

seleccionados = []
while True:
    opcion = input("Producto (número, 0 para salir): ")
    if opcion == "0":
        break
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(productos):
        print("Número incorrecto.")
        continue
    cantidad = int(input("Cantidad: "))
    base = productos[int(opcion)-1]
    seleccionados.append(Producto(base.nombre, base.precio, cantidad))

if seleccionados:
    total = calcular_total(seleccionados)
    print(f"Total a pagar: ${int(total)}")
else:
    print("No compraste nada.")
