#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Importamos los modulos/librerias necesarias
from scapy.all import *
import logging
import modules.funcionesCore
from modules.textoMenu import *
from termcolor import colored

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # Que no muestre warning

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANÁLISIS DE VULNERABILIDADES

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Funcion Principal, llamada desde el Menu principal del fichero vulnaSearch
def analisis_scapy():
    # Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
    while 1:
        try:
            # Capturamos la version de la aplicacion
            define_version = modules.funcionesCore.get_version()
            modules.funcionesCore.show_banner(define_version, '1')
            ###################################################
            #        USER INPUT: SHOW MAIN MENU               #
            ###################################################
            show_scapy_menu = Crear_menu(texto_principal, menu_principal_scapy)

            menu_scapy = (input(colored("Elija una opcion: ", 'blue')))

            if menu_scapy == 'exit':
                break

            if menu_scapy == '1':  # Opcion Escaneo ACK
                while True:
                    print(colored("Opcion 1.Escaneo ACK.", 'magenta', attrs=['bold', 'blink']))
                    escaneoACK()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_scapy == '2':  # Opcion Escaneo TCP
                print(colored("Opcion 2. Escaneo TCP", 'magenta', attrs=['bold', 'blink']))
                while True:
                    escaneoTCP()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_scapy == '3':  # Opcion 3. Escaneo UDP
                print(colored("Opcion 3. Escaneo UDP.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    escaneoUDP()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_scapy == '4':  # 'Opcion 4. Escaneo NULL
                print(colored("Opcion 4. Escaneo NULL.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    escaneoNull()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_scapy == '5':  # 'Opcion Escaneo XMAS
                print(colored("Opcion 5. Escaneo XMAS.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    #dom_usuario = textoUsuario()
                    escaneoXmas()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_scapy == '99':
                break

        except:
            print('Ups! Ha ocurrido un error: %s' % Exception)
            input(colored("Pulse INTRO para continuar.", 'red', attrs=['bold', 'blink']))
            break


"""""""""""""""""""""""""""""""""""""""""""""""""""

              ESCANEO ACK

"""""""""""""""""""""""""""""""""""""""""""""""""""


def escaneoACK():
    try:
        # Capturamos direccion del equipo a analizar
        ip_destino = entrada_ip()
        # Capturamos los puertos a analizar
        scanPorts = entada_puertos_scapy()

        print(colored("IP a escanear: ", 'yellow') + colored(str(ip_destino), 'green'))
        print(colored("Puerto/s a escanear: ", 'yellow') + colored(str(scanPorts), 'green'))

        for puerto in scanPorts:
            print(colored("Analizando puerto: ", 'yellow') + colored(str(puerto), 'green'))
            syn_packet = IP(dst=ip_destino) / TCP(dport=int(puerto), flags='A')
            response = sr1(syn_packet)
            print(colored("Respuesta del tipo: ", 'yellow') + colored(str(type(response)), 'green'))

            if str(type(response)) == "<class 'NoneType'>":
                print(colored("[+] Encontrado firewall", 'red'))
            elif response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x4:
                    print(colored("[-] No encontrado firewall", 'green', attrs=['bold', 'blink']))
            elif response.haslayer(ICMP):
                if response.getlayer(ICMP).type == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                    print(colored("[+] Encontrado firewall", 'red'))

    except KeyboardInterrupt:  # In case the user wants to quit
        print("\n[*] Operacion cancelada por usuario...")

    except:
        print("Se ha producido un error.")


"""""""""""""""""""""""""""""""""""""""""""""""""""

               ESCANEO TCP

"""""""""""""""""""""""""""""""""""""""""""""""""""


def escaneoTCP():
    try:
        # Capturamos direccion del equipo a analizar
        ip_destino = entrada_ip()
        # Capturamos los puertos a analizar
        scanPorts = entada_puertos_scapy()
        puerto_origen = RandShort()

        print(colored("IP a escanear: ", 'yellow') + colored(str(ip_destino), 'green'))
        print(colored("Puerto/s a escanear: ", 'yellow') + colored(str(scanPorts), 'green'))

        for i in scanPorts:
            print(colored("Analizando puerto: ", 'blue') + colored(str(i), 'green'))
            response = sr1(IP(dst=ip_destino) / TCP(dport=int(i), flags="S"), timeout=3)
            #response = sr1(IP(dst=ip_destino) / TCP(dport=int(i), flags="S"), timeout=3)
            print(colored("Respuesta del tipo: ", 'blue') + colored(str(type(response)), 'green'))

            if (str(type(response)) == "<class 'NoneType'>"):
                print(colored("[-] Puerto ", 'yellow') + colored(i, 'red') + colored(" cerrado", 'red'))

            elif (response.haslayer(TCP)):
                if (response.getlayer(TCP).flags == 0x12):
                    print(colored("[+] Puerto ", 'yellow') + colored(i, 'red') + colored(" abierto", 'green'))

            elif (response.haslayer(ICMP)):
                if (response.getlayer(TCP).flags == 0x14):
                    print(colored("[-] Puerto ", 'yellow') + colored(i, 'red') + colored(" cerrado", 'magenta'))

    except KeyboardInterrupt:  # In case the user wants to quit
        print("\n[*] Operacion cancelada por usuario...")

    except:
        print("Se ha producido un error.")


"""""""""""""""""""""""""""""""""""""""""""""""""""

             ESCANEO UDP

"""""""""""""""""""""""""""""""""""""""""""""""""""


def escaneoUDP():
    try:
        # Capturamos direccion del equipo a analizar
        ip_destino = entrada_ip()
        # Capturamos los puertos a analizar
        scanPorts = entada_puertos_scapy()

        print(colored("IP a escanear: ", 'yellow') + colored(str(ip_destino), 'green'))
        print(colored("Puerto/s a escanear: ", 'yellow') + colored(str(scanPorts), 'green'))

        for i in scanPorts:
            print(colored("Analizando puerto: ", 'blue') + colored(str(i), 'green'))
            response = sr1(IP(dst=ip_destino)/UDP(dport=int(i)), timeout=3)
            print(colored("Respuesta del tipo: ", 'blue') + colored(str(type(response)), 'green'))

            if (str(type(response))=="<class 'NoneType'>"):
                print(colored("Tipo de clase Nonetype", 'yellow'))
                print(colored("No se ha recibo ningun paquete.", 'yellow'))
            elif (response.haslayer(UDP)):
                print(colored("[+] Puerto ", 'yellow') + colored(i, 'blue') + colored(" abierto", 'green', attrs=['blink']))
                #print ("[+] Puerto " + i + " abierto")
            elif (response.haslayer(ICMP)):
                if (int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code==3)):
                    print(colored("[-] Puerto ", 'yellow') + colored(i, 'blue') + colored(" cerrado", 'red'))

                elif (int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,9,10,13]):
                    print(colored("[-] Puerto ", 'yellow') + colored(i, 'blue') + colored(" filtrado", 'magenta'))

    except KeyboardInterrupt:  # In case the user wants to quit
        print("\n[*] Operacion cancelada por usuario...")

    except:
        print("Se ha producido un error.")


"""""""""""""""""""""""""""""""""""""""""""""""""""

              ESCANEO NULL

"""""""""""""""""""""""""""""""""""""""""""""""""""


def escaneoNull():
    try:
        # Capturamos direccion del equipo a analizar
        ip_destino = entrada_ip()
        # Capturamos los puertos a analizar
        scanPorts = entada_puertos_scapy()

        print(colored("IP a escanear: ", 'yellow') + colored(str(ip_destino), 'green'))
        print(colored("Puerto/s a escanear: ", 'yellow') + colored(str(scanPorts), 'green'))

        for i in scanPorts:
            print(colored("Analizando puerto: ", 'blue') + colored(str(i), 'green'))
            response = sr1(IP(dst=ip_destino) / TCP(dport=int(i), flags=""), timeout=3)
            print(colored("Respuesta del tipo: ", 'blue') + colored(str(type(response)), 'green'))

            if str(type(response) == "<class 'NoneType'>"):
                print(colored("[+] Puerto %s Abierto " % i, 'green'))

            elif response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x14:
                    print(colored("[-] Puerto %s Cerrado " % i, 'magenta'))

            elif response.haslayer(ICMP):
                if response.getlayer(ICMP).type == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                    print(colored("[x] Puerto %s Filtrado " % i, 'green'))

    except KeyboardInterrupt:  # In case the user wants to quit
        print("\n[*] Operacion cancelada por usuario...")

    except:
        print("Se ha producido un error.")


"""""""""""""""""""""""""""""""""""""""""""""""""""
                    ESCANEO XMAS
"""""""""""""""""""""""""""""""""""""""""""""""""""


def escaneoXmas():
    try:
        # Capturamos direccion del equipo a analizar
        ip_destino = entrada_ip()
        # Capturamos los puertos a analizar
        scanPorts = entada_puertos_scapy()

        print(colored("IP a escanear: ", 'yellow') + colored(str(ip_destino), 'green'))
        print(colored("Puerto/s a escanear: ", 'yellow') + colored(str(scanPorts), 'green'))

        for i in scanPorts:
            response = sr1(IP(dst=ip_destino)/TCP(dport=int(i), flags="FPU"), timeout=3)
            if response is None:
                print(colored("[+] Puerto %s Abierto o filtrado " % (i), 'green'))

            elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                print(colored("[-] Puerto %s Cerrado " % (i), 'magenta'))

            elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3:
                print(colored("[x] Puerto %s Filtrado " % (i), 'green'))

            else:
                print(colored("Puerto invalido", 'red'))

    except KeyboardInterrupt:  # In case the user wants to quit
        print("\n[*] Operacion cancelada por usuario...")

    except:
        print("Se ha producido un error.")
