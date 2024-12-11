#/usr/bin/python
""" V.1 Gestor Peliculas Python. """
peliculas = []
#Colores mensaje
MENSAJE = """Gestion de peliculas
------------------------
1.Añadir pelicula
2.Eliminar pelicula
3.Mostrar peliculas
4.Buscar pelicula
5.Salir
-------------------------
Elija una opcion:"""

#Que de formato primera en mayus? Control input, que ahora mismo se puede usar de todo
def insertar_pelicula():
    titulo = input("Insertar titulo: ")
    genero = input("Insertar el genero: ")
    peliculas.append({
        'titulo': titulo,
        'genero': genero
    })
    print("Se ha insertado la pelicula.\n")

#Por ahora es case sensitive
def eliminar_pelicula():
    buscar = input("Introduzca el titulo de la pelicula que desee eliminar.")
    for pelicula in peliculas:
        if pelicula['titulo'] == buscar:
            peliculas.remove(pelicula)
            print("Se ha eliminado la pelicula.\n")
        else:
            print("Esa pelicula no existe.\n")
    
def listar_peliculas():
    numero = len(peliculas)
    titulos = [pelicula['titulo'] for pelicula in peliculas]
    titulos = '\n'.join(titulos)
    if numero:
        print(f'\nLista de las peliculas almacenadas: \n{titulos}\n')
    else:
        print('No hay ninguna pelicula en el sistema.\n')

def mostrar_info(pelicula):
    print('La informacion de la pelicula es:')
    print(f'Titulo: {pelicula["titulo"]},')
    print(f'Genero: {pelicula["genero"]}.\n')

#Por ahora es case sensitive
def buscar_pelicula():
    buscar = input("Introduzca el titulo de la pelicula que desee buscar.")
    for pelicula in peliculas:
        if pelicula['titulo'] == buscar:
            mostrar_info(pelicula)
        else:
            print("Esa pelicula no existe.\n")

input_usuario = {
    '1': insertar_pelicula,
    '2': eliminar_pelicula,
    '3': listar_peliculas,
    '4': buscar_pelicula,
}

#Añadir que se pueda salir dentro de las opciones por si te equivocas
def menu():
    interaccion = input(MENSAJE)
    while interaccion != '5':
        if interaccion in input_usuario:
            opcion_seleccionada = input_usuario[interaccion]
            opcion_seleccionada()
        else:
            print("Input erroneo, por favor seleccione una opcion entre: 1, 2, 3, 4 y 5.")
        interaccion = input(MENSAJE)
    print("Gracias por usar el sistema de gestion de peliculas.")

if __name__ == '__main__':
    menu()

