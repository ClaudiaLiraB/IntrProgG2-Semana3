def calcular_volumen_area_cilindro(radio, altura):
    area_base = math.pi * radio ** 2
    volumen = area_base * altura
    area_lateral = 2 * math.pi * radio * altura
    area_superficial = area_lateral + 2 * area_base
    return volumen, area_superficial

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
volumen, area_superficial = calcular_volumen_area_cilindro(radio, altura)

print(f"Radio ingresado: {radio:.2f}")
print(f"Altura ingresada: {altura:.2f}")
print(f"Volumen calculado: {volumen:.2f}")
print(f"Área superficial calculada: {area_superficial:.2f}")