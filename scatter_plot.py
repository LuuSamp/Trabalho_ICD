from reorganizador import reorganiza
import pandas as pd

df_vacina = reorganiza("dados/dtp3_immunized_percent_of_one_year_olds.csv", "Porcentagem de Vacinação", 1990, 2010)

df_mortes = reorganiza("dados/child_mortality_0_5_year_olds_dying_per_1000_born.csv", "Mortes a cada 1000 nascimentos", 1990, 2010)

df_vacina["Quantidade"] = df_mortes["Quantidade"]

















