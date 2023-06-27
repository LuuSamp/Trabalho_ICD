#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
import math

def graf_barras_pib(datapath):
    '''
    Essa função tem como objetivo produzir um gráfico de barras com a média do PIB de cada
    país do G20 e da UE durante o período de 20 anos (1990-2010) de forma ordenada.
    '''
    
    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "indice_analisado", 1990, 2010) #vai fazer um recorte nos dados
    dataframe = filtro_paises_do_g20(dataframe, "indice_analisado") #vai filtrar apenas os países do g20
    dataframe = dataframe.groupby('country')['indice_analisado'].mean().round(2).reset_index() #vai agrupar por país fazendo a média dos 20 anos
    dataframe = dataframe.sort_values(["indice_analisado"], ascending=False) #vai ordenar o dataframe do menor para o maior

    dataframe["indice_analisado"] = dataframe["indice_analisado"]/1000000000


    dicionario_de_cores = {"Brazil":"blue","Argentina":"royalblue","France":"skyblue","Germany":"coral","Canada":"red","Japan":"indianred"}
    lista_de_cores = []
    lista_de_preenchimento = []

    for cada_pais in dataframe["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
            lista_de_preenchimento.append(0.7)
        else:
            lista_de_cores.append("gray")
            lista_de_preenchimento.append(0.15)

    dataframe["color"] = lista_de_cores
    dataframe["preenchimento"] = lista_de_preenchimento

    source = ColumnDataSource(dataframe) #vai transformar em CDS

    #CONFECÇÃO DO GRÁFICO

    #configuração do nome do arquivo
    output_file("ranking_pib.html")

    #criação do objeto figure
    bar_plot = figure(title="Média dos PIB's do G20 (1990-2010) ", width = 1350, height = 720, 
                      x_range=dataframe['country'], y_range=(0, max(dataframe['indice_analisado']) * 1.1))
    
    #adição da ferramenta hover
    hover = HoverTool(tooltips=[('País', '@country'), ('PIB (Bilhões de Dólares)', '@indice_analisado{$0,00}')])
    bar_plot.add_tools(hover)
    
    #criação do gráfico de barras em si
    bar_plot.vbar(x='country', top='indice_analisado', color='color', source=source, width=0.8, alpha="preenchimento")
    
    #CONFIGURAÇÕES ESTÉTICAS DOS EIXOS
    bar_plot.xaxis.major_label_orientation = 0.7

    bar_plot.yaxis[0].ticker.desired_num_ticks = 10
    bar_plot.yaxis[0].ticker.num_minor_ticks = 0

    bar_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    bar_plot.xaxis.axis_label = "Países" 
    bar_plot.yaxis.axis_label = "Média do PIB (Bilhões de Dólares)" 

    bar_plot.xaxis.axis_label_text_font = "Times"
    bar_plot.yaxis.axis_label_text_font = "Times"

    bar_plot.xaxis.axis_label_text_font_size = "14pt"
    bar_plot.yaxis.axis_label_text_font_size = "14pt"

    bar_plot.xgrid.grid_line_color = None
    bar_plot.ygrid.grid_line_color = None

    #CONFIGURAÇÃO DO TÍTULO
    bar_plot.title.text_font = "Times"
    bar_plot.title.text_font_size = "20pt"
    bar_plot.title.align = "center"
    bar_plot.title.text_baseline = "middle"

    show(bar_plot)

graf_barras_pib("dados\\gdp_total.csv")
