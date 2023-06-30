from bokeh.palettes import Reds
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from criador_de_mapas import cria_mapa
from bokeh.models import Div

def grafico_mapa_Gini(datapath_Gini):

    '''
    Essa função deve receber um DataFrame com os coeficiente de Gini dos países
    do mundo inteiro. Ela tem o objetivo de criar um mapa mundial e destacar os
    países do G20 de acordo com os seus níveis de Gini.
    '''

    FIRST_YEAR = 1990
    LAST_YEAR = 2010

    # Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
    df_gini = reorganiza(datapath_Gini, FIRST_YEAR, LAST_YEAR)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_gini_g20 = filtro_paises_do_g20(df_gini, False, agrupamento="country")
    df_gini_g20 = df_gini_g20.sort_values("gini", ascending=False)

    # Criando um novo DataFrame com a média de gini para cada país:
    df_gini_g20_media = df_gini_g20.groupby('country')['gini'].mean().to_frame().reset_index()

    palette = Reds[6]
    palette = palette[::-1]

    plot = cria_mapa(df_gini_g20_media, "gini", palette)

    descricao = Div(text="""
                                    Este gráfico do Mapa Mundial tem o objetivo de destacar os países do G20 em relação aos<br> 
                                    seus níveis de Coeficiente de Gini, que mede o nível de desigualdade econômica do país.<br> 
                                    Utilizando uma paleta de cores com tons de vermelho, os países são categorizados em diferentes<br> 
                                    gradientes, revelando os países com Gini mais baixos em tons mais claros e os países com<br> 
                                    Gini mais altos em tons mais escuros. Observando o mapa, podemos notar que a Austrália detentora<br> 
                                    do maior IDH, tem um índice de Gini bem baixo, ou seja, ela possui um baixo nível de desigualdade.<br> 
                                    Já os EUA que contém o segundo maior IDH, possui um Gini maior, o que o torna um país com um nível<br> 
                                    alto de desigualdade. Por outro lado, a Índia que tem o pior IDH possui um índice de Gini mais baixo<br> 
                                    que o da Austrália tornando-a um país com menos desiguladade, o que não quer dizer algo positivo, já<br> 
                                    que a grande maioria da sociedade indiana está na pobreza. Enquanto isso, a China que possui o segundo<br> 
                                    menor IDH, possui um dos maiores níveis de Gini, rivalizando na questão de desigualdade social com Brasil.<br>  
                                    """)

    return plot, descricao