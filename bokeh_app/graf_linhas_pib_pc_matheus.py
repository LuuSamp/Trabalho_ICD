#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import HoverTool, NumeralTickFormatter, Range1d
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import *
from bokeh.io import save, output_file


def grafico_de_linhas_gdp(datapath):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh 
    sobre o PIB ou GDP Per Capita dos integrantes do G20
    '''
    
    print(f"Carregando {__name__}")

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
                       tools="pan,box_zoom,wheel_zoom,reset",
                       name="PIB Per Capita")

    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('Ano', '@year'), 
                                ('PIB Per Capita (Dólar)', '@PIB_PC{$0,0}')])
    line_plot.add_tools(hover)

    #DICIONÁRIO COM OS PAÍSES DESTACADOS
    paises_destacaveis = DICT_CORES

    #CRIAÇÃO DAS LINHAS DE CADA PAÍS
    for country in dataframe["country"].unique():
        country_data = dataframe[dataframe["country"]==country]
        data_source = transformador_CDS(country_data)

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
    configuracoes_visuais(line_plot,
                          titulo_xaxis="Anos",
                          titulo_yaxis="PIB Per Capita (Dólares)",
                          orientacao_xaxis=0,
                          posicao_legenda="top_left")

    line_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    line_plot.legend.click_policy="hide"
    
    #DESCRIÇÃO DO GRÁFICO
    descricao = DESCRICAO_LINHA_PIB_PC

    line_plot.sizing_mode = "stretch_width"

    return line_plot, descricao

