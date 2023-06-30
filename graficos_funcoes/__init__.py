from graf_boxplot_expectativa_de_vida_matheus import box_plot_life
from graf_bolhas_calorias_imc_kaiky import grafico_bolhas
from graf_barras_pib_total_medio_matheus import graf_barras_pib
from graf_linhas_pib_pc_matheus import grafico_de_linhas_gdp
from graf_linhas_anos_na_escola_kaiky import linha_escola
from graf_barras_emissao_carbono_kaiky import grafico_ranking_co2


dicionario_de_graficos = {"Expectativa de Vida": box_plot_life("dados\life_expectancy_male"),
                          "IMC X Calorias": grafico_bolhas("dados\pop.csv", "dados\body_mass_index_bmi_men_kgperm2.csv", "dados\body_mass_index_bmi_women_kgperm2.csv","dados\food_supply_kilocalories_per_person_and_day.csv"),
                          "PIB Médio": graf_barras_pib("dados\total_gdp_ppp_inflation_adjusted.csv"),
                          "PIB Per Capita": grafico_de_linhas_gdp("dados\gdp_pcap.csv"),
                          "Anos Na Escola": linha_escola("dados\anos_homens_na_escola.csv", "dados\anos_mulheres_na_escola.csv"),
                          "Emissão de CO2": grafico_ranking_co2("dados\co2.csv")}