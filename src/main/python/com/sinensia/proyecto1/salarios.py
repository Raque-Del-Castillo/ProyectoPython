#/usr/bin/python
import math
from statistics import stdev

# Función obtencion salario
def obtener_salario(persona): return persona["salario"]

# Función para obtener diferencia salario - salario medio
def obtener_diferencia_salario(
    persona): return round((persona["salario"] - salario_medio), 2)

# Lista de personas
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "salario": 25000},
    {"nombre": "Juan", "edad": 30, "ciudad": "Sevilla", "salario": 30000},
    {"nombre": "María", "edad": 22, "ciudad": "Madrid", "salario": 22000},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona", "salario": 35000},
]

# Calculo salario medio
salario_total = sum(map(obtener_salario, personas))
salario_medio = math.floor(salario_total / len(personas))

# Calculo desviacion estandar salario 
diferencias_salario = list(map(obtener_diferencia_salario, personas))
# Calculo con comrpesion diferencias_salario = [obtener_diferencia_salario(persona, salario_medio) for persona in personas]
desviacion_estandar = round(stdev(diferencias_salario), 2)

# Obtener persona con mayor ratio salario/edad
def ratio_salario_edad(persona): return persona["salario"] / persona["edad"]


persona_mayor_ratio = max(personas, key=lambda persona: (
    ratio_salario_edad(persona), persona["salario"]))

#Resultados por pantalla
print(f"El salario medio es: {salario_medio}")
print("La desviación estándar del salario es:", desviacion_estandar)
print("La persona que tiene el mayor ratio salario-edad es:", persona_mayor_ratio)