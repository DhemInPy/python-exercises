'''Métodos Específicos de Dicionário'''

'''# clear() -> Deleta todos os elementos do Dicionário (semelhante ao que aprendemos em listas)'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# vendas_mes.clear()
# print(vendas_mes)


'''# copy() -> Cria uma cópia do dicionário (semelhante ao que aprendemos em listas)'''

# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# vendas2_mes = vendas_mes.copy()
# print(vendas2_mes)

'''# fromkeys(chaves, valor_padrao) -> Cria um dicionário com as chaves e o mesmo valor padrão para todas as chaves'''
# chaves = ('jan', 'fev', 'mar')
# vendas = 100
# vendas_mes = dict.fromkeys(chaves, vendas)
# print(vendas_mes)


'''# get(chave) -> Retorna o valor especificado pela chave (Semelhante a fazer dictionario[chave]'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# print(vendas_mes.get('mar'))



'''# items() -> Retorna uma lista em que cada item é uma tupla com (chave, valor)'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# print(list(vendas_mes.items()))


'''# keys() -> Retorna uma lista com todas as chaves do dicionário'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# print(list(vendas_mes.keys()))


'''# pop(chave) -> Retira o item do dicionário e retorna o valor dele para ser usado'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# vendas_fev = vendas_mes.pop('fev') #retira o fevereiro do dicionário ao mesmo tempo que armazena o valor dele na variável
# print(vendas_fev)
# print(vendas_mes)


'''# popitem() -> Retira o último item adicionado ao dicionário'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# #retira o último item adicionado no dicionário ao mesmo tempo que armazena o item(chave, valor) dele na variável
# vendas_ult = vendas_mes.popitem()
# print(vendas_mes)
# print(vendas_ult)


'''# setdefault(chave, valor) -> Retorna o valor da chave passada, mas caso a chave não exista, cria no dicionário o item com a chave e valor passados.'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# vendas_fev = vendas_mes.setdefault('fev', 500)
# print(vendas_fev)
# #repare que como fevereiro existe na lista, ele procura pelo valor de fevereiro e ignora o 500 passado
# # agora quando não existe na lista:
# vendas_abr = vendas_mes.setdefault('abr', 600)
# #repare que agora além de vendas_abr retornar o 600 como valor, ele adicionou um item no dicionario
# print(vendas_abr)
# print(vendas_mes)


'''# update(dicionario) -> Adiciona o dicionário passado como parâmetro ao dicionário original'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# vendas_2tri = {'abr': 400, 'mai': 600, 'jun': 500}
# vendas_mes.update(vendas_2tri)
# print(vendas_mes)



'''# values() -> Retorna uma lista com todos os valores do dicionários'''
# vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
# print(list(vendas_mes.values()))



'''Dicionários em Python
Estrutura:
dicionario = {chave: valor, chave: valor, chave: valor, chave: valor ...}

Vantagens e Desvantagens
Não devem ser usados para pegar itens em uma determinada ordem
Podem ter valores heterogêneos (vários tipos de valores dentro de um mesmo dicionário: inteiros, strings, listas, etc)
Chaves são únicas obrigatoriamente
Mais intuitivos de trabalhar'''


mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}



'''Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
Quanto foi vendido de 'notebook asus' e de 'ipad'?'''
# livros = mais_vendidos.get('livros')
# lazer = mais_vendidos['lazer']
# print(livros,',',lazer)
#
# vendas_note = vendas_tecnologia.get('notebook dell')
# vendas_ipad = vendas_tecnologia['ipad']
# print('Foram vendidos {} unidades de ipad'.format((vendas_ipad)))
# print('Foram vendidos {} unidades de notebook dell'.format((vendas_note)))





'''Não confie na ordem dos dicionários, use as chaves
Python Versões Antigas x Versões Novas
Dicionários eram "sem ordem". Atualmente tem ordem, mas o certo é usar as chaves
2 formas de pegar um valor:
dicionario[chave]
.get(chave)'''


mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}
vendas_tecnologia = {"copo":5658 ,'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}


'''Verificar se item está no dicionário:
if
.get(chave) = None
Se tentarmos procurar as vendas de "copo" na lista de vendas tecnologia, o que acontece?'''
# if vendas_tecnologia.get('copo') == None:
#     print('Não tem copo dentro de vendas tecnologia')

    # '''### OOOOOOUUUUUU ####'''
# if "copo" in vendas_tecnologia:
#     print('tem copo')
# else:
#     print('não tem copo')



'''Adicionar, Remover e Modificar Itens no Dicionário

Estrutura:

Adicionar itens:

dicionario = {}

dicionario[chave] = valor

outra opção:

dicionario.update({chave: valor, chave: valor})'''

# lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
# lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}
# Adicionando 1 item
# print(lucro_1tri)
# lucro_1tri['abril'] = 8004
# print(lucro_1tri)

# Adicionando vários itens ou um dicionário a outro
# lucro_1tri.update({'abril': 88000, 'maio': 89000, 'junho': 120000})
# print(lucro_1tri)

# Adicionando um item já existente (manualamente ou pelo update)
# lucro_1tri['janeiro'] = 8474
# print(lucro_1tri)



'''Modificar itens:
Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.

dicionario[chave] = valor

Vamos modificar o lucro de fevereiro:
(Lembrando: caso o item não exista, ele vai criar o item no dicionário)'''

# lucro_fev = 8500
# lucro_1tri['fevereiro'] = lucro_fev
# print(lucro_1tri)


'''Remover itens:
del dicionario[chave]

ou então
        l-> valor = dicionario.pop(chave)

mas cuidado com:

del dicionario
        l-> que é diferente de dicionario.clear()'''
# removendo o mês de junho
# del lucro_1tri['junho']
# print(lucro_1tri)
#
# lucro_1tri.pop('maio')
# print(lucro_1tri)

# Obs: o del também funciona para listas, caso queira usar -> del lista[i]
# funcionarios = ["João", "Dhemison", "Programador", "Excelente"]
# print(funcionarios)
# del funcionarios
# print(funcionarios)




'''For nos Dicionarios
Estrutura:

for chave in dicionario:
    faça alguma coisa'''


vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#demonstrando o for
# for chave in vendas_tecnologia:
#     print('{}: {} unidades'.format(chave,vendas_tecnologia[chave]))

# Qual o total de notebooks vendidos?
# total_note = 0
# for chave in vendas_tecnologia:
#     if "notebook" in chave:
#         total_note += vendas_tecnologia[chave]
# print(total_note)



'''Exercícios
1. Identificando Locais de Risco
(Não conhecemos muito dos números e indicadores reais, esse é um exercício imaginário para treinarmos com um cenário mais prático)

Digamos que você está construindo um programa para identificar níveis de CO2 (gás carbônico) em determinados locais para evitar potenciais acidentes. 
Em cada um desses locais a sua empresa tem 5 sensores que captam o nível de CO2 do local.

Os níveis normais de CO2 são em média 350. O nível de CO2 de um local é dado pela média captada pelos 5 sensores.

Isso significa que se tivermos os 5 sensores do Rio de Janeiro marcando: 350, 400, 450, 350, 300, o nível de CO2 do Rio de Janeiro será dado por: 
(350 + 400 + 450 + 350 + 300) / 5 = 370.

Caso o nível seja maior do que 450, um aviso deve ser exibido pelo seu programa dizendo, por exemplo: 
Rio de Janeiro está com níveis altíssimos de CO2 (490), chamar equipe especializada para verificar a região.

Os resultados dos sensores são monitorados frequentemente e são dados para o sistema em forma de dicionário:'''


niveis_co2 = {
    'AC': [325,405,429,486,402],
    'AL': [492,495,310,407,388],
    'AP': [507,503,368,338,400],
    'AM': [429,456,352,377,363],
    'BA': [321,508,372,490,412],
    'CE': [424,328,425,516,480],
    'ES': [449,506,461,337,336],
    'GO': [425,460,385,485,460],
    'MA': [361,310,344,425,490],
    'MT': [358,402,425,386,379],
    'MS': [324,357,441,405,427],
    'MG': [345,367,391,427,516],
    'PA': [479,514,392,493,329],
    'PB': [418,499,317,302,476],
    'PR': [420,508,419,396,327],
    'PE': [404,444,495,320,343],
    'PI': [513,513,304,377,475],
    'RJ': [502,481,492,502,506],
    'RN': [446,437,519,356,317],
    'RS': [427,518,459,317,321],
    'RO': [517,466,512,326,458],
    'RR': [466,495,469,495,310],
    'SC': [495,436,382,483,479],
    'SP': [495,407,362,389,317],
    'SE': [508,351,334,389,418],
    'TO': [339,490,304,488,419],
    'DF': [376,516,320,310,518],
}


# for cidades in niveis_co2:
#     qntd_censores = len(niveis_co2[cidades])
#     nivel_alto = sum(niveis_co2[cidades]) / qntd_censores
#     if nivel_alto > 450:
#         print('{} está acima do nivel min,({}) chamar reforços'.format(cidades, nivel_alto))





'''2. Case da Hashtag
Recentemente tivemos que fazer backup dos vídeos que temos hospedados no Vimeo. 
Acontece que não existe um botão de Download de todos os vídeos ao mesmo tempo, precisamos entrar em 1 por 1 e fazer o download manualmente.

A alternativa é gerar um código em Python que converse com a API do Vimeo 
(API é uma integração que as ferramentas abrem para programadores poderem fazer integrações dos seus próprios programas/scripts com a ferramenta).

Para resolver isso, a gente fez a integração e fizemos uma "requisição" de todos os vídeos para a Vimeo. 
Essa requisição dá como resposta para o nosso código isso:'''

# video = {'uri': '/videos/465407533', 'name': '15 Atalhos no Excel para Ficar Mais Produtivo', 'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivosource.mp4', 'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442, 'md5': 'af09508ceceed4994554f04e8b931e22', 'public_name': 'Original', 'size_short': '384.02MB'}, {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo175.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205, 'md5': '3c05e1e69bd6b13eb1464451033907d2', 'public_name': 'HD 1080p', 'size_short': '165.52MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo165.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848, 'md5': '4a5c5c96cdf18202ed20ca534fd88007', 'public_name': 'SD 540p', 'size_short': '85.72MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc949d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo139.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450, 'md5': '91cc0229087ec94bf67f64b01ad8768d', 'public_name': 'SD 240p', 'size_short': '26.13MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo164.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155, 'md5': '548640bf79ce1552a3401726bb0e4224', 'public_name': 'SD 360p', 'size_short': '46.37MB'}]}
#
# for vimeo in video:
#     print(vimeo)
# # print(video['download'])
# print(video['download'][0]['link'])

'''Repare que é um código completamente confuso, mas que no fim do dia é um dicionário.

Dentro dele queremos printar o link de download do vídeo para depois simplesmente clicar em todos os links e fazer o download de todos os vídeos.

No nosso caso, tínhamos uma lista com os mais de 2.000 vídeos (sendo cada vídeo um dicionário exatamente como esse aí em cima),
e por isso fizemos exatamente esse mesmo procedimento que você vai construir aqui abaixo, 
só que dentro de um "for" para percorrer todos os vídeos. Não podemos disponibilizar a lista inteira por questões de segurança 
e proteção de dados mesmo, mas o dicionário acima já vale o exemplo.'''

###############################################################################################################




'''Métodos úteis em dicionários

items() dos dicionários

Estrutura:'''


'''itens_dicionario = dicionario.items()

ou então:

for item in dicionario.items()
>>>>>> cada item do dicionario em formato de tupla <<<<<<<<
'''
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# for produto, qntd in vendas_tecnologia.items():
#     print(produto,':', qntd, 'unidades')

'''  Quais produtos venderam mais de 5000 unidades?   '''

'''#forma 1 -> usando apenas o dicionario e as chaves'''
# for produto in vendas_tecnologia:
#     if vendas_tecnologia[produto] > 5000:
#         print('produto {} bateu a meta de {} unidades vendidos'.format(produto, vendas_tecnologia[produto]))
# print('=' * 70)
'''#forma 2 -> usando o dicionario.items()'''
# for produto,qntd in vendas_tecnologia.items():
#     if qntd > 5000:
#         print('produto {} bateu a meta de {} unidades vendidos'.format(produto, qntd))

'''Listas importantes a partir do Dicionário
Métodos importantes:

.keys() -> uma "lista" com todas as chaves do dicionario

.values() -> uma "lista" com todos os valores do dicionario

Obs: Se o dicionario for modificado, automaticamente essas variáveis são modificadas, mesmo tendo sido criadas anteriormente'''
# chaves = vendas_tecnologia.keys()
# valores = vendas_tecnologia.values()
# vendas_tecnologia['Dhemisin'] = 100
# print(chaves)
# print(valores)
# print(list(valores))


'O for vai funcionar normal em dict_listas, porque não deixa de ser uma lista de itens que pode ser percorrida (iterable), mas o que aprendemos '
'de lista não necessariamente se aplicam a essas dict_listas.Para transformar as dict_listas em listas normais, usamos a função list:'

'lista_chaves = list(dicionario.keys())'

'Pode ser útil caso a gente queira fazer alguma organização das chaves. Ex: Imprimir uma lista com os valores em ordem alfabética, de forma que todas as tvs fiquem juntas, todos os iphone/ipad também e assim vai'''


#agora se quisermos organizar isso, fazemos:
# listas_chaves = list(chaves)
# listas_chaves.sort()
# for chave in listas_chaves:
#     print('{}: {} unidades.'.format(chave, vendas_tecnologia[chave]))



'''Transformando Listas em Dicionários e Function zip
Estrutura:'''

'''###Dicionário com valores padrões:
        dicionario = dict.fromkeys(lista_chaves, valor_padrao)


###Dicionário a partir de listas de tuplas:
        dicionario = dict(lista_tuplas)'''


'''Dicionário a partir de 2 listas:

        Passo 1: Transformar listas em lista de tuplas com o método zip
        Passo 2: Transformar em dicionario

lista_tuplas = zip(lista1, lista2)
dicionario = dict(lista_tuplas)'''


produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

#
# print(produtos)
# trans_em_tuplas = zip(produtos,vendas)
# print(trans_em_tuplas)
# dicionario = dict(trans_em_tuplas)
# print(dicionario)


'''Quanto vendemos de ipad?'''
# #fazendo por listas
# i_ipad = produtos.index('ipad')
# print('vendemos {} unidades de {}'.format(vendas[i_ipad], produtos[i_ipad]))

#fazendo por dicionario
# tupla = zip(produtos, vendas)
# dicio = dict(tupla)
#
# print('vendemos {} unidades de ipad'.format(dicio['ipad']))


'''Exercícios
1. Exercício "menos prático" para treinar manipulação de dicionário
Dessa vez, vamos apenas treinar a manipulação de dicionário. Transforme as listas abaixo em 1 único dicionário no formato:'''


'''dicionario = {
    produto: (vendas2019, vendas2020),
    produto2: (vendas2019, vendas2020),
    produto3: (vendas2019, vendas2020),
    ...
}
Apesar de parecer "menos prático" esse é um procedimento que precisamos nos acostumar a fazer, visto que algumas funções 
(tema dos próximos módulos) precisam de dicionários para funcionar e saber transformar listas em dicionários (e vice-versa)
é uma habilidade muito útil.

Obs: Lembre do zip para juntar listas.
Obs2: Repare que cada item das vendas é na verdade uma lista. Então é provável que você precise fazer esse código em 2 etapas'''


produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]


