import dict_graficos
from bokeh.io import output_file, save, show
from bokeh.plotting import column, figure
from bokeh.models import Div

dicionario = dict_graficos.dicionario_de_graficos

for nome, elementos in dicionario.items():
    output_file(f"html/{nome}.html")
    save(elementos)


'''
coisa_pra_mostrar = tuple([column(*each_plot) for each_plot in dicionario.values()])
print(coisa_pra_mostrar)

show(column(*coisa_pra_mostrar))    
'''