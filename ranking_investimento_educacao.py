from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import random
import pandas as pd



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

# É criado um DataFrame a partir de um dicionário
dicionario_paises = dict(zip(paises, valores))

# É criado um DataFrame do Pandas com o país e seu respectivo valor
df = pd.DataFrame.from_dict(dicionario_paises, orient='index', columns=['Valor']).reset_index()

# É reordenado o DataFrame de acordo com os valores
df_ordenado = df.sort_values(by='Valor', ascending=False)

# É adicionado o objeto base do gráfico
investimento_educacao = figure(x_range=df_ordenado["index"], height=650, width=1300, title="Investimento em Educação por Países", toolbar_location=None, tools="")

# É adicionado o gráfico de barras 
investimento_educacao.vbar(x=df_ordenado["index"], top=df_ordenado["Valor"], width=0.9, color="#AEB7BF")

# É alterado o background do gráfico
investimento_educacao.xgrid.grid_line_color = None

# É rotacionado os rótulos do eixo x
investimento_educacao.xaxis.major_label_orientation = 45

# É alterado o tamanho do título
investimento_educacao.title.text_font_size = "18pt"

# Título Centralizado
investimento_educacao.title.align = "center"

# Tamanho do nome dos países alterado
investimento_educacao.below[0].major_label_text_font_size = '14px'

# Tamanho dos valores do eixo y alterado 
investimento_educacao.yaxis.major_label_text_font_size = "12pt"


show(investimento_educacao)
