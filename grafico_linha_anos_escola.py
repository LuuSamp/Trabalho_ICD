from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, Range1d
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
import pandas as pd
from variaveis_globais import *

def linha_escola(datapath1,datapath2):
    # Tratamento da base de dados.
    df_homens = reorganiza(datapath1, column_name = "Média de anos na Escola por Homens", first_year = 1970, last_year = 2015, csv = False)
    df_homens["Média de anos na Escola por Homens"] = df_homens["Média de anos na Escola por Homens"].apply(traduz_milhares).astype(float)
    df_mulheres = reorganiza(datapath2, column_name = "Média de anos na Escola por Mulheres", first_year = 1970, last_year = 2015, csv = False)
    df_mulheres["Média de anos na Escola por Mulheres"] = df_mulheres["Média de anos na Escola por Mulheres"].apply(traduz_milhares).astype(float)
    df_homens = filtro_paises_do_g20(df_homens, agrupamento="year")
    df_mulheres = filtro_paises_do_g20(df_mulheres, agrupamento="year")

    df_anos_escola = pd.DataFrame()
    df_anos_escola["country"] = df_homens["country"]
    df_anos_escola["year"] = df_mulheres["year"]
    df_anos_escola["Média de anos na Escola por Homens"] = df_homens["Média de anos na Escola por Homens"]
    df_anos_escola["Média de anos na Escola por Mulheres"] = df_mulheres["Média de anos na Escola por Mulheres"]
    df_anos_escola["Média de anos na Escola"] = (df_anos_escola["Média de anos na Escola por Mulheres"] + df_anos_escola["Média de anos na Escola por Homens"]) / 2

    # Criação de ColumnDataSource.
    data_source = ColumnDataSource(df_anos_escola)

    # Objeto base do gráfico.
    grafico_linha_escola = figure(title="Média de anos na escola", 
                                width=LARGURA, 
                                height=ALTURA, 
                                x_range=Range1d(1970, 2015, bounds="auto"), 
                                y_range=Range1d(0, 16, bounds="auto"), 
                                tools="pan,box_zoom,wheel_zoom,reset")

    # Adionando colunas referentes a transparência e cor dos países.
    for country in df_anos_escola["country"].unique():
        country_data = df_anos_escola[df_anos_escola["country"]==country]

    # Países em destaque.
        if country in DICT_CORES.keys():
            grafico_linha_escola.line(x="year", 
                                      y="Média de anos na Escola", 
                                      source=country_data, color=DICT_CORES[country], 
                                      line_width=ESPESSURA_DESTAQUES, 
                                      line_alpha=ALPHA_DESTAQUES,
                                      legend_label = country)
            
    # Países sem destaque.
        else:
            grafico_linha_escola.line(x="year", 
                                      y="Média de anos na Escola", 
                                      source=country_data, color="gray", 
                                      line_width=ESPESSURA_COMUNS, 
                                      line_alpha=ALPHA_COMUNS,
                                      legend_label = "Other Countries")

    # Implementação de ferramenta HoverTool.
    hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('Média de tempo na Escola', '@{Média de anos na Escola}{0,0.00} anos')])
    grafico_linha_escola.add_tools(hover)

    # Aplicação de elementos estéticos.
    grafico_linha_escola.background_fill_color = BACKGROUND_FILL

    grafico_linha_escola.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
    grafico_linha_escola.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
    grafico_linha_escola.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    grafico_linha_escola.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    grafico_linha_escola.xaxis.axis_label = "Anos" 
    grafico_linha_escola.yaxis.axis_label = "Média de anos na escola" 

    grafico_linha_escola.xaxis.axis_label_text_font = FONTE_TEXTO
    grafico_linha_escola.yaxis.axis_label_text_font = FONTE_TEXTO

    grafico_linha_escola.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    grafico_linha_escola.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    grafico_linha_escola.xgrid.grid_line_color = LINHAS_GRADE
    grafico_linha_escola.ygrid.grid_line_color = LINHAS_GRADE


    grafico_linha_escola.title.text_font = FONTE_TEXTO
    grafico_linha_escola.title.text_font_size =TAMANHO_TITULO
    grafico_linha_escola.title.align = ALINHAMENTO_TITULO
    grafico_linha_escola.title.text_baseline = BASELINE_TITULO

    grafico_linha_escola.toolbar.logo = None 
    grafico_linha_escola.toolbar.autohide = True 
    grafico_linha_escola.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    show(grafico_linha_escola)
    output_file("../desenvolvimento_educacional.html")

linha_escola("dados/anos_homens_na_escola.csv", "dados/anos_mulheres_na_escola.csv")

