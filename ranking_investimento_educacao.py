from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import random

# É adicionado uma lista com países e valores aleatórios relacionados a cada um.
paises = ["Argentina", "Alemanha", "China", "Brasil", "EUA", "Japão", "Rússia"]
valores = random.sample(range(0, 100), len(paises))