tupla = list(zip(vendas2019,vendas2020))
dio = list(zip(produtos,tupla))

zipado = dict(dio)
print(zipado)

# for chaves in zipado:
#     print(chaves, zipado[chaves])


'''                                            # EXERCIOS EXTRAS #                                         '''


# Exercício 1
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

produto = input('Nome do produto: ')

if produto in precos.keys():
    print('PRODUTO: {} VALOR: R${} reais'.format(produto, precos[produto]))
else:
    print('Tente novamente!')


# Exercício 2
# Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
# Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
# Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado

# produto = input('Nome do produto: ')
# if produto in precos.keys():
#     print('R${} reais'.format(precos[produto]))
#
# elif produto not in precos.keys():
#     cadastro = input('Não encontrado, deseja cadastrar um novo produto ?')
#     if cadastro == "sim":
#         nv_produto = input('Nome do novo produto: ')
#         preco_nv_produto = int(input('Preço do novo produto: '))
#         precos[nv_produto] = preco_nv_produto
#         print('cadastro completo')
#         print(precos)
# else:
#     print('Tente novamente!')




# Exercício 3
# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos.
# calcule o novo valor dos produtos com base nas seguintes regras:
# Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
# Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
# Preços acima de 2.000 vão ter reajuste de 20%

# precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
# novo_dicionario = []
# for produto, preco in precos.items():
#     if 1000 < preco < 2000 :
#         nv_preco = preco * 0.15
#         reajuste = preco + nv_preco
#         novo_dicionario.append((produto,reajuste))
#         print('15%',produto, preco,'reajuste:R$',reajuste)
#
#     elif preco > 2000:
#         nv_preco = preco * 0.2
#         reajuste = preco + nv_preco
#         novo_dicionario.append((produto,reajuste))
#         print('20%',produto, preco, 'reajuste:R$',reajuste)
#
#     else:
#         if preco <= 1000:
#             nv_preco = preco * 0.1
#             reajuste = preco + nv_preco
#             novo_dicionario.append((produto,reajuste))
#             print('10%',produto,preco,'reajuste:R$',reajuste)
#
#
#
# # Exercício 4
# # Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
# # Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final
# print('-'*50,'\n')
# #
# for no in novo_dicionario:
#     entai = dict(novo_dicionario)
# print(entai)





