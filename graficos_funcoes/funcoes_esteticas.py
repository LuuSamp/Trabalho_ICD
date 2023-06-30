from variaveis_globais import *

def configuracoes_visuais(objeto_plot, 
                          titulo_xaxis, 
                          titulo_yaxis, 
                          orientacao_xaxis=0, 
                          posicao_legenda="bottom_right"):
    """
    Função que tem como objetivo configurar a estética geral dos gráficos com elementos que por 
    decisão do grupo seriam de certa forma padrão em todos os gráficos.
    """
    
    #COR DE FUNDO
    objeto_plot.background_fill_color = BACKGROUND_FILL

    #ORIENTAÇÃO DOS TICKS 
    objeto_plot.xaxis.major_label_orientation = orientacao_xaxis

    #NÚMERO DE TICKS
    objeto_plot.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    objeto_plot.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    #TÍTULOS DOS EIXOS
    objeto_plot.xaxis.axis_label = f"{titulo_xaxis}" 
    objeto_plot.yaxis.axis_label = f"{titulo_yaxis}" 

    #FONTE DOS TÍTULOS DOS EIXOS
    objeto_plot.xaxis.axis_label_text_font = FONTE_TEXTO
    objeto_plot.yaxis.axis_label_text_font = FONTE_TEXTO

    #TAMANHO DOS TÍTULOS DOS EIXOS
    objeto_plot.xaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS
    objeto_plot.yaxis.axis_label_text_font_size = TAMANHO_TITULO_EIXOS

    #LINHAS DE GRADE
    objeto_plot.xgrid.grid_line_color = LINHAS_GRADE
    objeto_plot.ygrid.grid_line_color = LINHAS_GRADE

    #TÍTULO PRINCIPAL (ESTÉTICA E POSICIONAMENTO)
    objeto_plot.title.text_font = FONTE_TEXTO
    objeto_plot.title.text_font_size =TAMANHO_TITULO
    objeto_plot.title.align = ALINHAMENTO_TITULO
    objeto_plot.title.text_baseline = BASELINE_TITULO

    #BARRA DE FERRAMENTAS
    objeto_plot.toolbar.logo = None 
    objeto_plot.toolbar.autohide = True 
    objeto_plot.toolbar_location = POSICAO_BARRA_FERRAMENTAS 

    #LEGENDA
    objeto_plot.legend.location = f"{posicao_legenda}"
    objeto_plot.legend.title = ""
    objeto_plot.legend.border_line_color = COR_DA_LINHA
    objeto_plot.legend.border_line_width = ESPESSURA_DA_LINHA
    objeto_plot.legend.border_line_alpha = ALPHA_DA_LINHA