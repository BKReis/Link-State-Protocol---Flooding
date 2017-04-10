import sys

class Nodos:
	def __init__(self,nome):
		self.nome = nome
		self.conectadoCom = {}
		self.contadorIdadeVizinho = {}
		self.contadorSequencia = {}

	def adicionaVizinhos(self,vizinho,peso=0,contadorSequencia=1):
		self.conectadoCom[vizinho] = peso
		#TO DO 
		#Alem do contadorIdade o livro sugere uma segunda variavel
		#para toda vez que esse contadorIdade estourar incrementar
		#essa segunda variavel para nao haver erros de interpreta-
		#cao de idades por parte dos nos
		self.contadorIdadeVizinho[vizinho] = sys.maxint
		self.contadorSequencia[vizinho] = contadorSequencia

	#TO DO
	#def reiniciaNodo(self,nome):

	def desativaLink(self,vizinho):
		self.conectadoCom[vizinho] = sys.maxint

	def getContadorSequencia(self,vizinho):
		return self.contadorSequencia[vizinho]

	def getContadorIdadeLink(self,vizinho):
		return self.contadorIdadeVizinho[vizinho]

	def getConexoes(self):
		return self.conectadoCom.keys()

	def getNome(self):
		return self.nome

	def getPeso(self,vizinho):
		return self.conectadoCom[vizinho]