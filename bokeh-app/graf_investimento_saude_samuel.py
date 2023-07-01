from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from bokeh.plotting import figure
from descricoes_dos_graficos import *
from funcoes_esteticas import configuracoes_visuais
from fun_cores_legendas_alpha import *
from bokeh.io import save, output_file

def grafico_investimento_saude(datapath_investimento_saude):

    '''
    Essa função deve receber um DataFrame relacionado aos investimentos dos países
    em saúde. Ela tem o objetivo de retornar um ranking(gráfico de barras) dos países 
    do G20 que mais investem em saúde nos anos de 1995 a 2010.
    '''

    output_file("./html/graf_barras_saude.html")

    # Criando um Data Frame "tratado" a partir da utilização da função "reorganiza": 
    df_investimento_saude = reorganiza(datapath_investimento_saude, "Investimento em Saúde", 1995, 2010)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_investimento_saude_g20 = filtro_paises_do_g20(df_investimento_saude, agrupamento="country")

    # Ordenando os valores da coluna "Investimento em Saúde":
    df_investimento_saude_g20 = df_investimento_saude_g20.sort_values(by='Investimento em Saúde', ascending=False).reset_index(drop=True)

    # Criando listas de cor e preenchimento para os países:
    criador_colunas_esteticas(df_investimento_saude_g20)

    # Criando um ColumnDataSource:
    source = ColumnDataSource(df_investimento_saude_g20)

    # Base do Gráfico:
    ranking_investimento_saude_g20 = figure(x_range=df_investimento_saude_g20["country"], 
                                            y_range=(0,30), 
                                            height=ALTURA, 
                                            width=LARGURA, 
                                            title="Média dos Investimentos em Saúde nos últimos anos", 
                                            tools="",
                                            name="Investimento em Saúde")

    # Criando o Gráfico de Barras:
    ranking_investimento_saude_g20.vbar(x="country", 
                                        top="Investimento em Saúde", 
                                        source=source, 
                                        width=0.9, 
                                        color="color", 
                                        alpha="preenchimento", 
                                        line_color=COR_DA_LINHA, 
                                        line_width=ESPESSURA_DA_LINHA, 
                                        line_alpha=ALPHA_DA_LINHA, 
                                        legend_field = "legenda")

    # Implementando ferramenta Hover:
    hover = HoverTool(tooltips=[('País', '@country'), 
                                    ('Investimento em Saúde', '@{Investimento em Saúde}%')])
    ranking_investimento_saude_g20.add_tools(hover)

    # Adicionando elementos estéticos ao Ranking:
    configuracoes_visuais(ranking_investimento_saude_g20,
                          titulo_xaxis="Países",
                          titulo_yaxis="Porcentagem de Investimento em Saúde",
                          orientacao_xaxis=0.7,
                          posicao_legenda="top_right")

    ranking_investimento_saude_g20.yaxis.formatter = NumeralTickFormatter(format = "0.0%") 

    descricao = DESCRICAO_BARRAS_SAUDE

    save(ranking_investimento_saude_g20)

    return ranking_investimento_saude_g20, descricao

grafico_investimento_saude("dados/government_health_spending_of_total_gov_spending_percent.csv")
