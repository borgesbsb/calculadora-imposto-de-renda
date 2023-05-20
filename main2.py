from calculadora import Calculadora
import pandas as pd
import plotly.express as px



calculadora = Calculadora('stocks-dataset.csv')
calculadora.calcular_carteira()


output1 = pd.DataFrame(columns=['Mes', 'Compra/R$', 'Venda/R$', 'Rendimento Bruto/R$', 'Imposto/R$', 'Rendimento Liquido/R$'])


output1['Mes'] = calculadora.carteira['Data'].dt.month_name().unique()

for index, row in output1.iterrows():
        mes = row['Mes']
        compras_df = calculadora.carteira[(calculadora.carteira['Oper'] == 'Compra') & (calculadora.carteira['Data'].dt.month_name() == mes)]
        valor_compra_total = compras_df['Valor Executado'].sum()
        vendas_df = calculadora.carteira[(calculadora.carteira['Oper'] == 'Venda') & (calculadora.carteira['Data'].dt.month_name() == mes)]
        valor_vendas_total = vendas_df['Valor Executado'].sum()
        rendimento_absoluto_bruto = calculadora.carteira[calculadora.carteira['Data'].dt.month_name() == mes].loc[:,'Resultado Auferido'].sum() 
        imposto_devido = calculadora.calcula_imposto(rendimento_absoluto_bruto) if rendimento_absoluto_bruto > 0 else 0
        rendimento_liquido = rendimento_absoluto_bruto - imposto_devido
        output1.loc[index] = [mes, valor_compra_total, valor_vendas_total, rendimento_absoluto_bruto, imposto_devido, rendimento_liquido ] 
         

output1 = round(output1, 2)
output1.to_csv('informações_consolidadas.csv', index=False)


fig = px.line(output1, x='Mes', y=['Compra/R$', 'Venda/R$', 'Rendimento Bruto/R$', 'Imposto/R$', 'Rendimento Liquido/R$'])
fig.show()

