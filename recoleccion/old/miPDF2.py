#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def obtenerMetadatos():
    while True:
        # Listado de los fichero PDF en el directorio de ejecucion.
        print("Listado de fichero PDF encontrados en el directorio de ejecucion:")
        pdfFiles = []
        for filename in os.listdir('.'):
            if filename.endswith('.pdf'):
                print("Fichero: " + filename)

        nombre_fichero = input("Introduzca el nombre del fichero PDF a analizar: ")

        # Le pasamos a la funcion el fichero introducido por el usuario
        #obtenerMetadatos(nombre_fichero)
        try:
            # El pdf esta situado en el mismo directorio que este script
            # Leemos el archivo
            archivo_pdf = PdfFileReader(nombre_fichero,'rb')

            # Obtenemos la información que queremos
            info_documento = archivo_pdf.getDocumentInfo()
            info_numpaginas = archivo_pdf.getNumPages()
            info_encriptado = archivo_pdf.isEncrypted

            # La imprimimos por pantalla

            print("\n")
            print("###############################################################################")
            print("                         Información metadatos")
            print("###############################################################################")
            print("\n")

            for metadato in info_documento:
                try:
                    print ("[+] " + metadato + ":" + info_documento[metadato])
                except:
                    print("Error en salida del metadato %s" %metadato)

            print("[+] /Numero de Paginas: %s" %info_numpaginas)
            if info_encriptado:
                ficheroEncriptado = "Si"
            else:
                ficheroEncriptado = "No"

            print("[+] /PDF Encriptado: %s" %ficheroEncriptado)

        except:
            print("Se ha producido un error.")


        repite_consulta = input("Desea repetir la consulta? (s/n): ")
        if repite_consulta == 'n':
            break


##############################################
#   Parte Principal
##############################################
#
obtenerMetadatos()