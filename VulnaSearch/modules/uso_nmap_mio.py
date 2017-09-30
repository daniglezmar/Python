#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                                USO DE NMAP

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import nmap
import modules.funcionesCore
from modules.textoMenu import *
from termcolor import colored       #Libreria para colores
import sys


def analisis_nmap():
    # Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
    while 1:
        try:
            # Capturamos la version de la aplicacion
            define_version = modules.funcionesCore.get_version()
            modules.funcionesCore.show_banner(define_version, '1')
            ###################################################
            #        USER INPUT: SHOW MAIN MENU NMAP              #
            ###################################################
            muestra_nmap_menu = Crear_menu(texto_principal, menu_principal_nmap)

            menu_nmap = (input(colored("Elija una opcion: ", 'blue')))

            if menu_nmap == 'exit':
                break

            if menu_nmap == '1':  # Opcion 1. Uso de nmap con formato Escaneo rango de puerto Host.
                while True:
                    print(colored("Opcion 1. Uso de nmap con formato.", 'magenta', attrs=['bold', 'blink']))
                    escaneo_uso_nmap()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '2':  # 'Opcion 2. Escaneo de red Rapido
                print(colored("Opcion 2. Escaneo de RED.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    escanedo_red()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '3':  # 'Opcion 3. Escaneo de red Asincrono (mas lento)
                print(colored("Opcion 3. Escaneo de Red Asincrono.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    escanedo_red_completo()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '4':  # Opcion 4. Escaneo con smb-os-discovery.
                while True:
                    print(colored("Opcion 4. Escaneo con smb-os-discovery..", 'magenta', attrs=['bold', 'blink']))
                    script_smb_os_discovery_2()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '5':  # Opcion 5. Escaneo con Script address-info
                print(colored("Opcion 5. Escaneo con Script address-info.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    script_address_info_2()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '6':  # Opcion 6. Analisis Banner con NMAP
                print(colored("Opcion 6. Analisis Banner con NMAP.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    analisis_banner_script()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '7':  # Opcion 7. Escaneo con script de clase
                print(colored("Opcion 7. Uso de nmap (Script Clase).", 'magenta', attrs=['bold', 'blink']))
                while True:
                    analisis_nmap_puertos()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if menu_nmap == '99':
                break

        except:
            print('Ups! Ha ocurrido un error: %s' % Exception)
            input(colored("Pulse INTRO para continuar.", 'red', attrs=['bold', 'blink']))
            break


"""""""""""""""""""""""""""""""""""""""""""""""""""

              ESCANEOS CON NMAP

"""""""""""""""""""""""""""""""""""""""""""""""""""


def escaneo_uso_nmap():
    try:
        nm = nmap.PortScanner()  # instantiate nmap.PortScanner object
        # Capturamos la informacion necesaria para el escaneo, direccion IP y puertos a analizar
        host = entrada_ip()
        rango_puertos = entada_puertos()

        # Comprobamos si el rango esta en una lista
        if isinstance(rango_puertos, list):
            rango_puertos = ",".join(rango_puertos)

        nm.scan(host, rango_puertos)
        print("")
        print(colored("\nLinea de comandos nmap", 'magenta'))
        # Conseguimos la linea de comandos a ejecutar en nmap para sacar el mismo resultado.
        print(nm.command_line())
        print("")

        for port in nm[host]['tcp']:
            thisDict = nm[host]['tcp'][port]
            print(colored('   Puerto Abierto Econtrado - Informacion Detallada', 'cyan'))
            print(colored('\n\tPuerto : %s \n\tEstado : %s \n\tProducto : %s \n\tVersion : %s', 'green') %
                  (str(port), thisDict['state'], thisDict['product'], thisDict['version']))
            print('')

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def analisis_nmap_puertos():
    try:
        nm = nmap.PortScanner()  # instantiate nmap.PortScanner object
        # Capturamos la informacion necesaria para el escaneo, direccion IP y puertos a analizar
        ip = entrada_ip()
        puertos = entada_puertos()

        print(colored("Puertos a escanear: ", 'green', attrs=['bold']) + puertos)
        print(colored("IP a escanear: ", 'green', attrs=['bold']) + ip)
        resultados=nm.scan(ip, puertos)

        print(colored("\n***************************** ", 'red', attrs=['bold', 'blink']))
        print(colored("\t SCAN INFO ", 'green', attrs=['bold', 'blink']))
        print(colored("***************************** \n", 'red', attrs=['bold', 'blink']))

        print(nm.scaninfo())

        print(colored("\n***************************** ", 'red',attrs=['bold', 'blink']))
        print(colored("\t COMMAND LINE ", 'green', attrs=['bold', 'blink']))
        print(colored("***************************** \n", 'red',attrs=['bold', 'blink']))

        print(nm.command_line())

        print(colored("\n***************************** ", 'red', attrs=['bold', 'blink']))
        print(colored("\t ALL HOST ", 'green', attrs=['bold', 'blink']))
        print(colored("***************************** \n", 'red', attrs=['bold', 'blink']))

        print(nm.all_hosts())

        print(colored("\n***************************** ", 'red', attrs=['bold', 'blink']))
        print(colored("\t ARCHIVO CSV ", 'green', attrs=['bold', 'blink']))
        print(colored("***************************** \n", 'red', attrs=['bold', 'blink']))

        print(nm.csv())

        print(colored("\n***************************** ", 'red', attrs=['bold', 'blink']))
        print(colored("\t LOCALIZACION ", 'green', attrs=['bold', 'blink']))
        print(colored("***************************** \n", 'red', attrs=['bold', 'blink']))

        print(dir(nm))

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def escanedo_red():
    try:
        # instantiate nmap.PortScanner object
        nm = nmap.PortScanner()
        # Capturamos la red a analizar
        escan_red = input("Introduzca una subred a escanear con su mascara. (x.x.x.x/xx): ")

        # Analizamos la red que se ha introducido
        nm.scan(hosts=escan_red, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        # Recorremos la informacion obtenida
        for host, status in hosts_list:
            print("-" * 60)
            print('{0}:{1}'.format(host, status))

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def escanedo_red_completo():
    try:
        nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
        # Capturamos la red a analizar
        escan_red = input("Introduzca una subred a escanear con su mascara. (x.x.x.x/xx): ")

        nm.scan(hosts=escan_red, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        # Recorremos la informacion obtenida
        for host, status in hosts_list:
            print("-" * 60)
            print('{0}:{1}'.format(host, status))

        # Iniciamos en modo Asincrono
        nm = nmap.PortScannerAsync()
        nm.scan(escan_red, arguments="-O -v", callback=callback_result)

        # Espremos hasta que termine el escaneo
        while nm.still_scanning():
            print("Waiting >>>")
            nm.wait(2)

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def callback_result(host, scan_result):
    print('------------------')
    print(host, scan_result)


def script_smb_os_discovery_2():
    try:
        host_scan = entrada_ip()
        puerto = '445'

        # instantiate nmap.PortScanner object
        nm = nmap.PortScanner()
        # Almacenamos el resultado en variable para despues extraer informacion
        respuesta = nm.scan(host_scan, '445', arguments='--script=/usr/share/nmap/scripts/smb-os-discovery.nse')

        print("Info: ", respuesta)
        print("-" * 100)

        print('\n'.join(str(p) for p in respuesta['scan'][host_scan]['hostscript']))
        print(colored("-", 'magenta') * 50)

        # Capturamos la informacion del puerto 445
        thisdict = nm[host_scan]['tcp'][int(puerto)]
        print(colored("Puerto : ", 'cyan') + colored(str(puerto), 'red') + '  - Nombre: ' + thisdict['name'] +
              '  - Estado: ' + thisdict['state'])
        print("")
        # Obtenemos la informacion del puerto smb
        print(nm[host_scan]['tcp'][int(puerto)])
        print(colored("-", 'magenta') * 50)
        print("")

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def analisis_banner_script():
    try:
        # Capturamos la direccion del servidor web a analizar
        host_scan = entrada_ip()
        # Establecemos el puerto
        port = '80'
        # instantiate nmap.PortScanner object
        nm = nmap.PortScanner()
        # Almacenamos el resultado en variable para despues extraer informacion
        respuesta = (nm.scan(host_scan, port, arguments='-v --script=/usr/share/nmap/scripts/banner.nse'))

        print(colored("All info: ", 'cyan'), colored(respuesta, 'green'))
        print("")

        print(colored("Scan: ", 'cyan'), colored(nm.scanstats(), 'green'))
        print("")

        thisdict = nm[host_scan]['tcp'][int(port)]
        print(colored('Puerto : ', 'cyan') + str(port) + '  - Nombre: ' + thisdict['name'] + '  - Estado: ' + thisdict['state'])
        print("")

        thisdict2 = nm[host_scan]['tcp']
        print(colored("Detalle puerto : ", 'cyan'), thisdict2)
        print("")

        print(colored("Estado: ", 'cyan'), respuesta['nmap']['scanstats'])
        print("")
        print(colored("Equipo: ", 'cyan'), respuesta['scan'][host_scan])

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


def script_address_info_2():
    try:
        # Capturamos la direccion del servidor web a analizar
        host_scan = entrada_ip()
        # instantiate nmap.PortScanner object
        nm = nmap.PortScanner()
        # Almacenamos el resultado en variable para despues extraer informacion
        respuesta = nm.scan(host_scan, arguments='--script=/usr/share/nmap/scripts/address-info.nse')

        print(colored("All info: ", 'cyan'), colored(respuesta, 'green'))
        print("")

        print(colored("Scan: ", 'cyan'), colored(nm.scanstats(), 'green'))
        print("")

        thisdict2 = nm[host_scan]['tcp']
        print(colored("Detalle puerto : ", 'cyan'), thisdict2)
        print("")

        print(colored("Estado: ", 'cyan'), respuesta['nmap']['scanstats'])
        print("")
        print(colored("Equipo: ", 'cyan'), respuesta['scan'][host_scan])
        print("")

        # Recorremos la lista de puertos a analizar
        for puerto in nm[host_scan]['tcp']:
            # Obtenemos informacion concreta de uno de los puertos encontramos
            thisdict = nm[host_scan]['tcp'][int(puerto)]

            # Imprimimos el estado, nombre y el puerto
            print(colored("Puerto : ", 'cyan') + colored(str(puerto), 'red') + '  - Nombre: ' + thisdict['name'] +
                  '  - Estado: ' + thisdict['state'])
            print("")
            print(nm[host_scan]['tcp'][puerto])
            print(colored("-", 'magenta') * 50)
            print("")

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))
