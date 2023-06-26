#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20

def grafico_de_linhas(datapath="teste.csv", column_name="INDICE", title="Título Genérico"):

    '''
    a função tem como objetivo receber o path dos arquivos e o 
    título do gráfico e gerar automaticamente um gráfico com bokeh
    '''

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, f"{column_name}", 1990, 2010) #vai filtrar a base de dados para os anos de 1990 e 2010
    dataframe = filtro_paises_do_g20(dataframe) #vai filtrar a base de dados apenas para países do g20 e UE
    dataframe[f"{column_name}"] = dataframe[f"{column_name}"].apply(traduz_milhares) #vai modificar os valores numéricos
    source = ColumnDataSource(dataframe) #vai transformar o dataframe para o formato CDS
    

    #CONFECÇÃO DO GRÁFICO

    #configuração do nome do arquivo
    output_file(f"{title}.html")

    #criação do objeto figure
    line_plot = figure(title=f"{title}", width = 1240, height = 720)

    #adição da ferramenta hover
    hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('PIB Per Capita (Dólar)', f'@{column_name}')])
    line_plot.add_tools(hover)

    #dicionário de países de destaque e suas cores
    paises_destacaveis = {"Brazil":"green","Argentina":"blue","France":"purple","Germany":"yellow","Canada":"pink","Japan":"orange"}

    #criação das várias linhas e suas respectivas formatações
    for each_country in dataframe["country"].unique():
        country_data = dataframe[dataframe["country"]==each_country]

        #PAÍS DESTACADOS
        if each_country in paises_destacaveis.keys():
            line_plot.line(x="year", y=f"{column_name}", source=country_data, color=paises_destacaveis[each_country], line_width=4)

        #OUTROS PAÍSES
        else:
            line_plot.line(x="year", y="{column_name}", source=country_data, color="gray", line_width=1)

    show(line_plot)

grafico_de_linhas("dados\gdp_pcap.csv")