def calcular_duracion_total_pelicula(duracion_pelicula, duracion_comerciales_previos, cantidad_pausas, duracion_pausa):
    total_comerciales_pausas = cantidad_pausas * duracion_pausa
    duracion_total = duracion_pelicula + duracion_comerciales_previos + total_comerciales_pausas
    return duracion_total, total_comerciales_pausas

duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
duracion_comerciales_previos = float(input("Ingrese la duración de los comerciales previos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales: "))
duracion_pausa = float(input("Ingrese la duración de cada pausa comercial: "))
duracion_total, total_comerciales_pausas = calcular_duracion_total_pelicula(duracion_pelicula, duracion_comerciales_previos, cantidad_pausas, duracion_pausa)

print(f"Duración original de la película: {duracion_pelicula:.2f}")
print(f"Duración de los comerciales totales: {total_comerciales_pausas:.2f}")
print(f"Tiempo total de la proyección: {duracion_total:.2f}")