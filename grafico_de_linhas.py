#import de bibliotecas e módulos

import pandas as pd 
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool
from reorganizador import reorganiza, traduz_milhares


def grafico_de_linhas(datapath="teste.csv", column_name="INDICE", title="Título Genérico"):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh
    '''

    dataframe = reorganiza(datapath, f"{column_name}", 1990, 2010)
    # dataframe[f"{column_name}"].apply(traduz_milhares)

    output_file(f"{title}.html")

    source = ColumnDataSource(dataframe) #vai transformar o dataframe para o formato CDS

    line_plot = figure(title=f"{title}", width = 1240, height = 720) #vai criar o objeto figure que iremos trabalhar

    hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('Nº Mortes', f'@{column_name}')])
    line_plot.add_tools(hover)








    paises_destacaveis = {"Brazil":"green","Argentina":"blue","France":"purple","Germany":"yellow","Canada":"pink","Japan":"orange"}

    for country in dataframe["country"].unique():

        country_data = dataframe[dataframe["country"]==country]

        if country in paises_destacaveis.keys():
            line_plot.line(x="year", y="INDICE", source=country_data, color=paises_destacaveis[country], line_width=4)

        else:
            line_plot.line(x="year", y="INDICE", source=country_data, color="gray", line_width=1)









    show(line_plot)
    save(line_plot)

grafico_de_linhas("dados\hiv_anual_deaths.csv")