# Importações necessárias:
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
import pandas as pd
from bokeh.palettes import Reds
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.models import HoverTool
from converte_iso import converte_iso2, converte_iso3
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20

FIRST_YEAR = 1990
LAST_YEAR = 2010

# Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
df_gini = reorganiza("dados/gini_2100.csv", "gini", FIRST_YEAR, LAST_YEAR)

# Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
df_gini_g20 = filtro_paises_do_g20(df_gini, False, agrupamento="country")
df_gini_g20 = df_gini_g20.sort_values("gini", ascending=False)

# Criando um novo DataFrame com a média de gini para cada país:
df_gini_g20_media = df_gini_g20.groupby('country')['gini'].mean().to_frame().reset_index()

# Adicionando uma coluna iso3 no DataFrame:
coluna_iso2 = df_gini_g20_media["country"].apply(converte_iso2)
coluna_iso3 = coluna_iso2.apply(converte_iso3)
df_gini_g20_media["iso_a3"] = coluna_iso3

# Carregando os dados dos países usando geopandas:
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Criando Data Frame para colorir os países do g20:
world = pd.merge(
    left = world,
    right = df_gini_g20_media.filter(items=['gini','iso_a3']), 
    on='iso_a3'
)

# Criando os objetos GeoJSONDataSource:
dados_geograficos = GeoJSONDataSource(geojson=world.to_json())
dados_geograficos_g20 = GeoJSONDataSource(geojson=world.to_json())

# Definindo paleta de cores:
palette = Reds[6]
palette = palette[::-1]

# Fazendo cortes lineares na escala para para aplicar paleta:
color_mapper = LinearColorMapper(
    palette = palette, 
    low = df_gini_g20_media['gini'].min(), 
    high = df_gini_g20_media['gini'].max(), 
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
plot = figure(title="Mapa Mundial", width = 1080, height = 720)
plot.patches('xs', 'ys', fill_alpha=0.7, line_color='black', line_width=1,
                 source=dados_geograficos, fill_color = "grey")
paises_g20 = plot.patches('xs', 'ys', source=dados_geograficos_g20, 
                 fill_color = {'field' :'gini', 'transform':color_mapper}, 
                 line_color = 'grey', line_width = 0.25, fill_alpha = 1)

# Adicionando hover:
hover = HoverTool(
    tooltips = [('País','@name'),
                ('gini','@gini')],
    renderers = [paises_g20]
    )
plot.add_tools(hover)

# GUI
curdoc().add_root(plot)