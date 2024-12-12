#/usr/bin/python
import random

canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones = [5.55, 8.02, 6.30, 3.03, 5.01] #Duraciones en minutos

#Objetiovo 1: Combinar en un diccionario
diccionario = dict(zip(canciones, duraciones))
print(diccionario)

#Objetivo 2: Seleccionar las 3 canciones más largas en un diccionario
canciones_largas = sorted(diccionario.items(), key = lambda x: x[1], reverse = True)[:3]
print(canciones_largas)

#Objetivo 3: Crear diccionario con seleccion aleatoria de canciones
random_keys = random.sample(list(diccionario.keys()), 5)
diccionario_random = {key: diccionario[key] for key in random_keys}
print(diccionario_random)