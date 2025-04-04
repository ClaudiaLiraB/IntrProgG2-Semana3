def convertir_dolares(dolares, tasa_euro, tasa_libra, tasa_yen):
    euros = dolares * tasa_euro
    libras = dolares * tasa_libra
    yenes = dolares * tasa_yen
    return euros, libras, yenes

dolares = float(input("Ingrese la cantidad en dólares: "))
tasa_euro = float(input("Ingrese la tasa de cambio a euros: "))
tasa_libra = float(input("Ingrese la tasa de cambio a libras: "))
tasa_yen = float(input("Ingrese la tasa de cambio a yenes: "))
euros, libras, yenes = convertir_dolares(dolares, tasa_euro, tasa_libra, tasa_yen)

print(f"Cantidad en dólares: {dolares:.2f}")
print(f"Cantidad en euros: {euros:.2f}")
print(f"Cantidad en libras: {libras:.2f}")
print(f"Cantidad en yenes: {yenes:.2f}")