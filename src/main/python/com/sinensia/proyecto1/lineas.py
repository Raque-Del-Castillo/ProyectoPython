#/usr/bin/python
textos = []
#Simular texto de 1000 lineas
texto_largo = ["Linea " + str(i + 1) for i in range(1000)]

for texto_largo in texto_largo:
    if(len(texto_largo) <= 1000):
        textos.append(texto_largo)
        print(texto_largo)

for texto_largo in textos:
    print(texto_largo)
    if(textos.index(texto_largo)%25 == 0):
        print("\nSe han completado 25 lineas.\n")