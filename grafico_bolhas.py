from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import pandas as pd
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza, traduz_milhares

# As bases de dados são convertidas a partir da função reorganiza.
df_populacao = reorganiza(datapath = "dados/pop.csv", column_name = "População", first_year = 1990, last_year = 2008, csv = False)
df_imc_homens = reorganiza(datapath = "dados/body_mass_index_bmi_men_kgperm2.csv", column_name = "IMC dos Homens", first_year = 1990, last_year = 2008, csv = False)
df_imc_mulheres = reorganiza(datapath = "dados/body_mass_index_bmi_women_kgperm2.csv", column_name = "IMC das Mulheres", first_year = 1990, last_year = 2008, csv = False)
df_calorias = reorganiza(datapath = "dados/food_supply_kilocalories_per_person_and_day.csv", column_name = "Média de Calorias", first_year = 1990, last_year = 2008, csv = False)

# Criando o DataFrame Final
df_final = pd.DataFrame()
df_final["country"] = df_populacao["country"]
df_final["year"] = df_populacao["year"]
df_final["População"] = df_populacao["População"]
df_final["IMC dos Homens"] = df_imc_homens["IMC dos Homens"]
df_final["IMC das Mulheres"] = df_imc_mulheres["IMC das Mulheres"]
df_final["Média de Calorias"] = df_calorias["Média de Calorias"]
df_final['IMC Médio'] = (df_final['IMC dos Homens'] + df_final['IMC das Mulheres']) / 2

# Filtro de Países do G20
df_final = filtro_paises_do_g20(df_final)

print(df_final)
