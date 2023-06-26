from reorganizador import reorganiza

df_vacina = reorganiza("dados/dtp3_immunized_percent_of_one_year_olds.csv", "Porcentagem de Vacinação", 1990, 2010)

df_mortes = reorganiza("dados/child_mortality_0_5_year_olds_dying_per_1000_born.csv", "Mortes a cada 1000 nascimentos", 1990, 2010)
















'''
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.plotting import figure, output_file, show
import pandas as pd

data = pd.read_csv('C:\\Users\\b51988\\Desktop\\bokeh\\GDPpercapita_reorganized.csv')

output_file("scatter_plot.html")

scatter_plot = figure(title='Gráfico de Dispersão', x_axis_label='X', y_axis_label='Y')

scatter_plot.scatter(data['GDP per capita'], data['year'], size=10, color='blue')

show(scatter_plot)
'''


