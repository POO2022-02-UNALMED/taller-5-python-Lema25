
class Animal:

	_totalAnimales = 0

	def __init__(self,nombre, edad, habitat, genero, zona=None):
		self._nombre = nombre
		self._edad = edad
		self._habitat = habitat
		self._genero = genero
		self._zona = zona
		Animal._totalAnimales+=1

	def getHabitat(self):
		return self._habitat
	def setHabitat(self, habitat):
		self._habitat = habitat

	def getGenero(self):
		return self._genero
	def setGenero(self, genero):
		self._genero = genero

	def getZona(self):
		return self._zona[0]
	def setZona(self, zona):
		self._zona[0] = zona

	def getNombre(self):
		return self._nombre
	def setNombre(self,nombre):
		self._nombre = nombre

	def getEdad(self):
		return self._edad
	def setEdad(self, edad):
		self._edad = edad

	def getTotalAnimales(cls):
		return cls._totalAnimales

	def movimiento():
		return "desplazarse"

	@classmethod
	def totalPorTipo(cls):
		from Anfibio import Anfibio
		from Reptil import Reptil
		from Mamifero import Mamifero
		from Ave import Ave
		from Pez import Pez

		return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"

	def toString(self):
		if self._zona != None:
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()} en el {self._zona.getZoo().getNombre()}"
		else:
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"


