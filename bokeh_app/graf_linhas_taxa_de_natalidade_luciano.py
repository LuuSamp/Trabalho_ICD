from bokeh.plotting import figure, column
from bokeh.models import HoverTool, Range1d
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
import pandas as pd
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import DESCRICAO_LINHAS_NATALIDADE
from bokeh.io import save, output_file, show

def linha_natalidade(datapath):
    """
    Essa função recebe o datapath de um CSV do gapminder relacionado à taxa de natalidade
    """

    # Tratamento da base de dados.
    print(f"Carregando {__name__}")

    dataframe_natalidade = reorganiza(datapath, column_name = "Bebês por mulher", first_year = 1910, last_year = 2010)
    dataframe_natalidade = filtro_paises_do_g20(dataframe_natalidade, agrupamento="year")


    # Objeto base do gráfico.
    plot = figure(title="Taxa de Natalidade (20)", 
                                width=LARGURA, 
                                height=ALTURA, 
                                x_range=Range1d(1910, 2010, bounds="auto"), 
                                y_range=Range1d(0, 16, bounds="auto"), 
                                tools="pan,box_zoom,wheel_zoom,reset",
                                name="Anos Na Escola")

    # Adionando colunas referentes a transparência e cor dos países.
    for country in dataframe_natalidade["country"].unique():
        data_source = transformador_CDS(dataframe_natalidade[dataframe_natalidade["country"]==country])

    # Países em destaque.
        if country in DICT_CORES.keys():
            plot.line(x="year", 
                                      y="Bebês por mulher", 
                                      source=data_source, color=DICT_CORES[country], 
                                      line_width=ESPESSURA_DESTAQUES, 
                                      line_alpha=ALPHA_DESTAQUES,
                                      legend_label = country)
            
    # Países sem destaque.
        else:
            plot.line(x="year", 
                                      y="Bebês por mulher", 
                                      source=data_source, color="gray", 
                                      line_width=ESPESSURA_COMUNS, 
                                      line_alpha=ALPHA_COMUNS,
                                      legend_label = "Other Countries")

    # Implementação de ferramenta HoverTool.
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('Ano', '@year'), 
                                ('Bebês por mulher', '@{Bebês por mulher}{0.00}')])
    plot.add_tools(hover)

    # Aplicação de elementos estéticos.
    configuracoes_visuais(plot,
                          titulo_xaxis="Anos",
                          titulo_yaxis="Bebês por mulher",
                          orientacao_xaxis=0,
                          posicao_legenda="top_right")
    
    plot.legend.click_policy="hide"

    plot.sizing_mode = "stretch_width"

    return plot, DESCRICAO_LINHAS_NATALIDADE
output_file("html/Taxa_de_Natalidade.html")

save(column(*linha_natalidade("dados/children_per_woman_total_fertility.csv")))