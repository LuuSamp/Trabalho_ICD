from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
import media_escolaridade
import pandas as pd

df_homens = reorganiza(datapath = "dados/anos_homens_na_escola.csv", column_name = "Média de anos na Escola por Homens", first_year = 1970, last_year = 2015, csv = False)
df_mulheres = reorganiza(datapath = "dados/anos_mulheres_na_escola.csv", column_name = "Média de anos na Escola por Mulheres", first_year = 1970, last_year = 2015, csv = False)

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
media_anos_escola = figure(title="Média de anos na escola", width=1240, height=600, x_range=(1970,2015))

#dicionário de países de destaque e suas cores
paises_destacaveis = {"Brazil":"blue","Argentina":"royalblue","France":"skyblue","Germany":"coral","Canada":"red","Japan":"indianred"}

#criação das várias linhas e suas respectivas formatações
for country in df_anos_escola["country"].unique():
    country_data = df_anos_escola[df_anos_escola["country"]==country]

#PAÍS DESTACADOS
    if country in paises_destacaveis.keys():
        media_anos_escola.line(x="year", y="Média de anos na Escola", source=country_data, color=paises_destacaveis[country], line_width=3, line_alpha=0.8)
        
#OUTROS PAÍSES
    else:
        media_anos_escola.line(x="year", y="Média de anos na Escola", source=country_data, color="gray", line_width=2, line_alpha=0.25)

# O título é colocado no centro
media_anos_escola.title.align = "center"

# Adicionei a ferramenta HoverTool
hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('Média de anos na Escola', '@{Média de anos na Escola}{0,0.00}')])
media_anos_escola.add_tools(hover)

# É adicionado nome nos eixos
media_anos_escola.xaxis.axis_label = "Anos"
media_anos_escola.yaxis.axis_label = "Média de anos na escola"

# Alterando tamanho dos eixos e do título
media_anos_escola.xaxis.axis_label_text_font_size = "14pt"
media_anos_escola.yaxis.axis_label_text_font_size = "14pt"
media_anos_escola.title.text_font_size = "18pt"

show(media_anos_escola)