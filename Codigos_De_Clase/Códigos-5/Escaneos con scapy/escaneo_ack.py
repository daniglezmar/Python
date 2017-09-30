#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANÁLISIS DE VULNERABILIDADES

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                    ESCANEO ACK
"""""""""""""""""""""""""""""""""""""""""""""""""""

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

if len(sys.argv) !=3 :
    print ("Uso: python escaneo_ack.py <IP> <lista de puertos separados por comas>")
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
    response = sr1(IP(dst=ip_destino)/TCP(dport=int(i),flags="A"))
    print ("Respuesta del tipo: " + str(type(response)))

    if (str(type(response))=="<class 'NoneType'>"):
        print ("[+] Encontrado firewall")

    elif (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags==0x4):
            print ("[-] No encontrado firewall")

    elif (response.haslayer(ICMP)):
        if (response.getlayer(ICMP).type==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print ("[+] Encontrado firewall")
