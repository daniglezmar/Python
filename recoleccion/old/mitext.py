#!/usr/bin/env python
########################################################################
#
# text menu for set menu stuff
#
########################################################################
from misetcore import *

# grab version of SET
define_version = get_version()

# check operating system
operating_system = check_os()

main_text = " Selecciona una opcion del Menu: "

main_menu = ['DNS. Busqueda por nombre de Dominio.',
             'WHOIS. Busqueda por nombre de Dominio.',
             'Geolocalizacion IP por Dominio',
             'Google Hack Database',
             'Shodan. Busquedas',
             'Facets de Shodan']


dns_main_menu = ['DNS. Consulta por nombre de Dominio',
        'DNS Reverse Map Name',
        'Look up A record.',
        'Look up AAAA record.',
        'Look up MX record.',
        'Look up TXT record.']


dns_menu2 = ['Busqueda por dominio',
            'Buscqueda inversa',
            '0D']
