from bokeh.plotting import figure, column, row
from bokeh.models import Slider, ColumnDataSource, Button, HoverTool, NumeralTickFormatter, FixedTicker
from reorganizador import *
from traducao_g20 import filtro_paises_do_g20
from bokeh.io import curdoc
import pandas as pd
from variaveis_globais import *

# Dataframe a ser usado
dataframe_homens = filtro_paises_do_g20(pd.read_csv("dados/anos_homens_na_escola.csv"), True, "country")
dataframe_mulheres = filtro_paises_do_g20(pd.read_csv("dados/anos_mulheres_na_escola.csv"), True, "country")
dataframe_total = dataframe_homens.copy()
print(dataframe_total)
for year in range(1970, 2016):
    dataframe_total[str(year)] = dataframe_homens[str(year)] + dataframe_mulheres[str(year)]
print(dataframe_total)

# Dados
year = 1970
#sorted_dataframe = dataframe.sort_values(by=[f"{year}"])
raw_data = {"country": list(dataframe_total["country"]), 
            "Homens": list(dataframe_homens[f"{year}"]/dataframe_total[f"{year}"]),
            "Mulheres": list(dataframe_mulheres[f"{year}"]/dataframe_total[f"{year}"])}
data_source = ColumnDataSource(raw_data)
sorted_countries = list(pd.DataFrame(raw_data).sort_values(by=["Mulheres"])["country"])

# O gráfico
plot = figure(width=900, 
              height=500, 
              title="Proporção nos anos escolares de homens e mulheres (1970-2015)", 
              x_range = (0, 1), 
              y_range=sorted_countries,
              tools = "")

bars = plot.hbar_stack(["Homens", "Mulheres"], 
                       y = "country", height=0.9, 
                       color = ["Blue", "Red"], 
                       source = data_source)

# Atualização do gráfico
def update_chart():
    global year
    year += 1
    if year > 2015:
        year = 1970
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
slider = Slider(start = 1970, end = 2015, value = 1970, step=1, title="Year", width = 800, align = "center")

def slider_action(attr, old, new):
    '''
    Função que é executada ao mover o slider. Muda o ano para aquele do slider.
    '''
    global year
    year = slider.value
    raw_data = {"country": list(dataframe_total["country"]), 
            "Homens": list(dataframe_homens[f"{year}"]/dataframe_total[f"{year}"]),
            "Mulheres": list(dataframe_mulheres[f"{year}"]/dataframe_total[f"{year}"])}
    bars[0].data_source.data = raw_data

slider.on_change("value", slider_action)

# Linha central
plot.ray(x=.5, y=0, length=1, angle=1.57079633, color='black', line_dash = "dashed", line_width = 2)

# Alterações estéticas
plot.xaxis.formatter = NumeralTickFormatter(format="0 %")
plot.title.text_font = FONTE_TEXTO
plot.title.text_font_size = TAMANHO_TITULO
plot.background_fill_color = BACKGROUND_FILL


plot.xaxis.ticker=FixedTicker(ticks=[tick/100 for tick in range(0, 101, 10)])

plot.xaxis.axis_label_text_font = FONTE_TEXTO
plot.yaxis.axis_label_text_font = FONTE_TEXTO

plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

plot.xgrid.grid_line_color = LINHAS_GRADE
plot.ygrid.grid_line_color = LINHAS_GRADE

plot.title.text_font = FONTE_TEXTO
plot.title.text_font_size =TAMANHO_TITULO
plot.title.align = ALINHAMENTO_TITULO
plot.title.text_baseline = BASELINE_TITULO

plot.toolbar.logo = None 
plot.toolbar.autohide = True 
# plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

# A GUI
curdoc().add_root(column(row(button, slider), plot))