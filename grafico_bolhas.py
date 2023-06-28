from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, Range1d
from bokeh.io import output_file
import pandas as pd
import numpy as np
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza, traduz_milhares
from variaveis_globais import *

# Reorganizando o DataFrame.
df_populacao = reorganiza(datapath = "dados/pop.csv", column_name = "População", first_year = 1990, last_year = 2008, csv = False)
df_imc_homens = reorganiza(datapath = "dados/body_mass_index_bmi_men_kgperm2.csv", column_name = "IMC dos Homens", first_year = 1990, last_year = 2008, csv = False)
df_imc_mulheres = reorganiza(datapath = "dados/body_mass_index_bmi_women_kgperm2.csv", column_name = "IMC das Mulheres", first_year = 1990, last_year = 2008, csv = False)
df_calorias = reorganiza(datapath = "dados/food_supply_kilocalories_per_person_and_day.csv", column_name = "Média de Calorias", first_year = 1990, last_year = 2008, csv = False)

df_populacao = filtro_paises_do_g20(df_populacao, False)
df_populacao["População"] = df_populacao["População"].apply(traduz_milhares).astype(float)

df_populacao = filtro_paises_do_g20(df_populacao, True, agrupamento="country")
df_imc_homens = filtro_paises_do_g20(df_imc_homens, True, agrupamento="country")
df_imc_mulheres = filtro_paises_do_g20(df_imc_mulheres, True, agrupamento="country")
df_calorias = filtro_paises_do_g20(df_calorias, True, agrupamento="country")

# Criação de DataFrame Final.
df_final = pd.DataFrame()
df_final["country"] = df_populacao["country"]
df_final["População"] = df_populacao["População"]
df_final["Média de Calorias"] = df_calorias["Média de Calorias"]
df_final["IMC Médio"] = (df_imc_homens["IMC dos Homens"] + df_imc_mulheres["IMC das Mulheres"]) / 2
df_final["População em Proporção"] = np.sqrt(df_final["População"])/200
print(df_final)



# Criação de ColumnDataSource.
source = ColumnDataSource(df_final)

# Criação de colunas referentes a cores e transparência.
lista_de_cores = []
lista_de_preenchimento = []

for cada_pais in df_final["country"]:
    if cada_pais in DICT_CORES.keys():
        lista_de_cores.append(DICT_CORES[cada_pais])
        lista_de_preenchimento.append(ALPHA_DESTAQUES)
    else:
        lista_de_cores.append(CORES_COMUNS)
        lista_de_preenchimento.append(ALPHA_COMUNS)
df_final["color"] = lista_de_cores
df_final["preenchimento"] = lista_de_preenchimento

sem_destaques = ColumnDataSource(df_final[df_final["color"]=="gray"]) 
paises_com_destaque = ColumnDataSource(df_final[df_final["color"] != "gray"])
    
# Objeto base do gráfico.
imc_calorias = figure(title="Média de calorias consumidas por IMC no G20", 
                      width=LARGURA, 
                      height=ALTURA, 
                      x_range=Range1d(2150,3800,bounds="auto"), 
                      y_range=Range1d(19,29,bounds="auto"), 
                      tools="pan,box_zoom,wheel_zoom,reset")

# Gráfico de Bolhas.
imc_calorias.circle(x="Média de Calorias", 
                    y="IMC Médio", 
                    size="População em Proporção", 
                    source=sem_destaques, 
                    color="color", 
                    fill_alpha = "preenchimento", 
                    line_alpha=ALPHA_DA_LINHA, 
                    line_color=COR_DA_LINHA, 
                    line_width=ESPESSURA_DA_LINHA)
imc_calorias.circle(x="Média de Calorias", 
                    y="IMC Médio", 
                    size="População em Proporção", 
                    source=paises_com_destaque, 
                    color="color", 
                    fill_alpha = "preenchimento", 
                    line_alpha=ALPHA_DA_LINHA, 
                    line_color=COR_DA_LINHA, 
                    line_width=ESPESSURA_DA_LINHA)

# Configurando a ferramenta HoverTool.
hover = HoverTool(tooltips=[("País", "@{country}"), ("IMC Médio", "@{IMC Médio}"), 
                            ("Média de Calorias", "@{Média de Calorias}{0,0.00} kcal"), 
                            ("População Média", "@{População}{0,0.00}")])
imc_calorias.add_tools(hover)

# Configuração de ferramentas estéticas.
imc_calorias.background_fill_color = BACKGROUND_FILL

imc_calorias.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
imc_calorias.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
imc_calorias.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
imc_calorias.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

imc_calorias.xaxis.axis_label = "Média de Calorias" 
imc_calorias.yaxis.axis_label = "IMC Médio" 

imc_calorias.xaxis.axis_label_text_font = FONTE_TEXTO
imc_calorias.yaxis.axis_label_text_font = FONTE_TEXTO

imc_calorias.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
imc_calorias.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

imc_calorias.xgrid.grid_line_color = LINHAS_GRADE
imc_calorias.ygrid.grid_line_color = LINHAS_GRADE

imc_calorias.title.text_font = FONTE_TEXTO
imc_calorias.title.text_font_size =TAMANHO_TITULO
imc_calorias.title.align = ALINHAMENTO_TITULO
imc_calorias.title.text_baseline = BASELINE_TITULO

imc_calorias.toolbar.logo = None 
imc_calorias.toolbar.autohide = True 
imc_calorias.toolbar_location = POSICAO_BARRA_FERRAMENTAS

show(imc_calorias)