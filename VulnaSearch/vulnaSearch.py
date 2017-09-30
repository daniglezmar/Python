#!/usr/bin/env python
#
# Importamos los modulos/librerias necesarias

from modules.uso_nmap_mio import *
from modules.uso_scapy import *
from modules.uso_banner_mio import *
from modules.textoMenu import *
import modules.funcionesCore
from termcolor import colored       #Libreria para colores
import argparse

#########################################
#                                       #
# Menu de Analisis de Vulnerabilidades  #
# Escrito por: Daniel Gonzalez (DGM)    #
#                                       #
#########################################
#
# Parte principal

# Capturamos la version de la aplicacion
define_version = modules.funcionesCore.get_version()

# ArgumentParser con una descripción de la aplicación
parser = argparse.ArgumentParser(description='%(prog)s es una herramienta de anlisis de Vulnerabilidades.')

# Añadimos un argumento opcional
parser.add_argument("--verbose", help="Activamos la depuracion de la aplicacion",
                    action="store_true")
args = parser.parse_args()
# Comprobamos si le hemos pasado el argumento --verbosity
if args.verbose:
    print(colored("\nDepuramos activada. Proximamente... ;)", 'green'))


# Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
while 1:
    try:
        # Llamamos al Banner pasandole la version de la aplicacion.
        show_banner(define_version, '1')
        # Creamos un objeto de la clase Menu. Le pasamos el texto del fichero mitext.py con las opciones
        muestra_menu_principal = Crear_menu(texto_principal, menu_principal)

        # Caso especial del elemento de lista 99
        print(colored('\n  99) Salir del Script.\n', 'yellow'))

        # Carga del Menu Principal manera Standard (sin nada especial)
        eleccion_menu_prin = input(colored("Elija una opcion: ", 'blue'))

        # Salir de la aplicacion
        if eleccion_menu_prin == 'exit' or eleccion_menu_prin == "99" or eleccion_menu_prin == "quit":
            exit_program()

        # Llama a la funcion para analasis de vulnerabilidades con scapy
        if eleccion_menu_prin == '1':
            analisis_scapy()

        # Llama a la funcion para analasis de vulnerabilidades con nmap
        if eleccion_menu_prin == '2':
            analisis_nmap()

        # Llama a la funcion para analasis de vulnerabilidades en Banner
        if eleccion_menu_prin == '3':
            analisisBanner()

        # Llama a la funcion vulrenabilidadHTTP
        if eleccion_menu_prin == '4':
            vulrenabilidadHTTP()

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
