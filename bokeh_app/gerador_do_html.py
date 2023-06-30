#import dict_graficos
from jinja2 import Template
from bokeh.io import output_file, save, show
from bokeh.plotting import column, figure
from bokeh.models import Div

#dicionario = dict_graficos.dicionario_de_graficos

template = Template(
    '''
    <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>plot</title>
    <style>
    .wrapper {
        width: 800px;
        background-color: yellow;
        margin: 0 auto;
        }

    .plotdiv {
        margin: 0 auto;
        }
    </style>
    </head>
    <body>
    <div class='wrapper'>
        {{ div }}
    </div>
    </body>
    </html>
    '''
)

template = """
{% block postamble %}
<style>
.bk-root .bk {
    margin: 0 auto !important;
}
</style>
{% endblock %}
"""

output_file("../index.html")

fig = figure(width = 500, height = 500)
div = Div(text="aaaA")

show(column(fig, div), template) 

'''
coisa_pra_mostrar = tuple([column(*each_plot) for each_plot in dicionario.values()])
print(coisa_pra_mostrar)

show(column(*coisa_pra_mostrar))    
'''