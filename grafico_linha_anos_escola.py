from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
import media_escolaridade
import pandas as pd

df_homens = reorganiza(datapath = "dados/anos_homens_na_escola.csv", column_name = "Média de anos na Escola por Homens", first_year = 1990, last_year = 2010, csv = False)
df_mulheres = reorganiza(datapath = "dados/anos_mulheres_na_escola.csv", column_name = "Média de anos na Escola por Mulheres", first_year = 1990, last_year = 2010, csv = False)

df_homens = filtro_paises_do_g20(df_homens, "Média de anos na Escola por Homens").reset_index()
df_mulheres = filtro_paises_do_g20(df_mulheres, "Média de anos na Escola por Mulheres").reset_index()

df_anos_escola = pd.DataFrame()
df_anos_escola["country"] = df_homens["country"]
df_anos_escola["year"] = df_mulheres["year"]
df_anos_escola["Média de anos na Escola por Homens"] = df_homens["Média de anos na Escola por Homens"]
df_anos_escola["Média de anos na Escola por Mulheres"] = df_mulheres["Média de anos na Escola por Mulheres"]
df_anos_escola["Média de anos na Escola"] = (df_anos_escola["Média de anos na Escola por Mulheres"] + df_anos_escola["Média de anos na Escola por Homens"]) / 2

# É criado um ColumnDataSource.
source = ColumnDataSource(df_anos_escola)

# Objeto base do gráfico.
media_anos_escola = figure(title="Média de anos na escola", width=1240, height=600)