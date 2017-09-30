#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  F U N C I O N E S      A N A L I Z A N D O L O S       M E T A D A T O S

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
            PARA DOCUMENTOS PDFs.
    Solicita el nombre del archivo por parámetro.
    
"""""""""""""""""""""""""""""""""""""""""""""""""""
# Importamos los métodos que vamos a utilizar de la librería
from modules.funcionesCore import *
from modules.textoMenu import *
from PyPDF2 import PdfFileReader
import os
from PIL.ExifTags import TAGS
from PIL import Image
from termcolor import colored       #Libreria para colores


# Definimos una funcion que lea los datos de un pdf en concreto
def obtenerMetadatosPDF():
    # Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
    while True:
        # Llamamos a la funcion mostrar_contenido filtrando por extension PDF
        mostrar_conternido('.pdf')
        # Solicitamos el nombre del fichero PDF a analizar
        nombre_fichero = input(colored("\nIntroduzca el nombre del fichero PDF a analizar: ", 'blue'))

        try:
            # El pdf esta situado en el mismo directorio que este script
            # Leemos el archivo
            archivo_pdf = PdfFileReader(nombre_fichero,'rb')

            # Obtenemos la información que queremos
            info_documento = archivo_pdf.getDocumentInfo()
            # Obtenemos el numero de paginas del fichero
            info_numpaginas = archivo_pdf.getNumPages()
            # Consultamos si el fichero esta encryptado
            info_encriptado = archivo_pdf.isEncrypted

            # La imprimimos por pantalla
            print("\n")
            print("###############################################################################")
            print("                         Información metadatos")
            print("###############################################################################")
            print("\n")

            # Recorremos la informacion conseguida en la variable info_documento
            for metadato in info_documento:
                try:
                    print(
                        colored("[+] ", 'yellow') + colored(metadato, 'green') + ":" + colored(info_documento[metadato],
                                                                                               'blue'))
                except:
                    print(colored("\nError en salida del metadato %s" % metadato, 'red'))

            print(
                colored("[+]", 'yellow') + colored("/Numero de Paginas: ", 'green') + colored(info_numpaginas, 'blue'))

            # Comprobamos si el fichero esta encriptado, ya que devuelve True o False lo cambiamos por Si o No
            if info_encriptado:
                ficheroEncriptado = "Si"
            else:
                ficheroEncriptado = "No"

            print(colored("[+]", 'yellow') + colored("/PDF Encriptado: ", 'green') + colored(ficheroEncriptado, 'blue'))

        except:
            print(colored("\nSe ha producido un error. Nombre de fichero invalido.", 'red'))

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            ANALIZANDO LOS METADATOS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                PARA IMÁGENES
"""""""""""""""""""""""""""""""""""""""""""""""""""


def menu_imagenes():
    while True:
        show_banner(define_version, '1')
        ###################################################
        #        USER INPUT: SHOW MAIN MENU               #
        ###################################################
        show_dns_menu = Crear_menu(texto_principal, image_menu)

        opcion_img_menu = (input(colored("Elija una opcion: ",'blue')))

        if opcion_img_menu == '1':  # Analis de Metadatos de una imagen
            #print("Opcion 1.Analisis de Metadatos")
            analisis_imagen()

        if opcion_img_menu == '2':  # Muestra la resolucion de una imagen
            #print("Opcion 2.")
            resolucion_imagen()

        if opcion_img_menu == '3':  # Visualizar imagen
            #print("Opcion 3. Show Image")
            mostrar_imagen()

        if opcion_img_menu == '99':
            break


# Definimos una funcion que lea los datos de una imagen en concreto
def analisis_imagen():
    while True:
        # Llamamos a la funcion para mostrar los ficheros con extension ".jpg"
        mostrar_conternido('.jpg')
        nombre_imagen = input(colored("\nIntroduzca el nombre de la imagen a analizar: ",'blue'))
        try:
            metadatos_exif = {}

            #Abrimos la imagen
            archivo_imagen = Image.open(nombre_imagen)

            #Extraemos la información necesaria de ella, los EXIF
            info = archivo_imagen._getexif()

            # Extraemos la información necesaria de ella, los EXIF
            info = archivo_imagen._getexif()

            # Conseguimos la descripcion del formato
            print(colored("Descripcion del Formato: ", 'cyan') + archivo_imagen.format_description)

            print("\n")
            print("###############################################################################")
            print("                         Información general")
            print("###############################################################################")
            print("\n")
            print(info)

            if info:
                for (tag,value) in info.items():
                    decoded = TAGS.get(tag,tag)
                    metadatos_exif[decoded] = value

                if metadatos_exif:

                    print("\n")
                    print("###############################################################################")
                    print("                         Información metadatos")
                    print("###############################################################################")
                    print("\n")

                    for meta_info in metadatos_exif:
                        print(colored("[+]", 'yellow') + colored(str(nombre_imagen), 'blue') + colored(" Datos: ", 'green') + str(metadatos_exif[meta_info]))

        except:
            print(colored("\nSe ha producido un error. Nombre de fichero invalido.", 'red'))

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


def mostrar_imagen():
    while True:
        mostrar_conternido('.jpg')
        nombre_imagen = input(colored("\nNombre de la imagen a visualizar: ", 'blue'))
        img = Image.open(nombre_imagen)
        img.show()

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


def resolucion_imagen():
    while True:
        print(colored("Resolucion de imagen.", 'cyan', attrs=['bold', 'blink']))
        print("")
        mostrar_conternido('.jpg')
        nombre_imagen = input(colored("\nIntroduzca el nombre de la imagen para mostrar su resolucion: ", 'blue'))

        img = Image.open(nombre_imagen)
        print(img.format, img.size, img.mode)

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


def mostrar_conternido(extension):
    print(colored("\nFiltrando por extension: ", 'green') + colored(extension, 'red', attrs=['bold']))
    for filename in os.listdir('.'):
        if filename.endswith(extension):
            print(colored("Fichero: ", 'green') + colored(filename, 'cyan'))

