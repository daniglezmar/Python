#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                    CREACION DE LA CLASE Producto

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Producto:
  """Ejemplo de clase con la cantidad y el precio de un producto """

  def __init__(self,producto,precio,unidades):
      self.producto = producto
      self.precio = precio
      self.unidades = unidades

  def coste_total(self):
      coste = self.precio * self.unidades
      return coste

  def nuevo_precio(self,precio):
      self.precio = precio

  def agrega (self, cantidad):
      self.unidades = self.unidades + cantidad

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    CREACION DE OBJETOS DE LA CLASE
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
pantalon_bonito = Producto("Pantalón bonito",100,6)
camiseta_fea = Producto("Camiseta fea",50,5)
zapatillas_nike = Producto("Zapatillas Nike",200,60)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                    USO DE LOS OBJETOS Y MÉTODOS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print ("El precio del producto Pantalon bonito " + "es " + str(pantalon_bonito.precio))
print ("Existen " + str(zapatillas_nike.unidades) + " unidades del producto zapatillas nike")
