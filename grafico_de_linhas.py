#import de bibliotecas e módulos

import pandas as pd 
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from reorganizador import reorganiza


def grafico_de_linhas(datapath="teste.csv", column_name="INDICE", title="Título Genérico"):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh
    '''

    dataframe = reorganiza(datapath, f"{column_name}", 1990, 2010)

    output_file(f"{title}.html")

    source = ColumnDataSource(dataframe) #vai transformar o dataframe para o formato CDS

    line_plot = figure(title=f"{title}") #vai criar o objeto figure que iremos trabalhar

    show(line_plot)
    save(line_plot)

grafico_de_linhas("dados\hiv_anual_deaths.csv")