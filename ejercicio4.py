def calcular_tiempo_total_viaje(tramo1, escala1, tramo2, escala2, tramo3):
    tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3
    return tiempo_total

tramo1 = float(input("Ingrese la duración del primer tramo: "))
escala1 = float(input("Ingrese la duración de la primera escala: "))
tramo2 = float(input("Ingrese la duración del segundo tramo: "))
escala2 = float(input("Ingrese la duración de la segunda escala: "))
tramo3 = float(input("Ingrese la duración del tercer tramo: "))
tiempo_total = calcular_tiempo_total_viaje(tramo1, escala1, tramo2, escala2, tramo3)

print(f"Tiempo total del viaje: {tiempo_total:.2f}")