#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANALIZANDO LOS METADATOS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                PARA IMÁGENES
"""""""""""""""""""""""""""""""""""""""""""""""""""

#Importamos los métodos que vamos a utilizar de la librería
from PIL.ExifTags import TAGS
from PIL import Image

#Definimos una funcion que lea los datos de una imagen en concreto
def analisis_imagen(nombre_imagen):

    metadatos_exif = {}

    #Abrimos la imagen
    archivo_imagen = Image.open(nombre_imagen)

    #Extraemos la información necesaria de ella, los EXIF
    info = archivo_imagen._getexif()

    print("\n")
    print("###############################################################################")
    print("                         Información general")
    print("###############################################################################")
    print("\n")
    print (info)

    if (info):
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
                print ("[+] " + str(nombre_imagen) + " Datos: " + str(metadatos_exif[meta_info]))


"""""""""""""""""""""""""""""""""""""""""""""""""""
                USO DE LA FUNCIÓN
"""""""""""""""""""""""""""""""""""""""""""""""""""

analisis_imagen("jlaw.jpg")
