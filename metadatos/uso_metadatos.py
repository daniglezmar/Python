#!/usr/bin/env python

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANALIZANDO LOS METADATOS

                     EN FICHEROS DE IMAGENES Y FICHEROS PDF

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from metadatos import *
from termcolor import colored       #Libreria para colores
import argparse

# ArgumentParser con una descripción de la aplicación
parser = argparse.ArgumentParser(description='%(prog)s es una herramienta de anlisis de metadatos.')

# Añadimos un argumento opcional
parser.add_argument("--verbose", help="Activamos la depuracion de la aplicacion",
                    action="store_true")
args = parser.parse_args()
# Comprobamos si le hemos pasado el argumento --verbosity
if args.verbose:
    print("\nDepuramos activada. Proximamente... ;)")

# Hacemos un bucle para volver al Menu Principal si no se elige una de las opciones ofrecidas
while 1:
    try:
        #Llamamos al banner
        show_banner('1')
        # Creamos un objeto de la Clase Crear_Menu y le pasamos el texto ya prefijado en el modulo metadatos.py
        Crear_menu(texto_principal, menu_principal)

        # Caso especial del elemento de lista 99
        print(colored('\n  99) Salir del Script.\n','yellow',attrs=['bold']))

        # Carga del Menu Principal manera Standard (sin nada especial)
        eleccion_menu_prin = input(colored("Elija una opcion: ", 'magenta', attrs=['bold']))

        # Salir de la aplicacion
        if eleccion_menu_prin == 'exit' or eleccion_menu_prin == "99" or eleccion_menu_prin == "quit":
            break

        # Llama a la funcion obtenerMetadatosPDF
        if eleccion_menu_prin == '1':
            obtenerMetadatosPDF()

        # Llama a la funcion obtenerMetadatosIMG
        if eleccion_menu_prin == '2':
            obtenerMetadatosIMG()

    # Capturamos alguna excepcion ocurrida
    except Exception as error:
        print(colored(error,'yellow',attrs=['bold']))
        print(colored("\n\n[!] Algo fue mal, mostrando error por pantalla: " + str(error),'red',attrs=['bold']))
        break