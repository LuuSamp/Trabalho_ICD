#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import HoverTool, NumeralTickFormatter
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import *

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
    configuracoes_visuais(bar_plot, 
                          titulo_yaxis="PIB Médio de 1990-2010 (Em Bilhões de Dólares)",
                          titulo_xaxis="Integrantes do G20",
                          orientacao_xaxis=0.7,
                          posicao_legenda="top_right")
    
    bar_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")
    
    #DESCRIÇÃO DO GRÁFICO
    descricao = DESCRICAO_BARRAS_PIB

    return bar_plot, descricao
