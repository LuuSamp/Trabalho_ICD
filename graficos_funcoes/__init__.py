from box_plot_life import box_plot_life
from grafico_bolhas import grafico_bolhas
from grafico_de_barras_PIB import graf_barras_pib
from grafico_de_linhas_gdp_pc import grafico_de_linhas_gdp
from grafico_linha_anos_escola import linha_escola
from ranking_co2o import grafico_ranking_co2


dicionario_de_graficos = {"Expectativa de Vida": box_plot_life("dados/life_expectancy_male.csv"),
                          "IMC X Calorias": grafico_bolhas("dados/pop.csv", "dados/body_mass_index_bmi_men_kgperm2.csv", "dados/body_mass_index_bmi_women_kgperm2.csv","dados/food_supply_kilocalories_per_person_and_day.csv"),
                          "PIB Médio": graf_barras_pib("dados/total_gdp_ppp_inflation_adjusted.csv"),
                          "PIB Per Capita": grafico_de_linhas_gdp("dados/gdp_pcap.csv"),
                          "Anos Na Escola": linha_escola("dados/anos_homens_na_escola.csv", "dados/anos_mulheres_na_escola.csv"),
                          "Emissão de CO2": grafico_ranking_co2("dados/co2.csv")}