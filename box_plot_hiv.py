#BIBLIOTECAS E MÓDULOS IMPORTADOS
from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, HoverTool, Whisker
from reorganizador import reorganiza, traduz_milhares
from traducao_g20 import filtro_paises_do_g20
from transformador_de_log import transformador_log10

def box_plot_hiv(datapath):
    '''
    Função com o objetivo de receber um datapath de uma base de dados, trata e converte ela e depois 
    produz um boxplot para cada país do g20 sobre mortes anuais de HIV
    '''
    #CONFIGURANDO O ARQUIVO DE SAÍDA
    output_file("boxplot_hiv.html")

    #TRATAMENTO DA BASE DE DADOS
    dataframe = reorganiza(datapath, "indice_analisado", 1910, 2010) #vai fazer um recorte nos dados
    dataframe = filtro_paises_do_g20(dataframe, "indice_analisado") #vai filtrar apenas os países do g20
    dataframe["indice_analisado"] = dataframe["indice_analisado"].apply(traduz_milhares) #vai traduzir todos os valores para numérico
    dataframe['indice_analisado'] = dataframe['indice_analisado'].astype(float) #vai transformar a coluna toda em float

    #MANOBRA PARA CONSEGUIR FAZER O BOXPLOT
    dataframe = dataframe.fillna(0)

    #CALCULANDO OS QUANTIS PARA CONFECCIONAR OS BOXPLOTS
    dataframe_quantis = dataframe.groupby('country')['indice_analisado'].agg([lambda x: x.quantile(0.05),
                                                                              lambda x: x.quantile(0.25), 
                                                                              lambda x: x.quantile(0.50),
                                                                              lambda x: x.quantile(0.75),
                                                                              lambda x: x.quantile(0.95)]).round(2).reset_index()

    lista_nomes_colunas = ["country","q05", "q25", "q50", "q75", "q95"]
    dataframe_quantis.columns = lista_nomes_colunas

    #CRIANDO AS COLUNAS LOG
    dataframe_quantis = transformador_log10(dataframe_quantis, ["q05", "q25", "q50", "q75", "q95"])
    
    dataframe_quantis = dataframe_quantis.sort_values("q50", ascending=True).reset_index()

    #CONFIGURANDO AS CORES
    dicionario_de_cores = {"Brazil":"blue","Argentina":"royalblue","France":"skyblue","India":"coral","Canada":"red","Japan":"indianred"}
    lista_de_cores = []

    for cada_pais in dataframe_quantis["country"]:
        if cada_pais in dicionario_de_cores.keys():
            lista_de_cores.append(dicionario_de_cores[cada_pais])
        else:
            lista_de_cores.append("gray")

    dataframe_quantis["color"] = lista_de_cores


    #CRIANDO O BOXPLOT
    source = ColumnDataSource(dataframe_quantis)

    plot = figure(x_range=dataframe_quantis["country"], title="Mortes Por HIV nos Integrantes do G20",
                   y_axis_label="Número de Mortes na Escala Log10", width = 1350, height = 720, y_range=(0, 60000))
    
    whisker = Whisker(base="country", upper="q95", lower="q05", source=source, line_color="gray")
    whisker.upper_head.size = whisker.lower_head.size = 20
    plot.add_layout(whisker)

    plot.vbar("country", 0.7, "q50", "q75", source=source, color="color", line_color="black", alpha = 0.7)
    plot.vbar("country", 0.7, "q25", "q50", source=source, color="color", line_color="black", alpha = 0.7)

    plot.xaxis.major_label_orientation = 0.7

    #ADICIONANDO A FERRAMENTA DO HOVER
    hover = HoverTool(tooltips=[('Integrante', '@country'), ('Média', '@q50{$0,00}'),
                                ('Q05', '@q05{$0,00}'), ('Q25', '@q25{$0,00}'), 
                                ('Q75', '@q75{$0,00}'), ('Q95', '@q95{$0,00}')])
    plot.add_tools(hover)



    show(plot)
    print(dataframe_quantis)


box_plot_hiv("dados\\gdp_pcap.csv")