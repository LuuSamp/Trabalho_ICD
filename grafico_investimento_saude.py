from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from bokeh.models import ColumnDataSource, HoverTool, Div, NumeralTickFormatter
from bokeh.plotting import figure

def grafico_investimento_saude(datapath_investimento_saude):

    '''
    Essa função deve receber um DataFrame relacionado aos investimentos dos países
    em saúde. Ela tem o objetivo de retornar um ranking(gráfico de barras) dos países 
    do G20 que mais investem em saúde nos anos de 1995 a 2010.
    '''

    # Criando um Data Frame "tratado" a partir da utilização da função "reorganiza": 
    df_investimento_saude = reorganiza(datapath_investimento_saude, "Investimento em Saúde", 1995, 2010)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_investimento_saude_g20 = filtro_paises_do_g20(df_investimento_saude, agrupamento="country")

    # Ordenando os valores da coluna "Investimento em Saúde":
    df_investimento_saude_g20 = df_investimento_saude_g20.sort_values(by='Investimento em Saúde', ascending=False).reset_index(drop=True)

    # Criando listas de cor e preenchimento para os países:

    dicionario_de_cores = DICT_CORES
    lista_de_cores = []
    lista_de_preenchimento = []
    lista_de_legenda = []

    for cada_pais in df_investimento_saude_g20["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
            lista_de_preenchimento.append(ALPHA_DESTAQUES)
            lista_de_legenda.append(cada_pais)
        else:
            lista_de_cores.append(CORES_COMUNS)
            lista_de_preenchimento.append(ALPHA_COMUNS)
            lista_de_legenda.append("Other Countries")

    # Adicionando coluna para cores e preenchimentos:
    df_investimento_saude_g20["Cor"] = lista_de_cores
    df_investimento_saude_g20["Preenchimento"] = lista_de_preenchimento
    df_investimento_saude_g20["Legenda"] = lista_de_legenda

    # Criando um ColumnDataSource:
    source = ColumnDataSource(df_investimento_saude_g20)

    # Base do Gráfico:
    ranking_investimento_saude_g20 = figure(x_range=df_investimento_saude_g20["country"], y_range=(0,30), 
                                            height=ALTURA, width=LARGURA, title="Média dos Investimentos em Saúde nos últimos anos", tools="")

    # Criando o Gráfico de Barras:
    ranking_investimento_saude_g20.vbar(x="country", top="Investimento em Saúde", source=source, width=0.9, 
                                        color="Cor", alpha="Preenchimento", line_color=COR_DA_LINHA, line_width=ESPESSURA_DA_LINHA, 
                                        line_alpha=ALPHA_DA_LINHA, legend_field = "Legenda")

    # Implementando ferramenta Hover:
    hover = HoverTool(tooltips=[('País', '@country'), 
                                    ('Investimento em Saúde', '@{Investimento em Saúde}%')])
    ranking_investimento_saude_g20.add_tools(hover)

    # Adicionando elementos estéticos ao Ranking:
    ranking_investimento_saude_g20.background_fill_color = BACKGROUND_FILL

    ranking_investimento_saude_g20.xaxis.major_label_orientation = 0.7

    ranking_investimento_saude_g20.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    ranking_investimento_saude_g20.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    ranking_investimento_saude_g20.xaxis.axis_label = "Países" 
    ranking_investimento_saude_g20.yaxis.axis_label = "Porcentagem de Investimento em Saúde" 

    ranking_investimento_saude_g20.xaxis.axis_label_text_font = FONTE_TEXTO
    ranking_investimento_saude_g20.yaxis.axis_label_text_font = FONTE_TEXTO

    ranking_investimento_saude_g20.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    ranking_investimento_saude_g20.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    ranking_investimento_saude_g20.xgrid.grid_line_color = LINHAS_GRADE
    ranking_investimento_saude_g20.ygrid.grid_line_color = LINHAS_GRADE

    ranking_investimento_saude_g20.title.text_font = FONTE_TEXTO
    ranking_investimento_saude_g20.title.text_font_size =TAMANHO_TITULO
    ranking_investimento_saude_g20.title.align = ALINHAMENTO_TITULO
    ranking_investimento_saude_g20.title.text_baseline = BASELINE_TITULO

    ranking_investimento_saude_g20.toolbar.logo = None 
    ranking_investimento_saude_g20.toolbar.autohide = True 
    ranking_investimento_saude_g20.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    ranking_investimento_saude_g20.yaxis.formater = NumeralTickFormatter(format = "0.0%") 

    # Adicionando legenda:
    ranking_investimento_saude_g20.legend.location = "top_right"
    ranking_investimento_saude_g20.legend.title = ""
    ranking_investimento_saude_g20.legend.border_line_color = COR_DA_LINHA
    ranking_investimento_saude_g20.legend.border_line_width = ESPESSURA_DA_LINHA
    ranking_investimento_saude_g20.legend.border_line_alpha = ALPHA_DA_LINHA

    descricao = Div(text="""
                                  Esse ranking procura mostrar os países do G20 que mais investem na área da saúde no período dos<br> 
                                  anos de 1995 a 2010. Além disso, foram destacados quatro países que tiveram os dois maiores e<br> 
                                  os dois menores Índices de Desenvolvimento Humano. Os países com cores de tons vermelhos são a<br> 
                                  Índia e a China que representam os países com os menores IDHs, enquanto os países com cores de<br> 
                                  tons azuis são a Austrália e os Estados Unidos que representam os países com os maiores IDHs.<br> 
                                  Pode-se perceber que, em relação ao gráfico, a Índia, que possui um IDH muito baixo também possui 
                                  uma média de investimentos muito baixa em saúde, sendo ela o país com a pior média do G20. Já<br>
                                  a China que possui o segundo menor IDH, possui um investimento mediano com relação aos outros<br>
                                  países. Por outro lado, os EUA que possui o segundo maior IDH é o país com o maior investimento<br>
                                  em saúde, enquanto a Austrália que possui o maior IDH está em sexto lugar no ranking de investimentos. 
                                    """)

    return ranking_investimento_saude_g20, descricao
