#/usr/bin/python
from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre, apellidos):
        self._nombre = nombre           #Atributo protegido
        self._apellidos = apellidos     #Atributo protegido
        self.__id_fiscal                #Atributo privado
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellidos(self):
        return self._apellidos
    
    @nombre.setter
    def apellidos(self, value):
        self._apellidos = value

    @property
    def id_fiscal(self):
        return self.__id_fiscal
    
    @nombre.setter
    def id_fiscal(self, value):
        self.__id_fiscal = value

    def __str__(self):
        return self._nombre + " " + self._apellidos + " " + self.__id_fiscal
    
    def saludar(self):
        pass

class Cliente(Persona):
    def __init__(self, nombre, apellidos):
        self._nombre = nombre           #Atributo protegido
        self._apellidos = apellidos     #Atributo protegido
        self.__id_fiscal                #Atributo privado

    def saludar():
        print("Saludando")



class Factura:
    def __init__(self, id_factura):
        self._id_factura = id_factura           #Atributo protegido
        
    @property
    def id_factura(self):
        return self._id_factura
    
    @id_factura.setter
    def id_factura(self, value):
        self._id_factura = value

    #ID fiscal? no el nombre del cliente, que aqui no esta aun
    def __str__(self):
        return self._nombre + " " + self._id_factura 