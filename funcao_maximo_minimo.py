import pandas as pd

def funcao_maximo_minimo(dataframe, nome_coluna, nome_coluna_pais):
    '''
    Essa função irá receber um DataFrame juntamente com a sua coluna que deve ser 
    analisada. A função tem o objetivo de analisar os dois maiores valores dessa 
    coluna e os dois menores valores dessa coluna. Associa os valores aos nomes dos
    países usando a coluna especificada.
    '''
    maiores_valores = dataframe[nome_coluna].nlargest(2)
    maiores_paises = dataframe[nome_coluna_pais].iloc[maiores_valores.index]

    menores_valores = dataframe[nome_coluna].nsmallest(2)
    menores_paises = dataframe[nome_coluna_pais].iloc[menores_valores.index]

    dicionario = {}

    for valor, pais in zip(maiores_valores, maiores_paises):
        dicionario[pais] = valor

    for valor, pais in zip(menores_valores, menores_paises):
        dicionario[pais] = valor

    return dicionario

