from bokeh.plotting import figure, column, row
from bokeh.models import Slider, ColumnDataSource, Button, HoverTool, NumeralTickFormatter, FixedTicker
from reorganizador import *
from traducao_g20 import filtro_paises_do_g20
from bokeh.io import curdoc
import pandas as pd
from variaveis_globais import *

# Dataframe a ser usado
dataframe = pd.read_csv("dados/total_gdp_ppp_inflation_adjusted.csv")
for year in range(1800, 2014):
    dataframe[str(year)] = dataframe[str(year)].apply(traduz_milhares)
print(dataframe)
dataframe = filtro_paises_do_g20(dataframe, True, "country")

# Dados
year = 1990
sorted_dataframe = dataframe.sort_values(by=[f"{year}"])
raw_data = {"country": list(sorted_dataframe["country"]), 
            "GDP": list(sorted_dataframe[f"{year}"]/1000000000)}
data_source = ColumnDataSource(raw_data)

# O gráfico
plot = figure(width=700, height=500, title="PIB dos países do G20 (em bilhões)", y_range=sorted_dataframe["country"], tools = "")
bars = plot.hbar(y = "country", right = "GDP", height = 0.9, source = data_source)

# Atualização do gráfico
def update_chart():
    global year
    year += 1
    if year > 2010:
        year = 1990
    slider.value = year

# O botão
button = Button(label = "Play", align = "center")

callback = None
def button_action():
    '''
    Função que é executada quando o botão é apertado. Inicia ou para as atualizações periódicas na tabela
    '''
    global callback
    if button.label == "Play":
        callback = curdoc().add_periodic_callback(update_chart, 100)
        button.label = "Pause"
    elif button.label == "Pause":
        curdoc().remove_periodic_callback(callback)
        button.label = "Play"

button.on_click(button_action)

# O Slider
slider = Slider(start = 1990, end = 2010, value = 1990, step=1, title="Year", width = 800, align = "center")

def slider_action(attr, old, new):
    '''
    Função que é executada ao mover o slider. Muda o ano para aquele do slider.
    '''
    global year
    year = slider.value
    sorted_dataframe = dataframe.sort_values(by=[f"{year}"])
    raw_data = {"country": list(sorted_dataframe["country"]), 
                "GDP": list(sorted_dataframe[f"{year}"]/1000000000)}
    bars.data_source.data = raw_data

slider.on_change("value", slider_action)

# Alterações estéticas
plot.xaxis.formatter = NumeralTickFormatter(format="$0,0")
plot.title.text_font = FONTE_TEXTO
plot.title.text_font_size = TAMANHO_TITULO
plot.background_fill_color = BACKGROUND_FILL

plot.xaxis.axis_label_text_font = FONTE_TEXTO
plot.yaxis.axis_label_text_font = FONTE_TEXTO

plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

plot.title.text_font = FONTE_TEXTO
plot.title.text_font_size =TAMANHO_TITULO
plot.title.align = ALINHAMENTO_TITULO
plot.title.text_baseline = BASELINE_TITULO

plot.toolbar.logo = None 
plot.toolbar.autohide = True 

# A GUI
curdoc().add_root(column(button, slider, plot))