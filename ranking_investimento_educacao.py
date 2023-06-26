from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import random

# É adicionado uma lista com países e valores aleatórios relacionados a cada um.
paises = ["Argentina", "Alemanha", "China", "Brasil", "EUA", "Japão", "Rússia"]
valores = random.sample(range(0, 100), len(paises))

# É adicionado o objeto base do gráfico
investimento_educacao = figure(x_range=paises, height=350, title="Investimento em Educação por Países", toolbar_location=None, tools="")

# É adicionado o gráfico de barras 
investimento_educacao.vbar(x=paises, top=valores, width=0.9)

show(investimento_educacao)
