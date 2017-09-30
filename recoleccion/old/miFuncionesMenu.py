#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################
#                                                                       #
#     F U N C I O N E S   P A R A   B U S C A   E N   L A   R E D       #
#                                                                       #
#########################################################################

import dns
import dns.resolver
import pythonwhois
import pygeoip
from termcolor import colored  # Libreria para colores
import socket  # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import shodan
import pprintpp  # Libreria para pretty prints
import sys
from mitext import *
from misetcore import *

# Capturamos la version de la aplicacion
define_version = get_version()

def menuDNS():

    try:
        while 1:
            show_banner(define_version, '1')
            ###################################################
            #        USER INPUT: SHOW MAIN MENU               #
            ###################################################
            show_dns_menu = create_menu(mitext.main_text, mitext.dns_main_menu)

            # special case of list item 99
            print('\n  99) Volver al menu principal.\n')

            dns_menu_choice = (raw_input(setprompt("0", "")))

            if dns_menu_choice == 'exit':
                break

            if dns_menu_choice == '1':  # 'Spearphishing Attack Vectors
                print("Opcion 1.")

            if dns_menu_choice == '2':  # 'Spearphishing Attack Vectors
                print("Opcion 2.")

            if dns_menu_choice == '3':  # 'Spearphishing Attack Vectors
                print("Opcion A 3.")
                #Capturamos individualmente las exepciones para que muestre los registros que si existan
                try:
                    """Consulta sobre registro IPV4"""
                    ansA = dns.resolver.query(entradaUsuario, 'A')
                    print(colored("\nRespuesta de DNS en IPV4: ", 'red', attrs=['bold', 'blink']))
                    print(ansA.response.to_text())

                except Exception as e:
                    print(colored("\Excepcion: ", 'red', attrs=['bold', 'blink']))
                    print('Ups! Ha ocurrido un error: %s' % e)

            if dns_menu_choice == '4':  # 'Spearphishing Attack Vectors
                print("Opcion 4 NS.")
                try:
                    """Consulta sobre registro NameServers"""
                    ansNS = dns.resolver.query(entradaUsuario, 'NS')
                    print(colored("\nRespuesta de DNS en NameServers: ", 'red', attrs=['bold', 'blink']))
                    print(ansNS.response.to_text())

                except Exception as e:
                    print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
                    print('Ups! Ha ocurrido un error: %s' % e)

            if dns_menu_choice == '5':  # 'Spearphishing Attack Vectors
                print("Opcion 5 MX.")
                try:
                    """Consulta sobre registro MailServers"""
                    ansMX = dns.resolver.query(entradaUsuario, 'MX')
                    print(colored("\nRespuesta de DNS en MailServers: ", 'red', attrs=['bold', 'blink']))
                    print(ansMX.response.to_text())

                except Exception as e:
                    print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
                    print('Ups! Ha ocurrido un error: %s' % e)

            if dns_menu_choice == '99':
                break

    except:
        print('Ups! Ha ocurrido un error: %s' % Exception)


# Menu WHOIS. Le pasamos el dominio introducido por el usuario.
def menuWhois(entradaUsuario):

    try:
        print("Busqueda por Whois.")
        # Utilizamos la API de pythonwhois para extraer información desde cualquier script en Python
        """Recuperamos el servidor raiz para un dominio determinado"""
        pythonwhois.net.get_root_server(entradaUsuario)

        """Obtenemos un diccionario con toda la información sobre el dominio"""
        whois = pythonwhois.get_whois(entradaUsuario)

        """Obtenemos la información del dominio de manera 'cruda'"""
        whois_raw = pythonwhois.net.get_whois_raw(entradaUsuario)

        print(colored("\nValores de keys para el servidor: ", 'red', attrs=['bold', 'blink']))
        print(whois.keys())

        print(colored("\nValores de la búsqueda para el servidor: ", 'red', attrs=['bold', 'blink']))
        print(whois.values())

        print(colored("\nValores de la búsqueda para el servidor crudo: ", 'red', attrs=['bold', 'blink']))
        print(whois_raw)

    except Exception as e:
        print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)


