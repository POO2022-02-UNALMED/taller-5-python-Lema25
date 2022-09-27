from zooAnimales.Animal import Animal

class Anfibio(Animal):
	_listado = []
	ranas = 0
	salamandras = 0

	def __init__(self,nombre, edad, habitat, genero, colorPiel, venenoso):
		super().__init__(nombre, edad, habitat, genero)
		self._colorPiel = colorPiel
		self._venenoso = venenoso
		Anfibio._listado.append(self)

	def getColorPiel(self):
		return self._colorPiel
	def setColorPiel(self,colorPiel):
		self._colorPiel = colorPiel

	def isVenenoso(self):
		return self._venenoso
	def setVenenoso(self,venenoso):
		self._venenoso = venenoso

	def getListado(cls):
		return Anfibio._listado
	def setListado(cls,listado):
		Anfibio._listado = listado
        
	@classmethod
	def crearRana(cls,nombre,edad,genero):
		Anfibio.ranas+=1
		return Anfibio(nombre, edad, "selva", genero, "rojo", True)

	@classmethod
	def crearSalamandra(cls,nombre,edad,genero):
		Anfibio.salamandras+=1
		return Anfibio(nombre, edad, "selva", genero, "negro", False)

	@classmethod
	def cantidadAnfibios(cls):
		return len(Anfibio._listado)

