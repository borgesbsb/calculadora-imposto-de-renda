import requests
from bs4 import BeautifulSoup

class NewsScraper:
    @staticmethod
    def obter_ultimas_noticias(papeis):
        # Construir a URL da página de notícias do Google com base nos papéis fornecidos
        query = ' '.join(papeis)
        url = f"https://news.google.com/search?q={query}&hl=pt-BR&gl=BR&ceid=BR%3Apt-419"

        # Enviar requisição GET para obter o conteúdo da página
        response = requests.get(url)

        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Parsear o conteúdo HTML usando BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Encontrar os elementos HTML que contêm as notícias
            news_elements = soup.find_all("div", class_="NiLAwe")

            # Lista para armazenar os títulos das notícias
            titulos = []

            # Contador para controlar o número de notícias exibidas
            count = 0

            # Iterar sobre os elementos de notícias e extrair os títulos
            for news in news_elements:
                title = news.find("a", class_="DY5T1d").text
                titulos.append(title)
                count += 1

                if count >= 10:
                    break
            titulos = ' '.join(titulos)
            return titulos
        else:
            print("Falha ao obter as últimas notícias.")
