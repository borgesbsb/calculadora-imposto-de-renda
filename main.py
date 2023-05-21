from calculadora import Calculadora
from graficos import Grafico


calculadora = Calculadora('stocks-dataset.csv')

calculadora.calcular_carteira()

output1 = calculadora.calcular_resumo_mensal()

output1.to_csv('informações_consolidadas.csv', index=False)

output2 = Grafico(calculadora, output1)

output2.criar_dashboard()