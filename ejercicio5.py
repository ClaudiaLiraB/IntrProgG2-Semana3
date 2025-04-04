def convertir_segundos(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

segundos = int(input("Ingrese la cantidad total de segundos: "))
horas, minutos, segundos = convertir_segundos(segundos)

print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")