# Exercício 5
# Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
# Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
# Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022
# vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
# vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}
#
#
# for mes in vendas_22:
#     crescimento = ( vendas_23[mes] - vendas_22[mes]) / vendas_22[mes] * 100
#     if crescimento < 0:
#         print('Mês de {} ficou negativo, com {:.2f}%'.format(mes,crescimento))
#
#     else:
#         print('Mês de {} teve {:.2f}% de aumento'.format(mes, crescimento,))
#
# valor_total_22 = sum(vendas_22.values())
# valor_total_23 = sum(vendas_23.values())
#
# print('O crescimento de 2022 para 2023 foi de {:.2f}%'.format((valor_total_23 - valor_total_22) / valor_total_22 * 100))



# Exercício 6 - Desafio
# No final da reunião de apresentação dos números, seu chefe perguntou:
# E se nos meses de 2023 que a gente vendeu menos do que 2022 a gente tivesse pelo menos empatado com 2022
#(ou seja, se nos meses de 2023 em que as vendas foram menores do que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022)
# Qual teria sido o nosso crescimento de 2023 frente a 2022?
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}
print('=' * 56)
for mes in vendas_22:
    if vendas_23[mes] < vendas_22[mes]:
        vendas_23[mes] = vendas_22[mes]

for mes in vendas_22:
    crescimento = ( vendas_23[mes] - vendas_22[mes]) / vendas_22[mes] * 100
    if crescimento < 0:
        print('Mês de {} ficou negativo, com {:.2f}%'.format(mes,crescimento))

    else:
        print('Mês de {} teve {:.2f}% de aumento'.format(mes, crescimento,))

valor_total_22 = sum(vendas_22.values())
valor_total_23 = sum(vendas_23.values())

print('O crescimento de 2023 seria de {:.2f}%'.format((valor_total_23 - valor_total_22) / valor_total_22 * 100))














