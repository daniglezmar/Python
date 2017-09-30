#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        ARCHIVO PRINCIPAL DE MATEMÁTICAS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import matematicas.constantes, matematicas.operaciones

radio = 14

radio_cuadrado = matematicas.operaciones.cuadrado(radio)

circunferencia = matematicas.operaciones.multiplica(matematicas.constantes.pi, radio_cuadrado)

print ("El radio de la circunferencia es: ")
print (radio)
print ("Longitud de la circunferencia: ")
print (circunferencia)
