from ordenador import *

#Crear un raton nuevo
raton_drakonia = Raton("Drakonia","20DPIs", 50)

#Crear un teclado nuevo
teclado_base = Teclado("Base","Español", 30)

#Crear una tarjeta grafica
tarjeta_nvidia = TarjetaGrafica("NVIDIA", "9600", 100, 8, "V1.0")

#Creamos nuestro propio ordenador
ordenador_juan = Ordenador(raton_drakonia,teclado_base,tarjeta_nvidia)

#Sacamos la informacion por pantalla
print(ordenador_juan.obtenerInformacion())
