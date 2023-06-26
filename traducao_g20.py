def filtro_paises_do_g20(dataframe):
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

    for indice in range (dataframe.shape[0]):
        if dataframe["country"][indice] in countries:
            pass
        else:
            dataframe = dataframe.drop(indice)
    
    return dataframe
