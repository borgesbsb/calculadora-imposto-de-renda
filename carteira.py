class Carteira:
    def __init__(self):
        self._preco_medio = 0.0
        self._quantidade_media = 0
        self._resultado_mes = 0.0
        self._prejuizo_acumulado = 0.0

    def calcular_compra(self, preco_compra, quantidade_compra, taxa_corretagem_compra):
        self._preco_medio = (self._preco_medio * self._quantidade_media + preco_compra * quantidade_compra + taxa_corretagem_compra) / (self._quantidade_media + quantidade_compra)
        self._quantidade_media += quantidade_compra

    def calcular_venda(self, preco_venda, quantidade_venda, taxa_corretagem_venda):
        resultado_atual = (preco_venda - self._preco_medio) * quantidade_venda - taxa_corretagem_venda
        self._quantidade_media -= quantidade_venda
        self._resultado_mes += resultado_atual

        if resultado_atual < 0:
            self._prejuizo_acumulado += resultado_atual
        else:
            self._prejuizo_acumulado -= min(resultado_atual, self._prejuizo_acumulado)

    def calcular_imposto(self):
        imposto_devido = (self._resultado_mes - min(self._resultado_mes, self._prejuizo_acumulado)) * 0.15
        return imposto_devido

    @property
    def preco_medio(self):
        return self._preco_medio

    @preco_medio.setter
    def preco_medio(self, valor):
        self._preco_medio = valor

    @property
    def quantidade_media(self):
        return self._quantidade_media

    @quantidade_media.setter
    def quantidade_media(self, valor):
        self._quantidade_media = valor

    @property
    def resultado_mes(self):
        return self._resultado_mes

    @resultado_mes.setter
    def resultado_mes(self, valor):
        self._resultado_mes = valor

    @property
    def prejuizo_acumulado(self):
        return self._prejuizo_acumulado

    @prejuizo_acumulado.setter
    def prejuizo_acumulado(self, valor):
        self._prejuizo_acumulado = valor
