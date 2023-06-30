from bokeh.models import Div

"""
Arquivo que tem como objetivo armazenar as descrições de cada gráfico feita por seu respectivo autor.
"""

DESCRICAO_BARRAS_CARBONO = Div(text="""Esse Ranking busca ordenar os países de acordo com a emissão de carbono realizada <br>
                                 por cada um deles. As barras do gráfico foram colocadas de maneira vertical para que <br>
                                 itens com barras mais longas ou mais altas sejam visualmente distintos dos itens com <br>
                                 barras mais curtas ou mais baixas, facilitando a identificação dos melhores ou piores <br>
                                 classificados e também contribuindo para a compreensão das diferenças entre os países. <br>
                                 Além disso, é válido ressaltar que algumas das barras foram destacadas com cor, sendo <br>
                                 a cor azul utilizada para representar os melhores e a cor vermelha para representar as <br>
                                 piores nações no quesito de IDH (Índice de Desenvolvimento Humano). Outro ponto a ser <br>
                                 destacado é a utilização de ferramentas interativas por meio da função HoverTool, que <br>
                                 permite a visualização dos dados de cada barra, incluindo informações sobre o país e <br>
                                 o valor do investimento realizado. O título foi colocado no centro para alinhar-se com <br>
                                as informações do gráfico. Os nomes dos países foram rotacionados para facilitar a <br>
                                leitura. Quanto aos rótulos, foram padronizados com base no módulo de variáveis globais.""")

DESCRICAO_BARRAS_PIB = Div(text="""Esse gráfico tem como objetivo representar a média do PIB dos integrantes do G20 do período de 1990 à 2010. <br>
                                    Assim como em todos os gráficos, chamamos atenção para os Estados Unidos, Austrália, China e Índia. <br> 
                                    Vemos que na questão econômica, a ordem se inverte e que não traduz a mesma ideia quando olhamos para o IDH. <br>
                                    A China, com um PID muitas vezes maior do que o da Austrália, não consegue transformar isso em melhoras significativas <br>
                                    para o bem estar do cidadão. Vamos ver no gráfico seguinte que isso pode ser explicado. Quantos as cores, elas foram <br>
                                    as mesmas utilizadas em todos os outros gráficos, o azul para representar os países com alto IDH e o vermelho os com <br>
                                    IDH baixo. Destaco, por fim, que utilizamos apenas a ferramenta Hover, uma vez que, no gráfico de barras, <br>
                                    não faz sentido ferramentas como a Pan, Box_Zoom e outras.""")

DESCRICAO_BOLHAS_CALORIAS = Div(text="""O gráfico de Bolhas tem como objetivo comparar se há uma correlação entre a quantidade <br>
                                    média de calorias disponíveis e o Índice de Massa Corporal (IMC) das pessoas. Além disso, <br>
                                    o tamanho das bolhas foi utilizado para representar o tamanho da população, a fim de <br>
                                    verificar se isso influencia nos resultados do gráfico. Também foram definidos limites <br>
                                    para exibir as bolhas em uma área central do gráfico. As cores foram usadas para destacar <br>
                                    os países com bom desempenho (cor azul) e os países sem destaque (cor vermelha) na área de <br>
                                    IDH (Índice de Desenvolvimento Humano). As grades de fundo foram removidas, pois não eram <br>
                                    relevantes para o contexto do gráfico. Através da ferramenta HoverTool, é possível visualizar <br>
                                    o país, o IMC médio e a média de calorias disponíveis ao passar o mouse sobre as bolhas. <br>
                                    Conforme mencionado anteriormente, os rótulos foram padronizados com base no módulo variaveis_globais.
                                """)

DESCRICAO_BOXPLOT_EXP_VIDA = Div(text="""Esse gráfico tem como objetivo apresentar a distribuição dentre os dados de expectativa de vida <br>
                                    de cada integrante do G20 de 1950 à 2020. O destaque permanece para os mesmos países, Estados Unidos, <br>
                                    Austrália, China e Índia, donos dos melhores e piores IDH's do G20, respectivamente. Podemos observar que <br>
                                    conseguimos visualizar algo uma tendência coerente com o IDH. Vemos que EUA e Austrália possuíram uma espectativa <br>
                                    de vida maiores que China e Índia. Porém a China, mesmo com o IDH baixo, não possuí uma das menores expectativas de vida <br>
                                    algo que pode ser explicado por diversos fatores. Alguns expecialistas, por exemplo, atribuem a longevidade de alguns povos <br>
                                    asiáticos à alimentação e à cultura muito específica. Novamente, pontuo que escolhemos não disponibilizar <br>
                                    todas as ferramentas, mas apenas o Hover. Não seria coerente permitir ao usuário se mover por todo <br>
                                    o espaço disponível, sendo que todos os dados estão agrupados nessa janela de visualização.""")

DESCRICAO_LINHAS_ANOS_ESCOLA = Div(text="""Neste gráfico de Linhas, é relacionada a média de anos de presença na escola ao <br>
                                    longo dos anos, em que cada linha representa um país. A visualização tem o objetivo <br>
                                    de identificar melhorias na frequência dos alunos nas escolas e detectar tendências <br>
                                    futuras com base nos padrões observados. Além disso, foram utilizadas cores para destacar <br>
                                    alguns países, sendo a cor azul para os melhores desempenhos e a cor vermelha para os <br>
                                    piores desempenhos no quesito de IDH (Índice de Desenvolvimento Humano). Por meio do <br>
                                    módulo HoverTool, foi criada uma ferramenta de interatividade que, ao passar o cursor <br>
                                    do mouse sobre cada linha, exibe o país, o ano correspondente e a média de anos na escola <br>
                                    para aquele período. O título foi posicionado no centro para alinhar-se com as informações <br>
                                    do gráfico. Por fim, vários rótulos foram padronizados em todos os gráficos usando o <br>
                                    módulo variaveis_globais, proporcionando uma estética consistente para cada representação.""")

DESCRICAO_LINHA_PIB_PC = Div(text="""Esse gráfico, embora esteja relacionado com o anterior, tem como objetivo representar a evolução <br>
                                    do PIB per capita dos países. Olhando para os destaques, vemos claramente uma tendência. Os países <br>
                                    com maior IDH possuem um dos maiores PIB's per capita e China e Índia vão na contramão disso. <br>
                                    Como foi antecipado na descrição anterior, mesmo que a China nos últimos anos tenha um dos maiores <br>
                                    PIB's brutos do planeta, sua população é gigantesca e toda essa riqueza produzida quando é normalizada <br>
                                    pela população retorna um valor bem abaixo do esperado. O mesmo acontece para a Índia. Ambas com populações <br>
                                    acima do 1 bilhão de habitantes. Destaco também, por mais que não seja um dos países destacados, a Arábia Saudita <br>
                                    na década de 1970 até meados da década de 1980 teve um aumento gritante no seu PIB per capita e isso tem uma <br>
                                    explicação história simples: A Primeira Crise do Petróleo. Quando os países membros da OPEP, Organização dos Países <br>
                                    Exportadores de Petróleo, resolveu aumentar muito o valor do combustível fóssil, que é a principal alavanca da <br>
                                    economia saudita há muito tempo, e isso aumentou muito a arrecadação do país e o seu PIB per capita, uma vez que a <br>
                                    população não cresceu no mesmo rítimo. Por fim, destaco que nesse gráfico a maioria das ferramentas foram adicionadas, <br>
                                    mas só é possível utilizá-las dentro dos limites da janela de visualização dos dados. 
    """)