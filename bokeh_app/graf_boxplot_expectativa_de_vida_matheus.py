#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import HoverTool, Whisker
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import *
from fun_cores_legendas_alpha import criador_colunas_esteticas
from bokeh.io import save, output_file

def box_plot_life(datapath):
    '''
    Função com o objetivo de receber um datapath de uma base de dados, trata e converte ela e depois 
    produz um boxplot para a espectativa de vida dos países do G20.
    '''

    output_file("./html/graf_boxplot.html")

    print(f"Carregando {__name__}")
    
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

    #CRIANDO COLUNAS PARA COR, PREENCHIMENTO E LEGENDA
    dataframe_quantis = criador_colunas_esteticas(dataframe_quantis)

    #CRIANDO O BOXPLOT
    data_source = transformador_CDS(dataframe_quantis)

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
    configuracoes_visuais(boxplot,
                          titulo_xaxis="Países",
                          titulo_yaxis="Expectativa de Vida",
                          orientacao_xaxis=0.7,
                          posicao_legenda="bottom_right")

    #DESCRIÇÃO DO GRÁFICO
    descricao = DESCRICAO_BOXPLOT_EXP_VIDA

    save(boxplot)

    return boxplot, descricao

box_plot_life("dados/life_expectancy_male.csv")

