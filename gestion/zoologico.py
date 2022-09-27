class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def getNombre(self): 
        return self._nombre
    def setNombre(self, nombre): 
        self._nombre = nombre

    def getZoo(self,): 
        return self._zoo
    def setZoo(self, zoo): 
        self._zoo = zoo

    def getZona(self): 
        return self._zonas
    def setZona(self, zonas): 
        self._zonas = zonas

    def agregarZonas(self, zona): 
        self._zonas.append(zona)

    def cantidadTotalAnimales(self): 
        cont=0
        for i in self._zonas:
            total+= i.cantidadAnimales()
        return cont 

