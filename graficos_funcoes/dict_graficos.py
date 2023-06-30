from graf_boxplot_expectativa_de_vida_matheus import box_plot_life
from graf_bolhas_calorias_imc_kaiky import grafico_bolhas
from graf_barras_pib_total_medio_matheus import graf_barras_pib
from graf_linhas_pib_pc_matheus import grafico_de_linhas_gdp
from graf_linhas_anos_na_escola_kaiky import linha_escola
from graf_barras_emissao_carbono_kaiky import grafico_ranking_co2
from graf_mapa_gini_luciano import grafico_mapa_Gini
from graf_mapa_idh_samuel import grafico_mapa_IDH
from graf_barras_pib_animado_luciano import ranking_animado_PIB
from graf_proporcoes_luciano import educacao_por_genero

dicionario_de_graficos = {"Expectativa de Vida": box_plot_life("dados/life_expectancy_male.csv"),
                          "IMC X Calorias": grafico_bolhas("dados/pop.csv", "dados/body_mass_index_bmi_men_kgperm2.csv", "dados/body_mass_index_bmi_women_kgperm2.csv","dados/food_supply_kilocalories_per_person_and_day.csv"),
                          "PIB Médio": graf_barras_pib("dados/gdp_total.csv"),
                          "PIB Per Capita": grafico_de_linhas_gdp("dados/gdp_pcap.csv"),
                          "Anos Na Escola": linha_escola("dados/anos_homens_na_escola.csv", "dados/anos_mulheres_na_escola.csv"),
                          "Emissão de CO2": grafico_ranking_co2("dados/co2.csv"),
                          "Coeficiente de Gini": grafico_mapa_Gini("dados/gini_2100.csv"),
                          "Índice de Desenvolvimento Humano": grafico_mapa_IDH("dados/hdi_human_development_index.csv"),
                          "PIB por ano": ranking_animado_PIB("dados/gdp_total_yearly_growth.csv"),
                          "Comparação de anos escolares homens e mulheres": educacao_por_genero("dados/anos_homens_na_escola.csv", "dados/anos_mulheres_na_escola.csv")}
