#!/usr/bin/env python
#
##################################################
#   Centralized core modules for CLASS MI MENU   #
##################################################
import re
import sys
import socket
import subprocess
import shutil
import os
import time
import datetime
import random
import string

# needed for backwards compatibility of python2 vs 3 - need to convert to threading eventually
try:
    import thread

except ImportError:
    import _thread as thread

try:
    raw_input

except:
    raw_input = input


##########################################
############  SISTEMA  ###################

# exit routine
def exit_program():
    print("\n\n Gracias por " + bcolors.RED + "Utilizar la herramienta" + bcolors.ENDC +
          " espero le haya gustado.\n\n Codigo en desarrollo. Estamos trabajando en ello.\n")
    sys.exit()


def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system


def show_banner(define_version, graphic):
    if graphic == "1":
        if check_os() == "posix":
            os.system("clear")
        if check_os() == "windows":
            os.system("cls")
        show_graphic()
    else:
        os.system("clear")


def get_version():
    define_version = '1.0'
    return define_version

#
# Class for colors
#
if check_os() == "posix":
    class bcolors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'
        backBlack = '\033[40m'
        backRed = '\033[41m'
        backGreen = '\033[42m'
        backYellow = '\033[43m'
        backBlue = '\033[44m'
        backMagenta = '\033[45m'
        backCyan = '\033[46m'
        backWhite = '\033[47m'

        def disable(self):
            self.PURPLE = ''
            self.CYAN = ''
            self.BLUE = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.RED = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERL = ''
            self.backBlack = ''
            self.backRed = ''
            self.backGreen = ''
            self.backYellow = ''
            self.backBlue = ''
            self.backMagenta = ''
            self.backCyan = ''
            self.backWhite = ''
            self.DARKCYAN = ''

# if we are windows or something like that then define colors as nothing
else:
    class bcolors:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERL = ''
        ENDC = ''
        backBlack = ''
        backRed = ''
        backGreen = ''
        backYellow = ''
        backBlue = ''
        backMagenta = ''
        backCyan = ''
        backWhite = ''

        def disable(self):
            self.PURPLE = ''
            self.CYAN = ''
            self.BLUE = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.RED = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERL = ''
            self.backBlack = ''
            self.backRed = ''
            self.backGreen = ''
            self.backYellow = ''
            self.backBlue = ''
            self.backMagenta = ''
            self.backCyan = ''
            self.backWhite = ''
            self.DARKCYAN = ''


##########################################
############ RUNTIME MESSAGES ############

def print_status(message):
    print(bcolors.GREEN + bcolors.BOLD + "[*] " + bcolors.ENDC + str(message))


def print_info(message):
    print(bcolors.BLUE + bcolors.BOLD + "[-] " + bcolors.ENDC + str(message))


def print_info_spaces(message):
    print(bcolors.BLUE + bcolors.BOLD + "  [-] " + bcolors.ENDC + str(message))


def print_warning(message):
    print(bcolors.YELLOW + bcolors.BOLD + "[!] " + bcolors.ENDC + str(message))


def print_error(message):
    print(bcolors.RED + bcolors.BOLD +
          "[!] " + bcolors.ENDC + bcolors.RED + str(message) + bcolors.ENDC)


##########################################
############  CLASE MENU  ################


class create_menu:

    def __init__(self, text, menu):
        self.text = text
        self.menu = menu
        print(text)

        for i, option in enumerate(menu):
            menunum = i + 1
            # Check to see if this line has the 'return to main menu' code
            match = re.search("0D", option)
            # If it's not the return to menu line:
            if not match:
                if menunum < 10:
                    print(('   %s) %s' % (menunum, option)))
                else:
                    print(('  %s) %s' % (menunum, option)))
            else:
                print('\n  99) Volver al Menu Principal\n')
        return


def setprompt(category, text):

    # if no special prompt and no text, return plain prompt
    if category == '0' and text == "":
        return bcolors.UNDERL + bcolors.DARKCYAN + "Escriba una opcion:"

    # if the loop is here, either category or text was positive
    # if it's the category that is blank...return prompt with only the text
    if category == '0':
        return bcolors.UNDERL + bcolors.DARKCYAN + "Elija una Opcion:"
    # category is NOT blank
    else:
        # initialize the base 'set' prompt
        prompt = bcolors.UNDERL + bcolors.DARKCYAN + "Elija una Opcion:"
        # if there is a category but no text
        if text == "":
            prompt += "Opcion: "
            promptstring = str(prompt)
            promptstring += ">"
            return promptstring
        # if there is both a category AND text
        else:
            prompt += ":"
            promptstring = str(prompt)
            promptstring = promptstring + "> " + text + ":"
            return promptstring


def definePregunta(text):

    if text == "":
        return bcolors.DARKCYAN + "Escriba una opcion por teclado: "
    else:
        return bcolors.DARKCYAN + text


def show_banner(define_version, graphic):
    if graphic == "1":
        if check_os() == "posix":
            os.system("clear")
        if check_os() == "windows":
            os.system("cls")
        show_graphic()
    else:
        os.system("clear")

    print(bcolors.BLUE + """
    [---]   Herramienta para Exploracion con Motores de Busqueda (""" + bcolors.YELLOW + """BuscaEnRed""" + bcolors.BLUE + """)     [---]
    [---]        Creado por:""" + bcolors.RED + """ Daniel Gonzalez Martinez """ + bcolors.BLUE + """(""" + bcolors.YELLOW + """DGM""" + bcolors.BLUE + """)                       [---]
    [---]                Version: """ + bcolors.RED + """%s""" % (define_version) + bcolors.BLUE + """                                             [---]
    [---]       Homepage: """ + bcolors.YELLOW + """https://www.EstamoEnEllo.com""" + bcolors.BLUE + """                            [---]
    """ + bcolors.GREEN + """        Bienvenidos a la herramienta Busca en Red  (BeR).  
    """)


def show_graphic():
        print(bcolors.YELLOW + r"""
         /$$$$$$$                                                                          /$$$$$$$                  /$$
        | $$__  $$                                                                        | $$__  $$                | $$
        | $$  \ $$ /$$   /$$  /$$$$$$$  /$$$$$$$  /$$$$$$         /$$$$$$  /$$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$$
        | $$$$$$$ | $$  | $$ /$$_____/ /$$_____/ |____  $$       /$$__  $$| $$__  $$      | $$$$$$$/ /$$__  $$ /$$__  $$
        | $$__  $$| $$  | $$|  $$$$$$ | $$        /$$$$$$$      | $$$$$$$$| $$  \ $$      | $$__  $$| $$$$$$$$| $$  | $$
        | $$  \ $$| $$  | $$ \____  $$| $$       /$$__  $$      | $$_____/| $$  | $$      | $$  \ $$| $$_____/| $$  | $$
        | $$$$$$$/|  $$$$$$/ /$$$$$$$/|  $$$$$$$|  $$$$$$$      |  $$$$$$$| $$  | $$      | $$  | $$|  $$$$$$$|  $$$$$$$
        |_______/  \______/ |_______/  \_______/ \_______/       \_______/|__/  |__/      |__/  |__/ \_______/ \_______/
        
        """ + bcolors.ENDC)
        return
