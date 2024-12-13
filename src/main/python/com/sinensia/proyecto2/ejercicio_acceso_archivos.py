import os
import locale

print(locale.getdefaultolocale())

print(os.getcwd())

with open("mi_archivo.txt", "w", encoding='UTF-8') as archivo:
    archivo.write("Línea")

try:
    with open("mi_archivo.txt", "w", encoding='UTF-8') as archivo:
        print("El archuvo existe")
except FileNotFoundError:
    with open("mi_archivo.txt", "w", encoding='UTF-8') as archivo:
        print("El archivo ha sido creado")

try:
    with open("mi_archivo.txt", "w", encoding='UTF-8') as archivo:
        print("El archivo no existe")
except FileExistsError:
        print("El archivo ya existe")

with open("mi_archivo.txt", 'a', encoding='UTF-8') as archivo:
     archivo.write("\Línea 1")
     archivo.write("\Línea 2")
     archivo.write("\Línea 3")

with open("mi_archivo.txt", 'r', encoding='UTF-8') as archivo:
     while True:
          line = archivo.readline()
          if not line:
               break
          posicion = archivo.tell()
          print(f"La posiciones es (posicion)")

with open("mi_archivo.txt", 'w', encoding='UTF-8') as archivo:
     archivo.write("\nEsta linea sobreescribe todo.")