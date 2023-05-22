import openai
class OpenAIChat:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def realizar_consulta(self, pergunta, contexto, max_tokens=600):
        prompt = f"Q: Faça uma análise da pespectiva de crescimento mesmo que limitada sobre {pergunta} conforme as seguintes noticias: {contexto}  \nA:"
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                                messages=[{
                                                        "role": "user", 
                                                        "content": prompt}])
        resposta = response["choices"][0]["message"]["content"]
        return resposta

        return "Nada aqui"