def menuGeo(entradaUsuario):
    print("Busqueda por Geolocalizacion.")
    try:
        #Llamamos a la funcion importada del socket gethostbyname y le pasamos la entrada del usuario
        direccionIP = socket.gethostbyname(entradaUsuario)

        #Si la direccion IP esta vacia o es 0.0.0.0 mensaje de IP incorrecta si
        if direccionIP == "0.0.0.0":
            print("Direccion IP incorrecta.")
        else:
            #Imprimimos por pantalla la direccion IP convertida
            print("\nDireccion IP del dominio seleccionado: " + direccionIP)

            """Utilizamos la base de datos GeoLite"""
            gi = pygeoip.GeoIP('GeoLiteCity.dat')

            print(colored("\n Código del pais del servidor por dominio: ", 'red', attrs=['bold', 'blink']) + gi.country_code_by_name(entradaUsuario))
            print(colored("\n Código del país del servidor por IP: ", 'red', attrs=['bold', 'blink']) + gi.country_code_by_addr(direccionIP))
            print(colored("\n Time zone del servidor por IP: ", 'red', attrs=['bold', 'blink']) + gi.time_zone_by_addr(direccionIP))

            print(colored("\n Información completa del servidor por IP: ", 'red', attrs=['bold', 'blink']))
            pprintpp.pprint(gi.record_by_addr(direccionIP))

    except socket.gaierror:
        print('oops no se ha podido validar la direccion IP.')


def menuMotorShodan():
    # Solicitamos al usuario que introduzca un concepto a buscar
    try:
        entrada = str(input("Introduzca un concepto a buscar (Webcam, OS, Apache, netcam, etc.):  "))

    except Exception as e:
        print('Introduzca una cadena de texto valida: %s' % e)

    print("\nMotores de Busqueda.")

    # Clave de desarrollador de la API de shodan
    ShodanKeyString = open('shodanKey').readline().rstrip('\n')

    # Realizamos la conexion con la base de datos de Shodan
    ShodanApi = shodan.Shodan(ShodanKeyString)

    # Ponemos el código entre un try/catch para manejar las excepcionesOS
    try:
        # Buscamos en Shodan con el método WebAPI.search()
        resultados = ShodanApi.search(entrada)

        # Mostramos el resultado
        print('Cantidad de resultados encontrados: %s' % resultados['total'])
        for i in resultados['matches']:
            print('IP: %s' % i['ip'])
            print('O.S: %s' % i['os'])
            print('Puerto: %s' % i['port'])
            print('Hostnames: %s' % i['hostnames'])
            print(i['data'])
            print('-----' * 10)
    except Exception as e:
        print('Ups! Ha ocurrido un error: %s' % e)


def menuFacets():
    # The list of properties we want summary information on
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',
        # We only care about the top 5 countries, this is how we let Shodan know to return 5 instead of the
        # default 10 for a facet. If you want to see more than 10, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 5)
    ]

    FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'asn': 'Top 5 Autonomous Systems',
        'country': 'Top 5 Countries',
    }

    # Validamos la captura del usuario
    try:
        entrada = str(input("Introduzca un concepto a buscar (Apache, Webcam, OS, etc.):  "))

    except Exception as e:
        print('Introduzca una cadena de texto valida: %s' % e)

    try:
        # Clave de desarrollador de la API de shodan
        ShodanKeyString = open('shodanKey').readline().rstrip('\n')

        # Realizamos la conexion con la base de datos de Shodan
        api = shodan.Shodan(ShodanKeyString)

        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        result = api.count(entrada, facets=FACETS)

        print('Resumen de Informacion de Shodan')
        print('Consulta: %s' % entrada)
        print('Resultado Total: %s\n' % result['total'])

        # Imprimimos la informacion desde Facets
        for facet in result['facets']:
            print(FACET_TITLES[facet])

            for term in result['facets'][facet]:
                print('%s: %s' % (term['value'], term['count']))

            # Separamos los resultados para mayor claridad
            print('*****************')
            print('')

    except Exception as e:
        print('Error: %s' % e)
        sys.exit(1)

