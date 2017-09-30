#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

     F U N C I O N E S   P A R A   B U S C A   E N   L A   R E D 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import dns
import dns.resolver
import pythonwhois
import pygeoip
from termcolor import colored  # Libreria para colores
import socket  # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import shodan
import pprintpp  # Libreria para pretty prints
import sys
import re

## Menu de Busquedas en Python
def print_menu():
    print(40 * "-", "BUSCA EN LA RED", 40 * "-")
    print("1. DNS")
    print("2. WHOIS")
    print("3. Geolocalizacion")
    print("4. Motor SHODAN")
    print("5. Facets de SHODAN")
    print("6. Exit")
    print(95 * "-")


# Funcion tomada prestada para validar un nombre de Host
def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))



# Funcion que solicita la entrada de un dominio al usuario.
def textoUsuario():

    # Capturamos la entrada del usuario
    try:
        entradaUsuario = str(input("Introduzca un nombre de dominio para la busqueda: "))

        #Validamos si la entrada es un dominio valido y no la entrada del usuario no esta vacia
        if is_valid_hostname(entradaUsuario) and entradaUsuario!="":
            #Devolvemos la entrada ya validada. De lo contrario devuelve NONE
            return entradaUsuario
        else:
            print(colored("\nError, no es un nombre de dominio valido.", 'red', attrs=['bold', 'blink']))

    except Exception as e:
        print('Ups! Ha ocurrido un error: %s' % e)



# Menu DNS, le pasamos como argumento un dominio
def menuDNS(entradaUsuario):

    #Capturamos individualmente las exepciones para que muestre los registros que si existan
    try:
        """Consulta sobre registro IPV4"""
        ansA = dns.resolver.query(entradaUsuario, 'A')
        print(colored("\nRespuesta de DNS en IPV4: ", 'red', attrs=['bold', 'blink']))
        print(ansA.response.to_text())

    except Exception as e:
        print(colored("\Excepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)

    try:
        """Consulta sobre registro NameServers"""
        ansNS = dns.resolver.query(entradaUsuario, 'NS')
        print(colored("\nRespuesta de DNS en NameServers: ", 'red', attrs=['bold', 'blink']))
        print(ansNS.response.to_text())

    except Exception as e:
        print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)

    try:
        """Consulta sobre registro MailServers"""
        ansMX = dns.resolver.query(entradaUsuario, 'MX')
        print(colored("\nRespuesta de DNS en MailServers: ", 'red', attrs=['bold', 'blink']))
        print(ansMX.response.to_text())

    except Exception as e:
        print(colored("\nExcepcion: ", 'red', attrs=['bold', 'blink']))
        print('Ups! Ha ocurrido un error: %s' % e)



## Menu WHOIS. Le pasamos el dominio introducido por el usuario.
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

