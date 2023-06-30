# Importações necessárias:
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
import pandas as pd
from bokeh.palettes import Reds
from bokeh.models import LinearColorMapper, ColorBar, Range1d
from bokeh.models import HoverTool
from variaveis_globais import *
from converte_iso import *
from descricoes_dos_graficos import *

def grafico_mapa_IDH(datapath_IDH):

    '''
    Essa função deve receber um DataFrame dos IDHs dos países. Ela tem o objetivo de criar um mapa 
    mundial que destaca os países do G20 com um gradiente de cor, mostrando através da tonalidade 
    da cor os países que possuem os maiores e os menores Índices de Desenvolvimento Humano.
    '''

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

    # Carregando os dados dos países usando geopandas:
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Criando Data Frame para colorir os países do g20:
    world1 = pd.merge(
        left = world,
        right = df_IDH_g20_media.filter(items=['IDH','iso_a3']), 
        on='iso_a3'
    )

    # Criando os objetos GeoJSONDataSource:
    dados_geograficos = GeoJSONDataSource(geojson=world.to_json())
    dados_geograficos_g20 = GeoJSONDataSource(geojson=world1.to_json())

    # Definindo paleta de cores:
    palette = Reds[6]
    palette = palette[::-1]

    # Fazendo cortes lineares na escala para para aplicar paleta:
    color_mapper = LinearColorMapper(
        palette = palette, 
        low = df_IDH_g20_media['IDH'].min(), 
        high = df_IDH_g20_media['IDH'].max(), 
        nan_color = '#d9d9d9')

    # Ajustando ferramenta para popup com mouse:
    hover = HoverTool(
        tooltips = [ ('País','@name'),
                    ('IDH','@IDH')
        ])

    # Criando barras de cores:
    color_bar = ColorBar(
        color_mapper=color_mapper, 
        label_standoff=6,
        width = 500, 
        height = 20,
        border_line_color=None,
        location = (0,0), 
        orientation = 'horizontal', 
    )

    # Configurando a figura e adicionando o gráfico:
    mapa_IDH = figure(title="IDH do G20", 
                    width = LARGURA, 
                    height = ALTURA, 
                    x_range = Range1d(-180, 180, bounds="auto"), 
                    y_range = Range1d(-90, 90, bounds="auto"),
                    tools="pan,reset,wheel_zoom,box_zoom",
                    name="Índice de Desenvolvimento Humano")

    # Adicionando barra com grade de cor: 
    mapa_IDH.add_layout(color_bar, 'below')

    mapa_IDH.toolbar.logo = None 
    mapa_IDH.toolbar.autohide = True 
    mapa_IDH.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    mapa_IDH.patches('xs', 'ys', 
                    fill_alpha=0.7, 
                    line_color='black', 
                    line_width=1,
                    source=dados_geograficos, 
                    fill_color = "grey")

    paises_g20 = mapa_IDH.patches('xs', 'ys', source=dados_geograficos_g20, 
                    fill_color = {'field' :'IDH', 'transform':color_mapper}, 
                    line_color = 'grey', line_width = 0.25, fill_alpha = 1)

    # Adicionando hover:
    hover.renderers = [paises_g20]
    mapa_IDH.add_tools(hover)

    # Configurações estéticas:
    mapa_IDH.xaxis[0].ticker.desired_num_ticks = 20
    mapa_IDH.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    mapa_IDH.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    mapa_IDH.title.text_font = FONTE_TEXTO
    mapa_IDH.title.text_font_size =TAMANHO_TITULO
    mapa_IDH.title.align = ALINHAMENTO_TITULO
    mapa_IDH.title.text_baseline = BASELINE_TITULO

    descricao = DESCRICAO_MAPA_IDH
    return mapa_IDH, descricao
