from bokeh.plotting import figure 
from bokeh.models import HoverTool, Range1d
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
import pandas as pd
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import *

def linha_escola(datapath_homens,datapath2_mulheres):
    # Tratamento da base de dados.

    print(f"Carregando {__name__}")

    df_homens = reorganiza(datapath_homens, column_name = "Média de anos na Escola por Homens", first_year = 1970, last_year = 2015, csv = False)
    df_homens["Média de anos na Escola por Homens"] = df_homens["Média de anos na Escola por Homens"].apply(traduz_milhares).astype(float)
    df_mulheres = reorganiza(datapath2_mulheres, column_name = "Média de anos na Escola por Mulheres", first_year = 1970, last_year = 2015, csv = False)
    df_mulheres["Média de anos na Escola por Mulheres"] = df_mulheres["Média de anos na Escola por Mulheres"].apply(traduz_milhares).astype(float)
    df_homens = filtro_paises_do_g20(df_homens, agrupamento="year")
    df_mulheres = filtro_paises_do_g20(df_mulheres, agrupamento="year")

    df_anos_escola = pd.DataFrame()
    df_anos_escola["country"] = df_homens["country"]
    df_anos_escola["year"] = df_mulheres["year"]
    df_anos_escola["Média de anos na Escola por Homens"] = df_homens["Média de anos na Escola por Homens"]
    df_anos_escola["Média de anos na Escola por Mulheres"] = df_mulheres["Média de anos na Escola por Mulheres"]
    df_anos_escola["Média de anos na Escola"] = (df_anos_escola["Média de anos na Escola por Mulheres"] + df_anos_escola["Média de anos na Escola por Homens"]) / 2

    # Criação de ColumnDataSource.
    data_source = transformador_CDS(df_anos_escola)

    # Objeto base do gráfico.
    grafico_linha_escola = figure(title="Média de anos na escola", 
                                width=LARGURA, 
                                height=ALTURA, 
                                x_range=Range1d(1970, 2015, bounds="auto"), 
                                y_range=Range1d(0, 16, bounds="auto"), 
                                tools="pan,box_zoom,wheel_zoom,reset",
                                name="Anos Na Escola")

    # Adionando colunas referentes a transparência e cor dos países.
    for country in df_anos_escola["country"].unique():
        country_data = df_anos_escola[df_anos_escola["country"]==country]

    # Países em destaque.
        if country in DICT_CORES.keys():
            grafico_linha_escola.line(x="year", 
                                      y="Média de anos na Escola", 
                                      source=country_data, color=DICT_CORES[country], 
                                      line_width=ESPESSURA_DESTAQUES, 
                                      line_alpha=ALPHA_DESTAQUES,
                                      legend_label = country)
            
    # Países sem destaque.
        else:
            grafico_linha_escola.line(x="year", 
                                      y="Média de anos na Escola", 
                                      source=country_data, color="gray", 
                                      line_width=ESPESSURA_COMUNS, 
                                      line_alpha=ALPHA_COMUNS,
                                      legend_label = "Other Countries")

    # Implementação de ferramenta HoverTool.
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('Ano', '@year'), 
                                ('Média de tempo na Escola', '@{Média de anos na Escola}{0,0.00} anos')])
    grafico_linha_escola.add_tools(hover)

    # Aplicação de elementos estéticos.
    configuracoes_visuais(grafico_linha_escola,
                          titulo_xaxis="Anos",
                          titulo_yaxis="Média de Anos na Escola",
                          orientacao_xaxis=0,
                          posicao_legenda="bottom_right")
    
    grafico_linha_escola.legend.click_policy="hide"

    #DESCRIÇÃO DO GRÁFICO
    descricao = DESCRICAO_LINHAS_ANOS_ESCOLA

    return grafico_linha_escola, descricao