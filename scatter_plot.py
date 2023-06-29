# Bibliotecas e módulos necessários:
from reorganizador import reorganiza
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, Range1d, Paragraph
from bokeh.plotting import figure, output_file
from bokeh.models import Title 
from traducao_g20 import filtro_paises_do_g20 
from variaveis_globais import *

def grafico_de_dispersao(datapath_vacinas, datapath_mortes):  
    ''''
    Essa função deve receber dois DataFrames, pois ela tem o objetivo de criar um 
    Scatter Plot (Gráfico de Dispersão) que compara dois assuntos bem importantes 
    na área da saúde, a Vacinação de crianças e a Mortalidade Infantil.
    '''

    # Criação de Data Frames "tratados" a partir da utilização da função "reorganiza": 
    df_vacina = reorganiza(datapath_vacinas, "Porcentagem de Vacinação", 1990, 2010)
    df_mortes = reorganiza(datapath_mortes, "Mortes a cada 1000 nascimentos", 1990, 2010)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_vacina_g20 = filtro_paises_do_g20(df_vacina, False, agrupamento="country")
    df_mortes_g20 = filtro_paises_do_g20(df_mortes, False, agrupamento="country")

    # Criando um DataFrame com todas as colunas necessárias:
    df_final = pd.DataFrame()
    df_final["country"] = df_vacina_g20["country"]
    df_final["Porcentagem de Vacinação"] = df_vacina_g20["Porcentagem de Vacinação"]
    df_final["Mortes a cada 1000 nascimentos"] = df_mortes_g20["Mortes a cada 1000 nascimentos"]

    # Criação de colunas referentes a cores, transparência e legenda:
    lista_de_cores = []
    lista_de_preenchimento = []
    lista_legenda = []

    for cada_pais in df_final["country"]:
        if cada_pais in DICT_CORES.keys():
            lista_de_cores.append(DICT_CORES[cada_pais])
            lista_de_preenchimento.append(ALPHA_DESTAQUES)
            lista_legenda.append(cada_pais)
        else:
            lista_de_cores.append(CORES_COMUNS)
            lista_de_preenchimento.append(ALPHA_COMUNS)
            lista_legenda.append("Other Countries")

    df_final["color"] = lista_de_cores
    df_final["preenchimento"] = lista_de_preenchimento
    df_final["legenda"] = lista_legenda

    # Criação de ColumnDataSource:
    paises_destacados = ColumnDataSource(df_final)

    # Definindo o arquivo de saída para o gráfico:
    output_file("scatter_plot.html")

    # Criando uma variável para o título que o centraliza, aumenta seu tamanho e 
    # muda sua cor:
    titulo = Title(text="Vacinação e Mortalidade Infantil", align="center", text_font_size = "20pt")

    # Criando um objeto figure:
    scatter_plot = figure(title=titulo, 
                        x_axis_label="Porcentagem de crianças vacinadas", 
                        y_axis_label="Mortes a cada 1000 nascimentos", 
                        width=LARGURA, 
                        height=ALTURA, 
                        x_range=Range1d(63,100,bounds="auto"), 
                        y_range=Range1d(0,95,bounds="auto"), 
                        tools="pan,box_zoom,wheel_zoom,reset",
                        name="vacinaXmorte")

    # Criando scatter plot:
    scatter_plot.scatter(x = "Porcentagem de Vacinação",
                        y = "Mortes a cada 1000 nascimentos",
                        source=paises_destacados, 
                        color="color", 
                        fill_alpha = "preenchimento", 
                        line_alpha=ALPHA_DA_LINHA, 
                        line_color=COR_DA_LINHA, 
                        line_width=ESPESSURA_DA_LINHA,
                        legend_field="legenda", 
                        size = 15)

    # Configurando a ferramenta HoverTool:
    hover = HoverTool(tooltips=[("País", "@country"), 
                                ("Porcentagem de Vacinação", "@{Porcentagem de Vacinação}%"),
                                ("Média de mortes/1000 nascimentos", "@{Mortes a cada 1000 nascimentos}")])
    scatter_plot.add_tools(hover)

    # Configuração de ferramentas estéticas:
    scatter_plot.background_fill_color = BACKGROUND_FILL

    scatter_plot.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
    scatter_plot.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
    scatter_plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    scatter_plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    scatter_plot.xaxis.axis_label_text_font = FONTE_TEXTO
    scatter_plot.yaxis.axis_label_text_font = FONTE_TEXTO

    scatter_plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    scatter_plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    scatter_plot.xgrid.grid_line_color = LINHAS_GRADE
    scatter_plot.ygrid.grid_line_color = LINHAS_GRADE

    scatter_plot.title.text_font = FONTE_TEXTO
    scatter_plot.title.text_font_size =TAMANHO_TITULO
    scatter_plot.title.align = ALINHAMENTO_TITULO
    scatter_plot.title.text_baseline = BASELINE_TITULO

    scatter_plot.legend.location = "top_right"
    scatter_plot.legend.title = ""
    scatter_plot.legend.border_line_color = COR_DA_LINHA
    scatter_plot.legend.border_line_width = ESPESSURA_DA_LINHA
    scatter_plot.legend.border_line_alpha = ALPHA_DA_LINHA

    scatter_plot.toolbar.logo = None 
    scatter_plot.toolbar.autohide = True 
    scatter_plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    descricao = Paragraph(text="""
                                    Esse gráfico tem como objetivo comparar os países do G20 com relação a dois assuntos muito importantes na área da<br>
                                    Saúde: a Vacinação de Crianças e a Mortalidade Infantil do período de 1990 à 2010. Além disso, foram destacados<br>
                                    quatro países que tiveram os dois maiores e os dois menores Índices de Desenvolvimento Humano. Os países com cores<br> 
                                    de tons vermelhos são a Índia e a China que representam os países com os menores IDHs, enquanto os países com cores<br> 
                                    de tons azuis são a Austrália e os Estados Unidos que representam os países com os maiores IDHs. Pode-se perceber<br> 
                                    que, em relação ao gráfico, a Índia, que possui um IDH muito baixo também possui uma média de mortes muito elevada,<br> 
                                    o que justifica a sua baixa porcentagem de crianças vacinadas. Por outro lado, a China, que também tem um IDH baixo<br> 
                                    possui uma porcentagem alta de crianças vacinadas e, consequentemente uma baixa média de mortes. Um resultado esperado<br> 
                                    foi observado em relação aos países com IDHs altos, que ao longo dos anos tiveram grande parte das crianças vacinadas<br> 
                                    e, consequentemente, poucas mortes.  
                                    """)

    return scatter_plot, descricao















