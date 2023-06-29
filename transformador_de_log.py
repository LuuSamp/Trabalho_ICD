import numpy as np
def transformador_log10(dataframe, lista_de_variaveis):
    '''
    Função para mudar a escala dos dados para a escala log10 e facilitar a visualização.
    '''

    for cada_variavel in lista_de_variaveis:
        dataframe[f"{cada_variavel}_log"] = np.log10(dataframe[cada_variavel])

    return dataframe