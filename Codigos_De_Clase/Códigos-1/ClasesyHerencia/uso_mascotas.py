"""
    USO DE LA CLASE MASCOTA

"""
from mascotas import Mascota, Perro

mi_primera_mascota = Mascota("Fluffy", "Perro")

print(mi_primera_mascota)


"""
    USO DE LA CLASE PERRO
"""

bingo = Perro("Bingo", "Si")

print(bingo)
print(bingo.getPersigue())

rudolf = Perro("Rudolf", "No")
print(rudolf)
print(rudolf.getPersigue())

print(isinstance(bingo,Perro))
print(isinstance(mi_primera_mascota,Perro))
print(isinstance(bingo,Mascota))
