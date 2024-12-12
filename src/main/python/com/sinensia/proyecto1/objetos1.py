#/usr/bin/python

class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca      #Atributo publico
        self._modelo = modelo   #Atributo protegido
        self.__anio = 2020      #Atributo privado

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self._modelo}, Año: {self.__anio}"
    
#Creacion objeto
auto = Automovil("Toyota", "Corolla")

#Acceso atributos
print(auto.marca)           #Acceso permitido
print(auto._modelo)         #Acceso permitido, pero no recomendado fuera de la clase o subclase
#print(auto.__anio)         #AttributeError: 'Automovil' object has no attribute '__anio'

print(auto.mostrar_info())   #Metodo publico que accede a los atributos protegidos y privados   