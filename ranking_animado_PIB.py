from bokeh.plotting import figure, column
from bokeh.models import Slider, ColumnDataSource
from reorganizador import *
from traducao_g20 import filtro_paises_do_g20
from bokeh.io import curdoc
import pandas as pd

# Dataframe a ser usado
dataframe = filtro_paises_do_g20(pd.read_csv("dados/gdp_total_yearly_growth.csv"))

# Dados
year = 1990
raw_data = {"country": list(dataframe["country"]), "GDP": list(dataframe[f"{year}"])}
data_source = ColumnDataSource(raw_data)

# O gráfico
plot = figure(width=700, height=500, title="Top 10 Countries by Population (1964-2013)", x_range=(0, 20), y_range=dataframe["country"])
bars = plot.hbar(y = "country", right = "GDP", source = data_source)

# O Slider
slider = Slider(start = 1990, end = 2010, value = 1990, step=1, title="Year")

def update_chart():
    global year
    if year > 2010:
        year = 1990
    raw_data["GDP"] = list(dataframe[f"{year}"])
    print(raw_data)
    data_source.data = raw_data
    bars.data_source.data = raw_data
    year += 1
    slider.value = year

curdoc().add_root(column(slider, plot))

callback = curdoc().add_periodic_callback(update_chart, 1000)