#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

             B U S C A   E N   L A   R E D 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from funcionesMenu import *


## Variable para bucle, inicializamos en True
loop = True


## Parte Principal
# Hacemos un bloque con la variable loop hasta que usuario introduzca la opcion salida. loop = false
while loop:
    print_menu()  ## Mostramos el menu

    try:
        choice = int(input("\nEnter your choice [1-6]: "))
    except:
        print("Introduzca un numero valido.")
        choice = 10

    if choice == 1:
        print("\nHa seleccionado la opcion 1.")
        entradaUsuario = textoUsuario()
        if entradaUsuario != None:
            menuDNS(entradaUsuario)

    elif choice == 2:
        print("\nHa seleccionado la opcion 2")
        entradaUsuario = textoUsuario()
        if entradaUsuario != None:
            # Llamamos a la funcion menuWHOIS
            menuWhois(entradaUsuario)

    elif choice == 3:
        print("\nHa seleccionado la opcion 3")
        entradaUsuario = textoUsuario()
        if entradaUsuario != None:
            # Llamamos a la funcion menuGEO
            menuGeo(entradaUsuario)

    elif choice == 4:
        print("\nHa seleccionado la opcion 4")
        # Llamamos a la funcion menuMotores
        menuMotorShodan()

    elif choice == 5:
        print("\nHa seleccionado la opcion 5")
        # Llamamos a la funcion menuMotores
        menuFacets()

    elif choice == 6:
        print("\nSaliendo del Menu")
        # Salimos de la aplicacion
        loop = False  # This will make the while loop to end as not value of loop is set to False

    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("\nOpcion incorrecta. \nHaga una nueva seleccion. ")
