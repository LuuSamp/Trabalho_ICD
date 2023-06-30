# Importações necessárias:
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from converte_iso import *
from descricoes_dos_graficos import *
from criador_de_mapas import cria_mapa

def grafico_mapa_IDH(datapath_IDH):

    '''
    Essa função deve receber o caminho do DataFrame com os IDHs dos países. Ela tem o objetivo de criar 
    um mapa mundial que destaca os países do G20 com um gradiente de cor, mostrando através da tonalidade 
    da cor os países que possuem os maiores e os menores Índices de Desenvolvimento Humano.
    '''

    print(f"Carregando {__name__}")

    # Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
    df_IDH = reorganiza(datapath_IDH, "IDH", 1990, 2010)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_IDH_g20 = filtro_paises_do_g20(df_IDH, False, agrupamento="country")
    df_IDH_g20 = df_IDH_g20.sort_values("IDH", ascending=False)

    # Criando um novo DataFrame com a média de IDH para cada país:
    df_IDH_g20_media = df_IDH_g20.groupby('country')['IDH'].mean().to_frame().reset_index()

    # Adicionando uma coluna iso3 no DataFrame:
    coluna_iso2 = df_IDH_g20_media["country"].apply(converte_iso2)
    coluna_iso3 = coluna_iso2.apply(converte_iso3)
    df_IDH_g20_media["iso_a3"] = coluna_iso3

    # Invertendo a paleta de cores:
    palette = palette[::-1]

    # Criando mapa através da função "cria_mapa":
    plot = cria_mapa(df_IDH_g20_media, "gini", palette)

    plot.name = "Coeficiente de Gini"

    descricao = DESCRICAO_MAPA_GINI

    return plot, descricao
