#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import ColumnDataSource, HoverTool, Whisker, Paragraph
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *

def box_plot_life(datapath):
    '''
    Função com o objetivo de receber um datapath de uma base de dados, trata e converte ela e depois 
    produz um boxplot para a espectativa de vida dos países do G20.
    '''

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "LIFE_EXP", 1950, 2020) #vai fazer um recorte nos dados
    dataframe["LIFE_EXP"] = dataframe["LIFE_EXP"].apply(traduz_milhares).astype(float)
    dataframe = filtro_paises_do_g20(dataframe, True, "year") #vai filtrar apenas os países do g20


    #CALCULANDO OS QUANTIS E PREPARANDO OS DADOS PARA CONFECCIONAR OS BOXPLOTS
    dataframe_quantis = dataframe.groupby('country')['LIFE_EXP'].agg([lambda x: x.quantile(0.05),
                                                                              lambda x: x.quantile(0.25), 
                                                                              lambda x: x.quantile(0.50),
                                                                              lambda x: x.quantile(0.75),
                                                                              lambda x: x.quantile(0.95)]).round(0).reset_index()

    lista_nomes_colunas = ["country","q05", "q25", "q50", "q75", "q95"]
    dataframe_quantis.columns = lista_nomes_colunas
    
    dataframe_quantis = dataframe_quantis.sort_values("q50", ascending=True).reset_index()

    #CRINDO A COLUNA DE CORES
    dicionario_de_cores = DICT_CORES
    lista_de_cores = []
    lista_de_preenchimentos = []
    lista_de_legenda = []

    for cada_pais in dataframe_quantis["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
            lista_de_preenchimentos.append(ALPHA_DESTAQUES)
            lista_de_legenda.append(cada_pais)
        else:
            lista_de_cores.append("gray")
            lista_de_preenchimentos.append(ALPHA_COMUNS)
            lista_de_legenda.append("Other Countries")

    dataframe_quantis["color"] = lista_de_cores
    dataframe_quantis["preenchimento"] = lista_de_preenchimentos
    dataframe_quantis["legenda"] = lista_de_legenda

    #CRIANDO O BOXPLOT
    data_source = ColumnDataSource(dataframe_quantis)

    boxplot = figure(x_range=dataframe_quantis["country"], 
                     title="Expectativa de Vida G20 (1950-2020)",
                     width = LARGURA, 
                     height = ALTURA, 
                     y_range=(30, 85),
                     tools = "",
                     name="Expectativa de Vida")
    
    whisker = Whisker(base="country", 
                      upper="q95", 
                      lower="q05", 
                      source=data_source, 
                      line_color=COR_DA_LINHA)
    whisker.upper_head.size = whisker.lower_head.size = 20
    boxplot.add_layout(whisker)

    boxplot.vbar("country", 
                 0.7, 
                 "q50", 
                 "q75", 
                 source=data_source, 
                 color="color", 
                 line_color=COR_DA_LINHA, 
                 alpha = "preenchimento",
                 line_alpha = ALPHA_DA_LINHA, 
                 line_width = ESPESSURA_DA_LINHA,
                 legend_field="legenda")
    
    boxplot.vbar("country", 
                 0.7, 
                 "q25", 
                 "q50", 
                 source=data_source, 
                 color="color", 
                 line_color=COR_DA_LINHA, 
                 alpha = "preenchimento",
                 line_alpha = ALPHA_DA_LINHA,
                 line_width = ESPESSURA_DA_LINHA,
                 legend_field="legenda")

    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('Integrante', '@country'), ('Média', '@q50 anos'),
                                ('Q05', '@q05 anos'), ('Q25', '@q25 anos'), 
                                ('Q75', '@q75 anos'), ('Q95', '@q95 anos')])
    boxplot.add_tools(hover)

    #CONFIGURAÇÕES ESTÉTICAS
    boxplot.background_fill_color = BACKGROUND_FILL

    boxplot.xaxis.major_label_orientation = 0.7

    boxplot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    boxplot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    boxplot.xaxis.axis_label = "Países" 
    boxplot.yaxis.axis_label = "Anos" 

    boxplot.xaxis.axis_label_text_font = FONTE_TEXTO
    boxplot.yaxis.axis_label_text_font = FONTE_TEXTO

    boxplot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    boxplot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    boxplot.xgrid.grid_line_color = LINHAS_GRADE
    boxplot.ygrid.grid_line_color = LINHAS_GRADE

    boxplot.title.text_font = FONTE_TEXTO
    boxplot.title.text_font_size =TAMANHO_TITULO
    boxplot.title.align = ALINHAMENTO_TITULO
    boxplot.title.text_baseline = BASELINE_TITULO

    boxplot.toolbar.logo = None 
    boxplot.toolbar.autohide = True 
    boxplot.toolbar_location = POSICAO_BARRA_FERRAMENTAS 

    boxplot.legend.location = "bottom_right"
    boxplot.legend.title = ""
    boxplot.legend.border_line_color = COR_DA_LINHA
    boxplot.legend.border_line_width = ESPESSURA_DA_LINHA
    boxplot.legend.border_line_alpha = ALPHA_DA_LINHA

    descricao = Paragraph(text="""Esse gráfico tem como objetivo apresentar a distribuição dentre os dados de expectativa de vida <br>
                                    de cada integrante do G20 de 1950 à 2020. O destaque permanece para os mesmos países, Estados Unidos, <br>
                                    Austrália, China e Índia, donos dos melhores e piores IDH's do G20, respectivamente. Podemos observar que <br>
                                    conseguimos visualizar algo uma tendência coerente com o IDH. Vemos que EUA e Austrália possuíram uma espectativa <br>
                                    de vida maiores que China e Índia. Porém a China, mesmo com o IDH baixo, não possuí uma das menores expectativas de vida <br>
                                    algo que pode ser explicado por diversos fatores. Alguns expecialistas, por exemplo, atribuem a longevidade de alguns povos <br>
                                    asiáticos à alimentação e à cultura muito específica. Novamente, pontuo que escolhemos não disponibilizar <br>
                                    todas as ferramentas, mas apenas o Hover. Não seria coerente permitir ao usuário se mover por todo <br>
                                    o espaço disponível, sendo que todos os dados estão agrupados nessa janela de visualização.""")

    return boxplot, descricao