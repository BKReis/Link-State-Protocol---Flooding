class Mensagens:
	def __init__(self,nodoFonte,nodoDestino,codigoAresta,distancia):
		self.nodoFonte = nodoFonte
		self.nodoDestino = nodoDestino
		self.codigoAresta = codigoAresta
		self.distancia = distancia

		#self.contadorSequencia = nodoFonte.getContadorSequencia(nodoDestino)

	def enviaMensagem(self):
		self.nodoDestino.atualizaTopografia(self.codigoAresta,self.distancia)
