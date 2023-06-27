from reorganizador import reorganiza
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title  

df_vacina = reorganiza("dados/dtp3_immunized_percent_of_one_year_olds.csv", "Porcentagem de Vacinação", 1990, 2010)
df_mortes = reorganiza("dados/child_mortality_0_5_year_olds_dying_per_1000_born.csv", "Mortes a cada 1000 nascimentos", 1990, 2010)
df_vacina["Mortes a cada 1000 nascimentos"] = df_mortes["Mortes a cada 1000 nascimentos"]

output_file("scatter_plot.html")

titulo = Title(text="Vacinação e Mortalidade Infantil", align="center", text_font_size = "20pt")
scatter_plot = figure(title=titulo, x_axis_label="Mortes a cada 1000 nascimentos", y_axis_label="Porcentagem de crianças vacinadas")
scatter_plot.scatter(df_vacina["Mortes a cada 1000 nascimentos"], df_vacina["Porcentagem de Vacinação"], size=5, alpha = 0.5, color="red")
scatter_plot.xaxis.axis_label_text_font_size = "16pt"  
scatter_plot.yaxis.axis_label_text_font_size = "16pt"

show(scatter_plot)


















