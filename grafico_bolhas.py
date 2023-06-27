from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file
import pandas as pd
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza, traduz_milhares

# As bases de dados são convertidas a partir da função reorganiza.
df_populacao = reorganiza(datapath = "dados/pop.csv", column_name = "População", first_year = 1990, last_year = 2008, csv = False)
df_imc_homens = reorganiza(datapath = "dados/body_mass_index_bmi_men_kgperm2.csv", column_name = "IMC dos Homens", first_year = 1990, last_year = 2008, csv = False)
df_imc_mulheres = reorganiza(datapath = "dados/body_mass_index_bmi_women_kgperm2.csv", column_name = "IMC das Mulheres", first_year = 1990, last_year = 2008, csv = False)
df_calorias = reorganiza(datapath = "dados/food_supply_kilocalories_per_person_and_day.csv", column_name = "Média de Calorias", first_year = 1990, last_year = 2008, csv = False)

df_populacao = filtro_paises_do_g20(df_populacao).reset_index()
df_imc_homens = filtro_paises_do_g20(df_imc_homens).reset_index()
df_imc_mulheres = filtro_paises_do_g20(df_imc_mulheres).reset_index()
df_calorias = filtro_paises_do_g20(df_calorias).reset_index()

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
df_media_por_anos["População em Proporção"] = df_media_por_anos["População"]/20000000

# É criado um ColumnDataSource.
source = ColumnDataSource(df_media_por_anos)

# Objeto base do gráfico.
imc_caloraias = figure(width=400, height=400)

# Plotar o scatter plot.
imc_caloraias.scatter(x="IMC Médio", y="Média de Calorias", size="População em Proporção", source=source)

# Desativando as linhas de grade vertical e horizontal
imc_caloraias.xgrid.grid_line_color = None
imc_caloraias.ygrid.grid_line_color = None

# Configurando a ferramenta HoverTool
hover = HoverTool(tooltips=[("IMC Médio", "@{IMC Médio}"), ("Média de Calorias", "@{Média de Calorias}{0,0.00}"), ("População Média", "@{População}{0,0.00}")])
imc_caloraias.add_tools(hover)


show(imc_caloraias)





