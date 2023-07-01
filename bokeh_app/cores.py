from variaveis_globais import *
def lista_cores(pais):  
    if pais in DICT_CORES.keys():
        return DICT_CORES[pais]
    else:
        return CORES_COMUNS

def lista_alpha(pais): 
    if pais in DICT_CORES.keys():
        return ALPHA_DESTAQUES
    else:
        return ALPHA_COMUNS