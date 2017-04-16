from node import *
from arestas import *
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

    def inicializaDicionariosTopografias(self):
        for i in self.listaDeNodos.values():
            for j in range(self.numeroDeArestas):
                if j not in i.topografiaAtualiza.keys():
                    i.topografiaAtualiza[j] = False



    def criaAresta(self, a, b, peso=0):
        #Adiciona nas vizinhancas dos nodos
        self.listaDeNodos[a].adicionaVizinhos(self.listaDeNodos[b], self.codigoAresta, peso)
        self.listaDeNodos[b].adicionaVizinhos(self.listaDeNodos[a], self.codigoAresta, peso)
        #Instancia as Arestas
        novaAresta = Arestas(a,b,peso,self.codigoAresta)
        self.numeroDeArestas = self.numeroDeArestas + 1
        self.listaDeArestas[self.codigoAresta] = novaAresta
        self.codigoAresta = self.codigoAresta + 1

    def getArestaSrc(self,codigoAresta):
        return self.listaDeArestas[codigoAresta].getSrc

    def convergiu(self):
        for x in self.listaDeNodos.values():
            for i in x.topografiaAtualiza.values():
                if not i:
                    return False
        return True

    def getArestaDst(self,codigoAresta):
        return self.listaDeArestas[codigoAresta].getDst

    def __iter__(self):
        return iter(self.listaDeNodos.values())
