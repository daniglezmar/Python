#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            BANNER GRABBING

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import http.client
import socket
from termcolor import colored       #Libreria para colores
import modules.funcionesCore

################################################################
# Funcion para obtener el banner de un puerto para una IP dada #
################################################################


def obtenerBanner(ip_address, puerto):
    try:
        print(colored("Establecemos conexion...", 'cyan'))
        conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexion.connect((ip_address, puerto))
        banner = conexion.recv(1024)
        print(colored("Analizado: ", 'cyan') + colored(str(ip_address), 'green') + colored(" en el puerto ", 'cyan') +
              colored(str(puerto), 'red') + ':' + colored(str(banner), 'green'))

        print(colored("Leemos el archivo.", 'cyan'))
        archivo = open('banners_vulnerables.txt', 'r')
        print(colored("Archivo leido. Vamos a comprobar si es vulnerable", 'cyan', attrs=['bold']))
        for bannervulnerable in archivo:
            if str(bannervulnerable).strip() in str(banner).strip():
                print(colored('El banner SI es vulnerable', 'green', attrs=['bold', 'blink']))
            else:
                print(colored('El banner NO es vulnerable', 'red', attrs=['bold']))

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def vulrenabilidadHTTP():
    while True:
        try:
            # Solicitamos el nombre del dominio a analizar
            host = input(colored("Introduzca el nombre de un dominio: ", 'blue'))
            # Comprobamos el sitio introducido
            conn = http.client.HTTPConnection(host, timeout=2)
            conn.request("HEAD", "/")
            server = conn.getresponse().getheader('server')
            # Leemos el fichero con las vulnerabilidades previamente introducidas (CVE)
            vulnerables = open("vulnerablesHTTP.txt", "r")
            # Inicializamos la variable
            esVulnerable = False

            # Leemos cada una de las posibles vulnerabilidades que hay en el fichero de texto
            for servicio in vulnerables:
                s = servicio.split(" ")
                if (s[0] in server):
                    print(colored(host, 'yellow'), colored("tiene servicio", 'red'), colored(s[0], 'green'),
                          colored("con posible vulnerabilidad", 'red'), colored(s[1], 'green'))
                    esVulnerable = True

            if (not esVulnerable):
                print(colored(host, 'yellow'), colored("aparentemente el servidor no tiene una vulnerabilidad de las "
                                                       "indicadas en el fichero TXT.", 'green'))

            repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
            if repite_consulta == 'n':
                break

        except Exception as e:
            print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def analisisBanner():
    while True:         # Bucle para repetir consulta si se desea
        try:
            ip_address = input(colored("Introduzca una direccion IP: ", 'blue'))
            lista_puertos = input(colored("Introduzca los puertos a analizar, separados por comas: ", 'blue'))
            lista_puertos = lista_puertos.split(",")

            try:
                for puerto in lista_puertos:
                    puerto = int(puerto)
                    print(colored('\nAnalizando la dirección: ', 'blue') + colored(str(ip_address), 'green') +
                          colored(' en el puerto ', 'blue') + colored(str(puerto), 'red'))
                    # Llamamos a la funcion pasando host y puerto a analizar
                    obtenerBanner(ip_address, puerto)

            except:
                print("Error, puerto no valido.")

            repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
            if repite_consulta == 'n':
                break

        except Exception as e:
            print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))
