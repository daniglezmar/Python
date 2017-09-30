#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                                USO DE NMAP

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import nmap
from termcolor import colored       #Libreria para colores

nm = nmap.PortScanner()

ip = '127.0.0.1'
puertos = "21,22,80"

print (colored("Puertos a escanear: ",'green',attrs=['bold', 'blink']) + puertos)
print (colored("IP a escanear: ",'green',attrs=['bold', 'blink']) + ip)
resultados=nm.scan(ip, puertos)

print (colored("\n***************************** ",'red',attrs=['bold', 'blink']))
print (colored("\t SCAN INFO ",'green',attrs=['bold', 'blink']))
print (colored("***************************** \n",'red',attrs=['bold', 'blink']))

print(nm.scaninfo())

print (colored("\n***************************** ",'red',attrs=['bold', 'blink']))
print (colored("\t COMMAND LINE ",'green',attrs=['bold', 'blink']))
print (colored("***************************** \n",'red',attrs=['bold', 'blink']))

print(nm.command_line())

print (colored("\n***************************** ",'red',attrs=['bold', 'blink']))
print (colored("\t ALL HOST ",'green',attrs=['bold', 'blink']))
print (colored("***************************** \n",'red',attrs=['bold', 'blink']))

print(nm.all_hosts())

print (colored("\n***************************** ",'red',attrs=['bold', 'blink']))
print (colored("\t ARCHIVO CSV ",'green',attrs=['bold', 'blink']))
print (colored("***************************** \n",'red',attrs=['bold', 'blink']))

print (nm.csv())

print (colored("\n***************************** ",'red',attrs=['bold', 'blink']))
print (colored("\t LOCALIZACION ",'green',attrs=['bold', 'blink']))
print (colored("***************************** \n",'red',attrs=['bold', 'blink']))

print(dir(nm))
