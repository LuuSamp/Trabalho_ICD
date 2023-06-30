from variaveis_globais import *
dicionario_paises_cores = DICT_CORES

def criador_colunas_esteticas(dataframe, cores=True, alpha=True, legenda=True):
    """
    A função tem como objetivo receber um dataframe e criar nele uma coluna com cor, uma com preenchimento/alpha
    e uma com legenda. Essas colunas seão usadas por alguns gráficos para configurar esses mesmos atributos estéticos.
    """
    coluna_de_cores = []
    coluna_de_alpha = []
    coluna_de_legenda = []

    for cada_pais in dataframe["country"]:
        
        if cada_pais in dicionario_paises_cores.keys():
            if cores == True:
                coluna_de_cores.append(dicionario_paises_cores[cada_pais])
            if alpha == True:
                coluna_de_alpha.append(ALPHA_DESTAQUES)
            if legenda == True:
                coluna_de_legenda.append(cada_pais)
        else:
            if cores == True:
                coluna_de_cores.append(CORES_COMUNS)
            if alpha == True:
                coluna_de_alpha.append(ALPHA_COMUNS)
            if legenda == True:
                coluna_de_legenda.append("Other Countries")

    if cores == True:
        dataframe["color"] = coluna_de_cores
    if alpha == True:
        dataframe["preenchimento"] = coluna_de_alpha
    if legenda == True:
        dataframe["legenda"] = coluna_de_legenda

    return dataframe
    
