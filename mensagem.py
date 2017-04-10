class Mensagens:
	def __init__(self,nodoFonte,nodoDestino):
		self.nodoFonte = nodoFonte
		self.nodoDestino = nodoDestino
		self.peso = nodoFonte.getPeso(nodoDestino)
		self.contadorIdade = nodoFonte.getContadorIdadeLink(nodoDestino)
		self.contadorSequencia = nodoFonte.getContadorSequencia(nodoDestino)

		#TO DO
		#No quando recebe a mensagem decrementa contadorIdade,quando chega em
		#zero em algum link, a mensagem eh dita como velha
		#Incrementa-se contadorSequencia cada vez que a mensagem eh trocada
		#Pagina 85-86 ler novamente pra entender melhor o que eh pra fazer com o tempo