from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20

# Criando um Data Frame "tratado" a partir da utilização da função "reorganiza": 
df_investimento_saude = reorganiza("dados/dtp3_immunized_percent_of_one_year_olds.csv", "Porcentagem de Vacinação", 1990, 2010)

# Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
df_investimento_saude_g20 = filtro_paises_do_g20(df_investimento_saude, "Porcentagem de Vacinação")