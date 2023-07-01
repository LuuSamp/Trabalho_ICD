from bokeh.models import Div

"""
Arquivo que tem como objetivo armazenar as descrições de cada gráfico feita por seu respectivo autor.
"""

DESCRICAO_BARRAS_CARBONO = Div(text="""Esse Ranking busca ordenar os países de acordo com a emissão de carbono realizada 
                                 por cada um deles. As barras do gráfico foram colocadas de maneira vertical para que 
                                 itens com barras mais longas ou mais altas sejam visualmente distintos dos itens com 
                                 barras mais curtas ou mais baixas, facilitando a identificação dos melhores ou piores 
                                 classificados e também contribuindo para a compreensão das diferenças entre os países. 
                                 Além disso, é válido ressaltar que algumas das barras foram destacadas com cor, sendo 
                                 a cor azul utilizada para representar os melhores e a cor vermelha para representar as 
                                 piores nações no quesito de IDH (Índice de Desenvolvimento Humano). Outro ponto a ser 
                                 destacado é a utilização de ferramentas interativas por meio da função HoverTool, que 
                                 permite a visualização dos dados de cada barra, incluindo informações sobre o país e 
                                 o valor do investimento realizado. O título foi colocado no centro para alinhar-se com 
                                as informações do gráfico. Os nomes dos países foram rotacionados para facilitar a 
                                leitura. Quanto aos rótulos, foram padronizados com base no módulo de variáveis globais.
                                """)

DESCRICAO_BARRAS_PIB = Div(text="""Esse gráfico tem como objetivo representar a média do PIB dos integrantes do G20 do período de 1990 à 2010. 
                                    Assim como em todos os gráficos, chamamos atenção para os Estados Unidos, Austrália, China e Índia.  
                                    Vemos que na questão econômica, a ordem se inverte e que não traduz a mesma ideia quando olhamos para o IDH. 
                                    A China, com um PID muitas vezes maior do que o da Austrália, não consegue transformar isso em melhoras significativas 
                                    para o bem estar do cidadão. Quantos as cores, elas foram as mesmas utilizadas em todos os outros gráficos, 
                                    o azul para representar os países com alto IDH e o vermelho os com IDH baixo. Destaco, por fim, que utilizamos apenas
                                    a ferramenta Hover, uma vez que, no gráfico de barras, não faz sentido ferramentas como a Pan, Box_Zoom e outras.
                                    """)

DESCRICAO_BOLHAS_CALORIAS = Div(text="""O gráfico de Bolhas tem como objetivo comparar se há uma correlação entre a quantidade 
                                    média de calorias disponíveis e o Índice de Massa Corporal (IMC) das pessoas. Além disso, 
                                    o tamanho das bolhas foi utilizado para representar o tamanho da população, a fim de 
                                    verificar se isso influencia nos resultados do gráfico. Também foram definidos limites 
                                    para exibir as bolhas em uma área central do gráfico. As cores foram usadas para destacar 
                                    os países com bom desempenho (cor azul) e os países sem destaque (cor vermelha) na área de 
                                    IDH (Índice de Desenvolvimento Humano). As grades de fundo foram removidas, pois não eram 
                                    relevantes para o contexto do gráfico. Através da ferramenta HoverTool, é possível visualizar 
                                    o país, o IMC médio e a média de calorias disponíveis ao passar o mouse sobre as bolhas. Os rótulos 
                                    foram padronizados com base no módulo variaveis_globais.
                                """)

DESCRICAO_BOXPLOT_EXP_VIDA = Div(text="""Esse gráfico tem como objetivo apresentar a distribuição dentre os dados de expectativa de vida 
                                    de cada integrante do G20 de 1950 à 2020. O destaque permanece para os mesmos países, Estados Unidos, 
                                    Austrália, China e Índia, donos dos melhores e piores IDH's do G20, respectivamente. Podemos observar que 
                                    conseguimos visualizar alguma tendência coerente com o IDH. Vemos que EUA e Austrália possuíram uma espectativa 
                                    de vida maiores que China e Índia. Porém a China, mesmo com o IDH baixo, não possuí uma das menores expectativas de vida, 
                                    algo que pode ser explicado por diversos fatores. Alguns expecialistas, por exemplo, atribuem a longevidade de alguns povos 
                                    asiáticos à alimentação e à cultura muito específica. Pontuo que escolhemos não disponibilizar 
                                    todas as ferramentas, mas apenas o Hover. Não seria coerente permitir ao usuário se mover por todo 
                                    o espaço disponível, sendo que todos os dados estão agrupados nessa janela de visualização.
                                    """)

