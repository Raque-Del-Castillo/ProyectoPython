#/usr/bin/python
texto_largo = ["\nLinea " + str(i) for i in range(1, 1001)]

bloque_actual = "\nLinea 1"
contador_lineas = 1
contador_bloques = 0
for linea in texto_largo:
    contador_lineas += 1
    bloque_actual += linea
    if (contador_lineas % 25) == 0:
        contador_bloques += 1
        print(f"\nBloque de texto {contador_bloques}:\n",bloque_actual)
        bloque_actual = ""
        #continue dice que es redundante?

if bloque_actual == "":
    bloque_actual = linea.strip()

if bloque_actual:
    print("Bloque de texto final:\n", bloque_actual)


#Opcion 2, mejor?
texto_largo = [f"\nLinea {i}" for i in range(1, 1001)]

#Inicia variables para contar bloques
contador_bloques = 0

#Iterar con range pasando un step
for i in range(0, len(texto_largo), 25):
    contador_bloques += 1
    bloque_actual = "\n".join(texto_largo[i:i+25])
    print(f"\nBloque de texto {contador_bloques}:\n{bloque_actual}")

    #Finalizar el bucle despues del bloque que contiene la linea 52
    if i + 25 >= 51:
        break