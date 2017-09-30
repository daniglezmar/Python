#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANÁLISIS DE VULNERABILIDADES

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                    ESCANEO TCP
"""""""""""""""""""""""""""""""""""""""""""""""""""

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

if len(sys.argv) !=3 :
    print ("Uso: python escaneo_tcp.py <IP> <lista de puertos separados por comas>")
    exit()

puerto_origen = RandShort()
ip_destino = sys.argv[1]
puertos = sys.argv[2]
puertos.replace(" ", "")
scanPorts = puertos.strip().split(':')

print("IP a escanear: " + str(ip_destino))
print("Puerto/s a escanear: " + str(scanPorts))

for i in scanPorts:
    print("Analizando puerto: " + str(i))
    response = sr1(IP(dst=ip_destino)/TCP(dport=int(i),flags="S"))
    print ("Respuesta del tipo: " + str(type(response)))

    if (str(type(response))=="<class 'NoneType'>"):
        print ("[-] Puerto " + i + " cerrado")

    elif (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags==0x12):
            print ("[+] Puerto " + i + " abierto")

    elif (response.haslayer(ICMP)):
        if (response.getlayer(TCP).flags==0x14):
            print ("[-] Puerto " + i + " cerrado")
