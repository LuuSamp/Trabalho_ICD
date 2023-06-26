from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import random

# É adicionado uma lista com países e valores aleatórios relacionados a cada um.
paises = [
    'Argentina',
    'Australia',
    'Austria',
    'Belgium',
    'Brazil',
    'Bulgaria',
    'Canada',
    'China',
    'Croatia',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Estonia',
    'Finland',
    'France',
    'Germany',
    'Greece',
    'Hungary',
    'India',
    'Indonesia',
    'Ireland',
    'Italy',
    'Japan',
    'Latvia',
    'Lithuania',
    'Luxembourg',
    'Malta',
    'Mexico',
    'Netherlands',
    'Poland',
    'Portugal',
    'Romania',
    'Russia',
    'Saudi Arabia',
    'Slovakia',
    'Slovenia',
    'South Africa',
    'South Korea',
    'Spain',
    'Sweden',
    'Turkey',
    'United Kingdom',
    'United States'
]
valores = random.sample(range(0, 100), len(paises))

# É adicionado o objeto base do gráfico
investimento_educacao = figure(x_range=paises, height=650, width=1300, title="Investimento em Educação por Países", toolbar_location=None, tools="")

# É adicionado o gráfico de barras 
investimento_educacao.vbar(x=paises, top=valores, width=0.9)

# É alterado o background do gráfico
investimento_educacao.xgrid.grid_line_color = None

# É rotacionado os rótulos do eixo x
investimento_educacao.xaxis.major_label_orientation = 45

show(investimento_educacao)
