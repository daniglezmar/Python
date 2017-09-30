#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            ANALIZANDO LOS METADATOS
                            
                     EN FICHEROS DE IMAGENES Y FICHEROS PDF

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import re
# Importamos los métodos que vamos a utilizar de la librería
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
# Importamos los métodos que vamos a utilizar de la librería
from PIL.ExifTags import TAGS
from PIL import Image
from termcolor import colored       #Libreria para colores


texto_principal = "Selecciona una opcion del Menu: "

menu_principal = ['Analizar Metadatos de un fichero PDF.',
                  'Analizar Metadatos de una imagen.']

imagen_menu = ['Extraer Metadatos de una imagen.',
              'Mostrar resolucion.',
              'Mostart Imagen selccionada.',
              '0D']

# Clase Crear_menu
class Crear_menu:
    def __init__(self, text, menu):
        self.text = text
        self.menu = menu
        print(colored(text,'blue'))

        # Recorremos las opciones del array que contiene las distintas opcines del menu
        for i, option in enumerate(menu):
            menunum = i + 1
            # Check to see if this line has the 'return to main menu' code
            match = re.search("0D", option)
            # If it's not the return to menu line:
            if not match:
                print(colored(('   %s) %s' % (menunum, option)),'green'))
            else:
                print(colored('\n  99) Volver al Menu Principal\n','magenta'))
        return


# Definimos una funcion que lea los datos de un pdf en concreto
def obtenerMetadatosPDF():
    # Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
    while True:
        # Llamamos a la funcion mostrar_contenido filtrando por extension PDF
        mostrar_conternido('.pdf')
        # Solicitamos el nombre del fichero PDF a analizar
        nombre_fichero = input(colored("\nIntroduzca el nombre del fichero PDF a analizar: ",   'yellow'))

        try:
            # El pdf esta situado en el mismo directorio que este script
            # Leemos el archivo
            archivo_pdf = PdfFileReader(nombre_fichero, 'rb')

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
                    print(colored("[+] ", 'yellow') + colored(metadato, 'green') + ":" + colored(info_documento[metadato], 'blue'))
                except:
                    print(colored("\nError en salida del metadato %s" %metadato,'red'))

            print(colored("[+]",'yellow') + colored("/Numero de Paginas: ",'green') + colored(info_numpaginas, 'blue'))

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

def obtenerMetadatosIMG():
    while True:
        ###################################################
        #        USER INPUT: SHOW MAIN MENU               #
        ###################################################
        show_dns_menu = Crear_menu(texto_principal, imagen_menu)

        opcion_img_menu = (input(colored("Elija una opcion: ", 'yellow')))

        if opcion_img_menu == '1':  # Analis de Metadatos de una imagen
            #print("\nOpcion 1.Analisis de Metadatos")
            analisis_imagen()

        if opcion_img_menu == '2':  # Muestra la resolucion de una imagen
            #print("\nOpcion 2. Resolucion de Imagen")
            resolucion_imagen()

        if opcion_img_menu == '3':  # Mostrar imagen
            #print("\nOpcion 3. Muestra imagen.")
            mostrar_imagen()

        if opcion_img_menu == '99':
            break


# Definimos una funcion que lea los datos de una imagen en concreto
def analisis_imagen():
    while True:
        # Llamamos a la funcion para mostrar los ficheros con extension ".jpg"
        mostrar_conternido('.jpg')
        nombre_imagen = input(colored("\nIntroduzca el nombre de la imagen a analizar: ", 'blue'))
        try:
            metadatos_exif = {}

            #Abrimos la imagen
            archivo_imagen = Image.open(nombre_imagen)

            #Extraemos la información necesaria de ella, los EXIF
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
                        print(colored("[+]", 'yellow') + colored(str(nombre_imagen), 'blue') + colored(" Datos: ",
                                'green') + str(metadatos_exif[meta_info]))

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
        print(colored("\nResolucion de imagen.", 'yellow'))
        mostrar_conternido('.jpg')
        nombre_imagen = input(colored("\nIntroduzca el nombre de la imagen para mostrar su resolucion: ", 'cyan'))

        img = Image.open(nombre_imagen)
        print(img.format, img.size, img.mode)

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system


def mostrar_conternido(extension):
    print(colored("\nFiltrando por extension: ", 'green') + colored(extension, 'red', attrs=['bold']))
    for filename in os.listdir('.'):
        if filename.endswith(extension):
            print(colored("Fichero: ", 'green') + colored(filename, 'yellow'))


def show_banner(graphic):
    if graphic == "1":
        if check_os() == "posix":
            os.system("clear")
        if check_os() == "windows":
            os.system("cls")
        show_graphic()
    else:
        os.system("clear")

    print("""
    [---] """ + colored("       Herramienta para el Analisis de Metadatos ", 'red') + colored("(AM)", 'yellow') + """      [---]
    [---] """ + colored("         Creado por:", 'green') + colored("Daniel Gonzalez Martinez DGM", 'magenta') + """           [---]
    [---] """ + colored("                   Version: ", 'blue') + colored("1.0", 'blue') + """                            [---]
    [---] """ + colored("         Homepage: ", 'blue') + colored("https://www.EstamoEnEllo.com", 'magenta') + """            [---]
          """ + colored("  Bienvenidos a la herramienta de Analisis de Metadatos  (AM).", 'yellow') + """   
    """)


def show_graphic():
    print(colored(r"""    
     _                _ _     _           _        __  __      _            _       _            
    / \   _ __   __ _| (_)___(_)___    __| | ___  |  \/  | ___| |_ __ _  __| | __ _| |_ ___  ___ 
   / _ \ | '_ \ / _` | | / __| / __|  / _` |/ _ \ | |\/| |/ _ \ __/ _` |/ _` |/ _` | __/ _ \/ __|
  / ___ \| | | | (_| | | \__ \ \__ \ | (_| |  __/ | |  | |  __/ || (_| | (_| | (_| | || (_) \__ \
 /_/   \_\_| |_|\__,_|_|_|___/_|___/  \__,_|\___| |_|  |_|\___|\__\__,_|\__,_|\__,_|\__\___/|___/
                                                                                                 
        """,'yellow', attrs=['bold']))
    return
