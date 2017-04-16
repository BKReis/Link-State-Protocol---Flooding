import sys

class Nodos:
	def __init__(self,nome):
		self.nome = nome
		self.conectadoCom = {}
		self.contadorSequencia = {}
		#Dicionario codigo da aresta com Distancia
		self.topografiaDistancia = {}
		#Dicionario codigo da aresta com codigo se foi atualizado ou nao
		self.topografiaAtualiza = {}

	def atualizaTopografia(self,codigoAresta,Distancia):
		self.topografiaDistancia[codigoAresta] = Distancia
		self.topografiaAtualiza[codigoAresta] = True

	def adicionaVizinhos(self,vizinho,codigoAresta,peso=0,contadorSequencia=1):
		self.conectadoCom[vizinho] = peso
		self.contadorSequencia[vizinho] = contadorSequencia
		self.topografiaDistancia[codigoAresta] = peso
		self.topografiaAtualiza[codigoAresta] = True

	def getContadorSequencia(self,vizinho):
		return self.contadorSequencia[vizinho]

	def getConexoes(self):
		return self.conectadoCom.keys()

	def getNome(self):
		return self.nome

	def getPeso(self,vizinho):
		return self.conectadoCom[vizinho]