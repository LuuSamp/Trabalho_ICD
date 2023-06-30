import dict_graficos
from bokeh.io import output_file, save, show
from bokeh.plotting import column, figure
from bokeh.models import Div

dicionario = dict_graficos.dicionario_de_graficos

output_file("../index.html")

fig = figure(width = 500, height = 500)
div = Div(text="aaaA")

coisa_pra_mostrar = tuple([column(*each_plot) for each_plot in dicionario.values()])
print(coisa_pra_mostrar)

show(*coisa_pra_mostrar)