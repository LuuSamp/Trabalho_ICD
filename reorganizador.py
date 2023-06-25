import pandas as pd

def reorganiza(datapath: str, column_name: str, first_year: int, last_year: int):
    '''
    Deve receber um caminho para um arquivo CSV do gapminder e um nome relacionado aos dados.
    Cria um dataframe com 3 colunas: o nome do país, o ano e os valores com o nome recebido.
    Cria um CSV com caminho "dados/column_name_reorganized.csv.
    Retorna o dataframe criado.
    '''

    initial_dataframe = pd.read_csv(datapath)

    new_format = {
    "country":[],
    "year":[],
    column_name:[]
    }
    
    # Preenchendo os nomes dos países e os anos
    for country in initial_dataframe["country"]:
        for year in range(first_year, last_year + 1, 1):
            new_format["country"].append(country)
            new_format["year"].append(str(year))

    # Preenchendo a nova coluna
    for index, country in enumerate(new_format["country"]):
        new_format[column_name].append(initial_dataframe.loc[initial_dataframe["country"] == country, new_format["year"][index]].iloc[0])

    # Armazenando em um novo DataFrame e CSV
    new_dataframe = pd.DataFrame(new_format)
    new_dataframe.to_csv(f"dados/{column_name}_reorganized.csv", index = False)

    return new_dataframe