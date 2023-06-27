# Importações necessárias:
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd

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