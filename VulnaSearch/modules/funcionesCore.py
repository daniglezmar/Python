#!/usr/bin/env python
#
##################################################
#   Centralized core modules for CLASS MI MENU   #
##################################################
import re
import sys
import os
from termcolor import colored

##########################################
############  CLASE MENU  ################
##########################################


# Funcion solita direccion IP del host a analizar y devuelve el valor introducido
def entrada_ip():
    try:
        # Capturamos la direccion del host a analizar
        ip_destino = input(colored("Introduzca una direccion IP: ", 'blue'))
        # Si no hay contenido, analizaremos localhost
        if ip_destino == "":
            ip_destino = '127.0.0.1'
        return ip_destino

    except Exception as e:
        print(colored('Error en la direccion introducida. %s' %e, 'red'))

# Funcion solita direccion puertos a analizar y devuelve el o los valores introducidos
def entada_puertos():
    try:
        # Capturamos la entrada del usuario
        rango_puertos = input(colored("Introduzca los puertos a analizar separados por comas: ", 'blue', attrs=['bold']))

        #Si no se introduce nada, utilizaremos los puertos que suelen estar abiertos y propensos a vulnerabilidades
        if rango_puertos == "":
            rango_puertos = "21,53,80,88,135,139,389,443,445,464,593,636,1025,1027,1043,1044,1045,1050,1051," \
                            "1433,3268,3269,3306"
        else:
            rango_puertos.replace(" ", "")
            rango_puertos = rango_puertos.strip().split(',')

        return rango_puertos

    except Exception as e:
        print(colored('Error en los puertos introducidos, %s' %e, 'red'))


# Funcion especial para convierte en lista los valores introducidos
def entada_puertos_scapy():
    try:
        # Capturamos la intrada del usuario
        rango_puertos = input(colored("Introduzca los puertos a analizar separados por comas: ", 'blue', attrs=['bold']))

        if rango_puertos == "":
            rango_puertos = [21,53,80,88,135,139,389,443,445,464,593,636,1025,1027,1043,1044,1045,1050,1051,1433,3268,3269,3306]
        elif rango_puertos == "first":
            rango_puertos = range(1, 1024)
        else:
            rango_puertos.replace(" ", "")
            rango_puertos = rango_puertos.strip().split(',')

        return rango_puertos

    except Exception as e:
        print(colored('Error en los puertos introducidos, %s' %e, 'red'))


class Crear_menu:
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
                    print(colored(('   %s) %s' % (menunum, option)), 'cyan'))
                else:
                    print(colored('\n  99) Volver al Menu Principal\n', 'yellow'))
            else:
                print(colored('\n  99) Volver al Menu Principal\n', 'yellow'))
        return


# Funcion tomada que valida un nombre de Host
def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]  # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


# Funcion que solicita la entrada de un dominio al usuario.
def textoUsuario():
    # Capturamos la entrada del usuario
    try:
        entradausuario = str(input(colored("Introduzca un nombre de dominio para la busqueda: ", 'yellow')))

        # Validamos si la entrada es un dominio valido y no la entrada del usuario no esta vacia
        if is_valid_hostname(entradausuario) and entradausuario != "":
            # Devolvemos la entrada ya validada. De lo contrario devuelve NONE
            return entradausuario
        else:
            print(colored("\nError, no es un nombre de dominio valido.", 'red', attrs=['bold', 'blink']))

    except Exception as e:
        print(colored('Ups! Ha ocurrido un error: %s' % e, 'red'))


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
    [---]       Herramienta para la busquea de Vulnerabilidades (""" + bcolors.YELLOW + """VS""" + bcolors.BLUE + """)              [---]
    [---]        Creado por:""" + bcolors.RED + """ Daniel Gonzalez Martinez """ + bcolors.BLUE + """(""" + bcolors.YELLOW + """DGM""" + bcolors.BLUE + """)                       [---]
    [---]                Version: """ + bcolors.RED + """%s""" % (define_version) + bcolors.BLUE + """                                             [---]
    [---]       Homepage: """ + bcolors.YELLOW + """https://www.EstamoEnEllo.com""" + bcolors.BLUE + """                            [---]
    """ + bcolors.GREEN + """        Bienvenidos a la herramienta VulnaSearch (VS).  
    """)


def show_graphic():
    print(bcolors.YELLOW + r"""
    oooooo     oooo             oooo                         .oooooo..o                                        oooo        
     `888.     .8'              `888                        d8P'    `Y8                                        `888        
      `888.   .8'   oooo  oooo   888  ooo. .oo.    .oooo.   Y88bo.       .ooooo.   .oooo.   oooo d8b  .ooooo.   888 .oo.   
       `888. .8'    `888  `888   888  `888P"Y88b  `P  )88b   `"Y8888o.  d88' `88b `P  )88b  `888""8P d88' `"Y8  888P"Y88b  
        `888.8'      888   888   888   888   888   .oP"888       `"Y88b 888ooo888  .oP"888   888     888        888   888  
         `888'       888   888   888   888   888  d8(  888  oo     .d8P 888    .o d8(  888   888     888   .o8  888   888  
          `8'        `V88V"V8P' o888o o888o o888o `Y888""8o 8""88888P'  `Y8bod8P' `Y888""8o d888b    `Y8bod8P' o888o o888o
      """ + bcolors.ENDC)
    return

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

