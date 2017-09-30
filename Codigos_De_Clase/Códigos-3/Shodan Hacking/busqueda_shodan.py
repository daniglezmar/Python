#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON SHODAN

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                BUSCANDO CON SHODAN
"""""""""""""""""""""""""""""""""""""""""""""""""""

import shodan

# Clave de desarrollador de la API de shodan
ShodanKeyString = open('shodanKey').readline().rstrip('\n')

#Realizamos la conexion con la base de datos de Shodan
ShodanApi = shodan.Shodan(ShodanKeyString)

# Ponemos el código entre un try/catch para manejar las excepciones
try:
    # Buscamos en Shodan con el método WebAPI.search()
    resultados = ShodanApi.search('apache')

    # Mostramos el resultado
    print ('Cantidad de resultados encontrados: %s' % resultados['total'])
    for i in resultados['matches']:
        print ('IP: %s' % i['ip_str'])
        print ('Data: %s' % i['data'])
        print ('Hostnames: %s' % i['hostnames'])
        print ('Puerto: %s' % i['port'])
        print ('')

except shodan.APIError as e:
    print ('Ups! Ha ocurrido un error: %s' % e)
