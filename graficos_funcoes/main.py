from bokeh.plotting import figure, column, row
from bokeh.models import Button, Select, Paragraph
from bokeh.io import curdoc
from __init__ import dicionario_de_graficos

selected_plot = 0
plot, paragraph = list(dicionario_de_graficos.values())[selected_plot]

select = Select(title = "Gráfico:", value = list(dicionario_de_graficos.keys())[selected_plot], options = list(dicionario_de_graficos.keys()))
previous_button = Button(label = "Previous")
next_button = Button(label = "Next")

plot_layout = column(paragraph, plot, name = "plot_layout")
control_layout = row(previous_button, select, next_button, name = "control_layout")
full_layout = column(plot_layout, control_layout, name = "main_layout")

def change_plot(attr, old, new):
    global paragraph, plot, selected_plot
    plot, paragraph = dicionario_de_graficos[select.value]
    selected_plot = list(dicionario_de_graficos.keys()).index(select.value)
    plot_layout = curdoc().get_model_by_name("plot_layout")
    plot_layout.children.pop(0)
    plot_layout.children.pop(0)
    plot_layout.children.append(paragraph)
    plot_layout.children.append(plot)

select.on_change("value", change_plot)

def previous_button_action():
    '''
    Função que é executada quando o botão "previous" é clicado. Seleciona o gráfico anterior.
    '''
    global selected_plot
    selected_plot -= 1
    if selected_plot < 0:
        selected_plot = len(list(dicionario_de_graficos.keys())) - 1
    select.value = list(dicionario_de_graficos.keys())[selected_plot]

previous_button.on_click(previous_button_action)

def next_button_action():
    '''
    Função que é executada quando o botão "next" é clicado. Seleciona o gráfico seguinte.
    '''
    global selected_plot
    selected_plot += 1
    if selected_plot >= len(list(dicionario_de_graficos.keys())):
        selected_plot = 0
    select.value = list(dicionario_de_graficos.keys())[selected_plot]

next_button.on_click(next_button_action)

curdoc().add_root(full_layout)