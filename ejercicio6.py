def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc_redondeado = round(imc, 2)
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc < 25:
        clasificacion = "Peso normal"
    elif 25 <= imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    return imc_redondeado, clasificacion

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
imc, clasificacion = calcular_imc(peso, altura)

print(f"Peso ingresado: {peso:.2f}")
print(f"Altura ingresada: {altura:.2f}")
print(f"IMC calculado: {imc:.2f}")
print(f"Clasificación del IMC: {clasificacion}")