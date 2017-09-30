#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Suma todos los números del 1 al 100 y mostrar la suma final

"""

"""

Utilizando el bucle while

"""

total_suma=0
i=0
while (i<100):
    total_suma+=i #total_suma = total_suma + i
    i+=1
print (total_suma)

"""

Utilizando el iterador for

"""

total_suma_for=0
for i in range(0,100,1):
    total_suma_for+=i
print (total_suma_for)
