from bokeh.plotting import figure, column, row
from bokeh.models import Slider, ColumnDataSource, Button, NumeralTickFormatter, FixedTicker
from reorganizador import *
from traducao_g20 import filtro_paises_do_g20
from bokeh.io import show
import pandas as pd
from variaveis_globais import *
from cores import lista_alpha
from descricoes_dos_graficos import DESCRICAO_PROPORCAO_HOMENS_MULHERES

def educacao_por_genero_media(datapath_homens, datapath_mulheres):
    '''
    Gera um gráfico que analisa a média dos valores dos datapaths entre os anos de 1970 e 2015.
    Retorna o objeto figure.
    '''
    # Dataframe a ser usado
    dataframe_homens = reorganiza(datapath=datapath_homens, column_name="Anos_Escolares", first_year=1970, last_year=2015, )
    dataframe_mulheres = reorganiza(datapath=datapath_mulheres, column_name="Anos_Escolares", first_year=1970, last_year=2015, )
    dataframe_homens = filtro_paises_do_g20(dataframe_homens)
    dataframe_mulheres = filtro_paises_do_g20(dataframe_mulheres)
    dataframe_total = dataframe_homens.copy()
    dataframe_total["Anos_Escolares"] = dataframe_homens["Anos_Escolares"] + dataframe_mulheres["Anos_Escolares"]

    # Dados
    year = 1970

    raw_data = {"country": list(dataframe_total["country"]), 
                "Homens": list(dataframe_homens["Anos_Escolares"].groupby("country").mean()/dataframe_total["Anos_Escolares"].groupby("country").mean()),
                "Mulheres": list(dataframe_mulheres["Anos_Escolares"].groupby("country").mean()/dataframe_total["Anos_Escolares"].groupby("country").mean()),
                "alpha": dataframe_total["country"].groupby("country").apply(lista_alpha)}
    data_source = ColumnDataSource(raw_data)
    sorted_countries = list(pd.DataFrame(raw_data).sort_values(by=["Mulheres"])["country"])

    # O gráfico
    plot = figure(name = "Comparação de anos escolares homens e mulheres",width=900, 
                height=500, 
                title="Proporção nos anos escolares de homens e mulheres (1970-2015)", 
                x_range = (0, 1), 
                y_range=sorted_countries,
                tools = "")

    bars = plot.hbar_stack(["Homens", "Mulheres"], 
                        y = "country", height=0.9, 
                        color = ["Blue", "Red"], 
                        legend_label = ["Homens", "Mulheres"],
                        alpha = "alpha",
                        source = data_source)

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

    plot.legend.location = "right"
    plot.legend.title = ""
    plot.legend.border_line_color = COR_DA_LINHA
    plot.legend.border_line_width = ESPESSURA_DA_LINHA
    plot.legend.border_line_alpha = ALPHA_DA_LINHA

    # A GUI
    return (plot, DESCRICAO_PROPORCAO_HOMENS_MULHERES)

show(educacao_por_genero_media("dados/anos_homens_na_escola.csv", "dados/anos_mulheres_na_escola.csv"))