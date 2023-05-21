from calculadora import Calculadora
from graficos import Grafico
from scraping import NewsScraper
from chatgpt import OpenAIChat

calculadora = Calculadora('stocks-dataset.csv')

calculadora.calcular_carteira()

output1 = calculadora.calcular_resumo_mensal()

output1.to_csv('informações_consolidadas.csv', index=False)

scraper = NewsScraper()

chatgpt = OpenAIChat(api_key='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')

output2 = Grafico(calculadora, output1, scraper, chatgpt)

output2.criar_dashboard()