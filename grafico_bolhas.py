from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file
import pandas as pd
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza, traduz_milhares
from variaveis_globais import *

# As bases de dados são convertidas a partir da função reorganiza.
df_populacao = reorganiza(datapath = "dados/pop.csv", column_name = "População", first_year = 1990, last_year = 2008, csv = False)
df_imc_homens = reorganiza(datapath = "dados/body_mass_index_bmi_men_kgperm2.csv", column_name = "IMC dos Homens", first_year = 1990, last_year = 2008, csv = False)
df_imc_mulheres = reorganiza(datapath = "dados/body_mass_index_bmi_women_kgperm2.csv", column_name = "IMC das Mulheres", first_year = 1990, last_year = 2008, csv = False)
df_calorias = reorganiza(datapath = "dados/food_supply_kilocalories_per_person_and_day.csv", column_name = "Média de Calorias", first_year = 1990, last_year = 2008, csv = False)

df_populacao = filtro_paises_do_g20(df_populacao, "População").reset_index()
df_imc_homens = filtro_paises_do_g20(df_imc_homens, "IMC dos Homens").reset_index()
df_imc_mulheres = filtro_paises_do_g20(df_imc_mulheres, "IMC das Mulheres").reset_index()
df_calorias = filtro_paises_do_g20(df_calorias, "Média de Calorias").reset_index()

# Criando o DataFrame Final
df_final = pd.DataFrame()
df_final["country"] = df_populacao["country"]
df_final["year"] = df_populacao["year"]
df_final["População"] = df_populacao["População"]
df_final["IMC dos Homens"] = df_imc_homens["IMC dos Homens"]
df_final["IMC das Mulheres"] = df_imc_mulheres["IMC das Mulheres"]
df_final["Média de Calorias"] = df_calorias["Média de Calorias"]
df_final["IMC Médio"] = (df_final["IMC dos Homens"] + df_final["IMC das Mulheres"]) / 2

# É criada a conversão dos valores de População para um float.
df_final["População"] = df_final["População"].apply(traduz_milhares)

# É criada uma lista com as colunas que iremos fazer a média.
colunas_trabalhadas = ["População", "IMC Médio", "Média de Calorias"]

# É criada uma tabela contendo a média de população, calorias, IMC de acordo por Países ao longo dos anos.
df_media_por_anos = df_final.groupby("country")[colunas_trabalhadas].mean().reset_index()

# Ajustei a proporção da população para se adequar ao gráfico.
df_media_por_anos["População em Proporção"] = df_media_por_anos["População"]/7000000

# É criado um ColumnDataSource.
source = ColumnDataSource(df_media_por_anos)


# Criando colunas referentes a cores.
lista_de_cores = []
lista_de_preenchimento = []

for cada_pais in df_media_por_anos["country"]:
    if cada_pais in DICT_CORES.keys():
        lista_de_cores.append(DICT_CORES[cada_pais])
        lista_de_preenchimento.append(0.7)
    else:
        lista_de_cores.append("gray")
        lista_de_preenchimento.append(0.15)
df_media_por_anos["color"] = lista_de_cores
df_media_por_anos["preenchimento"] = lista_de_preenchimento

sem_destaques = ColumnDataSource(df_media_por_anos[df_media_por_anos["color"]=="gray"]) 
paises_com_destaque = ColumnDataSource(df_media_por_anos[df_media_por_anos["color"] != "gray"])
    
# Objeto base do gráfico.
imc_calorias = figure(title="Média de calorias consumidas por IMC no G20", width=1240, height=600, x_range=(2200,3800), y_range=(19,28))

# Plotar o scatter plot.
imc_calorias.circle(x="Média de Calorias", y="IMC Médio", size="População em Proporção", source=sem_destaques, color="color", fill_alpha = "preenchimento")
imc_calorias.circle(x="Média de Calorias", y="IMC Médio", size="População em Proporção", source=paises_com_destaque, color="color", fill_alpha = "preenchimento")

# Desativando as linhas de grade vertical e horizontal
imc_calorias.xgrid.grid_line_color = None
imc_calorias.ygrid.grid_line_color = None

# É adicionado nome nos eixos
imc_calorias.xaxis.axis_label = "Média de Calorias"
imc_calorias.yaxis.axis_label = "IMC Médio"

# O título é colocado no centro
imc_calorias.title.align = "center"

# É alterado o tamanho do título
imc_calorias.title.text_font_size = "18pt"

# Tamanho dos valores do eixo x alterado 
imc_calorias.xaxis.major_label_text_font_size = "12pt"

# Tamanho dos valores do eixo y alterado 
imc_calorias.yaxis.major_label_text_font_size = "12pt"

# Alterando tamanho dos eixos
imc_calorias.xaxis.axis_label_text_font_size = "14pt"
imc_calorias.yaxis.axis_label_text_font_size = "14pt"

# Modificando fonte dos eixos e título
imc_calorias.xaxis.axis_label_text_font = FONTE_TEXTO
imc_calorias.yaxis.axis_label_text_font = FONTE_TEXTO
imc_calorias.title.text_font = FONTE_TEXTO

# Alterarando a cor do background
imc_calorias.background_fill_color = "#F8F2FF"

# Configurando a ferramenta HoverTool
hover = HoverTool(tooltips=[("País", "@{country}"), ("IMC Médio", "@{IMC Médio}"), ("Média de Calorias", "@{Média de Calorias}{0,0.00}"), ("População Média", "@{População}{0,0.00}")])
imc_calorias.add_tools(hover)

show(imc_calorias)