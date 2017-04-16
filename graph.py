from node import *
from aresta import *
class Grafo:
    def __init__(self):
        self.listaDeNodos = {}
        self.listaDeArestas = {}
        self.numeroDeNodos = 0
        self.numeroDeArestas = 0 
        self.codigoAresta = 0

    def adicionaNodo(self, nome):
        self.numeroDeNodos = self.numeroDeNodos + 1
        novoNodo = Nodos(nome)
        self.listaDeNodos[nome] = novoNodo

        return novoNodo

    def criaAresta(self, a, b, peso=0):
        #Adiciona nas vizinhanças dos nodos
        self.listaDeNodos[a].adicionaVizinhos(self.listaDeNodos[b], peso)
        self.listaDeNodos[b].adicionaVizinhos(self.listaDeNodos[a], peso)
        #Instancia as Arestas
        self.numeroDeArestas = self.numeroDeAresta + 1
        novaAresta = Arestas(a,b,peso,self.codigoAresta)
        self.listaDeArestas[self.codigoAresta] = novaAresta
        self.codigoAresta = self.codigoAresta + 1

    def getArestaSrc(self,codigoAresta):
        return self.listaDeArestas[codigoAresta].getSrc 

    def getArestaDst(self,codigoAresta):
        return self.listaDeArestas[codigoAresta].getDst

    def __iter__(self):
        return iter(self.listaDeNodos.values())

