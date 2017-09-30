#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON DNSPYTHON

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
    CONSULTAS SOBRE VARIOS TIPOS DE REGISTRO
"""""""""""""""""""""""""""""""""""""""""""""""""""

import dns
import dns.resolver
from termcolor import colored                   #Libreria para colores

"""Consulta sobre registro IPV4"""
ansA = dns.resolver.query('google.com','A')

"""Consulta sobre registro IPV6"""
ansAAAA = dns.resolver.query('google.com','AAAA')

"""Consulta sobre registro MailServers"""
ansMX = dns.resolver.query('google.com','MX')

"""Consulta sobre registro NameServers"""
ansNS = dns.resolver.query('google.com','NS')


print (colored("\nRespuesta de DNS en IPV4: ",'red',attrs=['bold', 'blink']))
print (ansA.response.to_text())

print (colored("\nRespuesta de DNS en IPV6: ",'red', attrs=['bold', 'blink']))
print (ansAAAA.response.to_text())

print (colored("\nRespuesta de DNS en MailServers: ",'red',attrs=['bold', 'blink']))
print (ansMX.response.to_text())

print (colored("\nRespuesta de DNS en NameServers: ",'red',attrs=['bold', 'blink']))
print (ansNS.response.to_text())
