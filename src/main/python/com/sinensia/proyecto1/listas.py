#/usr/bin/python
import copy

empleados = [
    ["Pedro", ["Pyhton", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

print("Original: ", empleados)

#Paso 2
empleados_copia = empleados.copy()
empleados_deep_copia = copy.deepcopy(empleados)

#Paso 3
empleados[0][1] = 'JPA'
print("Copia: ", empleados_copia)
print("Deep copia: ", empleados_deep_copia)


