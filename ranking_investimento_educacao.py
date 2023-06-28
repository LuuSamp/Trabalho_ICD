from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import random
import pandas as pd
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza
from variaveis_globais import *

#dataframe = pd.read_csv("dados/investimento_educacao.csv")
#dataframe = filtro_paises_do_g20(dataframe, True, "country")
#print(dataframe)
#dataframe.iloc[:,1:] = dataframe.iloc[:,1:].interpolate(method = "linear", axis = 1, limit_direction="both")
#print(dataframe)


df_escola = reorganiza(datapath = "dados/anos_homens_na_escola.csv", column_name = "Média de anos na Escola", first_year = 1970, last_year = 2015, csv = False)
df_escola = filtro_paises_do_g20(df_escola, "Média de anos na Escola").reset_index()

df_anos_escola = pd.DataFrame()
df_anos_escola["country"] = df_escola["country"]
df_anos_escola["year"] = df_escola["year"]
df_anos_escola["Média de anos na Escola"] = df_escola["Média de anos na Escola"]

# É criada uma lista com as colunas que iremos fazer a média.
colunas_trabalhadas = ["Média de anos na Escola"]

# É criada uma tabela contendo a média dos anos
df_media_por_anos = df_anos_escola.groupby("country")[colunas_trabalhadas].mean().reset_index()

# É reordenado o DataFrame de acordo com os valores
df_ordenado = df_media_por_anos.sort_values(by='Média de anos na Escola', ascending=False)

#CONFIGURANDO A COLUNA DE CORES E PREENCHIMENTO
dicionario_de_cores = DICT_CORES
lista_de_cores = []
lista_de_preenchimento = []

for cada_pais in df_ordenado["country"]:
    if cada_pais in dicionario_de_cores.keys():
        lista_de_cores.append(dicionario_de_cores[cada_pais])
        lista_de_preenchimento.append(ALPHA_DESTAQUES)
    else:
        lista_de_cores.append(CORES_COMUNS)
        lista_de_preenchimento.append(ALPHA_COMUNS)

df_ordenado["color"] = lista_de_cores
df_ordenado["preenchimento"] = lista_de_preenchimento

# É adicionado o objeto base do gráfico
investimento_educacao = figure(x_range=df_ordenado["country"], height=650, width=1300, title="Média de anos na Escola", toolbar_location=None, tools="")

# É adicionado o gráfico de barras 
investimento_educacao.vbar(x=df_ordenado["country"], top=df_ordenado["Média de anos na Escola"], width=0.9, color="color", alpha="preenchimento")

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
