from reorganizador import traduz_milhares
import pandas as pd  

def filtro_paises_do_g20(dataframe, nome_da_coluna="indice_analisado"):
    '''
    Função recebe o dataframe, modifica ele, retira os países que não pertecenssem ao g20, 
    além disso ela vai juntar todos os países que fazem parte da UE (exceto ALE, FRA e ITA)
    e guarda em um único registro "European Union", fazendo uma média. 
    '''
    countries = [
    'Argentina',
    'Australia',
    'Austria',
    'Belgium',
    'Brazil',
    'Bulgaria',
    'Canada',
    'China',
    'Croatia',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Estonia',
    'Finland',
    'France',
    'Germany',
    'Greece',
    'Hungary',
    'India',
    'Indonesia',
    'Ireland',
    'Italy',
    'Japan',
    'Latvia',
    'Lithuania',
    'Luxembourg',
    'Malta',
    'Mexico',
    'Netherlands',
    'Poland',
    'Portugal',
    'Romania',
    'Russia',
    'Saudi Arabia',
    'Slovakia',
    'Slovenia',
    'South Africa',
    'South Korea',
    'Spain',
    'Sweden',
    'Turkey',
    'United Kingdom',
    'United States'
]
    eu_countries = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "Greece",
    "Hungary",
    "Ireland",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden"
]

    #VAI RETIRAR TODAS AS LINHAS QUE NÃO SÃO DO G20 E RESETAR O ÍNDICE
    for indice in range (dataframe.shape[0]):
        if dataframe["country"][indice] in countries:
            pass
        else:
            dataframe = dataframe.drop(indice)
    
    dataframe = dataframe.reset_index()
    del dataframe['index']

    #VAI CRIAR UMA NOVA COLUNA DE BOLEANOS PARA SABER SE SÃO DA UNIÃO EUROPEIA
    lista_de_confirmacao = list()
    for indice in range(dataframe.shape[0]):
        if dataframe["country"][indice] in eu_countries:
            lista_de_confirmacao.append(True)
        else:
            lista_de_confirmacao.append(False)

    dataframe["UE"] = lista_de_confirmacao

    #VAMOS CRIAR UM NOVO DATAFRAME SÓ COM DA UNIÃO EUROPEIA E VAMOS JUNTAR ELES AGRUPANDO POR ANO
    dataframe_ue = dataframe[dataframe["UE"]==True]
    dataframe_ue[f"{nome_da_coluna}"] = dataframe_ue[f"{nome_da_coluna}"].apply(traduz_milhares)
    dataframe_ue[f"{nome_da_coluna}"] = dataframe_ue[f"{nome_da_coluna}"].astype(float)
    dataframe_ue = dataframe_ue.groupby("year")[f"{nome_da_coluna}"].mean().round(2).reset_index()
    dataframe_ue["country"] = "European Union"

    #VAMOS RETIRAR DO DATAFRAME ORIGINAL OS QUE SERIAM DA UNIÃO EUROPEIA
    for indice in range(dataframe.shape[0]):
        if dataframe["country"][indice] in eu_countries:
            dataframe = dataframe.drop(indice)
        else:
            pass

    #VAI TRADUZIR A COLUNA QUANTITATIVA PARA FLOATS
    dataframe[f"{nome_da_coluna}"] = dataframe[f"{nome_da_coluna}"].apply(traduz_milhares)
    dataframe[f"{nome_da_coluna}"] = dataframe[f"{nome_da_coluna}"].astype(float)

    #VAI CONCATENAR OS DOIS DATAFRAMES E FORMATÁ-LOS
    dataframe_final = pd.concat([dataframe, dataframe_ue]).reset_index()
    del dataframe_final['UE']
    del dataframe_final['index']

    return dataframe_final
