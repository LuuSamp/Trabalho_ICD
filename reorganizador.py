import pandas as pd

def reorganiza(datapath: str, column_name: str, first_year: int, last_year: int, csv = False):
    '''
    Deve receber um caminho para um arquivo CSV do gapminder, um nome relacionado aos dados, o primeiro ano e o último ano.
    O quinto parâmetro, csv, deve ser um booleano (True or False).
    Cria um dataframe com 3 colunas: o nome do país, o ano e os valores com o nome recebido.
    Se csv = True, cria um CSV com caminho "dados/column_name_reorganized.csv.
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

    new_dataframe = pd.DataFrame(new_format)

    # Armazenando em um novoCSV
    if csv == True:
        new_dataframe.to_csv(f"dados/{column_name}_reorganized.csv", index = False)

    return new_dataframe

def traduz_milhares(initial_value):
    '''
    Recebe um valor.
    Converte todos os dados numéricos com k para seus valores exatos.
    Retorna o valor convertido
    '''
    if type(initial_value) == int: return initial_value
    if type(initial_value) == float: return initial_value
    if initial_value.isnumeric(): return initial_value 

    if "k" in initial_value:
        value = initial_value.split("k")[0]
        multiplier = 1000
    elif "M" in initial_value:
        value = initial_value.split("M")[0]
        multiplier = 1000000
    elif "B" in initial_value:
        value = initial_value.split("B")[0]
        multiplier = 1000000000
    elif "TR" in initial_value:
        value = initial_value.split("TR")[0]
        multiplier = 1000000000000
    value = float(value)

    return round(value*multiplier, 2)
    

if __name__ == "__main__":
    dataframe = reorganiza("dados/gdp_pcap.csv", "GDP per capita", 1990, 2010)
    print(dataframe)