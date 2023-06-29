#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import HoverTool, NumeralTickFormatter, Div, Paragraph
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS

def graf_barras_pib(datapath):
    '''
    Essa função tem como objetivo produzir um gráfico de barras com a média do PIB de cada
    país do G20 e da UE durante o período de 20 anos (1990-2010) de forma ordenada.
    '''

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "PIB", 1990, 2010) 
    dataframe["PIB"] = dataframe["PIB"].apply(traduz_milhares)
    dataframe = filtro_paises_do_g20(dataframe, agrupamento="country")
    dataframe = dataframe.sort_values(["PIB"], ascending=False).reset_index(drop=True)
    dataframe["PIB"] = dataframe["PIB"]/1000000000

    #CONFIGURANDO A COLUNA DE CORES E PREENCHIMENTO
    dicionario_de_cores = DICT_CORES
    lista_de_cores = []
    lista_de_preenchimento = []
    lista_de_legenda = []

    for cada_pais in dataframe["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
            lista_de_preenchimento.append(ALPHA_DESTAQUES)
            lista_de_legenda.append(cada_pais)
        else:
            lista_de_cores.append(CORES_COMUNS)
            lista_de_preenchimento.append(ALPHA_COMUNS)
            lista_de_legenda.append("Other Countries")

    dataframe["color"] = lista_de_cores
    dataframe["preenchimento"] = lista_de_preenchimento
    dataframe["legenda"] = lista_de_legenda

    #TRANSFORMANDO EM CDS
    data_source = transformador_CDS(dataframe)

    #CONFECÇÃO DO GRÁFICO
    bar_plot = figure(title="Média dos PIB's do G20 (1990-2010)", 
                      width = LARGURA, 
                      height = ALTURA, 
                      x_range=dataframe['country'], 
                      y_range=(0, 15000),
                      tools = "",
                      name="PIB Médio")
    
    bar_plot.vbar(x='country', 
                  top='PIB', 
                  color="color", 
                  source=data_source, 
                  width=0.9, 
                  alpha="preenchimento",
                  line_color = COR_DA_LINHA,
                  line_alpha = ALPHA_DA_LINHA,
                  line_width = ESPESSURA_DA_LINHA,
                  legend_field="legenda")
    
    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('PIB (Bilhões de Dólares)', '@PIB{$0,00}')])
    bar_plot.add_tools(hover)
    
    #CONFIGURAÇÕES ESTÉTICAS
    bar_plot.background_fill_color = BACKGROUND_FILL
    
    bar_plot.xaxis.major_label_orientation = 0.7

    bar_plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    bar_plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    bar_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    bar_plot.xaxis.axis_label = "Países" 
    bar_plot.yaxis.axis_label = "Média do PIB (Bilhões de Dólares)" 

    bar_plot.xaxis.axis_label_text_font = FONTE_TEXTO
    bar_plot.yaxis.axis_label_text_font = FONTE_TEXTO

    bar_plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    bar_plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    bar_plot.xgrid.grid_line_color = LINHAS_GRADE
    bar_plot.ygrid.grid_line_color = LINHAS_GRADE

    bar_plot.title.text_font = FONTE_TEXTO
    bar_plot.title.text_font_size =TAMANHO_TITULO
    bar_plot.title.align = ALINHAMENTO_TITULO
    bar_plot.title.text_baseline = BASELINE_TITULO

    bar_plot.toolbar.logo = None 
    bar_plot.toolbar.autohide = True 
    bar_plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    bar_plot.legend.location = "top_right"
    bar_plot.legend.title = ""
    bar_plot.legend.border_line_color = COR_DA_LINHA
    bar_plot.legend.border_line_width = ESPESSURA_DA_LINHA
    bar_plot.legend.border_line_alpha = ALPHA_DA_LINHA

    descricao = Paragraph(text="""Esse gráfico tem como objetivo representar a média do PIB dos integrantes do G20 do período de 1990 à 2010. <br>
                                    Assim como em todos os gráficos, chamamos atenção para os Estados Unidos, Austrália, China e Índia. <br> 
                                    Vemos que na questão econômica, a ordem se inverte e que não traduz a mesma ideia quando olhamos para o IDH. <br>
                                    A China, com um PID muitas vezes maior do que o da Austrália, não consegue transformar isso em melhoras significativas <br>
                                    para o bem estar do cidadão. Vamos ver no gráfico seguinte que isso pode ser explicado. Quantos as cores, elas foram <br>
                                    as mesmas utilizadas em todos os outros gráficos, o azul para representar os países com alto IDH e o vermelho os com <br>
                                    IDH baixo. Destaco, por fim, que utilizamos apenas a ferramenta Hover, uma vez que, no gráfico de barras, <br>
                                    não faz sentido ferramentas como a Pan, Box_Zoom e outras.""")

    return bar_plot, descricao