DESCRICAO_LINHAS_ANOS_ESCOLA = Div(text="""Neste gráfico de Linhas, é relacionada a média de anos de presença na escola ao 
                                    longo dos anos, em que cada linha representa um país. A visualização tem o objetivo 
                                    de identificar melhorias na frequência dos alunos nas escolas e detectar tendências 
                                    futuras com base nos padrões observados. Além disso, foram utilizadas cores para destacar 
                                    alguns países, sendo a cor azul para os melhores desempenhos e a cor vermelha para os 
                                    piores desempenhos no quesito de IDH (Índice de Desenvolvimento Humano). Por meio do 
                                    módulo HoverTool, foi criada uma ferramenta de interatividade que, ao passar o cursor 
                                    do mouse sobre cada linha, exibe o país, o ano correspondente e a média de anos na escola 
                                    para aquele período. O título foi posicionado no centro para alinhar-se com as informações 
                                    do gráfico. Por fim, vários rótulos foram padronizados em todos os gráficos usando o 
                                    módulo variaveis_globais, proporcionando uma estética consistente para cada representação.
                                    """)

DESCRICAO_LINHA_PIB_PC = Div(text="""Este gráfico tem como objetivo representar a evolução 
                                    do PIB per capita dos países. Olhando para os destaques, vemos claramente uma tendência. Os países 
                                    com maior IDH possuem um dos maiores PIB's per capita e China e Índia vão na contramão disso. 
                                    Mesmo que a China nos últimos anos tenha um dos maiores 
                                    PIB's brutos do planeta, sua população é gigantesca e toda essa riqueza produzida quando é normalizada 
                                    pela população retorna um valor bem abaixo do esperado. O mesmo acontece para a Índia. Ambas com populações 
                                    acima do 1 bilhão de habitantes. Destaco também, por mais que não seja um dos países destacados, a Arábia Saudita 
                                    na década de 1970 até meados da década de 1980 teve um aumento gritante no seu PIB per capita e isso tem uma 
                                    explicação história simples: A Primeira Crise do Petróleo. Quando os países membros da OPEP, Organização dos Países 
                                    Exportadores de Petróleo, resolveram aumentar muito o valor do combustível, que é a principal alavanca da 
                                    economia saudita há muito tempo, e isso aumentou muito a arrecadação do país e o seu PIB per capita, uma vez que a 
                                    população não cresceu no mesmo rítimo. Por fim, destaco que nesse gráfico a maioria das ferramentas foram adicionadas, 
                                    mas só é possível utilizá-las dentro dos limites da janela de visualização dos dados. 
                                    """)

DESCRICAO_MAPA_GINI = Div(text="""
                                    Este outro gráfico do Mapa Mundial tem o objetivo de destacar os países do G20 em relação aos 
                                    seus níveis de Coeficiente de Gini, que medem a desigualdade econômica de um país. 
                                    Utilizando uma paleta de cores com tons de vermelho, os países são categorizados em diferentes 
                                    gradientes, revelando os países com Gini mais baixos em tons mais claros e os países com 
                                    Gini mais altos em tons mais escuros. Observando o mapa, podemos notar que a Austrália detentora 
                                    do maior IDH, tem um índice de Gini bem baixo, ou seja, ela possui um baixo nível de desigualdade. 
                                    Já os EUA que contém o segundo maior IDH, possui um Gini maior, o que o torna um país com um nível 
                                    alto de desigualdade econômica. Por outro lado, a Índia que tem o pior IDH possui um índice de Gini menor 
                                    que o da Austrália, tornando-a um país com menos desigualadade, o que não quer dizer algo positivo, já 
                                    que a grande maioria da sociedade indiana está na pobreza. Enquanto isso, a China que possui o segundo 
                                    menor IDH, possui um dos maiores níveis de Gini, rivalizando na questão de desigualdade social com Brasil.  
                                    """)

DESCRICAO_MAPA_IDH = Div(text="""
                                    Este gráfico do Mapa Mundial tem o objetivo de destacar os países do G20 em relação aos 
                                    seus níveis de Índice de Desenvolvimento Humano(IDH). Utilizando uma paleta de cores 
                                    com tons de vermelho, os países são categorizados em diferentes gradientes, revelando 
                                    os países com IDH mais baixos em tons mais claros e os países com IDH mais altos em tons
                                    mais escuros. Observando o mapa, podemos notar que a Austrália possui o maior IDH, seguida 
                                    pelos Estados Unidos com o segundo maior IDH. Por outro lado, a Índia é o país com o menor 
                                    IDH, seguida pela China, que possui o segundo menor IDH o G20.

                                    É importante ressaltar que toda a análise deste trabalho se baseia na comparação entre os 
                                    dois países com os maiores IDH's e os dois países com os menores IDH's, sendo a Austrália o maior, 
                                    os EUA o segundo maior, a Índia o menor e a China o segundo menor. Portanto, essa visualização é 
                                    fundamental para compreender todas as próximas análises e interpretações do trabalho.  
                                    """)

