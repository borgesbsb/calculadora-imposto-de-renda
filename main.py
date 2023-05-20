import pandas as pd
import plotly.graph_objects as go
# from carteira import Carteira
# from acoes import Acoes
# from calculadoraImpostoRenda import CalculadoraImpostoRendaPadrao




# # Criando a carteira
# calculadora = CalculadoraImpostoRendaPadrao()
# carteira = Carteira(calculadora)

# Lendo o arquivo CSV com pandas
df = pd.read_csv('stocks-dataset.csv')

carteira = pd.DataFrame(columns=['Data', 'Nome', 'Preco Medio', 'Quantidade Media', 'Resultado Auferido'])


# Iterando sobre as linhas do DataFrame
preco_medio = 0
quantidade_media = 0
for index, row in df.iterrows():
    data_operacao = row['Data da operação']
    operacao = row['Operação']
    acao = row['Ação']
    preco = row['Preço']
    quantidade = row['Quantidade']
    taxa_corretagem = row['Taxa de corretagem']
#     carteira.loc[0] = [ '21/05/2021', 'PTBR4', 0, 0, 0]
#     carteira.loc[1] = [ '21/05/2021', 'PTBR4', 200, 150, 0]
#     carteira.loc[2] = [ '22/05/2021', 'PTBR4', 300, 150, 0]



    if  carteira.loc[carteira['Nome'] == acao].empty:
        carteira.loc[index] = [data_operacao, acao, round(preco,2), quantidade, 0]
    else:
        preco_medio_tmp = carteira.loc[carteira['Nome'] == acao, 'Preco Medio'].values[0]
        quantidade_media_tmp = carteira.loc[carteira['Nome'] == acao, 'Quantidade Media'].values[0]
        if operacao  == 'Compra': 
                preco_medio = ((preco_medio_tmp * quantidade_media_tmp) + (preco * quantidade) + taxa_corretagem) / (quantidade_media_tmp + quantidade)
                quantidade_media = quantidade_media_tmp + quantidade
        else:
                resultado_auferido = (preco - preco_medio_tmp) * (quantidade - taxa_corretagem)
                quantidade_media = quantidade_media_tmp - quantidade
                
                
        
        
        carteira.loc[index] = [data_operacao, acao, preco_medio, quantidade_media, 0]
        
    
print(carteira)





    # Verificando se o investimento já existe na carteira ou criando um novo
    





# # Gerando as informações consolidadas do mês
# informacoes_mes = carteira.obter_informacoes_mes()

# # Salvando as informações consolidadas em um arquivo CSV
# df_mes = pd.DataFrame(informacoes_mes, columns=["Mês", "Valor Total de Compras", "Valor Total de Vendas", "Rendimento Absoluto Bruto", "Imposto Devido", "Rendimento Absoluto Líquido"])
# df_mes.to_csv("informacoes_mes.csv", index=False)



# # Obtendo os meses e o rendimento absoluto líquido
# meses = []
# rendimento_absoluto_liquido = []
# for mes_info in informacoes_mes:
#     mes = mes_info[0]
#     rendimento_liquido = mes_info[5]
#     meses.append(mes)
#     rendimento_absoluto_liquido.append(rendimento_liquido)

# # Criando o gráfico 3D do rendimento absoluto líquido por mês
# fig = go.Figure(data=[go.Surface(z=rendimento_absoluto_liquido, x=meses, y=[1])])
# fig.update_layout(title='Rendimento Absoluto Líquido por Mês', autosize=False, width=800, height=600)
# fig.show()