def calcular_total(productos):
    IVA = 0.19  
    total = sum(producto.precio * producto.cantidad for producto in productos)
    total_con_iva = total * (1 + IVA)
    return total_con_iva