#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20

def graf_barras_pib(datapath):
    '''
    Essa função tem como objetivo produzir um gráfico de barras com a média do PIB de cada
    país do G20 e da UE durante o período de 20 anos (1990-2010) de forma ordenada.
    '''
    
    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "indice_analisado", 1990, 2010) #vai fazer um recorte nos dados
    dataframe = filtro_paises_do_g20(dataframe) #vai filtrar apenas os países do g20
    dataframe["indice_analisado"] = dataframe["indice_analisado"].apply(traduz_milhares) #vai traduzir todos os valores para numérico
    dataframe['indice_analisado'] = dataframe['indice_analisado'].astype(float) #vai transformar a coluna toda em float
    dataframe = dataframe.groupby('country')['indice_analisado'].mean().round(2).reset_index() #vai agrupar por país fazendo a média dos 20 anos
    dataframe = dataframe.sort_values(["indice_analisado"], ascending=False) #vai ordenar o dataframe do menor para o maior
    source = ColumnDataSource(dataframe) #vai transformar em CDS

    #CONFECÇÃO DO GRÁFICO

    #configuração do nome do arquivo
    output_file("ranking_pib.html")

    #criação do objeto figure
    bar_plot = figure(title="Média dos PIB's do G20 (1990-2010) ", width = 1350, height = 720, 
                      x_range=dataframe['country'], y_range=(0, max(dataframe['indice_analisado']) * 1.1))
    
    #adição da ferramenta hover
    hover = HoverTool(tooltips=[('País', '@country'), ('PIB (Bilhões de Dólares)', '@indice_analisado{$0,0}')])
    bar_plot.add_tools(hover)
    
    #criação do gráfico de barras em si
    bar_plot.vbar(x='country', top='indice_analisado', color='gray', source=source, width=0.8)
    
    #CONFIGURAÇÕES ESTÉTICAS DOS EIXOS
    bar_plot.xaxis.major_label_orientation = 0.7

    show(bar_plot)

graf_barras_pib("dados\\gdp_pcap.csv")
