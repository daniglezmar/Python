#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANÁLISIS DE VULNERABILIDADES

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                    ESCANEO XMAS
"""""""""""""""""""""""""""""""""""""""""""""""""""

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
if len(sys.argv) !=3 :
    print ("Uso: python escaneo_xmas.py <IP> <lista de puertos separados por comas>")
    exit()

puerto_origen = RandShort()
ip_destino = sys.argv[1]
puertos = sys.argv[2]
puertos.replace(" ", "")
scanPorts = puertos.strip().split(':')

print("IP a escanear: " + str(ip_destino))
print("Puerto/s a escanear: " + str(scanPorts))

for i in scanPorts:
    if (i.isdigit()):
        response = sr1(IP(dst=ip_destino)/TCP(dport=int(i),flags="FPU"))
        if response is None:
            print ("[+] Puerto %s Abierto o filtrado " % (i))
        elif (response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14):
            print ("[-] Puerto %s Cerrado " % (i))
        elif (response.haslayer(ICMP) and response.getlayer(ICMP).type == 3):
            print ("[x] Puerto %s Filtrado " % (i))
        else:
            print ("Puerto inválido")
