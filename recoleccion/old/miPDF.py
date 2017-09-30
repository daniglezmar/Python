#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos los métodos que vamos a utilizar de la librería
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

while True:
    nombre_fichero = input("Introduzca el nombre del fichero PDF a analizar: ")
    # El pdf esta situado en el mismo directorio que este script
    # Leemos el archivo
    try:
        #PyPDF2.PdfFileReader(open(nombre_fichero, "rb"))
        #archivo_pdf = PdfFileReader(nombre_fichero, 'rb')
        input1 = PdfFileReader(file(nombre_fichero, "rb"))

        print(input1)

        #pdfOne = PdfFileReader(file("..\" + nombre_fichero, "rb"))

        # Obtenemos la información que queremos
        info_documento = archivo_pdf.getDocumentInfo()

        # La imprimimos por pantalla

        print("\n")
        print("###############################################################################")
        print("                         Información metadatos")
        print("###############################################################################")
        print("\n")

        for metadato in info_documento:
            print ("[+] " + metadato + ":" + info_documento[metadato])

    except:
        print("invalid PDF file")

    repite_consulta = input("Desea repetir la consulta? (s/n): ")
    if repite_consulta == 'n':
        break
