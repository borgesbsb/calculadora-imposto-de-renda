from abc import abstractmethod

class Investimento():
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.valor_total = 0
        self.operacoes = []
   
    @abstractmethod
    def adicionar_operacao(self, operacao):
        self.operacoes.append(operacao)
   