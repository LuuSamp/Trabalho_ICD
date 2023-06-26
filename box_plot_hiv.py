#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter, Whisker, BoxAnnotation
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
import numpy as np


def box_plot_hiv(datapath):
    '''
    Função com o objetivo de receber um datapath de uma base de dados, trata e converte ela e depois 
    produz um boxplot para cada país do g20 sobre mortes anuais de HIV
    '''
    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "indice_analisado", 1990, 2010) #vai fazer um recorte nos dados
    dataframe = filtro_paises_do_g20(dataframe) #vai filtrar apenas os países do g20
    dataframe["indice_analisado"] = dataframe["indice_analisado"].apply(traduz_milhares) #vai traduzir todos os valores para numérico
    dataframe['indice_analisado'] = dataframe['indice_analisado'].astype(float) #vai transformar a coluna toda em float

    #MANOBRA PARA CONSEGUIR FAZER O BOXPLOT
    dataframe = dataframe.fillna(0)

    #CALCULANDO OS QUANTIS PARA CONFECCIONAR OS BOXPLOTS

    # compute quantile

    dataframe_quantis = dataframe.groupby('country')['indice_analisado'].agg([lambda x: x.quantile(0.25),
                                                lambda x: x.quantile(0.50),
                                                lambda x: x.quantile(0.75)]).round(2).reset_index()

    lista_nomes_colunas = ["country", "q25", "q50", "q75"]
    dataframe_quantis.columns = lista_nomes_colunas

    dataframe_quantis["iqr"] = dataframe_quantis["q75"] - dataframe_quantis["q25"]
    dataframe_quantis["upper"] = dataframe_quantis["q75"] + 1.5*dataframe_quantis["iqr"]
    dataframe_quantis["lower"] = dataframe_quantis["q25"] - 1.5*dataframe_quantis["iqr"]

    source = ColumnDataSource(dataframe_quantis)

    plot = figure(x_range=dataframe_quantis["country"], title="Highway MPG distribution by vehicle class",
           background_fill_color="#eaefef", y_axis_label="MPG", width = 1350, height = 720)
    
    # outlier range
    whisker = Whisker(base="country", upper="upper", lower="lower", source=source)
    whisker.upper_head.size = whisker.lower_head.size = 20
    plot.add_layout(whisker)

    plot.vbar("country", 0.7, "q50", "q75", source=source, color="gray", line_color="black")
    plot.vbar("country", 0.7, "q25", "q50", source=source, color="gray", line_color="black")

    show(plot)

    print(dataframe_quantis)
box_plot_hiv("dados\\hiv_deaths.csv")