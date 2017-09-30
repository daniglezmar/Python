#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        EJEMPLO ANIMALES Y PERROS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
            DEFINICION DE LAS CLASES
"""""""""""""""""""""""""""""""""""""""""""""""""""

class Patas():

    def _init__(self):
        self.patas = 0

    def __get__(self, objeto, owner):
        return self.patas

    def __set__(self, objeto, value):
        try:
            self.patas = int(value)
        except ValueError:
            print ("No es un entero")
            self.patas = 0

    def __delete__(self,objeto):
        del self.patas

class Animal():

    patas = Patas()

    def __init__(self,nombre,patas):
        self.nombre = nombre
        self.patas = patas

    def muestra(self):
        print ("El " + self.nombre + " tiene " + str(self.patas) + " patas.")


"""""""""""""""""""""""""""""""""""""""""""""""""""
            USO DE LAS CLASES
"""""""""""""""""""""""""""""""""""""""""""""""""""

#Caso de prueba de error
bingo = Animal ("perro", "A")
bingo.muestra()

bingo_sinfallos = Animal("perro de verdad", 4)
bingo_sinfallos.muestra()

"""""""""""""""""""""""""""""""""""""""""""""""""""
Ahora, gracias a nuestro descriptor Patas(), tenemos un manejo de excepciones
al asignar un valor al atributo patas de la clase Animal, que impide introducir
valores no enteros.
"""""""""""""""""""""""""""""""""""""""""""""""""""
