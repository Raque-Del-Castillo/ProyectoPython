import pandas as pd

#Crear una serie
datos = pd.Series([10, 20, 30, 40, 50])

#Mostrar la serie
print("Serie en Pandas:")
print(datos)

#Acceder a un elementos especifico usando su indice
print("\nValor en el indice 'c':", datos[2])

#Serie con indices personalizados
datos = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

#Acceder a un elemento especifico usando su indice
print("\nValor en el indice 'e':", datos['e'])