DESCRICAO_BARRAS_ANIMADO_PIB = Div(text="""<p> Este gráfico tem como principal objetivo mostrar a mudança do PIB nos países do g20 a cada ano. O PIB é mostrado em bilhões.</p>
                                        <p> É possível notar o incrível avanço do PIB dos Estados Unidos e, mais recente, o avanço da China. </p>""")

DESCRICAO_PROPORCAO_HOMENS_MULHERES = Div(text="""<p> Este gráfico tem como principal objetivo comparar a média de anos que mulheres e homens ficam na escola.</p>
                                        <p> É possível notar que, em vários países do g20, a média dos anos escolares das mulheres ultrapassou a média dos anos dos homens. </p>"""
                                   )

DESCRICAO_BARRAS_SAUDE = Div(text="""
                                  Esse ranking procura mostrar os países do G20 que mais investem na área da saúde no período dos 
                                  anos de 1995 a 2010. Além disso, foram destacados quatro países que tiveram os dois maiores e 
                                  os dois menores Índices de Desenvolvimento Humano. Os países com cores de tons vermelhos são a 
                                  Índia e a China que representam os países com os menores IDHs, enquanto os países com cores de 
                                  tons azuis são a Austrália e os Estados Unidos que representam os países com os maiores IDHs. 
                                  Pode-se perceber que, em relação ao gráfico, a Índia, que possui um IDH muito baixo também possui 
                                  uma média de investimentos muito baixa em saúde, sendo ela o país com a pior média do G20. Já
                                  a China que possui o segundo menor IDH, possui um investimento mediano com relação aos outros
                                  países. Por outro lado, os EUA que possui o segundo maior IDH é o país com o maior investimento
                                  em saúde, enquanto a Austrália que possui o maior IDH está em sexto lugar no ranking de investimentos. 
                                  Quanto às ferramentas e variáveis estéticas, reintero que a escolha do grupo foi de padronizar a grande
                                  maioria delas, inclusive sendo definidas por meio de uma função armazenada no módulo "funcoes_esteticas".
                                    """)

DESCRICAO_DISPERSAO_VACINA = Div(text="""
                                    Esse gráfico tem como objetivo comparar os países do G20 com relação a dois assuntos muito importantes na área da
                                    Saúde: a Vacinação de Crianças e a Mortalidade Infantil do período de 1990 à 2010. Além disso, foram destacados
                                    quatro países que tiveram os dois maiores e os dois menores Índices de Desenvolvimento Humano. Os países com cores 
                                    de tons vermelhos são a Índia e a China que representam os países com os menores IDHs, enquanto os países com cores 
                                    de tons azuis são a Austrália e os Estados Unidos que representam os países com os maiores IDHs. Pode-se perceber 
                                    que, em relação ao gráfico, a Índia, que possui um IDH muito baixo também possui uma média de mortes muito elevada, 
                                    o que justifica a sua baixa porcentagem de crianças vacinadas. Por outro lado, a China, que também tem um IDH baixo 
                                    possui uma porcentagem alta de crianças vacinadas e, consequentemente uma baixa média de mortes. Um resultado esperado 
                                    foi observado em relação aos países com IDHs altos, que ao longo dos anos tiveram grande parte das crianças vacinadas 
                                    e, consequentemente, poucas mortes.  
                                    """)

DESCRICAO_LINHAS_NATALIDADE = Div(text="""<p>Em um intervalo de 100 anos (1910 a 2010), a taxa de natalidade esteve em constante movimento. Ela é afetada por vários aspectos sociais e econômicos.</p>
                                  <p>Seguindo a linha da China, é possível ver um forte decrescimento entre os anos de 1957 e 1961. Essa data coincide com o período conhecido como A Grande Fome Chinesa (1958 - 1961).</p>
                                  <p>Em todos os países, houve um decrescimento que começou no fim do século passado. Isso se deve à crescente integração da mulher em empresas e o reconhecimento delas como mais que apenas donas de casa.</p>""")

"""
DESCRICAO_BARRAS_CARBONO.style = {'text-align': 'center'}
DESCRICAO_BARRAS_PIB.style = {'text-align': 'center'}
DESCRICAO_BOLHAS_CALORIAS.style = {'text-align': 'center'}
DESCRICAO_BOXPLOT_EXP_VIDA.style = {'text-align': 'center'}
DESCRICAO_LINHAS_ANOS_ESCOLA.style = {'text-align': 'center'}
DESCRICAO_LINHA_PIB_PC.style = {'text-align': 'center'}
DESCRICAO_MAPA_GINI.style = {'text-align': 'center'}
DESCRICAO_MAPA_IDH.style = {'text-align': 'center'}
DESCRICAO_BARRAS_ANIMADO_PIB.style = {'text-align': 'center'}
DESCRICAO_PROPORCAO_HOMENS_MULHERES.style = {'text-align': 'center'}
DESCRICAO_BARRAS_SAUDE.style = {'text-align': 'center'}
DESCRICAO_DISPERSAO_VACINA.style = {'text-align': 'center'}
"""



