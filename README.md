# Projeto Calculadora de Investimentos

Este projeto consiste em uma calculadora de investimentos que realiza o cálculo do rendimento de uma carteira de ações, considerando compras e vendas realizadas ao longo do tempo. Além disso, o projeto também inclui a geração de gráficos para visualização do desempenho da carteira e a obtenção de informações sobre as ações através de scraping de notícias.

## Funcionalidades

A calculadora de investimentos possui as seguintes funcionalidades:

1. Leitura de dados de operações a partir de um arquivo CSV: A classe `Calculadora` lê os dados de operações de compra e venda de ações a partir de um arquivo CSV, utilizando a biblioteca `pandas`.

2. Cálculo do rendimento e imposto devido: A classe `Calculadora` realiza o cálculo do rendimento bruto e líquido da carteira de investimentos, considerando as operações de compra e venda. Além disso, calcula o valor do imposto devido sobre o rendimento auferido.

3. Resumo mensal de rendimentos: A classe `Calculadora` gera um resumo mensal dos rendimentos, mostrando o valor total de compras, vendas, rendimento bruto, imposto devido e rendimento líquido para cada mês.

4. Geração de gráficos: A classe `Grafico` é responsável por gerar gráficos para visualização do desempenho da carteira de investimentos. São gerados dois tipos de gráficos: um gráfico de linha mostrando o rendimento por mês e gráficos de barras mostrando o resultado auferido por ação e o imposto devido.

5. Obtenção de informações sobre as ações: A classe `Grafico` realiza scraping de notícias para obter informações sobre as ações presentes na carteira de investimentos. Essas informações são utilizadas para explicar o desempenho das ações no gráfico.

## Tecnologias utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- Python 3: Linguagem de programação principal utilizada no projeto.
- pandas: Biblioteca de análise de dados utilizada para a leitura e manipulação dos dados de operações.
- plotly: Biblioteca utilizada para a geração de gráficos interativos.
- Dash: Framework utilizado para criar a interface de usuário em formato de dashboard.
- Dash Bootstrap Components: Biblioteca utilizada para estilizar a interface de usuário com o tema Cerulean.
- asyncio: Biblioteca utilizada para realizar operações assíncronas, como o scraping de notícias.
- OpenAI GPT-3.5: Modelo de linguagem utilizado para realizar consultas e obter informações sobre as ações.

## Como executar o projeto

Siga as instruções abaixo para executar o projeto:

1. Clone o repositório do projeto executando o seguinte comando:
```shell
git clone https://github.com/borgesbsb/calculadora-imposto-de-renda.git
```

2. Navegue até o diretório do projeto:
```shell
cd calculadora-imposto-de-renda
```

3. Instale as dependências do projeto executando o comando:
```shell
pip install -r requirements.txt
```
4. Insira a chave de API criada em  https://platform.openai.com/account/api-keys` no arquivo main.py no parametro "key_openai". 

5. Execute o comando abaixo para iniciar a aplicação:
```shell
python main.py
```

5. Acesse o aplicativo no navegador utilizando o endereço `http://localhost:8050`.

## Limitações e melhorias

É importante mencionar algumas limitações do projeto e possíveis melhorias futuras:

- O cálculo do imposto devido considera apenas a alíquota padrão para operações de venda de ações. Poderia ser implementada uma lógica mais complexa para considerar diferentes alíquotas de acordo com o valor da venda e o prazo de permanência na carteira.
- A obtenção de informações sobre as ações é realizada através de scraping de notícias utilizando o modelo OpenAI GPT-3.5. Essa abordagem pode ter algumas limitações e não garante a precisão das informações. Poderia ser implementada uma integração com uma API de dados financeiros para obter informações mais confiáveis.
- O aplicativo Dash atualmente possui uma interface básica. Poderia ser aprimorado com recursos adicionais, como filtros de data, seleção de ações, entre outros.

