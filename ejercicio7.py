def calcular_precio_final(precio_original, descuento_porcentaje, iva_porcentaje):
    descuento = precio_original * descuento_porcentaje / 100
    precio_con_descuento = precio_original - descuento
    iva = precio_con_descuento * iva_porcentaje / 100
    precio_final = precio_con_descuento + iva
    return precio_final, precio_con_descuento, descuento, iva

precio_original = float(input("Ingrese el precio original del producto: "))
descuento_porcentaje = float(input("Ingrese el porcentaje de descuento: "))
iva_porcentaje = float(input("Ingrese el porcentaje de IVA: "))
precio_final, precio_con_descuento, descuento, iva = calcular_precio_final(precio_original, descuento_porcentaje, iva_porcentaje)

print(f"Precio original: {precio_original:.2f}")
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Precio con descuento: {precio_con_descuento:.2f}")
print(f"IVA calculado: {iva:.2f}")
print(f"Precio final: {precio_final:.2f}")