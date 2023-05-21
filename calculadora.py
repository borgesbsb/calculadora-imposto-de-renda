import pandas as pd


class Calculadora:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, parse_dates=['Data da operação'])
        self.carteira = pd.DataFrame(columns=['Data', 'Nome', 'Preço', 'Preco Medio',
                                     'Quantidade', 'Quantidade Media', 'Oper', 'Valor Executado', 'Resultado Auferido', 'Lucro/Prejuizo'])
        self.lucro_prejuizo = 0

    def calcula_imposto(self, resultado_auferido_mes):
        if resultado_auferido_mes > 0:
            return resultado_auferido_mes * 0.15
        return 0

    def total_compra():
        return self.carteira.loc[self.carteira['Oper'] == 'Compra', 'Quantidade'].sum()

    def total_venda():
        return self.carteira.loc[self.carteira['Oper'] == 'Venda', 'Quantidade'].sum()
    
    def calcular_resumo_mensal(self):
        output1 = pd.DataFrame(columns=['Mes', 'Compra/R$', 'Venda/R$',
                                        'Rendimento Bruto/R$', 'Imposto/R$', 'Rendimento Liquido/R$'])

        output1['Mes'] = self.carteira['Data'].dt.month_name().unique()

        for index, row in output1.iterrows():
            mes = row['Mes']
            compras_df = self.carteira[(self.carteira['Oper'] == 'Compra') & (
                self.carteira['Data'].dt.month_name() == mes)]
            valor_compra_total = compras_df['Valor Executado'].sum()
            vendas_df = self.carteira[(self.carteira['Oper'] == 'Venda') & (
                self.carteira['Data'].dt.month_name() == mes)]
            valor_vendas_total = vendas_df['Valor Executado'].sum()
            rendimento_absoluto_bruto = self.carteira[self.carteira['Data'].dt.month_name(
            ) == mes].loc[:, 'Resultado Auferido'].sum()
            imposto_devido = self.calcula_imposto(
                rendimento_absoluto_bruto) if rendimento_absoluto_bruto > 0 else 0
            rendimento_liquido = rendimento_absoluto_bruto - imposto_devido
            output1.loc[index] = [mes, valor_compra_total, valor_vendas_total,
                                  rendimento_absoluto_bruto, imposto_devido, rendimento_liquido]

        output1 = output1.round(2)
        output1 = output1.applymap(lambda x: '{:.2f}'.format(x) if isinstance(x, (int, float)) else x)
        return output1

    def calcular_carteira(self):
        preco_medio = 0
        quantidade_media = 0

        for index, row in self.df.iterrows():
            data_operacao = pd.to_datetime(row['Data da operação'])
            operacao = row['Operação']
            acao = row['Ação']
            preco = row['Preço']
            quantidade = row['Quantidade']
            taxa_corretagem = row['Taxa de corretagem']

            if self.carteira.loc[self.carteira['Nome'] == acao].empty:
                preco_medio = ((preco * quantidade) +
                               taxa_corretagem) / quantidade
                self.carteira.loc[index] = [data_operacao, acao, preco, preco_medio,
                                            quantidade, quantidade, operacao,preco_medio*quantidade , 0, self.lucro_prejuizo]
            else:
                preco_medio_tmp = self.carteira.loc[self.carteira['Nome']
                                                    == acao, 'Preco Medio'].values[-1]
                quantidade_media_tmp = self.carteira.loc[self.carteira['Nome']
                                                         == acao, 'Quantidade Media'].values[-1]
                resultado_auferido_temp = self.carteira.loc[self.carteira['Nome']
                                                            == acao, 'Resultado Auferido'].values[-1]

                if operacao == 'Compra':
                    preco_medio = ((preco_medio_tmp * quantidade_media_tmp) + (
                        preco * quantidade) + taxa_corretagem) / (quantidade_media_tmp + quantidade)
                    quantidade_media = quantidade_media_tmp + quantidade
                    self.carteira.loc[index] = [data_operacao, acao, preco, preco_medio, quantidade,
                                                quantidade_media, operacao,preco_medio*quantidade, resultado_auferido_temp, self.lucro_prejuizo]
                else:
                    preco_medio = preco_medio_tmp
                    quantidade_media = quantidade_media_tmp - quantidade
                    resultado_auferido = (
                        preco - preco_medio_tmp) * quantidade - taxa_corretagem
                    self.lucro_prejuizo += resultado_auferido
                    imposto = self.calcula_imposto(resultado_auferido)
                    self.carteira.loc[index] = [data_operacao, acao, preco, preco_medio, quantidade,
                                                quantidade_media, operacao,preco_medio*quantidade, resultado_auferido, self.lucro_prejuizo - imposto]
