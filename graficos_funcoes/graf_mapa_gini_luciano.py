from bokeh.palettes import Reds
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from criador_de_mapas import cria_mapa
from descricoes_dos_graficos import *

def grafico_mapa_Gini(datapath_Gini):

    '''
    Essa função deve receber um DataFrame com os coeficiente de Gini dos países
    do mundo inteiro. Ela tem o objetivo de criar um mapa mundial e destacar os
    países do G20 de acordo com os seus níveis de Gini.
    '''

    FIRST_YEAR = 1990
    LAST_YEAR = 2010

    # Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
    df_gini = reorganiza(datapath_Gini, "gini", FIRST_YEAR, LAST_YEAR)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_gini_g20 = filtro_paises_do_g20(df_gini, False, agrupamento="country")
    df_gini_g20 = df_gini_g20.sort_values("gini", ascending=False)

    # Criando um novo DataFrame com a média de gini para cada país:
    df_gini_g20_media = df_gini_g20.groupby('country')['gini'].mean().to_frame().reset_index()

    palette = Reds[6]
    palette = palette[::-1]

    plot = cria_mapa(df_gini_g20_media, "gini", palette)

    plot.name = "Coeficiente de Gini"

    descricao = DESCRICAO_MAPA_GINI

    return plot, descricao