#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANALIZANDO LOS METADATOS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
            PARA DOCUMENTOS PDFs
        Sería interesante pasar el nombre
        del archivo por parámetro.
            Probadlo ;)
"""""""""""""""""""""""""""""""""""""""""""""""""""

#Importamos los métodos que vamos a utilizar de la librería
from PyPDF2 import PdfFileReader, PdfFileWriter

#Definimos una funcion que lea los datos de un pdf en concreto
def obtenerMetadatos():
    #El pdf esta situado en el mismo directorio que este script
    #Leemos el archivo
    archivo_pdf = PdfFileReader('Tem.pdf','rb')

    #Obtenemos la información que queremos
    info_documento = archivo_pdf.getDocumentInfo()

    #La imprimimos por pantalla

    print("\n")
    print("###############################################################################")
    print("                         Información metadatos")
    print("###############################################################################")
    print("\n")

    for metadato in info_documento:
        print ("[+] " + metadato + ":" + info_documento[metadato])

"""""""""""""""""""""""""""""""""""""""""""""""""""
                USO DE LA FUNCIÓN
"""""""""""""""""""""""""""""""""""""""""""""""""""

obtenerMetadatos()
