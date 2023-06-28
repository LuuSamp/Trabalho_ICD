import pandas as pd  

def filtro_paises_do_g20(dataframe, filtrar=True, agrupamento="year"):
    '''
    A função recebe um dataframe e um argumento opicional. Caso o argumento seja falso, ela apenas retira
    os países que não fazem parte do G20 do dataframe. Caso o argumento seja verdadeiro, ela, além de
    retirar todos que não fazem parte do G20, ela vai agrupar todos os países que pertencem à União Europeia 
    (exceto Alemanha, Itália e França) em um único registro "European Union", sendo ele a média de todos
    os países agrupados. 

    É necessário passar como agrupamento qual coluna que deve ser agrupada, caso não seja passado nenhum, ela 
    vai agrupar por ano.
    '''
    paises_do_g20 = [
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
    paises_ue = [
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
    for indice_de_cada_linha in range (dataframe.shape[0]):
        if dataframe["country"][indice_de_cada_linha] in paises_do_g20:
            pass
        else:
            dataframe = dataframe.drop(indice_de_cada_linha)

    dataframe = dataframe.reset_index()
    del dataframe['index']


    if filtrar == True:

        #VAI CRIAR UMA NOVA COLUNA DE BOLEANOS PARA SABER SE SÃO DA UNIÃO EUROPEIA
        lista_de_confirmacao = list()
        for indice in range(dataframe.shape[0]):
            if dataframe["country"][indice] in paises_ue:
                lista_de_confirmacao.append(True)
            else:
                lista_de_confirmacao.append(False)
        dataframe["PAIS_UE"] = lista_de_confirmacao
        
        dataframe_ue = dataframe[dataframe["PAIS_UE"]==True]
        dataframe_ue["country"] = "European Union"
   
        if agrupamento == "year":

            #VAMOS CRIAR UM NOVO DATAFRAME SÓ COM DA UNIÃO EUROPEIA E VAMOS JUNTAR ELES AGRUPANDO POR ANO
            del dataframe_ue["country"]
            dataframe_ue = dataframe_ue.groupby("year").mean().round(4).reset_index()
            dataframe_ue["country"] = "European Union"

        if agrupamento == "country":

            #VAMOS CRIAR UM NOVO DATAFRAME SÓ COM DA UNIÃO EUROPEIA E VAMOS JUNTAR ELES AGRUPANDO POR ANO"
            dataframe_ue = dataframe_ue.groupby("country").mean().round(4).reset_index()
            dataframe = dataframe.groupby("country").mean().round(4).reset_index()

         #VAMOS RETIRAR DO DATAFRAME ORIGINAL OS QUE SERIAM DA UNIÃO EUROPEIA
        for indice in range(dataframe.shape[0]):
            if dataframe["country"][indice] in paises_ue:
                dataframe = dataframe.drop(indice)
            else:
                pass

        #VAI CONCATENAR OS DOIS DATAFRAMES E FORMATÁ-LOS
        dataframe = pd.concat([dataframe, dataframe_ue]).reset_index()
        del dataframe['PAIS_UE']
        del dataframe['index']

    return dataframe