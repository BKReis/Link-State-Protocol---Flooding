class Nodos:
	def __init__(self,nome):
		self.nome = nome
		self.conectadoCom = {}
		self.contadorIdadeVizinho = {}

	def adicionaVizinhos(self,vizinho,peso=0,contadorIdade=0):
		self.conectadoCom[vizinho] = peso 
		self.contadorIdadeVizinho[vizinho] = contadorIdade

	def getContadorIdadeLink(self,vizinho):
		return self.contadorIdadeVizinho[vizinho]

	def getConexoes(self):
		return self.conectadoCom.keys()

	def getNome(self):
		return self.nome

	def getPeso(self,vizinho):
		return self.conectadoCom[vizinho]