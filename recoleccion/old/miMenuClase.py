#!/usr/bin/env python
#
import os
from miFuncionesMenu import *
from misetcore import *
import mitext

#########################################
# Menu de Busquedas en Red              #
# Escrito por: Daniel Gonzalez (DGM)    #
#########################################
#
# Parte principal

# Capturamos la version de la aplicacion
define_version = get_version()

try:
    while 1:
        # Llamamos al Banner
        show_banner(define_version, '1')
        # Creamos un objeto de la clase Menu. Le pasamos el texto del fichero mitext.py
        show_main_menu = create_menu(mitext.main_text, mitext.main_menu)

        # Caso especial del elemento de lista 99
        print('\n  99) Salir del Script: Busca en Red.\n')

        # Carga del Menu Principal manera Standard (sin nada especial)
        #main_menu_choice = (raw_input(setprompt("0", "")))
        #main_menu_choice = (raw_input(definePregunta("")))

        # Salir de la aplicacion
        if main_menu_choice == 'exit' or main_menu_choice == "99" or main_menu_choice == "quit":
            exit_program()

        # Carga Opcion 1
        if main_menu_choice == '1':
            print ("Menu DNS")
            menuDNS()

        # Carga Opcion 2
        if main_menu_choice == '2':
            print("Opcion 2")

        # Carga Opcion 3
        if main_menu_choice == '3':
            print("Opcion 3")

        # Carga Opcion 4
        if main_menu_choice == '4':
            print("Opcion 4")

        # Carga Opcion 5
        if main_menu_choice == '5':
            print("Opcion 5")

        # Carga Opcion 6
        if main_menu_choice == '6':
            print("Opcion 6")

# handle keyboard interrupts
except KeyboardInterrupt:
    print(("\n\nGracias por " + bcolors.RED + "utilizar la herramineta" + bcolors.ENDC +
           " Busca en Red.\n\nSeguimos trabajando en ello.\n"))

# handle exceptions
except Exception as error:
    log(error)
    print ("\n\n[!] Algo fue mal, mostrando error por pantalla: "+ str(error))
