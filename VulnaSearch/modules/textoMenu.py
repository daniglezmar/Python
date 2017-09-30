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

menu_principal = ['Busqueda de Vulnerabilidades con SCAPY.',
             'Busqueda de Vulnerabilidades con NMAP.',
             'Busqueda de Vulnerabilidades en Banners',
             'Busqueda de Vulnerabilidades en Servidores Webs.']


menu_principal_scapy = ['Escaneo ACK.',
        'Escaneo TCP.',
        'Escaneo UDP.',
        'Escaneo NULL.',
        'Escaneo XMAS.',
        '0D']


menu_principal_nmap = ['Uso de nmap con formato.',
        'Escanedo de red.',
        'Escaneo de red (PortScannerAsync).',
        'Escaneo con smb-os-discovery.',
        'Escaneo con Script address-info',
        'Analisis Banner con Script.',
        'Escaneo NMAP con varias opciones.',
        '0D']


image_menu = ['Extraer Metadatos de una imagen.',
              'Mostrar resolucion.',
              'Mostart Imagen selccionada.',
              '0D']
