import abc 

class CalculadoraImpostoRenda(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calcular_imposto(self, resultado_auferido, prejuizo_acumulado):
        pass

class CalculadoraImpostoRendaPadrao(CalculadoraImpostoRenda):
    def calcular_imposto(self, resultado_auferido, prejuizo_acumulado):
        return (resultado_auferido - min(resultado_auferido, prejuizo_acumulado)) * 0.15