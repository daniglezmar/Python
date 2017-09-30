###########################################################################################
#######   Dada una lista vamos a calcular la suma y la multiplicacion de sus elemenetos
###########################################################################################
'''
Otra forma de poner comentarios entre 3 comillas
'''

# definimos una lista
lista_numero = (1,2,3,4)

#definimos la funciona suma
def suma(lista):
    sum=0
    for i in lista:
        sum=sum+i
    return sum

#definimos la funcion multiplicacion
def multiplicacion(lista):
    multi=1
    for i in lista_numero:
        multi=multi*i
    return multi

print("La suma de la lista es %s" %suma(lista_numero))
print("La multiplicacion de la lista es %s" %multiplicacion(lista_numero))


