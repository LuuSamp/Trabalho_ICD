from bokeh.plotting import figure, column, row
from bokeh.io import curdoc
from bokeh.models import HoverTool, Whisker, Paragraph, Range1d, Select, Button, NumeralTickFormatter
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS
import pandas as pd
import numpy as np

#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import HoverTool, NumeralTickFormatter, Div, Paragraph
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS

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
    bar_plot.background_fill_color = BACKGROUND_FILL
    
    bar_plot.xaxis.major_label_orientation = 0.7

    bar_plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    bar_plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    bar_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    bar_plot.xaxis.axis_label = "Países" 
    bar_plot.yaxis.axis_label = "Média do PIB (Bilhões de Dólares)" 

    bar_plot.xaxis.axis_label_text_font = FONTE_TEXTO
    bar_plot.yaxis.axis_label_text_font = FONTE_TEXTO

    bar_plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    bar_plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    bar_plot.xgrid.grid_line_color = LINHAS_GRADE
    bar_plot.ygrid.grid_line_color = LINHAS_GRADE

    bar_plot.title.text_font = FONTE_TEXTO
    bar_plot.title.text_font_size =TAMANHO_TITULO
    bar_plot.title.align = ALINHAMENTO_TITULO
    bar_plot.title.text_baseline = BASELINE_TITULO

    bar_plot.toolbar.logo = None 
    bar_plot.toolbar.autohide = True 
    bar_plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    bar_plot.legend.location = "top_right"
    bar_plot.legend.title = ""
    bar_plot.legend.border_line_color = COR_DA_LINHA
    bar_plot.legend.border_line_width = ESPESSURA_DA_LINHA
    bar_plot.legend.border_line_alpha = ALPHA_DA_LINHA

    descricao = Paragraph(text="""Esse gráfico tem como objetivo representar a média do PIB dos integrantes do G20 do período de 1990 à 2010. <br>
                                    Assim como em todos os gráficos, chamamos atenção para os Estados Unidos, Austrália, China e Índia. <br> 
                                    Vemos que na questão econômica, a ordem se inverte e que não traduz a mesma ideia quando olhamos para o IDH. <br>
                                    A China, com um PID muitas vezes maior do que o da Austrália, não consegue transformar isso em melhoras significativas <br>
                                    para o bem estar do cidadão. Vamos ver no gráfico seguinte que isso pode ser explicado. Quantos as cores, elas foram <br>
                                    as mesmas utilizadas em todos os outros gráficos, o azul para representar os países com alto IDH e o vermelho os com <br>
                                    IDH baixo. Destaco, por fim, que utilizamos apenas a ferramenta Hover, uma vez que, no gráfico de barras, <br>
                                    não faz sentido ferramentas como a Pan, Box_Zoom e outras.""")

    return bar_plot, descricao

