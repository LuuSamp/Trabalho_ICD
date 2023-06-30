#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.models import HoverTool, NumeralTickFormatter, Range1d, Div
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais

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
    configuracoes_visuais(line_plot,
                          titulo_xaxis="Anos",
                          titulo_yaxis="PIB Per Capita (Dólares)",
                          orientacao_xaxis=0,
                          posicao_legenda="top_left")

    line_plot.yaxis.formatter = NumeralTickFormatter(format="$0,0")

    descricao = Div(text="""Esse gráfico, embora esteja relacionado com o anterior, tem como objetivo representar a evolução <br>
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