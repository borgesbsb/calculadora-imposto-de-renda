import requests
from bs4 import BeautifulSoup
from scrapping import NewsScraper

class Chatgpt:
    def __init__(self):
        self.api_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

    def generate_response(self, context):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "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"
        }

        data = {
            "prompt": context,
            "max_tokens": 50
        }

        response = requests.post(self.api_endpoint, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["text"]
        else:
            return "Erro ao gerar resposta."

    def run_chatbot(self, query):
        news_scraper = NewsScraper()
        context = news_scraper.scrape_news(query)

        response = self.generate_response(context)
        print(response)


