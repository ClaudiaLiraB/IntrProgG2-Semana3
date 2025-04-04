def calcular_area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * base + 2 * altura
    return area, perimetro

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area, perimetro = calcular_area_perimetro_rectangulo(base, altura)

print(f"Área del rectángulo: {area:.2f}")
print(f"Perímetro del rectángulo: {perimetro:.2f}")