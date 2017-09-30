#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON SHODAN

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
        BUSCANDO UN HOST EN CONCRETO
"""""""""""""""""""""""""""""""""""""""""""""""""""

import shodan

#ShodanKeyString = 'APIKEY'
ShodanKeyString = open('shodanKey').readline().rstrip('\n')

#Hacemos la conexion con la base de datos de Shodan
ShodanApi = shodan.Shodan(ShodanKeyString)

# Lookup the host
host = ShodanApi.host('184.73.97.222')

# Print general info

print ('IP: %s ' % host['ip_str'])
print ('Organizacion: %s ' % host.get('org', 'n/a'))
print ('Sistema operativo: %s ' % host.get('os', 'n/a'))
for item in host['data']:
    print ('Puerto: %s ' % item['port'])
    print ('Banner: %s ' % item['data'])
