#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, Whisker, NumeralTickFormatter
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from transformador_de_log import transformador_log10
from variaveis_globais import *

def box_plot_hiv(datapath):
    '''
    Função com o objetivo de receber um datapath de uma base de dados, trata e converte ela e depois 
    produz um boxplot para cada país do g20 sobre mortes anuais de HIV
    '''
    #CONFIGURANDO O ARQUIVO DE SAÍDA
    output_file("boxplot_hiv.html")

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "MORTES_HIV", 1950, 2020) #vai fazer um recorte nos dados
    dataframe["MORTES_HIV"] = dataframe["MORTES_HIV"].apply(traduz_milhares).astype(float)
    dataframe = filtro_paises_do_g20(dataframe, True, "year") #vai filtrar apenas os países do g20

    #MANOBRA PARA CONSEGUIR FAZER O BOXPLOT
    dataframe = dataframe.fillna(0)

    #CALCULANDO OS QUANTIS PARA CONFECCIONAR OS BOXPLOTS
    dataframe_quantis = dataframe.groupby('country')['MORTES_HIV'].agg([lambda x: x.quantile(0.05),
                                                                              lambda x: x.quantile(0.25), 
                                                                              lambda x: x.quantile(0.50),
                                                                              lambda x: x.quantile(0.75),
                                                                              lambda x: x.quantile(0.95)]).round(0).reset_index()

    lista_nomes_colunas = ["country","q05", "q25", "q50", "q75", "q95"]
    dataframe_quantis.columns = lista_nomes_colunas
    
    dataframe_quantis = dataframe_quantis.sort_values("q50", ascending=True).reset_index()

    #CONFIGURANDO AS CORES
    dicionario_de_cores = DICT_CORES
    lista_de_cores = []

    for cada_pais in dataframe_quantis["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
        else:
            lista_de_cores.append("gray")

    dataframe_quantis["color"] = lista_de_cores


    #CRIANDO O BOXPLOT
    source = ColumnDataSource(dataframe_quantis)

    boxplot = figure(x_range=dataframe_quantis["country"], title="Expectativa de Vida G20 (1950-2020)",
                     width = 1080, height = 720, y_range=(30, 85))
    
    whisker = Whisker(base="country", upper="q95", lower="q05", source=source, line_color="gray")
    whisker.upper_head.size = whisker.lower_head.size = 20
    boxplot.add_layout(whisker)

    boxplot.vbar("country", 0.7, "q50", "q75", source=source, color="color", line_color="black", alpha = 0.7)
    boxplot.vbar("country", 0.7, "q25", "q50", source=source, color="color", line_color="black", alpha = 0.7)

    boxplot.xaxis.major_label_orientation = 0.7

    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('Integrante', '@country'), ('Média', '@q50 anos'),
                                ('Q05', '@q05 anos'), ('Q25', '@q25 anos'), 
                                ('Q75', '@q75 anos'), ('Q95', '@q95 anos')])
    boxplot.add_tools(hover)

    #CONFIGURAÇÕES ESTÉTICAS
    boxplot.background_fill_color = (241, 242, 244, 0.5)

    boxplot.xaxis.major_label_orientation = 0.7

    boxplot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    boxplot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    boxplot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    boxplot.xaxis.axis_label = "Países" 
    boxplot.yaxis.axis_label = "Anos" 

    boxplot.xaxis.axis_label_text_font = FONTE_TEXTO
    boxplot.yaxis.axis_label_text_font = FONTE_TEXTO

    boxplot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    boxplot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    boxplot.xgrid.grid_line_color = LINHAS_GRADE
    boxplot.ygrid.grid_line_color = LINHAS_GRADE

    #CONFIGURAÇÃO DO TÍTULO
    boxplot.title.text_font = FONTE_TEXTO
    boxplot.title.text_font_size =TAMANHO_TITULO
    boxplot.title.align = "center"
    boxplot.title.text_baseline = "middle"
    show(boxplot)

box_plot_hiv("dados\\life_expectancy_male.csv")