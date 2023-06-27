#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *

def graf_barras_pib(datapath):
    '''
    Essa função tem como objetivo produzir um gráfico de barras com a média do PIB de cada
    país do G20 e da UE durante o período de 20 anos (1990-2010) de forma ordenada.
    '''
    
    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "PIB", 1990, 2010) #vai fazer um recorte nos dados
    dataframe["PIB"] = dataframe["PIB"].apply(traduz_milhares)
    dataframe = filtro_paises_do_g20(dataframe, agrupamento="country") #vai filtrar apenas os países do g20
    dataframe = dataframe.sort_values(["PIB"], ascending=False).reset_index(drop=True) #vai ordenar o dataframe do menor para o maior

    dataframe["PIB"] = dataframe["PIB"]/1000000000
    
    dicionario_de_cores = DICT_CORES
    lista_de_cores = []
    lista_de_preenchimento = []

    for cada_pais in dataframe["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
            lista_de_preenchimento.append(ALPHA_DESTAQUES)
        else:
            lista_de_cores.append(CORES_COMUNS)
            lista_de_preenchimento.append(ALPHA_COMUNS)

    dataframe["color"] = lista_de_cores
    dataframe["preenchimento"] = lista_de_preenchimento
    print(dataframe)

    source = ColumnDataSource(dataframe) #vai transformar em CDS

    #CONFECÇÃO DO GRÁFICO

    #configuração do nome do arquivo
    output_file("ranking_pib.html")

    #criação do objeto figure
    bar_plot = figure(title="Média dos PIB's do G20 (1990-2010) ", width = LARGURA, height = ALTURA, 
                      x_range=dataframe['country'], y_range=(0, 15000))
    
    bar_plot.background_fill_color = (241, 242, 244, 0.5)
    
    #adição da ferramenta hover
    hover = HoverTool(tooltips=[('País', '@country'), ('PIB (Bilhões de Dólares)', '@PIB{$0,00}')])
    bar_plot.add_tools(hover)
    
    #criação do gráfico de barras em si
    bar_plot.vbar(x='country', top='PIB', color='color', source=source, width=0.8, alpha="preenchimento")
    
    #CONFIGURAÇÕES ESTÉTICAS DOS EIXOS
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

    #CONFIGURAÇÃO DO TÍTULO
    bar_plot.title.text_font = FONTE_TEXTO
    bar_plot.title.text_font_size =TAMANHO_TITULO
    bar_plot.title.align = "center"
    bar_plot.title.text_baseline = "middle"

    show(bar_plot)
    
graf_barras_pib("dados\\gdp_total.csv")
