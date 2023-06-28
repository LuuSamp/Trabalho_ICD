from bokeh.models import ColumnDataSource

def transformador_CDS(dataframe):
    '''
    Função que recebe um dataframe, geralmente feito com pandas,
    mas não necessariamente, 
    e retorna um objeto CDS.
    '''
    datasource = ColumnDataSource(dataframe)
    return datasource