#!/usr/bin/env python
########################################################################
#
# text menu for set menu stuff
#
########################################################################
from modules.textoMenu import *
from modules.funcionesCore import *

# grab version of SET
define_version = get_version()

# check operating system
operating_system = check_os()

texto_principal = " Selecciona una opcion del Menu: "

menu_principal = ['DNS. Busqueda por nombre de Dominio.',
             'WHOIS. Busqueda por nombre de Dominio.',
             'Geolocalizacion IP por Dominio',
             'Shodan. Busquedas',
             'Facets de Shodan',
             'PDF. Analisis de Metadatos.',
             'Imagen. Analisis de Metadatos.']


menu_principal_dns = ['Consulta por Dominio.',
        'DNS Consulta reversa.',
        'Look up A record.',
        'Look up NS record.',
        'Look up MX record.',
        'Look up TXT record.'
        '0D']


dns_menu2 = ['Busqueda por dominio',
            'Buscqueda inversa',
            '0D']


image_menu = ['Extraer Metadatos de una imagen.',
              'Mostrar resolucion.',
              'Mostart Imagen selccionada.',
              '0D']
