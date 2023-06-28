#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter, Range1d
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *


def grafico_de_linhas_gdp(datapath):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh 
    sobre o PIB ou GDP Per Capita dos integrantes do G20
    '''

    #CONFIGURANDO A SAÍDA
    output_file("..\\grafico_de_linhas_pib_pc.html")

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "PIB_PC", 1910, 2020)
    dataframe["PIB_PC"] = dataframe["PIB_PC"].apply(traduz_milhares).astype(float)
    dataframe = filtro_paises_do_g20(dataframe, agrupamento="year")    

    #CONFECÇÃO DO GRÁFICO
    line_plot = figure(title="PIB Per Capita G20 (1910-2020)",
                       width = LARGURA,
                       height = ALTURA,
                       x_range = Range1d(1910, 2020, bounds="auto"), 
                       y_range = Range1d(0, 70000, bounds="auto"),
                       tools="pan,box_zoom,wheel_zoom,reset")

    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('Ano', '@year'), 
                                ('PIB Per Capita (Dólar)', '@PIB_PC{$0,0}')])
    line_plot.add_tools(hover)

    #DICIONÁRIO COM OS PAÍSES DESTACADOS
    paises_destacaveis = DICT_CORES

    lista_de_legenda = []
    for indice in range(dataframe.shape[0]):
        if dataframe["country"][indice] in paises_destacaveis.keys():
            lista_de_legenda.append(dataframe["country"][indice])
            print(dataframe["country"][indice])
        else:
            lista_de_legenda.append("G20 Countries")

    dataframe["legenda"] = lista_de_legenda

    #CRIAÇÃO DAS LINHAS DE CADA PAÍS
    for country in dataframe["country"].unique():
        country_data = dataframe[dataframe["country"]==country]
        data_source = ColumnDataSource(country_data)

        #PAÍS DESTACADOS
        if country in paises_destacaveis.keys():
            line_plot.line(x="year", 
                           y="PIB_PC", 
                           source=data_source, 
                           color=paises_destacaveis[country], 
                           line_width=ESPESSURA_DESTAQUES, 
                           line_alpha=ALPHA_DESTAQUES,
                           legend_label = country)
        
        #OUTROS PAÍSES
        else:
            line_plot.line(x="year", 
                           y="PIB_PC", 
                           source=data_source, 
                           color=CORES_COMUNS, 
                           line_width=ESPESSURA_COMUNS, 
                           line_alpha=ALPHA_COMUNS,
                           legend_label = "Other Countries")
            
        

    #CONFIGURAÇÕES ESTÉTICAS
    line_plot.background_fill_color = BACKGROUND_FILL

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

    line_plot.title.text_font = FONTE_TEXTO
    line_plot.title.text_font_size =TAMANHO_TITULO
    line_plot.title.align = ALINHAMENTO_TITULO
    line_plot.title.text_baseline = BASELINE_TITULO

    line_plot.toolbar.logo = None 
    line_plot.toolbar.autohide = True 
    line_plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    line_plot.legend.location = "top_left"
    line_plot.legend.title = ""
    line_plot.legend.border_line_color = COR_DA_LINHA
    line_plot.legend.border_line_width = ESPESSURA_DA_LINHA
    line_plot.legend.border_line_alpha = ALPHA_DA_LINHA

    show(line_plot)
    save(line_plot)

grafico_de_linhas_gdp("dados\\gdp_pcap.csv")
