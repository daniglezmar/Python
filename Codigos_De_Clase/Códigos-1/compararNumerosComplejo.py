#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Comparacion entre varios numeros para ver si son multiplos
print ("Vamos a comparar dos números: ")
numero1 = int (input("Escribe un primer numero: "))
numero2 = int (input("Escribir un segundo numero: "))

if (numero1 >= numero2 and numero1 % numero2):
    print(numero1, "no es multiplo de", numero2)
elif (numero1 >=numero2 and numero1 % numero2 == 0):
    print (numero1, "es multiplo de", numero2)
elif (numero1 < numero2 and numero2 % numero1):
    print (numero2, "no es multiplo de", numero1)
else:
    print (numero2, "es multiplo de", numero1)
