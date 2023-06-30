from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
import pandas as pd
from bokeh.palettes import Blues
from bokeh.models import LinearColorMapper, ColorBar, Range1d
from bokeh.models import HoverTool
from converte_iso import converte_iso2, converte_iso3
from variaveis_globais import *

def cria_mapa(dataframe, main_column_name: str, palette = Blues[6]):
    '''
    Recebe um dataframe com uma coluna "country", o nome de uma coluna com valores e uma paleta de cores.
    Retorna um objeto figure do bokeh que contém um gráfico com os países contidos destacados e os valores neles.
    '''
    # Adicionando uma coluna iso3 no DataFrame:
    coluna_iso2 = dataframe["country"].apply(converte_iso2)
    coluna_iso3 = coluna_iso2.apply(converte_iso3)
    dataframe["iso_a3"] = coluna_iso3

    # Carregando os dados dos países usando geopandas:
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Criando Data Frame para colorir os países selecionados:
    world1 = pd.merge(
        left = world,
        right = dataframe, 
        on='iso_a3'
    )

    # Criando os objetos GeoJSONDataSource:
    dados_geograficos = GeoJSONDataSource(geojson=world.to_json())
    dados_geograficos_selecionados = GeoJSONDataSource(geojson=world1.to_json())

    # Fazendo cortes lineares na escala para para aplicar paleta:
    color_mapper = LinearColorMapper(
    palette = palette, 
    low = dataframe[main_column_name].min(), 
    high = dataframe[main_column_name].max(), 
    nan_color = '#d9d9d9')
    
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
    plot = figure(title="Índice de Gini do G20", 
                  width = LARGURA, 
                    height = ALTURA, 
                    x_range = Range1d(-180, 180, bounds="auto"), 
                    y_range = Range1d(-90, 90, bounds="auto"),
                    tools="pan,reset,wheel_zoom,box_zoom")
    
    plot.patches('xs', 'ys', 
                 fill_alpha=0.7, 
                 line_color='black', 
                 line_width=1, 
                 source=dados_geograficos, fill_color = "grey")
    
    paises_g20 = plot.patches('xs', 'ys', 
                              source=dados_geograficos_selecionados, 
                              fill_color = {'field': main_column_name, 'transform': color_mapper}, 
                              line_color = 'grey', line_width = 0.25, fill_alpha = 1)
    
    # Adicionando barra com grade de cor: 
    plot.add_layout(color_bar, 'below')

    plot.toolbar.logo = None 
    plot.toolbar.autohide = True 
    plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    # Adicionando hover:
    hover = HoverTool(
        tooltips = [('País','@name'),
                    (main_column_name,f'@{main_column_name}')],
        renderers = [paises_g20]
        )
    plot.add_tools(hover)

    # Configurações estéticas:
    plot.xaxis[0].ticker.desired_num_ticks = 20
    plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    plot.title.text_font = FONTE_TEXTO
    plot.title.text_font_size =TAMANHO_TITULO
    plot.title.align = ALINHAMENTO_TITULO
    plot.title.text_baseline = BASELINE_TITULO
    return plot