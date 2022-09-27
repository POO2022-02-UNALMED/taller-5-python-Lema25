from gestion.zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
 
    def getNombre(self): 
        return self._nombre
    def setNombre(self, nombre): 
        self._nombre = nombre

    def getUbicacion(self,): 
        return self._ubicacion
    def setUbicacion(self, ubicacion): 
        self._ubicacion = ubicacion

    def getZoologico(self): 
        return self._animales
    def setZoologico(self, animales): 
        self._animales = animales

    def getZoo(self): 
        return self._zoo
    def setZoo(self, zoo): 
        self._zoo = zoo

    def agregarAnimales(self, nAnimal): 
        self._animales.append(nAnimal)

    def cantidadAnimales(self): 
        return len(self._animales)  