def grafico_bolhas(datapath_populacao, datapath_imc_homens, datapath_imc_mulheres, datapath_calorias):
    # Reorganizando o DataFrame.
    df_populacao = reorganiza(datapath_populacao, column_name = "População", first_year = 1990, last_year = 2008, csv = False)
    df_imc_homens = reorganiza(datapath_imc_homens, column_name = "IMC dos Homens", first_year = 1990, last_year = 2008, csv = False)
    df_imc_mulheres = reorganiza(datapath_imc_mulheres, column_name = "IMC das Mulheres", first_year = 1990, last_year = 2008, csv = False)
    df_calorias = reorganiza(datapath_calorias, column_name = "Média de Calorias", first_year = 1990, last_year = 2008, csv = False)

    df_populacao = filtro_paises_do_g20(df_populacao, False)
    df_populacao["População"] = df_populacao["População"].apply(traduz_milhares).astype(float)

    df_populacao = filtro_paises_do_g20(df_populacao, True, agrupamento="country")
    df_imc_homens = filtro_paises_do_g20(df_imc_homens, True, agrupamento="country")
    df_imc_mulheres = filtro_paises_do_g20(df_imc_mulheres, True, agrupamento="country")
    df_calorias = filtro_paises_do_g20(df_calorias, True, agrupamento="country")

    # Criação de DataFrame Final.
    df_final = pd.DataFrame()
    df_final["country"] = df_populacao["country"]
    df_final["População"] = df_populacao["População"]
    df_final["Média de Calorias"] = df_calorias["Média de Calorias"]
    df_final["IMC Médio"] = (df_imc_homens["IMC dos Homens"] + df_imc_mulheres["IMC das Mulheres"]) / 2
    df_final["População em Proporção"] = np.sqrt(df_final["População"])/200

    # Criação de colunas referentes a cores, transparência e legenda.
    lista_de_cores = []
    lista_de_preenchimento = []
    lista_legenda = []

    for cada_pais in df_final["country"]:
        if cada_pais in DICT_CORES.keys():
            lista_de_cores.append(DICT_CORES[cada_pais])
            lista_de_preenchimento.append(ALPHA_DESTAQUES)
            lista_legenda.append(cada_pais)
        else:
            lista_de_cores.append(CORES_COMUNS)
            lista_de_preenchimento.append(ALPHA_COMUNS)
            lista_legenda.append("Other Countries")
    df_final["color"] = lista_de_cores
    df_final["preenchimento"] = lista_de_preenchimento
    df_final["legenda"] = lista_legenda

    sem_destaques = transformador_CDS(df_final[df_final["color"]=="gray"]) 
    paises_com_destaque = transformador_CDS(df_final[df_final["color"] != "gray"])
        
    # Objeto base do gráfico.
    imc_calorias = figure(title="Calorias disponíveis por IMC no G20", 
                        width=LARGURA, 
                        height=ALTURA, 
                        x_range=Range1d(2150,3800,bounds="auto"), 
                        y_range=Range1d(19,29,bounds="auto"), 
                        tools="pan,box_zoom,wheel_zoom,reset",
                        name="IMC X Calorias")

    # Gráfico de Bolhas.
    imc_calorias.circle(x="Média de Calorias", 
                        y="IMC Médio", 
                        size="População em Proporção", 
                        source=sem_destaques, 
                        color="color", 
                        fill_alpha = "preenchimento", 
                        line_alpha=ALPHA_DA_LINHA, 
                        line_color=COR_DA_LINHA, 
                        line_width=ESPESSURA_DA_LINHA,
                        legend_field="legenda")
    imc_calorias.circle(x="Média de Calorias", 
                        y="IMC Médio", 
                        size="População em Proporção", 
                        source=paises_com_destaque, 
                        color="color", 
                        fill_alpha = "preenchimento", 
                        line_alpha=ALPHA_DA_LINHA, 
                        line_color=COR_DA_LINHA, 
                        line_width=ESPESSURA_DA_LINHA,
                        legend_field="country")

    # Configurando a ferramenta HoverTool.
    hover = HoverTool(tooltips=[("País", "@{country}"), ("IMC Médio", "@{IMC Médio}"), 
                                ("Média de Calorias", "@{Média de Calorias}{0,0.00} kcal"), 
                                ("População Média", "@{População}{0,0.00}")])
    imc_calorias.add_tools(hover)

    # Configuração de ferramentas estéticas.
    imc_calorias.background_fill_color = BACKGROUND_FILL

    imc_calorias.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
    imc_calorias.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
    imc_calorias.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    imc_calorias.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    imc_calorias.xaxis.axis_label = "Média de Calorias" 
    imc_calorias.yaxis.axis_label = "IMC Médio" 

    imc_calorias.xaxis.axis_label_text_font = FONTE_TEXTO
    imc_calorias.yaxis.axis_label_text_font = FONTE_TEXTO

    imc_calorias.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    imc_calorias.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    imc_calorias.xgrid.grid_line_color = LINHAS_GRADE
    imc_calorias.ygrid.grid_line_color = LINHAS_GRADE

    imc_calorias.title.text_font = FONTE_TEXTO
    imc_calorias.title.text_font_size =TAMANHO_TITULO
    imc_calorias.title.align = ALINHAMENTO_TITULO
    imc_calorias.title.text_baseline = BASELINE_TITULO

    imc_calorias.legend.location = "bottom_right"
    imc_calorias.legend.title = ""
    imc_calorias.legend.border_line_color = COR_DA_LINHA
    imc_calorias.legend.border_line_width = ESPESSURA_DA_LINHA
    imc_calorias.legend.border_line_alpha = ALPHA_DA_LINHA

    imc_calorias.toolbar.logo = None 
    imc_calorias.toolbar.autohide = True 
    imc_calorias.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    descricao = Paragraph(text="""O gráfico de Bolhas tem como objetivo comparar se há uma correlação entre a quantidade <br>
                                    média de calorias disponíveis e o Índice de Massa Corporal (IMC) das pessoas. Além disso, <br>
                                    o tamanho das bolhas foi utilizado para representar o tamanho da população, a fim de <br>
                                    verificar se isso influencia nos resultados do gráfico. Também foram definidos limites <br>
                                    para exibir as bolhas em uma área central do gráfico. As cores foram usadas para destacar <br>
                                    os países com bom desempenho (cor azul) e os países sem destaque (cor vermelha) na área de <br>
                                    IDH (Índice de Desenvolvimento Humano). As grades de fundo foram removidas, pois não eram <br>
                                    relevantes para o contexto do gráfico. Através da ferramenta HoverTool, é possível visualizar <br>
                                    o país, o IMC médio e a média de calorias disponíveis ao passar o mouse sobre as bolhas. <br>
                                    Conforme mencionado anteriormente, os rótulos foram padronizados com base no módulo variaveis_globais.
                                """)

    return imc_calorias, descricao

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

    descricao = Paragraph(text="""Esse Ranking busca ordenar os países de acordo com a emissão de carbono realizada <br>
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

def linha_escola(datapath_homens,datapath2_mulheres):
    # Tratamento da base de dados.
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
    hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('Média de tempo na Escola', '@{Média de anos na Escola}{0,0.00} anos')])
    grafico_linha_escola.add_tools(hover)

    # Aplicação de elementos estéticos.
    grafico_linha_escola.background_fill_color = BACKGROUND_FILL

    grafico_linha_escola.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
    grafico_linha_escola.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
    grafico_linha_escola.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    grafico_linha_escola.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    grafico_linha_escola.xaxis.axis_label = "Anos" 
    grafico_linha_escola.yaxis.axis_label = "Média de anos na escola" 

    grafico_linha_escola.xaxis.axis_label_text_font = FONTE_TEXTO
    grafico_linha_escola.yaxis.axis_label_text_font = FONTE_TEXTO

    grafico_linha_escola.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    grafico_linha_escola.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    grafico_linha_escola.xgrid.grid_line_color = LINHAS_GRADE
    grafico_linha_escola.ygrid.grid_line_color = LINHAS_GRADE


    grafico_linha_escola.title.text_font = FONTE_TEXTO
    grafico_linha_escola.title.text_font_size =TAMANHO_TITULO
    grafico_linha_escola.title.align = ALINHAMENTO_TITULO
    grafico_linha_escola.title.text_baseline = BASELINE_TITULO

    grafico_linha_escola.legend.location = "bottom_right"
    grafico_linha_escola.legend.title = ""
    grafico_linha_escola.legend.border_line_color = COR_DA_LINHA
    grafico_linha_escola.legend.border_line_width = ESPESSURA_DA_LINHA
    grafico_linha_escola.legend.border_line_alpha = ALPHA_DA_LINHA

    grafico_linha_escola.toolbar.logo = None 
    grafico_linha_escola.toolbar.autohide = True 
    grafico_linha_escola.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    descricao = Paragraph(text="""Neste gráfico de Linhas, é relacionada a média de anos de presença na escola ao <br>
                                    longo dos anos, em que cada linha representa um país. A visualização tem o objetivo <br>
                                    de identificar melhorias na frequência dos alunos nas escolas e detectar tendências <br>
                                    futuras com base nos padrões observados. Além disso, foram utilizadas cores para destacar <br>
                                    alguns países, sendo a cor azul para os melhores desempenhos e a cor vermelha para os <br>
                                    piores desempenhos no quesito de IDH (Índice de Desenvolvimento Humano). Por meio do <br>
                                    módulo HoverTool, foi criada uma ferramenta de interatividade que, ao passar o cursor <br>
                                    do mouse sobre cada linha, exibe o país, o ano correspondente e a média de anos na escola <br>
                                    para aquele período. O título foi posicionado no centro para alinhar-se com as informações <br>
                                    do gráfico. Por fim, vários rótulos foram padronizados em todos os gráficos usando o <br>
                                    módulo variaveis_globais, proporcionando uma estética consistente para cada representação.""")

    return grafico_linha_escola, descricao

def grafico_de_linhas_gdp(datapath):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh 
    sobre o PIB ou GDP Per Capita dos integrantes do G20
    '''

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "PIB_PC", 1910, 2020)
    dataframe["PIB_PC"] = dataframe["PIB_PC"].apply(traduz_milhares).astype(float)
    dataframe = filtro_paises_do_g20(dataframe, agrupamento="year")    

    #CONFECÇÃO DO GRÁFICO
    line_plot = figure(title="PIB Per Capita G20 (1910-2020)",
                       width = LARGURA,
                       height = ALTURA,
                       x_range = Range1d(1910, 2020, bounds="auto"), 
                       y_range = Range1d(0, 70000, bounds="auto"),
                       tools="pan,box_zoom,wheel_zoom,reset",
                       name="PIB Per Capita")

    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('País', '@country'), 
                                ('Ano', '@year'), 
                                ('PIB Per Capita (Dólar)', '@PIB_PC{$0,0}')])
    line_plot.add_tools(hover)

    #DICIONÁRIO COM OS PAÍSES DESTACADOS
    paises_destacaveis = DICT_CORES

    #CRIAÇÃO DAS LINHAS DE CADA PAÍS
    for country in dataframe["country"].unique():
        country_data = dataframe[dataframe["country"]==country]
        data_source = transformador_CDS(country_data)

        #PAÍS DESTACADOS
        if country in paises_destacaveis.keys():
            line_plot.line(x="year", 
                           y="PIB_PC", 
                           source=data_source, 
                           color=paises_destacaveis[country], 
                           line_width=ESPESSURA_DESTAQUES, 
                           line_alpha=ALPHA_DESTAQUES,
                           legend_label = country)
        
        #OUTROS PAÍSES
        else:
            line_plot.line(x="year", 
                           y="PIB_PC", 
                           source=data_source, 
                           color=CORES_COMUNS, 
                           line_width=ESPESSURA_COMUNS, 
                           line_alpha=ALPHA_COMUNS,
                           legend_label = "Other Countries")
            
        

    #CONFIGURAÇÕES ESTÉTICAS
    line_plot.background_fill_color = BACKGROUND_FILL

    line_plot.xaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_X
    line_plot.xaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS
    line_plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    line_plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    line_plot.xaxis.axis_label = "Anos" 
    line_plot.yaxis.axis_label = "PIB Per Capita (Dólares)" 

    line_plot.xaxis.axis_label_text_font = FONTE_TEXTO
    line_plot.yaxis.axis_label_text_font = FONTE_TEXTO

    line_plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    line_plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    line_plot.xgrid.grid_line_color = LINHAS_GRADE
    line_plot.ygrid.grid_line_color = LINHAS_GRADE

    line_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    line_plot.title.text_font = FONTE_TEXTO
    line_plot.title.text_font_size =TAMANHO_TITULO
    line_plot.title.align = ALINHAMENTO_TITULO
    line_plot.title.text_baseline = BASELINE_TITULO

    line_plot.toolbar.logo = None 
    line_plot.toolbar.autohide = True 
    line_plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    line_plot.legend.location = "top_left"
    line_plot.legend.title = ""
    line_plot.legend.border_line_color = COR_DA_LINHA
    line_plot.legend.border_line_width = ESPESSURA_DA_LINHA
    line_plot.legend.border_line_alpha = ALPHA_DA_LINHA

    descricao = Paragraph(text="""Esse gráfico, embora esteja relacionado com o anterior, tem como objetivo representar a evolução <br>
                                    do PIB per capita dos países. Olhando para os destaques, vemos claramente uma tendência. Os países <br>
                                    com maior IDH possuem um dos maiores PIB's per capita e China e Índia vão na contramão disso. <br>
                                    Como foi antecipado na descrição anterior, mesmo que a China nos últimos anos tenha um dos maiores <br>
                                    PIB's brutos do planeta, sua população é gigantesca e toda essa riqueza produzida quando é normalizada <br>
                                    pela população retorna um valor bem abaixo do esperado. O mesmo acontece para a Índia. Ambas com populações <br>
                                    acima do 1 bilhão de habitantes. Destaco também, por mais que não seja um dos países destacados, a Arábia Saudita <br>
                                    na década de 1970 até meados da década de 1980 teve um aumento gritante no seu PIB per capita e isso tem uma <br>
                                    explicação história simples: A Primeira Crise do Petróleo. Quando os países membros da OPEP, Organização dos Países <br>
                                    Exportadores de Petróleo, resolveu aumentar muito o valor do combustível fóssil, que é a principal alavanca da <br>
                                    economia saudita há muito tempo, e isso aumentou muito a arrecadação do país e o seu PIB per capita, uma vez que a <br>
                                    população não cresceu no mesmo rítimo. Por fim, destaco que nesse gráfico a maioria das ferramentas foram adicionadas, <br>
                                    mas só é possível utilizá-las dentro dos limites da janela de visualização dos dados. 
    """)

    return line_plot, descricao

dicionario_de_graficos = {"Expectativa de Vida": box_plot_life("dados/life_expectancy_male.csv"),
                          "IMC X Calorias": grafico_bolhas("dados/pop.csv", "dados/body_mass_index_bmi_men_kgperm2.csv", "dados/body_mass_index_bmi_women_kgperm2.csv","dados/food_supply_kilocalories_per_person_and_day.csv"),
                          "PIB Médio": graf_barras_pib("dados/total_gdp_ppp_inflation_adjusted.csv"),
                          "PIB Per Capita": grafico_de_linhas_gdp("dados/gdp_pcap.csv"),
                          "Anos Na Escola": linha_escola("dados/anos_homens_na_escola.csv", "dados/anos_mulheres_na_escola.csv"),
                          "Emissão de CO2": grafico_ranking_co2("dados/co2.csv")
                          }

selected_plot = 0
plot, paragraph = list(dicionario_de_graficos.values())[selected_plot]

select = Select(title = "Gráfico:", value = list(dicionario_de_graficos.keys())[selected_plot], options = list(dicionario_de_graficos.keys()))
previous_button = Button(label = "Previous")
next_button = Button(label = "Next")

plot_layout = column(paragraph, plot, name = "plot_layout")
control_layout = row(previous_button, select, next_button, name = "control_layout")
full_layout = column(plot_layout, control_layout, name = "main_layout")

def change_plot(attr, old, new):
    global paragraph, plot, selected_plot
    plot, paragraph = dicionario_de_graficos[select.value]
    selected_plot = list(dicionario_de_graficos.keys()).index(select.value)
    plot_layout = curdoc().get_model_by_name("plot_layout")
    plot_layout.children.pop(0)
    plot_layout.children.pop(0)
    plot_layout.children.append(paragraph)
    plot_layout.children.append(plot)

select.on_change("value", change_plot)

def previous_button_action():
    '''
    Função que é executada quando o botão "previous" é clicado. Seleciona o gráfico anterior.
    '''
    global selected_plot
    selected_plot -= 1
    if selected_plot < 0:
        selected_plot = len(list(dicionario_de_graficos.keys())) - 1
    select.value = list(dicionario_de_graficos.keys())[selected_plot]

previous_button.on_click(previous_button_action)

def next_button_action():
    '''
    Função que é executada quando o botão "next" é clicado. Seleciona o gráfico seguinte.
    '''
    global selected_plot
    selected_plot += 1
    if selected_plot >= len(list(dicionario_de_graficos.keys())):
        selected_plot = 0
    select.value = list(dicionario_de_graficos.keys())[selected_plot]

next_button.on_click(next_button_action)

curdoc().add_root(full_layout)