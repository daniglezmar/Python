#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON PyGeoIP

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pygeoip
import pprintpp                     #Libreria para pretty prints
from termcolor import colored       #Libreria para colores

"""Utilizamos la base de datos GeoLite"""
gi = pygeoip.GeoIP('GeoLiteCity.dat')

print(colored("\n Código del pais del servidor por dominio: ",'red',attrs=['bold', 'blink']) + gi.country_code_by_name('dragonjar.org'))
print(colored("\n Código del país del servidor por IP: ",'red',attrs=['bold', 'blink']) + gi.country_code_by_addr('104.27.161.40'))
print(colored("\n Time zone del servidor por IP: ",'red',attrs=['bold', 'blink']) + gi.time_zone_by_addr('104.27.161.40'))

print(colored("\n Información completa del servidor por IP: ",'red',attrs=['bold', 'blink']))
pprintpp.pprint(gi.record_by_addr('104.27.161.40'))
