import pandas as pd

#Serie con temperaturas semanales en grados Celsius
temperaturas = [21, 23, 25, 28, 26, 24, 22]
temperaturas = pd.Series(temperaturas, index = [
    "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])

#Serie con precipitaciones semanales en milimetros
precipitaciones = [5, 3, 0, 0, 7, 10, 12]
precipitaciones = pd.Series(precipitaciones, index = [
    "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])

print("Temperaturas semanales:")
print(temperaturas)

print("\nPrecipitaciones semanales:")
print(temperaturas)

#Tomar los primeros 4 dias de la serie temperatura
sliced_temp = pd.Series(temperaturas[:4])
print("\nSlicing de Serie A (primeros 4 dias):")
print(sliced_temp)

#Tomar los ultimos 4 dias de la serie precipitaciones
sliced_prec = pd.Series(precipitaciones[-4:])
print("\nSlicing de Serie B (ultimos 4 dias):")
print(sliced_prec)

#Combinar + nuevo indice
serie_combinada = pd.concat([sliced_temp, sliced_prec])
print("\nSerie combinada (sliced de A y B)")
print(serie_combinada)

#Operaciones basicas: Sum total
suma_total = serie_combinada.sum()
print("\nSuma total de la Serie combinada: {suma_total}")

#Operaciones basicas: Media de la serie combinada
media = serie_combinada.mean()
print(f"Media de la serie combinada: {media:.2f}")