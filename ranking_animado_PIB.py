from bokeh.plotting import figure, column
from bokeh.models import Slider, ColumnDataSource, Button
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

# Atualização do gráfico
def update_chart():
    global year
    raw_data["GDP"] = list(dataframe[f"{year}"])
    slider.value = year
    data_source.data = raw_data
    bars.data_source.data = raw_data
    year += 1
    if year > 2010:
        year = 1990

# O botão
button = Button(label = "Play")

callback = None
def button_action():
    '''
    Função que é executada quando o botão é apertado. Inicia ou para as atualizações periódicas na tabela
    '''
    global callback
    if button.label == "Play":
        callback = curdoc().add_periodic_callback(update_chart, 1000)
        button.label = "Pause"
    elif button.label == "Pause":
        curdoc().remove_periodic_callback(callback)
        button.label = "Play"

button.on_click(button_action)

# O Slider
slider = Slider(start = 1990, end = 2010, value = 1990, step=1, title="Year")

def slider_action(attr, old, new):
    '''
    Função que é executada ao mover o slider. Muda o ano para aquele do slider.
    '''
    global year
    year = slider.value

slider.on_change("value", slider_action)

# A GUI
curdoc().add_root(column(button, slider, plot))