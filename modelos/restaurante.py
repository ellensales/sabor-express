from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): #constructor
        self._nome  = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao =[]
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} - {restaurante.categoria} - {restaurante.ativo}')
            
    @property
    def ativo(self):
        return 'x' if self._ativo else ' '
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        return sum([avaliacao.nota for avaliacao in self._avaliacao]) / len(self._avaliacao)
