#import de bibliotecas e módulos

import pandas as pd 
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource

def grafico_de_linhas(datapath="teste.csv", title="Título Genérico", analized_column="indice"):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh
    '''
    output_file(f"{title}".html)

    dataframe = pd.read_csv(datapath) #vai ler o nosso arquivo csv com pandas e transformar em dataframe
    source = ColumnDataSource(dataframe) #vai transformar o dataframe para o formato CDS

    line_plot = figure(title=f"{title}") #vai criar o objeto figure que iremos trabalhar

    show(line_plot)
    save(line_plot)
