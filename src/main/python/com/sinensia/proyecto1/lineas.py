#/usr/bin/python

#Simular texto de 1000 lineas
texto_largo = ["Linea " + str(i + 1) for i in range(1000)]

for texto_largo in texto_largo:
    if(len(texto_largo) <= 1000):
        print(texto_largo)
    