from calculadora import Calculadora
import pandas as pd

from graficos import Grafico
calculadora = Calculadora('stocks-dataset.csv')
calculadora.calcular_carteira()


output1 = pd.DataFrame(columns=['Mes', 'Compra/R$', 'Venda/R$',
                       'Rendimento Bruto/R$', 'Imposto/R$', 'Rendimento Liquido/R$'])


output1['Mes'] = calculadora.carteira['Data'].dt.month_name().unique()

for index, row in output1.iterrows():
    mes = row['Mes']
    compras_df = calculadora.carteira[(calculadora.carteira['Oper'] == 'Compra') & (
        calculadora.carteira['Data'].dt.month_name() == mes)]
    valor_compra_total = compras_df['Valor Executado'].sum()
    vendas_df = calculadora.carteira[(calculadora.carteira['Oper'] == 'Venda') & (
        calculadora.carteira['Data'].dt.month_name() == mes)]
    valor_vendas_total = vendas_df['Valor Executado'].sum()
    rendimento_absoluto_bruto = calculadora.carteira[calculadora.carteira['Data'].dt.month_name(
    ) == mes].loc[:, 'Resultado Auferido'].sum()
    imposto_devido = calculadora.calcula_imposto(
        rendimento_absoluto_bruto) if rendimento_absoluto_bruto > 0 else 0
    rendimento_liquido = rendimento_absoluto_bruto - imposto_devido
    output1.loc[index] = [mes, valor_compra_total, valor_vendas_total,
                          rendimento_absoluto_bruto, imposto_devido, rendimento_liquido]


output1 = round(output1, 2)
output1.to_csv('informações_consolidadas.csv', index=False)

grafico = Grafico(calculadora, output1)
grafico.criar_dashboard()



# chart1 = px.line(output1, x='Mes', y=[
#                  'Compra/R$', 'Venda/R$', 'Rendimento Bruto/R$', 'Imposto/R$', 'Rendimento Liquido/R$'])

# petr4_data = calculadora.carteira.loc[calculadora.carteira['Nome'] == 'PETR4']

# petr4_data = calculadora.carteira.loc[calculadora.carteira['Nome'] == 'PETR4']
# # Adicionar coluna de cor
# petr4_data['Cor'] = petr4_data['Resultado Auferido'].apply(lambda x: 'blue' if x < 0 else 'red')
# # Criar o gráfico de barras
# chart2 = px.bar(petr4_data, x='Data', y='Resultado Auferido', color='Cor')


# # Configuração do layout do gráfico
# chart1.update_layout(
#     title={
#         'text': 'Rendimento por mês',
#         'x': 0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'
#     }
# )

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
# app.layout = html.Div(children=[
#     dbc.Row(
#         [
#             dbc.Col(html.H1('Welcome to my dash app', className='text-center'),
#                     width=9, style={'margin-left': '7px', 'margin-top': '7px'})
#         ],
#         justify='center',
#         style={'margin': '20px 0'}
#     ),
#     dbc.Row(
#         [
#             dbc.Col(
#                 dcc.Dropdown(
#                     id='combo-box',
#                     options=[{'label': 'Chart 1', 'value': 'chart1'},
#                              {'label': 'Chart 2', 'value': 'chart2'}],
#                     value='chart1'
#                 ),
#                 width=3,
#                 style={'margin-top': '7px'}
#             )
#         ],
#         justify='center',
#         style={'margin': '20px 0'}
#     ),
#     dbc.Row(
#         [
#             dbc.Col(
#                 dcc.Graph(id='graph', figure=chart1),
#                 width=9,
#                 style={'margin-left': '50px',
#                        'margin-top': '7px', 'margin-right': '15px'}
#             )
#         ],
#         justify='center',
#         style={'margin': '20px 0'}
#     )
# ])

# # Callback para atualizar o gráfico com base na seleção do combo box


# @app.callback(
#     Output('graph', 'figure'),
#     Input('combo-box', 'value')
# )
# def update_graph(selected_chart):
#     if selected_chart == 'chart1':
#         return chart1
#     elif selected_chart == 'chart2':
#         return chart2


# if __name__ == '__main__':
#     app.run_server(debug=True)
