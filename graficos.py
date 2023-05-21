from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from scrapping import NewsScraper


class Grafico:
    def __init__(self, calculadora, output1):
        self.output1 = output1
        self.calculadora = calculadora
        self.chart1 = None
        self.chart2 = None

    def criar_grafico_linha(self):
        self.chart1 = px.line(self.output1, x='Mes', y=['Compra/R$', 'Venda/R$', 'Rendimento Bruto/R$', 'Imposto/R$', 'Rendimento Liquido/R$'])
        self.chart1.update_layout(
            title={
                'text': 'Rendimento por mês',
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

    def criar_grafico_barras(self):
        graficos = {}
        acoes = self.calculadora.carteira['Nome'].unique()

        for acao in acoes:
            acao_data = self.calculadora.carteira.loc[self.calculadora.carteira['Nome'] == acao].copy()
            acao_data['Cor'] = acao_data['Resultado Auferido'].apply(lambda x: 'blue' if x < 0 else 'red')

            grafico = px.bar(acao_data, x='Data', y='Resultado Auferido', color='Cor', title=f'Resultado Auferido - {acao}')
            grafico.update_layout(
                title={
                    'text': f'Resultado Auferido - {acao}',
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'
                }
            )
            graficos[acao] = grafico
            
        imposto_data = self.output1[['Mes', 'Imposto/R$']]
        grafico_imposto = px.bar(imposto_data, x='Mes', y='Imposto/R$', title='Imposto de Renda a Pagar')
        grafico_imposto.update_layout(
            title={
                'text': 'Imposto de Renda a Pagar',
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )
        graficos['Imposto de Renda'] = grafico_imposto

        self.chart2 = graficos

    def criar_dropdown_options(self):
        acoes = self.calculadora.carteira['Nome'].unique()
        options = [{'label': f'Chart - {acao}', 'value': acao} for acao in acoes]
        options.append({'label': 'Chart - Rendimento por Mês', 'value': 'chart1'})
        options.append({'label': 'Chart - Imposto de Renda a Pagar', 'value': 'Imposto de Renda'})
        return options

    def explicar_desempenho(self, acao):
        if acao == 'chart1':
            informacoes = "Informações para Chart - Rendimento por Mês"
        elif acao == 'Imposto de Renda':
            informacoes = "Informações para Chart - Imposto de Renda a Pagar"
        elif acao != None:
            scraping = NewsScraper()
            papeis = ['PETR4']
            scraping.obter_ultimas_noticias(papeis)    
            informacoes = f"Informações para Chart - {acao}"
        else:
            informacoes = "Nenhuma informação disponível"

        return informacoes


    def criar_dashboard(self):
        self.criar_grafico_linha()
        self.criar_grafico_barras()

        app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

        app.layout = html.Div(children=[
            dbc.Row(
                [
                    dbc.Col(html.H1('Calculadora de Impostos', className='text-center'),
                            width=9, style={'margin-left': '7px', 'margin-top': '7px'})
                ],
                justify='center',
                style={'margin': '20px 0'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Dropdown(
                            id='combo-box',
                            options=self.criar_dropdown_options(),
                            value='Imposto de Renda'
                        ),
                        width=3,
                        style={'margin-top': '7px'}
                    )
                ],
                justify='center',
                style={'margin': '20px 0'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(id='graph'),
                        width=9,
                        style={'margin-left': '50px',
                               'margin-top': '7px', 'margin-right': '15px'}
                    )
                ],
                justify='center',
                style={'margin': '20px 0'}
            ),
            dbc.Row(
                [
                   dbc.Col(
                        dbc.Alert(
                            [
                                html.Img(src="./assets/chatgpt.png", className="chatgpt",style={"width": "50px", "height": "50px"}),
                                html.Div(id='explicacao-desempenho')
                            ],
                            color="info",
                            className="alert-logo"
                        ),
                        width=9,
                        style={'margin-left': '50px',
                               'margin-top': '7px', 'margin-right': '15px'}
                    )
                ],
                justify='center',
                style={'margin': '20px 0'}
            )
        ])

        @app.callback(
            Output('graph', 'figure'),
            Output('explicacao-desempenho', 'children'),
            Input('combo-box', 'value')
        )
        def update_graph(selected_chart):
            explicacao = self.explicar_desempenho(selected_chart)
            if selected_chart == 'chart1':
                explicacao = self.explicar_desempenho("Mês")
                return self.chart1, explicacao
            elif selected_chart == 'Imposto de Renda':
                explicacao = self.explicar_desempenho("Imposto de Renda")
                return self.chart2['Imposto de Renda'], explicacao
            elif selected_chart is not None:
                explicacao = self.explicar_desempenho(selected_chart)
                return self.chart2[selected_chart], explicacao
            else:
                return self.chart2[selected_chart], explicacao
        
        @app.callback(
                Output('explicacao-desempenho', 'children'),
                Input('combo-box', 'value')
        )
        def update_explicacao(selected_chart):
                explicacao = self.explicar_desempenho(selected_chart)
                return explicacao

        app.run_server(debug=True)
