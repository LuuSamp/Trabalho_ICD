# Importações necessárias:
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from funcao_maximo_minimo import funcao_maximo_minimo
import pandas as pd

# Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
df_IDH = reorganiza("dados\hdi_human_development_index.csv", "IDH", 1990, 2010)

# Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
df_IDH_g20 = filtro_paises_do_g20(df_IDH, agrupamento="country")
df_IDH_g20 = df_IDH_g20.sort_values("IDH", ascending=False)

# Deletando a coluna "year":
del df_IDH_g20["year"]

# Carregando os dados dos países usando geopandas:
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Criando um objeto GeoJSONDataSource:
dados_geograficos = GeoJSONDataSource(geojson=world.to_json())

# Configurando a figura e adicionando o gráfico
mapa_IDH = figure(title="Mapa Mundial")
mapa_IDH.patches('xs', 'ys', fill_alpha=0.7, line_color='black', line_width=0.5, source=dados_geograficos)

# Exibindo o mapa
output_file("mapa_mundial.html")
show(mapa_IDH)

print(df_IDH_g20)