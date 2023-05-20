from calculadora import Calculadora
import pandas as pd
import numpy as np


calculadora = Calculadora('stocks-dataset.csv')
calculadora.calcular_carteira()


output1 = pd.DataFrame(columns=['Mes', 'Valor total de Compra/R$', 'Valor total de Venda/R$',
                       'Rendimento Bruto/R$', 'Imposto Devido/R$', 'Rendimento Liquido/R$'])

output1['Mes'] = calculadora.carteira['Data'].dt.month_name().unique()

#print soma de quantidade de compra por mes
print(calculadora.carteira.loc[calculadora.carteira['Oper'] == 'Compra'].groupby(calculadora.carteira['Data'].dt.month_name())['Quantidade'].sum())