#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *


def grafico_de_linhas_gdp(datapath):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh
    '''

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "PIB_PC", 1910, 2010) #vai filtrar a base de dados para os anos de 1990 e 2010
    dataframe["PIB_PC"] = dataframe["PIB_PC"].apply(traduz_milhares).astype(float)
    dataframe = filtro_paises_do_g20(dataframe, agrupamento="year")    

    source = ColumnDataSource(dataframe) #vai transformar o dataframe para o formato CDS

    #CONFECÇÃO DO GRÁFICO

    #configuração do nome do arquivo
    output_file("grafico_de_linhas_pib_pc.html")

    #criação do objeto figure
    line_plot = figure(title="PIB Per Capita G20 (1910-2010)", width = 1080, height = 720, x_range = (1910, 2010), 
                       y_range = (0, 60000))

    #adição da ferramenta hover
    hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('PIB Per Capita (Dólar)', '@PIB_PC{$0,0}')])
    line_plot.add_tools(hover)

    #dicionário de países de destaque e suas cores
    paises_destacaveis = DICT_CORES

    #criação das várias linhas e suas respectivas formatações
    for country in dataframe["country"].unique():
        country_data = dataframe[dataframe["country"]==country]

        #PAÍS DESTACADOS
        if country in paises_destacaveis.keys():
            line_plot.line(x="year", y="PIB_PC", source=country_data, color=paises_destacaveis[country], line_width=3, line_alpha=0.8)
        
        #OUTROS PAÍSES
        else:
            line_plot.line(x="year", y="PIB_PC", source=country_data, color=CORES_COMUNS, line_width=2, line_alpha=0.25)

    #CONFIGURAÇÕES ESTÉTICAS DOS EIXOS
    line_plot.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
    line_plot.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
    line_plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    line_plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    line_plot.xaxis.axis_label = "Anos" 
    line_plot.yaxis.axis_label = "PIB Per Capita (Dólares)" 

    line_plot.xaxis.axis_label_text_font = FONTE_TEXTO
    line_plot.yaxis.axis_label_text_font = FONTE_TEXTO

    line_plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    line_plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    line_plot.xgrid.grid_line_color = LINHAS_GRADE
    line_plot.ygrid.grid_line_color = LINHAS_GRADE

    line_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    #CONFIGURAÇÃO DO TÍTULO
    line_plot.title.text_font = FONTE_TEXTO
    line_plot.title.text_font_size = TAMANHO_TITULO
    line_plot.title.align = "center"
    line_plot.title.text_baseline = "middle"
    
    show(line_plot)
