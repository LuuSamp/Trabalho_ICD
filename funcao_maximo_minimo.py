import pandas as pd

def funcao_maximo_minimo(dataframe, nome_coluna, nome_coluna_pais):
    '''
    Essa função irá receber um DataFrame juntamente com a sua coluna que deve ser 
    analisada. A função tem o objetivo de analisar os dois maiores valores dessa 
    coluna e os dois menores valores dessa coluna. Ela vai associar os valores aos 
    nomes dos países que cada um representa e especificar uma cor para cada país.
    '''
    maiores_valores = dataframe[nome_coluna].nlargest(2)
    maiores_paises = dataframe[nome_coluna_pais].iloc[maiores_valores.index].tolist()

    menores_valores = dataframe[nome_coluna].nsmallest(2)
    menores_paises = dataframe[nome_coluna_pais].iloc[menores_valores.index].tolist()

    cores = {
        'primeiro_maior': 'darkred',
        'segundo_maior': 'red',
        'primeiro_menor': 'darkblue',
        'segundo_menor': 'lightblue'
    }

    mapeamento = {
        maiores_paises[0]: 'primeiro_maior',
        maiores_paises[1]: 'segundo_maior',
        menores_paises[0]: 'primeiro_menor',
        menores_paises[1]: 'segundo_menor'
    }

    dicionario = {}

    for pais in maiores_paises + menores_paises:
        dicionario[pais] = cores[mapeamento[pais]]

    return dicionario

data = {
    'país': ['Brasil', 'Estados Unidos', 'China', 'Índia', 'Rússia'],
    'valor': [211, 328, 1439, 1393, 144]
}
df = pd.DataFrame(data)

data = funcao_maximo_minimo(df, 'valor', 'país')

print(data)