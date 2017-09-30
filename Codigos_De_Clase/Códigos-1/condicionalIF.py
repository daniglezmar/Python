#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Comparacion entre varios numeros
print ("Vamos a comparar dos números: ")
numero1 = int (input("Escribe un primer numero: "))
numero2 = int (input("Escribir un segundo numero: "))

if (numero1 < numero2):
    print ("Menor: ", numero1, "Mayor: ", numero2)
elif (numero1 > numero2):
    print ("Menor: ", numero2, "Mayor: ", numero1)
else:
    print ("Los dos numeros son iguales")
