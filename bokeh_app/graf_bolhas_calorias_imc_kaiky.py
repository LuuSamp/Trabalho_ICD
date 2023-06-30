from bokeh.plotting import figure
from bokeh.models import HoverTool, Range1d
import pandas as pd
import numpy as np
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza, traduz_milhares
from variaveis_globais import *
from CDS import transformador_CDS
from funcoes_esteticas import configuracoes_visuais
from descricoes_dos_graficos import *
from fun_cores_legendas_alpha import criador_colunas_esteticas
from bokeh.io import save, output_file

def grafico_bolhas(datapath_populacao, datapath_imc_homens, datapath_imc_mulheres, datapath_calorias):

    output_file("./html/graf_bolhas.html")

    print(f"Carregando {__name__}")

    # Reorganizando o DataFrame.
    df_populacao = reorganiza(datapath_populacao, column_name = "População", first_year = 1990, last_year = 2008, csv = False)
    df_imc_homens = reorganiza(datapath_imc_homens, column_name = "IMC dos Homens", first_year = 1990, last_year = 2008, csv = False)
    df_imc_mulheres = reorganiza(datapath_imc_mulheres, column_name = "IMC das Mulheres", first_year = 1990, last_year = 2008, csv = False)
    df_calorias = reorganiza(datapath_calorias, column_name = "Média de Calorias", first_year = 1990, last_year = 2008, csv = False)

    df_populacao = filtro_paises_do_g20(df_populacao, False)
    df_populacao["População"] = df_populacao["População"].apply(traduz_milhares).astype(float)

    df_populacao = filtro_paises_do_g20(df_populacao, True, agrupamento="country")
    df_imc_homens = filtro_paises_do_g20(df_imc_homens, True, agrupamento="country")
    df_imc_mulheres = filtro_paises_do_g20(df_imc_mulheres, True, agrupamento="country")
    df_calorias = filtro_paises_do_g20(df_calorias, True, agrupamento="country")

    # Criação de DataFrame Final.
    df_final = pd.DataFrame()
    df_final["country"] = df_populacao["country"]
    df_final["População"] = df_populacao["População"]
    df_final["Média de Calorias"] = df_calorias["Média de Calorias"]
    df_final["IMC Médio"] = (df_imc_homens["IMC dos Homens"] + df_imc_mulheres["IMC das Mulheres"]) / 2
    df_final["População em Proporção"] = np.sqrt(df_final["População"])/200

    #CRIANDO COLUNAS PARA COR, PREENCHIMENTO E LEGENDA
    df_final = criador_colunas_esteticas(df_final)

    sem_destaques = transformador_CDS(df_final[df_final["color"]=="gray"]) 
    paises_com_destaque = transformador_CDS(df_final[df_final["color"] != "gray"])
        
    # Objeto base do gráfico.
    imc_calorias = figure(title="Calorias disponíveis por IMC no G20", 
                        width=LARGURA, 
                        height=ALTURA, 
                        x_range=Range1d(2150,3800,bounds="auto"), 
                        y_range=Range1d(19,29,bounds="auto"), 
                        tools="pan,box_zoom,wheel_zoom,reset",
                        name="IMC X Calorias")

    # Gráfico de Bolhas.
    imc_calorias.circle(x="Média de Calorias", 
                        y="IMC Médio", 
                        size="População em Proporção", 
                        source=sem_destaques, 
                        color="color", 
                        fill_alpha = "preenchimento", 
                        line_alpha=ALPHA_DA_LINHA, 
                        line_color=COR_DA_LINHA, 
                        line_width=ESPESSURA_DA_LINHA,
                        legend_field="legenda")
    imc_calorias.circle(x="Média de Calorias", 
                        y="IMC Médio", 
                        size="População em Proporção", 
                        source=paises_com_destaque, 
                        color="color", 
                        fill_alpha = "preenchimento", 
                        line_alpha=ALPHA_DA_LINHA, 
                        line_color=COR_DA_LINHA, 
                        line_width=ESPESSURA_DA_LINHA,
                        legend_field="country")

    # Configurando a ferramenta HoverTool.
    hover = HoverTool(tooltips=[("País", "@{country}"), ("IMC Médio", "@{IMC Médio}"), 
                                ("Média de Calorias", "@{Média de Calorias}{0,0.00} kcal"), 
                                ("População Média", "@{População}{0,0.00}")])
    imc_calorias.add_tools(hover)

    # Configuração de ferramentas estéticas.
    configuracoes_visuais(imc_calorias, 
                          titulo_xaxis="Média de Calorias",
                          titulo_yaxis="IMC Médio" , 
                          orientacao_xaxis=0, 
                          posicao_legenda="bottom_right")
    
    imc_calorias.legend.click_policy="hide"

    #DESCRIÇÃO DO GRÁFICO
    descricao = DESCRICAO_BOLHAS_CALORIAS

    save(imc_calorias)

    return imc_calorias, descricao

grafico_bolhas("dados/pop.csv", "dados/body_mass_index_bmi_men_kgperm2.csv", "dados/body_mass_index_bmi_women_kgperm2.csv","dados/food_supply_kilocalories_per_person_and_day.csv")
