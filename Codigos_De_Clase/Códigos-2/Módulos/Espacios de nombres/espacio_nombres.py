#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            USO DEL ESPACIO DE NOMBRES

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import primero,segundo

variable = "Estoy en el programa principal"

def funcion_ejemplo():
    """Funcion que muestra un texto de ejemplo"""
    print (variable)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    CASO DE USO
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

print ("Llamamos a la función de este mismo módulo")
funcion_ejemplo()

print ("Llamamos a la función del módulo primero")
primero.funcion_ejemplo()

print ("Llamamos a la función del módulo segundo")
segundo.funcion_ejemplo()
