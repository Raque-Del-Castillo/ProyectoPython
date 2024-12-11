#/usr/bin/python
NITROGENO = -196

lista_temperaturas = (35, 523, 56, 234, 1, -34, -53, -254, -48, -315)
tupla_temperaturas = tuple(lista_temperaturas)
licuado = tuple(num < NITROGENO for num in tupla_temperaturas)
print(licuado)