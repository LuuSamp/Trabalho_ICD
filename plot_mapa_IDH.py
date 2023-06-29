# Importações necessárias:
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
import geopandas as gpd
from reorganizador import reorganiza
from traducao_g20 import filtro_paises_do_g20
import pandas as pd
from bokeh.palettes import Reds
from bokeh.models import LinearColorMapper, ColorBar, Range1d
from bokeh.models import HoverTool, Paragraph
from variaveis_globais import *

def grafico_mapa_IDH(datapath_IDH):

    '''
    Essa função deve receber um DataFrame dos IDHs dos países. Ela tem o objetivo de criar um mapa 
    mundial que destaca os países do G20 com um gradiente de cor, mostrando através da tonalidade 
    da cor os países que possuem os maiores e os menores Índices de Desenvolvimento Humano.
    '''
    
    # Dicionário pego do site country.io:
    dicionario_iso2 = {"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria", "BA": "Bosnia and Herzegovina", 
    "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Barthelemy", "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", 
    "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", 
    "WS": "Samoa", "BQ": "Bonaire, Saint Eustatius and Saba ", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey", "BY": "Belarus", 
    "BZ": "Belize", "RU": "Russia", "RW": "Rwanda", "RS": "Serbia", "TL": "East Timor", "RE": "Reunion", "TM": "Turkmenistan", 
    "TJ": "Tajikistan", "RO": "Romania", "TK": "Tokelau", "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala", 
    "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea", "GP": "Guadeloupe", 
    "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana", "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", 
    "GA": "Gabon", "SV": "El Salvador", "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", 
    "OM": "Oman", "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong", 
    "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico", "PS": "Palestinian Territory", 
    "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen", "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", 
    "PF": "French Polynesia", "PG": "Papua New Guinea", "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", 
    "PL": "Poland", "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "EE": "Estonia", "EG": "Egypt", 
    "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam", "SB": "Solomon Islands", "ET": "Ethiopia", "SO": 
    "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia", "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova", 
    "MG": "Madagascar", "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar", "ML": "Mali", 
    "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia", "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", 
    "MV": "Maldives", "MQ": "Martinique", "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man", 
    "UG": "Uganda", "TZ": "Tanzania", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France", "IO": "British Indian Ocean Territory", 
    "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji", "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", 
    "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia", "NE": "Niger", 
    "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", 
    "XK": "Kosovo", "CI": "Ivory Coast", "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile", 
    "CC": "Cocos Islands", "CA": "Canada", "CG": "Republic of the Congo", "CF": "Central African Republic", "CD": "Democratic Republic of the Congo", 
    "CZ": "Czech Republic", "CY": "Cyprus", "CX": "Christmas Island", "CR": "Costa Rica", "CW": "Curacao", "CV": "Cape Verde", "CU": "Cuba", 
    "SZ": "Swaziland", "SY": "Syria", "SX": "Sint Maarten", "KG": "Kyrgyzstan", "KE": "Kenya", "SS": "South Sudan", "SR": "Suriname", 
    "KI": "Kiribati", "KH": "Cambodia", "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia", 
    "KR": "South Korea", "SI": "Slovenia", "KP": "North Korea", "KW": "Kuwait", "SN": "Senegal", "SM": "San Marino", "SL": "Sierra Leone", 
    "SC": "Seychelles", "KZ": "Kazakhstan", "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic", 
    "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "British Virgin Islands", "DE": "Germany", "YE": "Yemen", "DZ": "Algeria", 
    "US": "United States", "UY": "Uruguay", "YT": "Mayotte", "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", 
    "LA": "Laos", "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka", "LI": "Liechtenstein", 
    "LV": "Latvia", "TO": "Tonga", "LT": "Lithuania", "LU": "Luxembourg", "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", 
    "TF": "French Southern Territories", "TG": "Togo", "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libya", "VA": "Vatican", 
    "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra", "AG": "Antigua and Barbuda", 
    "AF": "Afghanistan", "AI": "Anguilla", "VI": "U.S. Virgin Islands", "IS": "Iceland", "IR": "Iran", "AM": "Armenia", "AL": "Albania", 
    "AO": "Angola", "AQ": "Antarctica", "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba", 
    "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia", "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}

    # Dicionário pego do site country.io:
    dicionario_iso3 = {"BD": "BGD", "BE": "BEL", "BF": "BFA", "BG": "BGR", "BA": "BIH", "BB": "BRB", "WF": "WLF", "BL": "BLM", "BM": "BMU", "BN": "BRN", "BO": "BOL", 
    "BH": "BHR", "BI": "BDI", "BJ": "BEN", "BT": "BTN", "JM": "JAM", "BV": "BVT", "BW": "BWA", "WS": "WSM", "BQ": "BES", "BR": "BRA", "BS": "BHS", 
    "JE": "JEY", "BY": "BLR", "BZ": "BLZ", "RU": "RUS", "RW": "RWA", "RS": "SRB", "TL": "TLS", "RE": "REU", "TM": "TKM", "TJ": "TJK", "RO": "ROU", 
    "TK": "TKL", "GW": "GNB", "GU": "GUM", "GT": "GTM", "GS": "SGS", "GR": "GRC", "GQ": "GNQ", "GP": "GLP", "JP": "JPN", "GY": "GUY", "GG": "GGY", 
    "GF": "GUF", "GE": "GEO", "GD": "GRD", "GB": "GBR", "GA": "GAB", "SV": "SLV", "GN": "GIN", "GM": "GMB", "GL": "GRL", "GI": "GIB", "GH": "GHA", 
    "OM": "OMN", "TN": "TUN", "JO": "JOR", "HR": "HRV", "HT": "HTI", "HU": "HUN", "HK": "HKG", "HN": "HND", "HM": "HMD", "VE": "VEN", "PR": "PRI", 
    "PS": "PSE", "PW": "PLW", "PT": "PRT", "SJ": "SJM", "PY": "PRY", "IQ": "IRQ", "PA": "PAN", "PF": "PYF", "PG": "PNG", "PE": "PER", "PK": "PAK", 
    "PH": "PHL", "PN": "PCN", "PL": "POL", "PM": "SPM", "ZM": "ZMB", "EH": "ESH", "EE": "EST", "EG": "EGY", "ZA": "ZAF", "EC": "ECU", "IT": "ITA", 
    "VN": "VNM", "SB": "SLB", "ET": "ETH", "SO": "SOM", "ZW": "ZWE", "SA": "SAU", "ES": "ESP", "ER": "ERI", "ME": "MNE", "MD": "MDA", "MG": "MDG", 
    "MF": "MAF", "MA": "MAR", "MC": "MCO", "UZ": "UZB", "MM": "MMR", "ML": "MLI", "MO": "MAC", "MN": "MNG", "MH": "MHL", "MK": "MKD", "MU": "MUS", 
    "MT": "MLT", "MW": "MWI", "MV": "MDV", "MQ": "MTQ", "MP": "MNP", "MS": "MSR", "MR": "MRT", "IM": "IMN", "UG": "UGA", "TZ": "TZA", "MY": "MYS", 
    "MX": "MEX", "IL": "ISR", "FR": "FRA", "IO": "IOT", "SH": "SHN", "FI": "FIN", "FJ": "FJI", "FK": "FLK", "FM": "FSM", "FO": "FRO", "NI": "NIC", 
    "NL": "NLD", "NO": "NOR", "NA": "NAM", "VU": "VUT", "NC": "NCL", "NE": "NER", "NF": "NFK", "NG": "NGA", "NZ": "NZL", "NP": "NPL", "NR": "NRU", 
    "NU": "NIU", "CK": "COK", "XK": "XKX", "CI": "CIV", "CH": "CHE", "CO": "COL", "CN": "CHN", "CM": "CMR", "CL": "CHL", "CC": "CCK", "CA": "CAN", 
    "CG": "COG", "CF": "CAF", "CD": "COD", "CZ": "CZE", "CY": "CYP", "CX": "CXR", "CR": "CRI", "CW": "CUW", "CV": "CPV", "CU": "CUB", "SZ": "SWZ", 
    "SY": "SYR", "SX": "SXM", "KG": "KGZ", "KE": "KEN", "SS": "SSD", "SR": "SUR", "KI": "KIR", "KH": "KHM", "KN": "KNA", "KM": "COM", "ST": "STP", 
    "SK": "SVK", "KR": "KOR", "SI": "SVN", "KP": "PRK", "KW": "KWT", "SN": "SEN", "SM": "SMR", "SL": "SLE", "SC": "SYC", "KZ": "KAZ", "KY": "CYM", 
    "SG": "SGP", "SE": "SWE", "SD": "SDN", "DO": "DOM", "DM": "DMA", "DJ": "DJI", "DK": "DNK", "VG": "VGB", "DE": "DEU", "YE": "YEM", "DZ": "DZA", 
    "US": "USA", "UY": "URY", "YT": "MYT", "UM": "UMI", "LB": "LBN", "LC": "LCA", "LA": "LAO", "TV": "TUV", "TW": "TWN", "TT": "TTO", "TR": "TUR", 
    "LK": "LKA", "LI": "LIE", "LV": "LVA", "TO": "TON", "LT": "LTU", "LU": "LUX", "LR": "LBR", "LS": "LSO", "TH": "THA", "TF": "ATF", "TG": "TGO", 
    "TD": "TCD", "TC": "TCA", "LY": "LBY", "VA": "VAT", "VC": "VCT", "AE": "ARE", "AD": "AND", "AG": "ATG", "AF": "AFG", "AI": "AIA", "VI": "VIR", 
    "IS": "ISL", "IR": "IRN", "AM": "ARM", "AL": "ALB", "AO": "AGO", "AQ": "ATA", "AS": "ASM", "AR": "ARG", "AU": "AUS", "AT": "AUT", "AW": "ABW", 
    "IN": "IND", "AX": "ALA", "AZ": "AZE", "IE": "IRL", "ID": "IDN", "UA": "UKR", "QA": "QAT", "MZ": "MOZ"}

    # Função que converte o nome do país para iso2:
    def converte_iso2(pais):
        for chave, valor in dicionario_iso2.items():
            if valor == pais:
                return chave
            else: 
                pass

    #Função que converte o iso2 para iso3:
    def converte_iso3(pais_iso2):
        for chave, valor in dicionario_iso3.items():
            if chave == pais_iso2:
                return valor
            else:
                pass

    # Criação de Data Frames "tratados" a partir da utilização da função "reorganiza":
    df_IDH = reorganiza(datapath_IDH, "IDH", 1990, 2010)

    # Utilizando a função  "filtro_paises_do_g20" para filtrar apenas os países do g20:
    df_IDH_g20 = filtro_paises_do_g20(df_IDH, False, agrupamento="country")
    df_IDH_g20 = df_IDH_g20.sort_values("IDH", ascending=False)

    # Criando um novo DataFrame com a média de IDH para cada país:
    df_IDH_g20_media = df_IDH_g20.groupby('country')['IDH'].mean().to_frame().reset_index()

    # Adicionando uma coluna iso3 no DataFrame:
    coluna_iso2 = df_IDH_g20_media["country"].apply(converte_iso2)
    coluna_iso3 = coluna_iso2.apply(converte_iso3)
    df_IDH_g20_media["iso_a3"] = coluna_iso3

    # Carregando os dados dos países usando geopandas:
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Criando Data Frame para colorir os países do g20:
    world1 = pd.merge(
        left = world,
        right = df_IDH_g20_media.filter(items=['IDH','iso_a3']), 
        on='iso_a3'
    )

    # Criando os objetos GeoJSONDataSource:
    dados_geograficos = GeoJSONDataSource(geojson=world.to_json())
    dados_geograficos_g20 = GeoJSONDataSource(geojson=world1.to_json())

    # Definindo paleta de cores:
    palette = Reds[6]
    palette = palette[::-1]

    # Fazendo cortes lineares na escala para para aplicar paleta:
    color_mapper = LinearColorMapper(
        palette = palette, 
        low = df_IDH_g20_media['IDH'].min(), 
        high = df_IDH_g20_media['IDH'].max(), 
        nan_color = '#d9d9d9')

    # Ajustando ferramenta para popup com mouse:
    hover = HoverTool(
        tooltips = [ ('País','@name'),
                    ('IDH','@IDH')
        ])

    # Criando barras de cores:
    color_bar = ColorBar(
        color_mapper=color_mapper, 
        label_standoff=6,
        width = 500, 
        height = 20,
        border_line_color=None,
        location = (0,0), 
        orientation = 'horizontal', 
    )

    # Configurando a figura e adicionando o gráfico:
    mapa_IDH = figure(title="IDH do G20", 
                    width = LARGURA, 
                    height = ALTURA, 
                    x_range = Range1d(-180, 180, bounds="auto"), 
                    y_range = Range1d(-90, 90, bounds="auto"),
                    tools="pan,reset,wheel_zoom,box_zoom")

    # Adicionando barra com grade de cor: 
    mapa_IDH.add_layout(color_bar, 'below')

    mapa_IDH.toolbar.logo = None 
    mapa_IDH.toolbar.autohide = True 
    mapa_IDH.toolbar_location = POSICAO_BARRA_FERRAMENTAS

    mapa_IDH.patches('xs', 'ys', 
                    fill_alpha=0.7, 
                    line_color='black', 
                    line_width=1,
                    source=dados_geograficos, 
                    fill_color = "grey")

    paises_g20 = mapa_IDH.patches('xs', 'ys', source=dados_geograficos_g20, 
                    fill_color = {'field' :'IDH', 'transform':color_mapper}, 
                    line_color = 'grey', line_width = 0.25, fill_alpha = 1)

    # Adicionando hover:
    hover.renderers = [paises_g20]
    mapa_IDH.add_tools(hover)

    # Configurações estéticas:
    mapa_IDH.xaxis[0].ticker.desired_num_ticks = 20
    mapa_IDH.yaxis[0].ticker.desired_num_ticks = NUM_MAJOR_TICKS_Y
    mapa_IDH.yaxis[0].ticker.num_minor_ticks = NUM_MINOR_TICKS

    mapa_IDH.title.text_font = FONTE_TEXTO
    mapa_IDH.title.text_font_size =TAMANHO_TITULO
    mapa_IDH.title.align = ALINHAMENTO_TITULO
    mapa_IDH.title.text_baseline = BASELINE_TITULO

    descricao = Paragraph(text="""
                                    Este gráfico do Mapa Mundial tem o objetivo de destacar os países do G20 em relação aos<br> 
                                    seus níveis de Índice de Desenvolvimento Humano (IDH). Utilizando uma paleta de cores<br> 
                                    com tons de vermelho, os países são categorizados em diferentes gradientes, revelando<br> 
                                    os países com IDH mais baixos em tons mais claros e os países com IDH mais altos em tons<br>
                                    mais escuros. Observando o mapa, podemos notar que a Austrália possui o maior IDH, seguida<br> 
                                    pelos Estados Unidos com o segundo maior IDH. Por outro lado, a Índia é o país com o menor<br> 
                                    IDH, seguida pela China, que possui o segundo menor IDH no mundo.<br>

                                    É importante ressaltar que toda a análise deste trabalho se baseia na comparação entre os<br> 
                                    dois países com os maiores IDHs, Austrália e EUA, e os dois países com os menores IDHs, Índia<br> 
                                    e China. Portanto, essa visualização é fundamental para compreender todas as próximas análises<br> 
                                    e interpretações.  
                                    """)
    return mapa_IDH
