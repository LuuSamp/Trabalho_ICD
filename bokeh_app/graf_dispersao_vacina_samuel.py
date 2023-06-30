# Bibliotecas e módulos necessários:
from reorganizador import reorganiza
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, Range1d
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter
from traducao_g20 import filtro_paises_do_g20 
from variaveis_globais import *
from funcoes_esteticas import *
from fun_cores_legendas_alpha import *
from descricoes_dos_graficos import *
from bokeh.io import save, output_file

def grafico_de_dispersao(datapath_vacinas, datapath_mortes):  
    ''''
    Essa função deve receber dois DataFrames, pois ela tem o objetivo de criar um 
    Scatter Plot (Gráfico de Dispersão) que compara dois assuntos bem importantes 
    na área da saúde, a Vacinação de crianças e a Mortalidade Infantil.
    '''

    output_file("./html/graf_vacinas.html")

    # Criação de Data Frames "tratados" a partir da utilização da função "reorganiza": 
    df_vacina = reorganiza(datapath_vacinas, "Porcentagem de Vacinação", 1990, 2010)
    df_mortes = reorganiza(datapath_mortes, "Mortes a cada 1000 nascimentos", 1990, 2010)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_vacina_g20 = filtro_paises_do_g20(df_vacina, False, agrupamento="country")
    df_mortes_g20 = filtro_paises_do_g20(df_mortes, False, agrupamento="country")

    # Criando um DataFrame com todas as colunas necessárias:
    df_final = pd.DataFrame()
    df_final["country"] = df_vacina_g20["country"]
    df_final["Porcentagem de Vacinação"] = df_vacina_g20["Porcentagem de Vacinação"]/100
    df_final["Mortes a cada 1000 nascimentos"] = df_mortes_g20["Mortes a cada 1000 nascimentos"]

    # Criação de colunas referentes a cores, transparência e legenda:
    df_final = criador_colunas_esteticas(df_final)

    # Criação de ColumnDataSource:
    paises_destacados = ColumnDataSource(df_final)

    # Criando um objeto figure:
    scatter_plot = figure(title="Vacinação e Mortalidade Infantil", 
                        width=LARGURA, 
                        height=ALTURA, 
                        x_range=Range1d(0.63,1.00,bounds="auto"), 
                        y_range=Range1d(0,95,bounds="auto"), 
                        tools="pan,box_zoom,wheel_zoom,reset",
                        name="Vacinação X Mortalidade Infantil")

    # Criando scatter plot:
    scatter_plot.scatter(x = "Porcentagem de Vacinação",
                        y = "Mortes a cada 1000 nascimentos",
                        source=paises_destacados, 
                        color="color", 
                        fill_alpha = "preenchimento", 
                        line_alpha=ALPHA_DA_LINHA, 
                        line_color=COR_DA_LINHA, 
                        line_width=ESPESSURA_DA_LINHA,
                        legend_field="legenda", 
                        size = 15)

    # Configurando a ferramenta HoverTool:
    hover = HoverTool(tooltips=[("País", "@country"), 
                                ("Porcentagem de Vacinação", "@{Porcentagem de Vacinação}%"),
                                ("Média de mortes/1000 nascimentos", "@{Mortes a cada 1000 nascimentos}")])
    scatter_plot.add_tools(hover)

    # Configuração de ferramentas estéticas:
    configuracoes_visuais(scatter_plot,
                          titulo_xaxis="Porcentagem de crianças vacinadas",
                          titulo_yaxis="Mortes a cada 1000 nascimentos",
                          orientacao_xaxis=0,
                          posicao_legenda="top_right")
    
    scatter_plot.xaxis.formatter = NumeralTickFormatter(format = "0.0%")    

    descricao = DESCRICAO_DISPERSAO_VACINA

    save(scatter_plot)

    return scatter_plot, descricao

grafico_de_dispersao("dados/dtp3_immunized_percent_of_one_year_olds.csv", "dados/child_mortality_0_5_year_olds_dying_per_1000_born.csv")















