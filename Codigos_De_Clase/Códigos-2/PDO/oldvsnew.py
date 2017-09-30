#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        EJEMPLO DE CLASES OLD VS NEW STYLE

            Si se ejecuta con python2 se verá la diferencia entre old y new style
            Si se ejecuta con python3 se verá que el problema de las clases esta resuelto.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
            DEFINICION DE LAS CLASES
"""""""""""""""""""""""""""""""""""""""""""""""""""

class Old_style:
    """Ejemplo de clase old style"""

    def __init__(self,cadena):
        self.texto = cadena

    def mostrar (self):
        return self.texto

class New_style(object):
    """Ejemplo de clase new style"""

    def __init__(self,cadena):
        self.texto = cadena

    def mostrar (self):
        return self.texto

"""""""""""""""""""""""""""""""""""""""""""""""""""
            USO DE LAS CLASES
"""""""""""""""""""""""""""""""""""""""""""""""""""

vieja = Old_style("Hola, soy un objeto de la clase old style")
nueva = New_style("Hola, soy un objeto de la clase new style")

vieja.mostrar()
print (type(vieja))

nueva.mostrar()
print (type (nueva))
#Mostrará <class '__main__.Nuevo_Estilo'>
