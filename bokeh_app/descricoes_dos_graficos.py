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
                                leitura. Quanto aos rótulos, foram padronizados com base no módulo de variáveis globais.
                                """,
                                align = "center", width = 1080)

DESCRICAO_BARRAS_PIB = Div(text="""Esse gráfico tem como objetivo representar a média do PIB dos integrantes do G20 do período de 1990 à 2010. <br>
                                    Assim como em todos os gráficos, chamamos atenção para os Estados Unidos, Austrália, China e Índia. <br> 
                                    Vemos que na questão econômica, a ordem se inverte e que não traduz a mesma ideia quando olhamos para o IDH. <br>
                                    A China, com um PID muitas vezes maior do que o da Austrália, não consegue transformar isso em melhoras significativas <br>
                                    para o bem estar do cidadão. Vamos ver no gráfico seguinte que isso pode ser explicado. Quantos as cores, elas foram <br>
                                    as mesmas utilizadas em todos os outros gráficos, o azul para representar os países com alto IDH e o vermelho os com <br>
                                    IDH baixo. Destaco, por fim, que utilizamos apenas a ferramenta Hover, uma vez que, no gráfico de barras, <br>
                                    não faz sentido ferramentas como a Pan, Box_Zoom e outras.
                                    """,
                                    align = "center", width = 1080)

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
                                """,
                                align = "center", width = 1080)

DESCRICAO_BOXPLOT_EXP_VIDA = Div(text="""Esse gráfico tem como objetivo apresentar a distribuição dentre os dados de expectativa de vida <br>
                                    de cada integrante do G20 de 1950 à 2020. O destaque permanece para os mesmos países, Estados Unidos, <br>
                                    Austrália, China e Índia, donos dos melhores e piores IDH's do G20, respectivamente. Podemos observar que <br>
                                    conseguimos visualizar algo uma tendência coerente com o IDH. Vemos que EUA e Austrália possuíram uma espectativa <br>
                                    de vida maiores que China e Índia. Porém a China, mesmo com o IDH baixo, não possuí uma das menores expectativas de vida <br>
                                    algo que pode ser explicado por diversos fatores. Alguns expecialistas, por exemplo, atribuem a longevidade de alguns povos <br>
                                    asiáticos à alimentação e à cultura muito específica. Novamente, pontuo que escolhemos não disponibilizar <br>
                                    todas as ferramentas, mas apenas o Hover. Não seria coerente permitir ao usuário se mover por todo <br>
                                    o espaço disponível, sendo que todos os dados estão agrupados nessa janela de visualização.
                                    """,
                                    align = "center", width = 1080)

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
                                    módulo variaveis_globais, proporcionando uma estética consistente para cada representação.
                                    """,
                                    align = "center", width = 1080)

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
                                    """,
                                    align = "center", width = 1080)

DESCRICAO_MAPA_GINI = Div(text="""
                                    Este outro gráfico do Mapa Mundial tem o objetivo de destacar os países do G20 em relação aos<br> 
                                    seus níveis de Coeficiente de Gini, que medem a desigualdade econômica de um país.<br> 
                                    Utilizando uma paleta de cores com tons de vermelho, os países são categorizados em diferentes<br> 
                                    gradientes, revelando os países com Gini mais baixos em tons mais claros e os países com<br> 
                                    Gini mais altos em tons mais escuros. Observando o mapa, podemos notar que a Austrália detentora<br> 
                                    do maior IDH, tem um índice de Gini bem baixo, ou seja, ela possui um baixo nível de desigualdade.<br> 
                                    Já os EUA que contém o segundo maior IDH, possui um Gini maior, o que o torna um país com um nível<br> 
                                    alto de desigualdade econômica. Por outro lado, a Índia que tem o pior IDH possui um índice de Gini menor<br> 
                                    que o da Austrália, tornando-a um país com menos desigualadade, o que não quer dizer algo positivo, já<br> 
                                    que a grande maioria da sociedade indiana está na pobreza. Enquanto isso, a China que possui o segundo<br> 
                                    menor IDH, possui um dos maiores níveis de Gini, rivalizando na questão de desigualdade social com Brasil.<br>  
                                    """,
                                    align = "center", width = 1080)

DESCRICAO_MAPA_IDH = Div(text="""
                                    Este gráfico do Mapa Mundial tem o objetivo de destacar os países do G20 em relação aos<br> 
                                    seus níveis de Índice de Desenvolvimento Humano(IDH). Utilizando uma paleta de cores<br> 
                                    com tons de vermelho, os países são categorizados em diferentes gradientes, revelando<br> 
                                    os países com IDH mais baixos em tons mais claros e os países com IDH mais altos em tons<br>
                                    mais escuros. Observando o mapa, podemos notar que a Austrália possui o maior IDH, seguida<br> 
                                    pelos Estados Unidos com o segundo maior IDH. Por outro lado, a Índia é o país com o menor<br> 
                                    IDH, seguida pela China, que possui o segundo menor IDH no mundo.<br>

                                    É importante ressaltar que toda a análise deste trabalho se baseia na comparação entre os<br> 
                                    dois países com os maiores IDH's e os dois países com os menores IDH's, sendo a Austrália o maior,<br> 
                                    os EUA o segundo maior, a Índia o menor e a China o segundo menor. Portanto, essa visualização é<br> 
                                    fundamental para compreender todas as próximas análises e interpretações do trabalho.
                                    dois países com os maiores IDHs, Austrália e EUA, e os dois países com os menores IDHs, Índia<br> 
                                    e China. Portanto, essa visualização é fundamental para compreender todas as próximas análises<br> 
                                    e interpretações.  
                                    """,
                                    align = "center", width = 1080)

DESCRICAO_BARRAS_ANIMADO_PIB = Div(text="""<p> Este gráfico tem como principal objetivo mostrar a mudança do PIB nos países do g20 a cada ano. O PIB é mostrado em bilhões.</p>
                                        <p> É possível notar o incrível avanço do PIB dos Estados Unidos e, mais recente, o avanço da China. </p>""",
                                   align = "center", width = 1080)

DESCRICAO_PROPORCAO_HOMENS_MULHERES = Div(text="""<p> Este gráfico tem como principal objetivo comparar a média de anos que mulheres e homens ficam na escola.</p>
                                        <p> É possível notar que, em vários países do g20, a média dos anos escolares das mulheres ultrapassou a média dos anos dos homens. </p>""",
                                   align = "center", width = 1080
                                   )

DESCRICAO_BARRAS_SAUDE = Div(text="""
                                  Esse ranking procura mostrar os países do G20 que mais investem na área da saúde no período dos<br> 
                                  anos de 1995 a 2010. Além disso, foram destacados quatro países que tiveram os dois maiores e<br> 
                                  os dois menores Índices de Desenvolvimento Humano. Os países com cores de tons vermelhos são a<br> 
                                  Índia e a China que representam os países com os menores IDHs, enquanto os países com cores de<br> 
                                  tons azuis são a Austrália e os Estados Unidos que representam os países com os maiores IDHs.<br> 
                                  Pode-se perceber que, em relação ao gráfico, a Índia, que possui um IDH muito baixo também possui 
                                  uma média de investimentos muito baixa em saúde, sendo ela o país com a pior média do G20. Já<br>
                                  a China que possui o segundo menor IDH, possui um investimento mediano com relação aos outros<br>
                                  países. Por outro lado, os EUA que possui o segundo maior IDH é o país com o maior investimento<br>
                                  em saúde, enquanto a Austrália que possui o maior IDH está em sexto lugar no ranking de investimentos. 
                                    """)
