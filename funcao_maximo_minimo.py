import pandas as pd

def funcao_maximo_minimo (dataframe, nome_coluna):
    '''
    Essa função irá receber um Data Frame juntamente coma sua coluna que deve ser 
    analisada. A função tem o objetivo de analisar os dois maiores valores dessa 
    coluna e os dois menores valores dessa coluna.
    '''
    maiores_valores = dataframe[nome_coluna].nlargest(2).tolist()
    menores_valores = dataframe[nome_coluna].nsmallest(2).tolist()
    return maiores_valores, menores_valores


