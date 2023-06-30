from bokeh.plotting import figure
from bokeh.models import HoverTool
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import *
from fun_cores_legendas_alpha import criador_colunas_esteticas

def grafico_ranking_co2(datapath):
    # Tratamento de dados
    df_co2 = reorganiza(datapath, column_name = "CO2", first_year = 1990, last_year = 2018, csv = False)
    df_co2 = filtro_paises_do_g20(df_co2, agrupamento="country")
    del df_co2["year"]

    # Reoordenamento de DataFrame
    df_co2 = df_co2.sort_values(by='CO2', ascending=False).reset_index(drop=True)

    #CRIANDO COLUNAS PARA COR, PREENCHIMENTO E LEGENDA
    df_co2 = criador_colunas_esteticas(df_co2)

    # Criando um ColumnDataSource
    source = transformador_CDS(df_co2)

    # Base do Gráfico
    ranking_co2 = figure(x_range=df_co2["country"], 
                         y_range=(0,20),
                         height=ALTURA, 
                         width=LARGURA, 
                         title="Emissão de Carbono por Habitante", 
                         tools="",
                         name="Emissão de CO2")

    # Criação do Gráfico de Barras
    ranking_co2.vbar(x="country", 
                     top="CO2", 
                     source=source, 
                     width=0.9, 
                     color="color", 
                     alpha="preenchimento", 
                     line_color=COR_DA_LINHA, 
                     line_width=ESPESSURA_DA_LINHA, 
                     line_alpha=ALPHA_DA_LINHA,
                     legend_field="legenda")

    # Implementação de Ferramenta Hover
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('Emissão por Pessoa', '@CO2 toneladas')])
    ranking_co2.add_tools(hover)

    # Adição de elementos estéticos ao Ranking
    configuracoes_visuais(ranking_co2,
                          titulo_xaxis="Países",
                          titulo_yaxis="Média da Emissão de CO2 por Pessoa (Toneladas)",
                          orientacao_xaxis=0.7,
                          posicao_legenda="top_right")

    #DESCRIÇÃO DO GRÁFICO
    descricao = DESCRICAO_BARRAS_CARBONO

    return ranking_co2, descricao