from bokeh.plotting import figure 
from bokeh.models import HoverTool, Range1d, Paragraph
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
import pandas as pd
from variaveis_globais import *
from CDS import transformador_CDS

def linha_escola(datapath_homens,datapath2_mulheres):
    # Tratamento da base de dados.
    df_homens = reorganiza(datapath_homens, column_name = "Média de anos na Escola por Homens", first_year = 1970, last_year = 2015, csv = False)
    df_homens["Média de anos na Escola por Homens"] = df_homens["Média de anos na Escola por Homens"].apply(traduz_milhares).astype(float)
    df_mulheres = reorganiza(datapath2_mulheres, column_name = "Média de anos na Escola por Mulheres", first_year = 1970, last_year = 2015, csv = False)
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
    data_source = transformador_CDS(df_anos_escola)

    # Objeto base do gráfico.
    grafico_linha_escola = figure(title="Média de anos na escola", 
                                width=LARGURA, 
                                height=ALTURA, 
                                x_range=Range1d(1970, 2015, bounds="auto"), 
                                y_range=Range1d(0, 16, bounds="auto"), 
                                tools="pan,box_zoom,wheel_zoom,reset",
                                name="Anos Na Escola")

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

    grafico_linha_escola.legend.location = "bottom_right"
    grafico_linha_escola.legend.title = ""
    grafico_linha_escola.legend.border_line_color = COR_DA_LINHA
    grafico_linha_escola.legend.border_line_width = ESPESSURA_DA_LINHA
    grafico_linha_escola.legend.border_line_alpha = ALPHA_DA_LINHA

    grafico_linha_escola.toolbar.logo = None 
    grafico_linha_escola.toolbar.autohide = True 
    grafico_linha_escola.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    descricao = Paragraph(text="""Neste gráfico de Linhas, é relacionada a média de anos de presença na escola ao <br>
                                    longo dos anos, em que cada linha representa um país. A visualização tem o objetivo <br>
                                    de identificar melhorias na frequência dos alunos nas escolas e detectar tendências <br>
                                    futuras com base nos padrões observados. Além disso, foram utilizadas cores para destacar <br>
                                    alguns países, sendo a cor azul para os melhores desempenhos e a cor vermelha para os <br>
                                    piores desempenhos no quesito de IDH (Índice de Desenvolvimento Humano). Por meio do <br>
                                    módulo HoverTool, foi criada uma ferramenta de interatividade que, ao passar o cursor <br>
                                    do mouse sobre cada linha, exibe o país, o ano correspondente e a média de anos na escola <br>
                                    para aquele período. O título foi posicionado no centro para alinhar-se com as informações <br>
                                    do gráfico. Por fim, vários rótulos foram padronizados em todos os gráficos usando o <br>
                                    módulo variaveis_globais, proporcionando uma estética consistente para cada representação.""")

    return grafico_linha_escola, descricao