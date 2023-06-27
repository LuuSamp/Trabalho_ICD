import pandas as pd

def funcao_maximo_minimo(dataframe, nome_coluna, nome_coluna_pais):
    '''
    Essa função irá receber um DataFrame juntamente com a sua coluna que deve ser 
    analisada. A função tem o objetivo de analisar os dois maiores valores dessa 
    coluna e os dois menores valores dessa coluna. Ela vai associar os valores aos 
    nomes dos países que cada um representa e especificar uma cor para cada país.
    '''
    
    # Pegando os maiores valores da coluna e associando aos seus países:
    maiores_valores = dataframe[nome_coluna].nlargest(2)
    maiores_paises = dataframe[nome_coluna_pais].iloc[maiores_valores.index].tolist()

    # Pegando os menores valores da coluna e associando aos seus países:
    menores_valores = dataframe[nome_coluna].nsmallest(2)
    menores_paises = dataframe[nome_coluna_pais].iloc[menores_valores.index].tolist()

    # Juntando as duas listas de maiores e menores países:
    lista_total = maiores_paises + menores_paises

    # Criando o dicionário que atribui as cores para cada país:
    dicionario_paises_cores = {
        lista_total[0]: "#900C3F",
        lista_total[1]: "#FA4343",
        lista_total[2]: "#084C9F",
        lista_total[3]: "#2685F8"
    }

    return dicionario_paises_cores
