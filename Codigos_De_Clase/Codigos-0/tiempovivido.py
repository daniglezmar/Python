##########################################
##### Tiempo vivido  #####################
##########################################
#
print("Vamos a ver el tiempo que has vivido")
nombre = input("Introduzca su nombre: ")
print("Y que edad tiene ?")
edad = int(input("Introduzca su edad: "))

dias = edad * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(nombre, "ha vivido durante", dias, "dias", horas, "horas", minutos, "minutos", segundos, "segundos")

