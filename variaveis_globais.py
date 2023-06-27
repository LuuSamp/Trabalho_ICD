#ARQUIVO EM PYTHON COM AS VARIÁVEIS GLOBAIS
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from funcao_maximo_minimo import funcao_maximo_minimo

BACKGROUND = "#a1a1a1"
FONTE_TEXTO = "Arial"
TAMANHO_TITULO = "20pt"
TAMANHO_TITULO_EIXOS = "15pt"
NUM_MINOR_TICKS = 5
NUM_MAJOR_TICKS_X = 20
NUM_MAJOR_TICKS_Y = 15
LINHAS_GRADE = None

dataframe_idh = reorganiza("dados\idh_total.csv", "IDH", 1990, 2010)
dataframe_idh = filtro_paises_do_g20(dataframe_idh, agrupamento="country")
del dataframe_idh["year"]
DICT_CORES = funcao_maximo_minimo(dataframe_idh, "IDH", "country")
print(DICT_CORES)
