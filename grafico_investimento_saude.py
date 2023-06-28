from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
from variaveis_globais import *
from cores import lista_cores, lista_alpha

# Criando um Data Frame "tratado" a partir da utilização da função "reorganiza": 
df_investimento_saude = reorganiza("dados/government_health_spending_of_total_gov_spending_percent.csv", "Investimento em Saúde", 1995, 2010)

# Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
df_investimento_saude_g20 = filtro_paises_do_g20(df_investimento_saude, agrupamento="country")

# Ordenando os valores da coluna "Investimento em Saúde":
df_investimento_saude_g20 = df_investimento_saude_g20.sort_values(by='Investimento em Saúde', ascending=False).reset_index(drop=True)

# Criando listas de cor e preenchimento para os países:
paises = df_investimento_saude_g20["country"].apply 

lista_de_cores = []
lista_de_preenchimento = []

lista_de_preenchimento.append(lista_cores(paises))
lista_de_cores.append(lista_alpha(paises))
print(type(paises))

