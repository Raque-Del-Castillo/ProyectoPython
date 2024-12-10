#/usr/bin/python
""" Pruebas explicaciones Python. """

print("Hola".upper())
mi_variable = "Hola"
print(mi_variable.upper())

edad = 16
carnet = True
if edad >= 18 and carnet:
    print("Puede conducir.")
else:
    print("No puede conducir.")

#Ejemplo operador ternario
x = 13
mensaje1 = "x es igual a 12"
mensaje2 = "x no es igual a 12"
print(mensaje1 if (x == 12) else mensaje2)

#Prueba 0 evaluado como falso en contexto booleano
numero = 0
if numero:
    print(numero)
    #El bloque NO se ejecuta porque 0 se considera False

mi_array = []
if mi_array:
    print(mi_array)
    #El bloque No se ejecuta porque al estar vacio se considera False tambien con tuplas

#Compara directamente con None se hace con "is"
if x is None:
        print("x no tiene valor")

x = True
if x is True:
    print("x es exactamente True")
#x es un numero pero evalua como verdadero
x = 1 
if x == True:
     print("x es verdadero en un sentido logico")
x = 0
if x == True:
     print("x es falso en un sentido logico")
#Usar is si interesa asegurar que la variable es exactamente True o False
#Usar == si solo interesa el valor logico y puede venir de diferentes tipos de datos 
#que evaluan como verdadero o falso