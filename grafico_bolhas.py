from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.io import output_file
import pandas as pd
from traducao_g20 import filtro_paises_do_g20
from reorganizador import reorganiza, traduz_milhares


df_populacao = reorganiza("dados/pop.csv")
df_imc_homens = reorganiza("dados/body_mass_index_bmi_men_kgperm2.csv")
df_imc_mulheres = ("dados/body_mass_index_bmi_women_kgperm2.csv")
df_calorias = ("dados/food_supply_kilocalories_per_person_and_day.csv")



