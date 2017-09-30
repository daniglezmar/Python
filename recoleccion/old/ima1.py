
from __future__ import print_function
from PIL import Image
from PIL.ExifTags import TAGS

nombre_imagen = '1.jpg'

img = Image.open(nombre_imagen)
im = Image.open("4.jpg")

metadatos_exif = {}

metadatos_exif = img._getexif()

if metadatos_exif:
    print("\n")
    print("###############################################################################")
    print("                         Información metadatos")
    print("###############################################################################")
    print("\n")

    for meta_info in metadatos_exif:
        print("[+] " + str(nombre_imagen) + " Datos: " + str(metadatos_exif[meta_info]))


print("Resolucion de Imagen.")
print(img.format, img.size, img.mode)
