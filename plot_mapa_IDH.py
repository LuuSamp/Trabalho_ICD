# Importações necessárias:
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
import pandas as pd

# Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
df_IDH = reorganiza("dados\hdi_human_development_index.csv", "IDH", 1990, 2010)

# Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
df_IDH_g20 = filtro_paises_do_g20(df_IDH, "IDH")

# Carregar os dados usando geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Criar um objeto GeoJSONDataSource
dados_geograficos = GeoJSONDataSource(geojson=world.to_json())

# Configurar a figura e adicionar o gráfico
mapa_IDH = figure(title="Mapa Mundial")
mapa_IDH.patches('xs', 'ys', fill_alpha=0.7, line_color='black', line_width=0.5, source=dados_geograficos)

# Exibir o mapa
output_file("mapa_mundial.html")
show(mapa_IDH)