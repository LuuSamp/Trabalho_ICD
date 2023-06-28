
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
import pandas as pd
from bokeh.palettes import Blues
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.models import HoverTool
from converte_iso import converte_iso2, converte_iso3

def cria_mapa(dataframe, main_column_name: str, palette = Blues[6]):
    '''
    Recebe um dataframe com uma coluna "country", o nome de uma coluna com valores e uma paleta de cores.
    Retorna um objeto figure do bokeh que contém um gráfico com os países contidos destacados e os valores neles
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

    # Configurando a figura e adicionando o gráfico:
    plot = figure(title="Mapa Mundial", width = 1080, height = 720)
    plot.patches('xs', 'ys', fill_alpha=0.7, line_color='black', line_width=1,
                    source=dados_geograficos, fill_color = "grey")
    paises_g20 = plot.patches('xs', 'ys', source=dados_geograficos_selecionados, 
                    fill_color = {'field': main_column_name, 'transform': color_mapper}, 
                    line_color = 'grey', line_width = 0.25, fill_alpha = 1)

    # Adicionando hover:
    hover = HoverTool(
        tooltips = [('País','@name'),
                    (main_column_name,f'@{main_column_name}')],
        renderers = [paises_g20]
        )
    plot.add_tools(hover)
    return plot