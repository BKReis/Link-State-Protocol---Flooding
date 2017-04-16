class Arestas:
    def __init__(self, src, dst, peso, codigo):
        self.src = src
        self.dst = dst
        self.peso = peso
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def getPeso(self):
        return self.peso

    def getSrc(self):
        return self.src

    def getDst(self):
        return self.dst
