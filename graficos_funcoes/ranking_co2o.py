from bokeh.plotting import figure
from bokeh.models import HoverTool, Div
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza
from variaveis_globais import *
from CDS import transformador_CDS

def grafico_ranking_co2(datapath):
    # Tratamento de dados
    df_co2 = reorganiza(datapath, column_name = "CO2", first_year = 1990, last_year = 2018, csv = False)
    df_co2 = filtro_paises_do_g20(df_co2, agrupamento="country")
    del df_co2["year"]

    # Reoordenamento de DataFrame
    df_co2 = df_co2.sort_values(by='CO2', ascending=False).reset_index(drop=True)

    # Criando coluna de lista de cor e preenchimento relacionada a cada país
    dicionario_de_cores = DICT_CORES
    lista_de_cores = []
    lista_de_preenchimento = []
    lista_de_legenda = []

    for cada_pais in df_co2["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
            lista_de_preenchimento.append(ALPHA_DESTAQUES)
            lista_de_legenda.append(cada_pais)
        else:
            lista_de_cores.append(CORES_COMUNS)
            lista_de_preenchimento.append(ALPHA_COMUNS)
            lista_de_legenda.append("Other Countries")

    df_co2["color"] = lista_de_cores
    df_co2["preenchimento"] = lista_de_preenchimento
    df_co2["legenda"] = lista_de_legenda

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
    ranking_co2.background_fill_color = BACKGROUND_FILL

    ranking_co2.xaxis.major_label_orientation = 0.7

    ranking_co2.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    ranking_co2.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    ranking_co2.xaxis.axis_label = "Países" 
    ranking_co2.yaxis.axis_label = "Média da Emissão de CO2 por Pessoa (Toneladas)" 

    ranking_co2.xaxis.axis_label_text_font = FONTE_TEXTO
    ranking_co2.yaxis.axis_label_text_font = FONTE_TEXTO

    ranking_co2.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    ranking_co2.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    ranking_co2.xgrid.grid_line_color = LINHAS_GRADE
    ranking_co2.ygrid.grid_line_color = LINHAS_GRADE

    ranking_co2.title.text_font = FONTE_TEXTO
    ranking_co2.title.text_font_size =TAMANHO_TITULO
    ranking_co2.title.align = ALINHAMENTO_TITULO
    ranking_co2.title.text_baseline = BASELINE_TITULO

    ranking_co2.legend.location = "top_right"
    ranking_co2.legend.title = ""
    ranking_co2.legend.border_line_color = COR_DA_LINHA
    ranking_co2.legend.border_line_width = ESPESSURA_DA_LINHA
    ranking_co2.legend.border_line_alpha = ALPHA_DA_LINHA

    ranking_co2.toolbar.logo = None 
    ranking_co2.toolbar.autohide = True 
    ranking_co2.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    descricao = Div(text="""Esse Ranking busca ordenar os países de acordo com a emissão de carbono realizada <br>
                                 por cada um deles. As barras do gráfico foram colocadas de maneira vertical para que <br>
                                 itens com barras mais longas ou mais altas sejam visualmente distintos dos itens com <br>
                                 barras mais curtas ou mais baixas, facilitando a identificação dos melhores ou piores <br>
                                 classificados e também contribuindo para a compreensão das diferenças entre os países. <br>
                                 Além disso, é válido ressaltar que algumas das barras foram destacadas com cor, sendo <br>
                                 a cor azul utilizada para representar os melhores e a cor vermelha para representar as <br>
                                 piores nações no quesito de IDH (Índice de Desenvolvimento Humano). Outro ponto a ser <br>
                                 destacado é a utilização de ferramentas interativas por meio da função HoverTool, que <br>
                                 permite a visualização dos dados de cada barra, incluindo informações sobre o país e <br>
                                 o valor do investimento realizado. O título foi colocado no centro para alinhar-se com <br>
                                as informações do gráfico. Os nomes dos países foram rotacionados para facilitar a <br>
                                leitura. Quanto aos rótulos, foram padronizados com base no módulo de variáveis globais.""")

    return ranking_co2, descricao