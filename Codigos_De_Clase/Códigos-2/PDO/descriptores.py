#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        EJEMPLO DE DESCRIPTORES

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
            DEFINICION DE LAS CLASES
"""""""""""""""""""""""""""""""""""""""""""""""""""
class Descriptor():
    """ Ejemplo de clase para uso de descriptores """

    def __init__(self):
        self.var = " "

    def __set__(self,objeto,valor):
        print ("Asignando un valor al atributo")
        self.var = valor

    def __get__(self,objeto,clase):
        print ("Obteniendo el valor de un atributo")
        return self.var

    def __delete__(self,objeto):
        print ("Borrando el atributo")
        del self.var

class Mi_clase():

    mi_atributo = Descriptor()

    def __init__(self,texto):
        self.mi_atributo = texto

"""""""""""""""""""""""""""""""""""""""""""""""""""
            USO DE LAS CLASES
"""""""""""""""""""""""""""""""""""""""""""""""""""

mi_objeto = Mi_clase("hola")

#Get
texto = mi_objeto.mi_atributo

#Set
mi_objeto.mi_atributo = "adios"

#Del
del mi_objeto.mi_atributo

"""Imprimimos el mensaje final por pantalla"""
print (texto)
