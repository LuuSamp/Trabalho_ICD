#ARQUIVO EM PYTHON COM AS VARIÁVEIS GLOBAIS
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from funcao_maximo_minimo import funcao_maximo_minimo

FONTE_TEXTO = "Arial"
TAMANHO_TITULO = "20pt"
TAMANHO_TITULO_EIXOS = "15pt"
NUM_MINOR_TICKS = 0
NUM_MAJOR_TICKS_X = 20
NUM_MAJOR_TICKS_Y = 15
LINHAS_GRADE = None
LARGURA = 1080
ALTURA = 720

dataframe_idh = reorganiza("dados\idh_total.csv", "IDH", 1990, 2010)
dataframe_idh = filtro_paises_do_g20(dataframe_idh, agrupamento="country")
del dataframe_idh["year"]
DICT_CORES = funcao_maximo_minimo(dataframe_idh, "IDH", "country")

CORES_COMUNS = "gray"
ALPHA_DESTAQUES = 0.8
ALPHA_COMUNS = 0.2
ESPESSURA_DESTAQUES = 3
ESPESSURA_COMUNS = 2
BACKGROUND_FILL = (241, 242, 244, 0.5)
LARGURA = 1080
ALTURA = 720
POSICAO_BARRA_FERRAMENTAS = "below"
ALINHAMENTO_TITULO = "center"
BASELINE_TITULO = "middle"
