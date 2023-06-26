#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20

def grafico_de_linhas(datapath, column_name, titulo):

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
    output_file(f"{titulo}.html")

    #criação do objeto figure
    line_plot = figure(title=f"{titulo}", width = 1240, height = 720)

    #adição da ferramenta hover
    hover = HoverTool(tooltips=[('País', '@country'), ('Ano', '@year'), ('PIB Per Capita (Dólar)', f'@{column_name}')])
    line_plot.add_tools(hover)

    #dicionário de países de destaque e suas cores
    paises_destacaveis = {"Brazil":"green","Argentina":"blue","France":"purple","Germany":"yellow","Canada":"pink","Japan":"orange"}

    #criação das várias linhas e suas respectivas formatações
    for country in dataframe["country"].unique():
        country_data = dataframe[dataframe["country"]==country]

        #PAÍS DESTACADOS
        if country in paises_destacaveis.keys():
            line_plot.line(x="year", y=f"{column_name}", source=country_data, color=paises_destacaveis[country], line_width=4)
        
        #OUTROS PAÍSES
        else:
            line_plot.line(x="year", y=f"{column_name}", source=country_data, color="gray", line_width=1)

    #CONFIGURAÇÕES ESTÉTICAS DOS EIXOS
    line_plot.xaxis[0].ticker.desired_num_ticks = 20
    line_plot.xaxis[0].ticker.num_minor_ticks = 0
    line_plot.yaxis[0].ticker.desired_num_ticks = 10
    line_plot.yaxis[0].ticker.num_minor_ticks = 0

    line_plot.xaxis.axis_label = "Anos" 
    line_plot.yaxis.axis_label = "PIB Per Capita (Dólares)" 

    line_plot.xgrid.grid_line_color = None
    line_plot.ygrid.grid_line_color = None


    show(line_plot)

grafico_de_linhas("dados\gdp_pcap.csv", "PIB_PC", "PIB Per Capita G20 1990-2010")