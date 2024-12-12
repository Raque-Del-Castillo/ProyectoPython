#/usr/bin/python
# Lista de personas
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "salario": 25000},
    {"nombre": "Juan", "edad": 30, "ciudad": "Sevilla", "salario": 30000},
    {"nombre": "María", "edad": 22, "ciudad": "Madrid", "salario": 22000},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona", "salario": 35000},
]

from statistics import stdev
desviacion_estandar = stdev(diferencias_salario)

ratio_salario_edad = lambda persona: persona["salario"] / persona["edad"]


get_salary = lambda persona: persona["salario"]

salario_total = sum(map(get_salary, personas))
