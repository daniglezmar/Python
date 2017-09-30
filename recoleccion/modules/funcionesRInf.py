#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################
#                                                                       #
#     F U N C I O N E S   P A R A   B U S C A   E N   L A   R E D       #
#                                                                       #
#########################################################################

import dns
import dns.resolver
import dns.zone
import dns.ipv4
import pythonwhois
import pygeoip
import socket  # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import shodan
import pprintpp  # Libreria para pretty prints
import sys
from modules.funcionesCore import *
from modules.textoMenu import *
from termcolor import colored       #Libreria para colores

# Capturamos la version de la aplicacion
define_version = get_version()


def menuDNS():
    # Hacemos un bucle para volver al Menu Principal si no se elige una opcion predeterminada por nosotros
    while 1:
        try:
            show_banner(define_version, '1')
            ###################################################
            #        USER INPUT: SHOW MAIN MENU               #
            ###################################################
            show_dns_menu = Crear_menu(texto_principal, menu_principal_dns)

            opcion_dns_menu = (input(colored("Elija una opcion: ", 'blue')))

            if opcion_dns_menu == 'exit':
                break

            if opcion_dns_menu == '1':  # Opcion Conulta multiple de registros
                while True:
                    print(colored("Opcion 5. Consulta de registros (A, MS, MX).", 'magenta', attrs=['bold', 'blink']))
                    dom_usuario = textoUsuario()
                    consultaRegistroA(dom_usuario)
                    consultaRegistroNS(dom_usuario)
                    consultaRegistroMX(dom_usuario)
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if opcion_dns_menu == '2':  # Opcion Conulta Revsersa
                print(colored("Opcion 5. Consulta Reversa", 'magenta', attrs=['bold', 'blink']))
                while True:
                    consultaReversa()
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if opcion_dns_menu == '3':  # Opcion Conulta Registro A
                print(colored("Opcion 5. Consulta registro A.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    dom_usuario = textoUsuario()
                    consultaRegistroA(dom_usuario)
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if opcion_dns_menu == '4':  # 'Opcion Conulta Registro NS
                print(colored("Opcion 5. Consulta registro NS.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    dom_usuario = textoUsuario()
                    consultaRegistroNS(dom_usuario)
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if opcion_dns_menu == '5':  # 'Opcion Conulta Registro MX
                print(colored("Opcion 5. Consulta registro MX.", 'magenta', attrs=['bold', 'blink']))
                while True:
                    dom_usuario = textoUsuario()
                    consultaRegistroMX(dom_usuario)
                    repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
                    if repite_consulta == 'n':
                        break

            if opcion_dns_menu == '99':
                break

        except:
            print('Ups! Ha ocurrido un error: %s' % Exception)
            input(colored("Pulse INTRO para continuar.", 'red', attrs=['bold', 'blink']))


########################################################
#   Funciones especificas Menu DNS (1)                 #
########################################################

def consultaRegistroA(entradaUsuario):
    try:
        """Consulta sobre registro IPV4"""
        ansA = dns.resolver.query(entradaUsuario, 'A')
        print(colored("\nRespuesta de DNS en IPV4: ", 'cyan', attrs=['bold', 'blink']))
        print(ansA.response.to_text())

    except Exception as e:
        print(colored("\Excepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)


def consultaRegistroNS(entradaUsuario):
    try:
        """Consulta sobre registro NameServers"""
        ansNS = dns.resolver.query(entradaUsuario, 'NS')
        print(colored("\nRespuesta de DNS en NameServers: ", 'red', attrs=['bold', 'blink']))
        print(ansNS.response.to_text())

    except Exception as e:
        print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)


def consultaRegistroMX(entradaUsuario):
    try:
        """Consulta sobre registro MailServers"""
        ansMX = dns.resolver.query(entradaUsuario, 'MX')
        print(colored("\nRespuesta de DNS en MailServers: ", 'red', attrs=['bold', 'blink']))
        print(ansMX.response.to_text())

    except Exception as e:
        print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)


########################################################
#
#      C O N S U L T A        R E V E R S A
#               #
########################################################

def consultaReversa():
    entradausuario = input("Introduzca una direccion IP: ")
    try:
        # Comprobamos si es una IP valida
        socket.inet_aton(entradausuario)
        myresolver = dns.resolver.Resolver()
        req = '.'.join(reversed(entradausuario.split("."))) + ".in-addr.arpa"
        myanswers = myresolver.query(req, "PTR")
        for rdata in myanswers:
            print(rdata)

    except socket.error as e:
        print ("Error en la consulta. " + e)
        input("Pulse INTRO para continuar.")


#############################################
#                                           #
#       W  H O I S                          #
#                                           #
#############################################
#
# Menu WHOIS. Le pasamos el dominio introducido por el usuario.
def menuWhois():
    while True:
        try:
            entradaUsuario = textoUsuario()

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

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


#############################################
#                                           #
#  G E O L A C A L I Z A C I O N    I P     #
#                                           #
#############################################

def menuGeo():
    print("Busqueda por Geolocalizacion.")
    while True:
        try:
            entradaUsuario = textoUsuario()
            #Llamamos a la funcion importada del socket gethostbyname y le pasamos la entrada del usuario
            try:
                direccionIP = socket.gethostbyname(entradaUsuario)
            except:
                direccionIP = "0.0.0.0"

            #Si la direccion IP esta vacia o es 0.0.0.0 mensaje de IP incorrecta si
            if direccionIP == "0.0.0.0":
                print("Nombre de dominio incorrecto.")
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

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


#############################################
#                                           #
#     M O T O R    S H O D A N              #
#                                           #
#############################################

def menuMotorShodan():
    while True:
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


        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break


#############################################
#                                           #
#   F A C E T S   D E   S H O D A N         #
#                                           #
#############################################

def menuFacets():
    while True:
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

        repite_consulta = input(colored("\nDesea repetir la consulta? (s/n): ", 'magenta', attrs=['bold']))
        if repite_consulta == 'n':
            break
