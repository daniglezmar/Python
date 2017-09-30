#!/usr/bin/env python
#
# Importamos los modulos/librerias necesarias
from modules.funcionesRInf import *
import modules.funcionesCore
from modules.textoMenu import *
from modules.funcionesMeta import *
from termcolor import colored       #Libreria para colores

#########################################
#                                       #
# Menu de Recoleccion de Informacion    #
# Escrito por: Daniel Gonzalez (DGM)    #
#                                       #
#########################################
#
# Parte principal

# Capturamos la version de la aplicacion
define_version = modules.funcionesCore.get_version()

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


# Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
while 1:
    try:
        # Llamamos al Banner pasandole la version de la aplicacion.
        show_banner(define_version, '1')
        # Creamos un objeto de la clase Menu. Le pasamos el texto del fichero mitext.py con las opciones
        muestra_menu_principal = Crear_menu(texto_principal, menu_principal)

        # Caso especial del elemento de lista 99
        print(colored('\n  99) Salir del Script.\n','magenta'))

        # Carga del Menu Principal manera Standard (sin nada especial)
        eleccion_menu_prin = input(colored("Elija una opcion: ",'blue'))

        # Salir de la aplicacion
        if eleccion_menu_prin == 'exit' or eleccion_menu_prin == "99" or eleccion_menu_prin == "quit":
            exit_program()

        # Llama a la funcion menuDNS
        if eleccion_menu_prin == '1':
            menuDNS()

        # Llama a la funcion menuWHOIS
        if eleccion_menu_prin == '2':
            menuWhois()

        # Llama a la funcion menuGEO
        if eleccion_menu_prin == '3':
            menuGeo()

        # Llama a la funcion menuMotorShodan
        if eleccion_menu_prin == '4':
            menuMotorShodan()

        # Llama a la funcion Facets de Shodan
        if eleccion_menu_prin == '5':
            print("Facets de Shodan")
            menuFacets()

        # Llama a la funcion obtenerMetadatosPDF
        if eleccion_menu_prin == '6':
            obtenerMetadatosPDF()

        # Llama a la funcion menu_imagenes
        if eleccion_menu_prin == '7':
            menu_imagenes()

    # Capturamos una interrucion por teclado (Control+C)
    except KeyboardInterrupt:
        print(("\n\nGracias por " + bcolors.RED + "utilizar la herramineta" + bcolors.ENDC +
               " Busca en Red.\n\nSeguimos trabajando en ello.\n"))
        # Salimos del bucle While
        break

    # Capturamos alguna excepcion ocurrida
    except Exception as error:
        print(error)
        print("\n\n[!] Algo fue mal, mostrando error por pantalla: " + str(error))
        input("Pulse INTRO para volver al Menu Principal.")