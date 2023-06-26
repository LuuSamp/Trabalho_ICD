import pandas as pd   

def media_de_escolaridade(dataframe_homens, dataframe_mulheres, nome_da_coluna):
    '''
    A função tem como objetivo receber dois dataframes do mesmo indicador, um de homens e outro de mulheres, 
    receber também o nome da coluna desse indicador e retornar um dataframe idêntico aos dois anteriores, mas na
    coluna do indicador ele terá a média entre homens e mulheres. (Considerando que a proporção geralmente é 50/50)
    '''
    dataframe_final = pd.DataFrame()
    dataframe_final["country"] = dataframe_homens["country"]
    dataframe_final["year"] = dataframe_homens["year"]
    dataframe_final[f"{nome_da_coluna}"] = (dataframe_homens[f"{nome_da_coluna}"]+dataframe_mulheres[f"{nome_da_coluna}"])/2

    return dataframe_final
