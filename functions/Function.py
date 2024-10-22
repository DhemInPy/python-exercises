
'''Function Python
O que é?
As functions são blocos de código que servem 1 único propósito, fazem uma ação específica.

Estrutura Básica'''


'''def nome_funcao():
    faça alguma coisa
    faça outra coisa
    return valor_final'''


# Exemplo: vamos criar uma função de cadastro de um Produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.

# def cadastro_produto():
#     produto = input('qual o nome do produto: ')
#     produto.casefold()
#     print('{} cadastrado'.format(produto))
#
#
# for i in range(4):
#     cadastro_produto()


'''Retornar um valor na Function Python
Estrutura Básica

def nome_funcao():
    return valor_final'''

# Exemplo: vamos criar uma função de cadastro de um Produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.

def cadastro_produto():
    produto = input('qual o nome do produto: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto

# cadastro_produto = cadastro_produto()
# print('recebemos {} em nosso estoque'.format(cadastro_produto))


'''Argumentos/Parâmetros da Função

Estrutura:

def minha_funcao(parametro1, parametro2, parametro3):
    return parametro1 + parametro2 + parametro3'''


# def alguma_coisa(num1 ,num2 ,num3):
#     return num1 + num2 + num3
#
# minha_fun = alguma_coisa(5, 8, 87)
# print(minha_fun)

'''Digamos que estamos criando um programa para categorizar os produtos de uma revendedora de bebidas.

Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.'''

'''Ex:
Vinho -> BEB12302
Cerveja -> BEB12043
Vodka -> BEB34501

Guaraná -> BSA11104
Coca -> BSA54301
Sprite -> BSA34012
Água -> BSA09871'''



'''Repare que bebidas não alcóolicas começam com BSA e bebidas alcoolicas começam com BEB.

Crie um programa que analise uma lista de produtos e envie instruções para a equipe de estoque dizendo quais 
produtos devem ser enviados para a área de bebidas alcóolicas.'''

produtos = ['beb46275' ,'TFA23962' ,'TFA64715' ,'TFA69555' ,'TFA56743' ,'BSA45510' ,'TFA44968' ,'CAR75448' ,'CAR23596'
            ,'CAR13490' ,'BEB21365' ,'BEB31623' ,'BSA62419' ,'BEB73344' ,'TFA20079' ,'BEB80694' ,'BSA11769' ,'BEB19495'
            ,'TFA14792' ,'TFA78043' ,'BSA33484' ,'BEB97471' ,'BEB62362' ,'TFA27311' ,'TFA17715' ,'BEB85146' ,'BEB48898'
            ,'BEB79496' ,'CAR38417' ,'TFA19947' ,'TFA58799' ,'CAR94811' ,'BSA59251' ,'BEB15385' ,'BEB24213' ,'BEB56262'
            ,'BSA96915' ,'CAR53454' ,'BEB75073']

# 1- Pecorrer toda a minha lista de produtos
# 2 - Para cada produto, verificar se ele é bebida alcolica
# 3 - Se for bebida alcolica, exibir a msg...

# def if_alcool(produto):
#     for i, bebida in enumerate(produto):
#         bebida = bebida.upper()
#         if "BEB" in bebida:
#             return True
#
#             lista[bebida] = "É bebida alcolica"
#         else:
#             return False
#
#             lista[bebida] = "Não é alcolica"
#
#
# print(if_alcool(produtos))

# def ehalcolica(produto):
#     produto = produto.upper()
#     if "BEB" in produto:
#         return True
#     else:
#         return False
#
#
# for item in produtos:
#     item = item.upper()
#     if ehalcolica(item):
#         print(item,"É bebida alcolica")


'''Mais de 1 argumento e formas de passar argumento para uma função
Estrutura:

2 formas de passar o argumento:
    1 - Em ordem (positional argument)
    2 - Com o nome do argumento (keyword argument)

Vamos mudar a função que fizemos na aula passada para conseguir categorizar qualquer
tipo de bebida de acordo com o "rótulo" passado para a nsosa function. Basicamente nossa 
function agora tem que verificar se o produto é da categoria passada ou não.'''

# produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']
#
# def ehalcolica(produto,cod_categria):
#     produto = produto.upper()
#     if cod_categria in produto:
#         return True
#     else:
#         return False
#
# for produto in produtos:
#     if ehalcolica(produto, 'CAR'):
#         print(produto,'É da categora de carro')
#     elif ehalcolica(produto, 'BEB'):
#         print('é da categoria de alcol', produto)
#     elif ehalcolica(produto, 'BSA'):
#         print(produto,'não é da categoria de alcol', )


'''Exercícios
Para fazer um treino simples antes de avançarmos em mais functions, vamos criar uma function que resolve 1 "desafio simples"

1. Function para Cálculo de Carga Tributária
(Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo imaginário para
treinarmos as functions com algo mais prático)

Imagine que você trabalha no setor contábil de uma grande empresa de Varejo.

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, 
dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.'''


preco = 1500
custo = 400
lucro = 800
#
#
# # Repare que preço - custo não é igual ao lucro, porque ainda foi descontado o imposto.
# #Sua functiona deve calcular qual foi o % de imposto aplicado sobre o preço total.

# # crie sua function aqui
def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto /preco


#aplique sua function nos valores fornecidos para ver se ela está funcionando corretamente
# print("A carga tributaria foi de {:.1%}".format(carga_tributaria(preco, custo, lucro)))


'''Exemplos de parâmetros
upper() -> não tem parâmetros
sort() -> apenas parâmetros keyword
extend(lista) -> 1 parâmetro obrigatório
nossa função eh_da_categoria(bebida, cod_categoria) -> 2 parâmetros de posição obrigatórios'''


# def eh_da_categoria(bebida, cod_categoria):
#     bebida = bebida.upper()
#     if cod_categoria in bebida:
#         return True
#     else:
#         return False

#texto para upper
# cod_produto = 'beb12304'
# cod_produto.upper()
# lista para sort e extend
# vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
# vendas_novdez = [500, 1555]
# vendas_ano.extend(vendas_novdez)
# vendas_ano.sort()
# print(vendas_ano)


# if eh_da_categoria(cod_produto, 'B'):
#     print('é da categoria')





'''Valores Padrões para os argumentos
Estrutura
Nesse caso, você não é obrigado a passar o valor para usar a função, pode usar o valor padrão.'''

'''def minha_funcao(argumento = valor_padrao):
    ...
    return ...'''


'''Como vimos, o sort() para listas tem um argumento padrão. O reverse = False é padrão, então a ordem é crescente. 
Caso o usuário queira fazer em ordem decrescente, o reverse deve ser alterado para True'''


produtos = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']

# produtos.sort()
# print(produtos)
#
# produtos.sort(reverse = True)
# print(produtos)



'''Vamos criar uma função que padronize códigos de produtos. O default será padronizar os códigos para letras minúsculas (dado por 'm'), 
mas se o usuário quiser pode padronizar para maiúscula, dado por ('M').'''


def minha_funcao(lista, padrao="M"):
    for i, item in enumerate(lista):
        item = item.replace(' ', '')
        item = item.strip()
        if padrao == "m":
            item = item.casefold()
        elif padrao == "M":
            item = item.upper()
        lista[i] = item
    return lista


# print(minha_funcao(produtos))



'''Mais sobre o return
Pontos importantes:
Podemos usar no return praticamente qualquer tipo de objeto: (número, string, lista, tupla, dicionário, outros objetos, etc.)
O return, se for executado, encerra a função, mesmo que dentro dela haja um loop.'''


# retornar um número
# def minha_soma(num1, num2, num3):
#     return num1 + num2 + num3
# oi = 8
# ei = 6
# ens = 8
# print(minha_soma(oi, ei,ens))

# retornar um texto
# def padronizar_texto(texto):
#     texto = texto.casefold()
#     texto = texto.replace("  ", " ")
#     texto = texto.strip()
#     return texto
# texto = '     amo programAR hahaha      '
# print(padronizar_texto(texto))


# retornar um boolean
# def bateu_meta(vendas, meta):
#     if vendas >= meta:
#         return True
#     else:
#         return False


# vendas_dhemis = 855
# meta = 856
#
# if bateu_meta(vendas_dhemis,meta):
#     print('Conseguiu bater a meta')

# print(bateu_meta(vendas_dhemis, meta))


# retornar uma lista, tupla ou dicionario
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada
#
#
listas_gmails = ['dhemison236@gmail.com', 'rosi236@gmail.com', 'felipe236@hotmail.com', 'andrei235@hotmail.com']
lista = filtrar_lista_texto(listas_gmails, 'dhe')
# print(lista)





'''
                                                Exercícios


1. Function para Análise de Indicadores'''

'''A maioria das empresas tem suas próprias regras para cálculos de indicadores.

        1 - Algumas empresas definem que um cliente é considerado um cliente inadimplente quando 
        ele está devendo acima de X reais e por mais de X dias.

        2 - Algumas empresas definem que um vendedor bateu a meta quando ele vendeu acima de X reais 
        (outras ainda analisam não só as vendas desse vendedor, mas também da loja ou da unidade de negócios 
        que ele faz parte, ou ainda uma avaliação qualitativa).
        
        3 - Algumas empresas definem que um produto está em "falta" no estoque quando ele está abaixo 
        de um nível mínimo quando um cliente insere um novo pedido daquele produto.
        
        4 - E assim vai para dezenas de indicadores.

>>> - O ponto importante é, cada empresa tem alguma adaptação do cálculo de indicadores. E normalmente 
se formos analisar esses indicadores é interessante ter funções que façam todo o trabalho de análise deles. 
Por isso, vamos construir 2 exemplos aqui:

Item 1: Crie uma função que calcula o percentual de Stockout de uma empresa

        A: O % de stockout é dado por (Vendas Perdidas por Estoque) / (Vendas Concluídas + Vendas Perdidas por Estoque) 
            -> essas vendas são dadas em valor total (dinheiro) e não em quantidade de vendas
        
        
        B: Seu programa recebe um dicionário com todas as vendas da empresa, o status dela (se foi Concluída ou Cancelada) e, 
        caso tenha sido Cancelada, o motivo de Cancelamento. O formato é o seguinte:
'''
# vendas = {
#     'VE0001': (15000, 'Concluído', ''),
#     'VE0002': (13300, 'Cancelado', 'Cancelado pelo Cliente'),
#     'VE0003': (12000, 'Concluído', ''),
#     ...
#         }


'''Para reforçar: As vendas Canceladas por qualquer outro motivo que não seja a Falta de Estoque não devem ser consideradas para a conta do Stockout.'''


vendas = {'VE0001': (9868 ,'Concluído' ,'') ,'VE0002': (9642 ,'Concluído' ,'') ,'VE0003': (6007 ,'Concluído' ,'')
          ,'VE0004': (15562 ,'Concluído' ,'') ,'VE0005': (18752 ,'Cancelado' ,'Estoque em Falta')
          ,'VE0006': (16358 ,'Cancelado' ,'Estoque em Falta') ,'VE0007': (17045 ,'Concluído' ,'')
          ,'VE0008': (12230 ,'Concluído' ,'') ,'VE0009': (6747 ,'Concluído' ,'') ,'VE0010': (15114 ,'Concluído' ,'')
          ,'VE0011': (12497 ,'Concluído' ,'') ,'VE0012': (6001 ,'Concluído' ,'')
          ,'VE0013': (16227 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0014': (16150 ,'Concluído' ,'')
          ,'VE0015': (17705 ,'Concluído' ,'') ,'VE0016': (9978 ,'Concluído' ,'') ,'VE0017': (4266 ,'Concluído' ,'')
          ,'VE0018': (11531 ,'Concluído' ,'') ,'VE0019': (10352 ,'Cancelado' ,'Cancelada pelo Cliente')
          ,'VE0020': (16544 ,'Concluído' ,'') ,'VE0021': (15488 ,'Concluído' ,'') ,'VE0022': (15828 ,'Concluído' ,'')
          ,'VE0023': (1218 ,'Concluído' ,'') ,'VE0024': (11560 ,'Concluído' ,'') ,'VE0025': (14220 ,'Concluído' ,'')
          ,'VE0026': (17839 ,'Concluído' ,'') ,'VE0027': (4050 ,'Concluído' ,'')
          ,'VE0028': (7594 ,'Cancelado' ,'Estoque em Falta') ,'VE0029': (19586 ,'Concluído' ,'')
          ,'VE0030': (8453 ,'Concluído' ,'') ,'VE0031': (3589 ,'Concluído' ,'')
          ,'VE0032': (13472 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0033': (16994 ,'Concluído' ,'')
          ,'VE0034': (2139 ,'Concluído' ,'') ,'VE0035': (10173 ,'Concluído' ,'')
          ,'VE0036': (17784 ,'Cancelado' ,'Estoque em Falta') ,'VE0037': (12214 ,'Concluído' ,'')
          ,'VE0038': (5878 ,'Concluído' ,'') ,'VE0039': (2622 ,'Concluído' ,'') ,'VE0040': (9765 ,'Concluído' ,'')
          ,'VE0041': (8872 ,'Concluído' ,'') ,'VE0042': (16543 ,'Concluído' ,'') ,'VE0043': (8994 ,'Concluído' ,'')
          ,'VE0044': (4332 ,'Concluído' ,'') ,'VE0045': (19679 ,'Concluído' ,'') ,'VE0046': (14968 ,'Concluído' ,'')
          ,'VE0047': (6352 ,'Concluído' ,'') ,'VE0048': (11461 ,'Concluído' ,'') ,'VE0049': (5285 ,'Concluído' ,'')
          ,'VE0050': (11639 ,'Concluído' ,'') ,'VE0051': (6023 ,'Concluído' ,'') ,'VE0052': (4943 ,'Concluído' ,'')
          ,'VE0053': (5654 ,'Concluído' ,'') ,'VE0054': (11734 ,'Concluído' ,'') ,'VE0055': (2742 ,'Concluído' ,'')
          ,'VE0056': (5380 ,'Cancelado' ,'Estoque em Falta') ,'VE0057': (5578 ,'Concluído' ,'')
          ,'VE0058': (1897 ,'Concluído' ,'') ,'VE0059': (7857 ,'Concluído' ,'') ,'VE0060': (4472 ,'Concluído' ,'')
          ,'VE0061': (19874 ,'Concluído' ,'') ,'VE0062': (13323 ,'Cancelado' ,'Cancelada pelo Cliente')
          ,'VE0063': (5821 ,'Concluído' ,'') ,'VE0064': (4410 ,'Concluído' ,'') ,'VE0065': (16676 ,'Concluído' ,'')
          ,'VE0066': (10577 ,'Concluído' ,'') ,'VE0067': (10627 ,'Concluído' ,'') ,'VE0068': (1987 ,'Concluído' ,'')
          ,'VE0069': (13197 ,'Concluído' ,'') ,'VE0070': (15063 ,'Concluído' ,'') ,'VE0071': (14363 ,'Concluído' ,'')
          ,'VE0072': (10452 ,'Concluído' ,'') ,'VE0073': (15376 ,'Concluído' ,'') ,'VE0074': (4661 ,'Concluído' ,'')
          ,'VE0075': (13287 ,'Concluído' ,'') ,'VE0076': (8278 ,'Concluído' ,'') ,'VE0077': (7134 ,'Concluído' ,'')
          ,'VE0078': (16568 ,'Concluído' ,'') ,'VE0079': (17732 ,'Concluído' ,'') ,'VE0080': (5127 ,'Concluído' ,'')
          ,'VE0081': (4582 ,'Concluído' ,'') ,'VE0082': (14804 ,'Cancelado' ,'Cancelada pelo Cliente')
          ,'VE0083': (12362 ,'Concluído' ,'') ,'VE0084': (1148 ,'Concluído' ,'') ,'VE0085': (14018 ,'Concluído' ,'')
          ,'VE0086': (15891 ,'Concluído' ,'') ,'VE0087': (4517 ,'Concluído' ,'') ,'VE0088': (1770 ,'Concluído' ,'')
          ,'VE0089': (14926 ,'Concluído' ,'') ,'VE0090': (13627 ,'Concluído' ,'') ,'VE0091': (3047 ,'Concluído' ,'')
          ,'VE0092': (13924 ,'Concluído' ,'') ,'VE0093': (7158 ,'Concluído' ,'') ,'VE0094': (5942 ,'Concluído' ,'')
          ,'VE0095': (13480 ,'Concluído' ,'') ,'VE0096': (17686 ,'Concluído' ,'')
          ,'VE0097': (5722 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0098': (16963 ,'Concluído' ,'')
          ,'VE0099': (14225 ,'Concluído' ,'') ,'VE0100': (12553 ,'Concluído' ,'') ,'VE0101': (18047 ,'Concluído' ,'')
          ,'VE0102': (11420 ,'Concluído' ,'') ,'VE0103': (6191 ,'Concluído' ,'') ,'VE0104': (8388 ,'Concluído' ,'')
          ,'VE0105': (17210 ,'Concluído' ,'') ,'VE0106': (12217 ,'Concluído' ,'') ,'VE0107': (8984 ,'Concluído' ,'')
          ,'VE0108': (7638 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0109': (8462 ,'Concluído' ,'')
          ,'VE0110': (14081 ,'Concluído' ,'') ,'VE0111': (10842 ,'Concluído' ,'') ,'VE0112': (13261 ,'Concluído' ,'')
          ,'VE0113': (16953 ,'Cancelado' ,'Estoque em Falta') ,'VE0114': (5343 ,'Concluído' ,'')
          ,'VE0115': (4734 ,'Concluído' ,'') ,'VE0116': (13606 ,'Cancelado' ,'Cancelada pelo Cliente')
          ,'VE0117': (17106 ,'Cancelado' ,'Estoque em Falta') ,'VE0118': (17704 ,'Concluído' ,'')
          ,'VE0119': (12242 ,'Concluído' ,'') ,'VE0120': (7476 ,'Cancelado' ,'Estoque em Falta')
          ,'VE0121': (18408 ,'Concluído' ,'') ,'VE0122': (13612 ,'Concluído' ,'') ,'VE0123': (18198 ,'Concluído' ,'')
          ,'VE0124': (4844 ,'Concluído' ,'') ,'VE0125': (12750 ,'Concluído' ,'') ,'VE0126': (11969 ,'Concluído' ,'')
          ,'VE0127': (15337 ,'Concluído' ,'') ,'VE0128': (1100 ,'Concluído' ,'') ,'VE0129': (18893 ,'Concluído' ,'')
          ,'VE0130': (15850 ,'Concluído' ,'') ,'VE0131': (2097 ,'Concluído' ,'')
          ,'VE0132': (11636 ,'Cancelado' ,'Estoque em Falta') ,'VE0133': (12603 ,'Concluído' ,'')
          ,'VE0134': (10769 ,'Concluído' ,'') ,'VE0135': (11016 ,'Concluído' ,'') ,'VE0136': (14556 ,'Concluído' ,'')
          ,'VE0137': (1389 ,'Concluído' ,'') ,'VE0138': (11681 ,'Concluído' ,'')
          ,'VE0139': (16759 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0140': (16317 ,'Concluído' ,'')
          ,'VE0141': (5965 ,'Concluído' ,'') ,'VE0142': (4493 ,'Concluído' ,'') ,'VE0143': (5398 ,'Concluído' ,'')
          ,'VE0144': (9875 ,'Concluído' ,'') ,'VE0145': (17492 ,'Concluído' ,'') ,'VE0146': (7473 ,'Concluído' ,'')
          ,'VE0147': (10284 ,'Concluído' ,'') ,'VE0148': (10778 ,'Concluído' ,'') ,'VE0149': (2227 ,'Concluído' ,'')
          ,'VE0150': (14157 ,'Concluído' ,'') ,'VE0151': (9516 ,'Concluído' ,'') ,'VE0152': (9824 ,'Concluído' ,'')
          ,'VE0153': (5118 ,'Concluído' ,'') ,'VE0154': (5123 ,'Concluído' ,'') ,'VE0155': (2697 ,'Concluído' ,'')
          ,'VE0156': (19024 ,'Concluído' ,'') ,'VE0157': (5128 ,'Concluído' ,'')
          ,'VE0158': (8293 ,'Cancelado' ,'Estoque em Falta') ,'VE0159': (18782 ,'Concluído' ,'')
          ,'VE0160': (12182 ,'Concluído' ,'') ,'VE0161': (9063 ,'Concluído' ,'') ,'VE0162': (17608 ,'Concluído' ,'')
          ,'VE0163': (8456 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0164': (1291 ,'Concluído' ,'')
          ,'VE0165': (14018 ,'Concluído' ,'') ,'VE0166': (2791 ,'Concluído' ,'') ,'VE0167': (17953 ,'Concluído' ,'')
          ,'VE0168': (14627 ,'Concluído' ,'') ,'VE0169': (3296 ,'Concluído' ,'') ,'VE0170': (1863 ,'Concluído' ,'')
          ,'VE0171': (4719 ,'Concluído' ,'') ,'VE0172': (15060 ,'Concluído' ,'')
          ,'VE0173': (2596 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0174': (4919 ,'Concluído' ,'')
          ,'VE0175': (13770 ,'Concluído' ,'') ,'VE0176': (15041 ,'Cancelado' ,'Estoque em Falta')
          ,'VE0177': (6702 ,'Concluído' ,'') ,'VE0178': (9989 ,'Concluído' ,'') ,'VE0179': (5135 ,'Concluído' ,'')
          ,'VE0180': (13337 ,'Concluído' ,'') ,'VE0181': (13457 ,'Concluído' ,'') ,'VE0182': (17218 ,'Concluído' ,'')
          ,'VE0183': (6424 ,'Concluído' ,'') ,'VE0184': (5478 ,'Concluído' ,'')
          ,'VE0185': (10478 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0186': (3240 ,'Concluído' ,'')
          ,'VE0187': (16503 ,'Concluído' ,'') ,'VE0188': (12762 ,'Concluído' ,'')
          ,'VE0189': (6985 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0190': (13013 ,'Concluído' ,'')
          ,'VE0191': (5706 ,'Concluído' ,'') ,'VE0192': (6521 ,'Cancelado' ,'Estoque em Falta')
          ,'VE0193': (12904 ,'Concluído' ,'') ,'VE0194': (14691 ,'Concluído' ,'') ,'VE0195': (19338 ,'Concluído' ,'')
          ,'VE0196': (4556 ,'Cancelado' ,'Cancelada pelo Cliente') ,'VE0197': (9653 ,'Concluído' ,'')
          ,'VE0198': (4617 ,'Concluído' ,'') ,'VE0199': (4717 ,'Concluído' ,'') ,'VE0200': (8366 ,'Concluído' ,'')}

#sua function aqui
def calculo_checkout(vendas):
    numerador = 0
    denominador = 0
    for venda in vendas:
        valor, stts, motivo = vendas[venda]
        if stts == "Concluído":
            denominador += valor
        elif stts == "Cancelado" and motivo == "Estoque em Falta":
            denominador += valor
            numerador += valor
    return numerador / denominador


# print("{:.2%}".format(calculo_checkout(vendas)))





'''Item 2: Crie uma função para descobrir os clientes inadimplentes de uma empresa

    - O objetivo é identificar quem são os clientes e enviar essa lista de clientes para o setor de cobrança poder fazer a cobrança dos clientes
    
    - Sua função deve então receber uma lista de clientes, analisar quais clientes estão inadimplentes, e retonar uma lista com os clientes
     inadimplentes(apenas o CPF deles já é suficiente)
     
     - A inadimplência nessa empresa é calculada da seguinte forma:
        1. Se o cliente tiver devendo mais de 1000 reais por mais de 20 dias, ele é considerado inadiplente.
        
        2. Isso significa que caso ou cliente esteja devendo 2000 reais a 10 dias, ele não é inadimplente, pois não se passaram  20 dias 
        ainda. Da mesma forma, se ele estiver devendo 500 reais por 40 dias, ele também não é inadimplente, dado que ele deve menos de 1000 reais.
        
        3. As informações vêm no formato (cpf, valor_devido, quantidade, qtde de dias):
        
'''
clientes_devedores = [('462.286.561-65' ,14405 ,24) ,('251.569.170-81' ,16027 ,1) ,('297.681.579-21' ,8177 ,28)
                      ,('790.223.154-40' ,9585 ,10) ,('810.442.219-10' ,18826 ,29) ,('419.210.299-79' ,11421 ,15)
                      ,('908.507.760-43' ,12445 ,24) ,('911.238.364-17' ,1345 ,4) ,('131.115.339-28' ,11625 ,8)
                      ,('204.169.467-27' ,5364 ,22) ,('470.806.376-11' ,932 ,29) ,('938.608.980-69' ,13809 ,19)
                      ,('554.684.165-26' ,11227 ,2) ,('119.225.846-34' ,4475 ,9) ,('358.890.858-95' ,13932 ,20)
                      ,('786.547.940-70' ,17048 ,25) ,('468.487.741-94' ,2902 ,8) ,('540.685.100-32' ,5806 ,21)
                      ,('379.729.796-80' ,7622 ,24) ,('980.173.363-94' ,13167 ,24) ,('833.285.374-56' ,19581 ,24)
                      ,('103.669.436-50' ,17126 ,4) ,('386.836.124-46' ,18825 ,11) ,('588.404.964-15' ,1545 ,30)
                      ,('600.556.177-18' ,1921 ,7) ,('670.346.230-99' ,18079 ,28) ,('771.352.915-13' ,16581 ,23)
                      ,('430.314.324-46' ,13942 ,24) ,('629.507.759-51' ,17951 ,11) ,('348.683.225-73' ,12424 ,10)
                      ,('406.133.151-17' ,5888 ,30) ,('310.985.894-64' ,17316 ,30) ,('964.317.132-30' ,18818 ,30)
                      ,('845.331.524-14' ,14284 ,13) ,('781.995.738-18' ,19369 ,29) ,('921.558.128-63' ,3206 ,27)
                      ,('941.386.982-65' ,10228 ,26) ,('551.135.290-10' ,18822 ,18) ,('537.124.578-35' ,12670 ,6)
                      ,('119.383.169-76' ,790 ,20) ,('938.473.410-98' ,8851 ,5) ,('279.775.182-54' ,5212 ,20)
                      ,('210.872.954-53' ,13569 ,8) ,('684.995.531-65' ,8649 ,21) ,('653.886.282-57' ,504 ,28)
                      ,('973.580.738-53' ,2533 ,9) ,('285.864.892-85' ,8200 ,21) ,('777.154.423-98' ,10336 ,8)
                      ,('769.786.401-34' ,3233 ,12) ,('521.566.565-97' ,11882 ,14) ,('491.799.681-92' ,653 ,8)
                      ,('344.357.819-36' ,8856 ,18) ,('265.362.581-99' ,8962 ,8) ,('331.410.527-56' ,18516 ,18)
                      ,('143.188.958-61' ,7234 ,29) ,('751.630.472-61' ,13552 ,6) ,('714.707.807-80' ,2898 ,7)
                      ,('585.584.932-83' ,239 ,25) ,('165.554.107-13' ,9572 ,23) ,('718.225.984-87' ,10534 ,25)
                      ,('611.715.653-32' ,3210 ,11) ,('397.994.286-79' ,13651 ,24) ,('967.160.575-69' ,8997 ,25)
                      ,('369.750.998-94' ,13952 ,2) ,('767.400.554-79' ,18320 ,11) ,('171.104.286-74' ,5821 ,21)
                      ,('152.817.649-24' ,3358 ,30) ,('645.308.846-62' ,15176 ,25) ,('273.884.570-92' ,4436 ,13)
                      ,('888.818.341-45' ,15730 ,3) ,('577.836.712-40' ,14670 ,16) ,('513.529.919-95' ,4002 ,1)
                      ,('201.476.809-95' ,17442 ,21) ,('657.816.571-87' ,1582 ,2) ,('810.494.975-87' ,2157 ,9)
                      ,('531.749.410-17' ,12355 ,18) ,('486.290.887-24' ,18576 ,26) ,('432.376.642-62' ,8027 ,23)
                      ,('207.274.437-91' ,5125 ,29) ,('634.244.673-72' ,11387 ,15) ,('346.871.172-72' ,8105 ,23)
                      ,('166.330.605-50' ,7865 ,11) ,('829.181.731-94' ,2425 ,8) ,('197.305.464-63' ,9681 ,8)
                      ,('887.877.706-59' ,15681 ,10) ,('847.598.885-51' ,323 ,23) ,('817.170.984-26' ,5169 ,27)
                      ,('591.397.550-29' ,13362 ,25) ,('872.733.198-95' ,5756 ,18) ,('615.629.238-82' ,11678 ,23)
                      ,('194.782.846-77' ,11044 ,17) ,('146.392.158-88' ,6848 ,4) ,('240.427.458-70' ,3906 ,25)
                      ,('583.662.427-52' ,3306 ,5) ,('841.627.523-64' ,4778 ,4) ,('985.337.216-77' ,15308 ,4)
                      ,('912.410.722-57' ,11683 ,6) ,('700.720.266-23' ,12638 ,21) ,('605.405.529-53' ,3831 ,3)
                      ,('383.256.402-25' ,2599 ,10) ,('248.103.486-68' ,9121 ,1) ,('261.974.594-90' ,2139 ,26)
                      ,('297.126.704-91' ,18529 ,16) ,('680.569.318-52' ,10176 ,23) ,('296.334.647-38' ,225 ,13)
                      ,('200.761.898-70' ,16244 ,20) ,('258.232.687-17' ,19462 ,18) ,('597.295.672-38' ,18840 ,11)
                      ,('894.479.102-52' ,11375 ,12) ,('556.156.341-36' ,16269 ,23) ,('987.874.553-86' ,11253 ,17)
                      ,('248.927.998-94' ,6510 ,1) ,('852.796.660-25' ,2662 ,23) ,('741.370.204-36' ,9303 ,16)
                      ,('536.714.951-95' ,2877 ,23) ,('320.395.830-44' ,14554 ,5) ,('520.645.562-80' ,17547 ,24)
                      ,('553.700.674-28' ,3147 ,14) ,('913.525.896-32' ,17651 ,28) ,('750.456.495-86' ,11524 ,9)
                      ,('246.171.748-38' ,15184 ,4) ,('760.248.897-67' ,4953 ,25) ,('920.890.990-46' ,17172 ,20)
                      ,('805.469.913-50' ,17500 ,21) ,('878.594.225-48' ,6255 ,3) ,('356.715.924-36' ,3454 ,13)
                      ,('847.150.802-96' ,8602 ,22) ,('625.846.640-53' ,10888 ,19) ,('539.300.108-41' ,11225 ,21)
                      ,('549.151.467-76' ,1286 ,21) ,('738.451.908-29' ,18905 ,22) ,('987.288.834-69' ,17533 ,25)
                      ,('898.532.296-94' ,9719 ,11) ,('620.531.607-13' ,13584 ,10) ,('169.415.202-43' ,1871 ,29)
                      ,('757.885.355-97' ,18150 ,28) ,('252.581.376-21' ,2497 ,3) ,('177.937.460-78' ,7178 ,8)
                      ,('523.895.611-54' ,9878 ,26) ,('883.680.201-23' ,16761 ,3) ,('936.678.268-71' ,11017 ,9)
                      ,('871.912.703-73' ,1754 ,9) ,('957.749.478-56' ,6914 ,9) ,('725.636.354-80' ,8605 ,13)
                      ,('898.316.244-33' ,14363 ,12) ,('894.748.325-28' ,2764 ,3) ,('647.106.954-60' ,1482 ,6)
                      ,('628.716.937-98' ,14107 ,8) ,('332.677.483-83' ,19146 ,15) ,('186.870.928-82' ,17050 ,12)
                      ,('216.248.879-71' ,4384 ,16) ,('287.929.269-44' ,4894 ,19) ,('278.335.932-42' ,17220 ,13)
                      ,('824.107.287-13' ,11797 ,7) ,('535.354.954-30' ,9195 ,22) ,('311.762.241-12' ,13871 ,2)
                      ,('209.759.133-88' ,13580 ,21) ,('505.728.766-53' ,16950 ,13) ,('879.471.988-23' ,17427 ,14)
                      ,('772.329.947-39' ,3462 ,8) ,('321.123.241-10' ,2592 ,22) ,('407.342.963-78' ,11435 ,21)
                      ,('786.935.637-47' ,14240 ,9) ,('461.791.351-55' ,142 ,2) ,('770.920.161-42' ,1247 ,24)
                      ,('639.870.185-59' ,6430 ,10) ,('815.943.237-83' ,19550 ,22) ,('141.774.255-61' ,17866 ,13)
                      ,('379.995.400-37' ,9503 ,29) ,('261.103.178-64' ,19167 ,13) ,('495.461.913-57' ,12265 ,29)
                      ,('498.848.750-79' ,14549 ,16) ,('578.770.731-84' ,1462 ,5) ,('408.987.269-72' ,5647 ,28)
                      ,('191.970.336-40' ,6313 ,15) ,('761.137.848-34' ,10654 ,23) ,('810.512.154-21' ,14928 ,1)
                      ,('256.371.788-38' ,7085 ,2) ,('216.401.188-57' ,1531 ,23) ,('956.318.620-43' ,6327 ,22)
                      ,('986.516.478-33' ,3866 ,25) ,('105.665.555-60' ,7118 ,4) ,('259.228.430-72' ,1601 ,8)
                      ,('133.627.971-58' ,10142 ,14) ,('327.988.845-70' ,14985 ,23) ,('363.167.322-63' ,17236 ,7)
                      ,('189.986.406-38' ,16888 ,18) ,('661.194.373-45' ,7824 ,1) ,('805.728.877-53' ,514 ,10)
                      ,('887.826.412-21' ,15977 ,24) ,('122.975.174-32' ,9409 ,25) ,('456.550.370-55' ,19922 ,18)
                      ,('388.243.133-66' ,19785 ,17) ,('208.788.890-61' ,11893 ,22) ,('881.332.662-49' ,6344 ,16)
                      ,('912.349.944-52' ,6858 ,15) ,('534.904.583-32' ,9559 ,11) ,('825.175.334-25' ,19805 ,15)
                      ,('339.191.298-46' ,13325 ,8) ,('569.993.915-78' ,4339 ,15)]

# sua function aqui

# def cliente_inadimplente(lista_devedores):
#     cliente_inadim = []
#     for lista in lista_devedores:
#         cliente, valor, dia = lista
#         if valor > 1000 and dia > 20:
#             cliente_inadim.append(cliente)
#
#     return cliente_inadim
#
#
#
# # rode sua function aqui com a lista dada para ver se está funcionando
#
# print('Foram {} clientes: {}'.format(len(cliente_inadimplente(clientes_devedores)), cliente_inadimplente(clientes_devedores)))





'''Exercícios
Antes de irmos para o desafio que apresentamos na última aula (que é bem mais complexo do que um exemplo simples) 
vamos resolver um exercício um pouco mais simples para treinar

    1. Cálculo do Percentual e da Lista de Vendedores
        Queremos criar uma function que consiga identificar os vendedores que bateram uma meta, mas além disso, consigo 
        já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta (para eu não precisar calcular manualmente depois)
        
        Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas vendas. E me dar 2 respostas: 
        uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a meta.'''


meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}
#
#
# #crie sua function aqui
def caulculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    percentual_bateram_meta = len(bateram_meta) / len(vendas)
    return percentual_bateram_meta, bateram_meta


# aplique sua function nas informações para ver se está funcionando
percentual, vendedores = caulculo_meta(meta, vendas)
# print(vendedores)




'''Como "retornar" mais de um objeto
    É possível retornar 2 "coisas"? 2 listas, 2 strings, 2 números...
        Sim, basta retornar como uma tupla com 2 itens (vamos fazer um exemplo)'''



# def operacoes_basicas(num1, num2):
#     soma = num1 + num2
#     diferenca = num1 - num2
#     mult = num1 * num2
#     divisao = num1 / num2
#     return soma, diferenca, mult, divisao
#
#
#
# print(operacoes_basicas(5,5))



'''Como "retornar" mais de um objeto
É possível retornar 2 "coisas"? 2 listas, 2 strings, 2 números...
Sim, basta retornar como uma tupla com 2 itens (vamos fazer um exemplo)

def operacoes_basicas(num1, num2):
    soma = num1 + num2
    diferenca = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2
    return soma, diferenca, mult, divisao
    
Aplicação:

Data Science e Inteligência Artificial usa MUITO isso.

1. Quando criamos um modelo de previsão, precisamos treinar esse modelo e testar para ver se ele está sendo um bom modelo ou não.
2. Temos então que pegar os nossos dados e dividir em 2 pedaços, uma lista de treino e uma lista de teste.
3. Vamos então pensar no exemplo de um modelo que tenta identificar qual o valor justo de um imóvel de acordo com o tamanho do imóvel. Temos então 2 listas:
    Lista 1: Preços Reais dos Imóveis
    Lista 2: Tamanho do imóvel.
4. Vamos criar então uma função que recebe 2 listas como entrada e que divide cada uma dessas listas em 2, um pedaço de treino e um pedaço de teste. O percentual que a
lista vai ser dividida é definida por um fator (que também vai ser um parâmetro da função)
'''


#exemplo mais simples para facilitar a visualização
precos_imoveis = [2.17 ,1.54 ,1.45 ,1.94 ,2.37 ,2.3 ,1.79 ,1.8 ,2.25 ,1.37]
tamanho_imoveis = [207 ,148 ,130 ,203 ,257 ,228 ,160 ,194 ,232 ,147]

# Vamos definir qual o fator que vamos dividir as listas (ou seja, quantos % da lista vai ficar pra teste. O resto fica pra treino)
#Vamos usar 0.1 (10%)
fator = 0.5

#Isso significa que a lista de teste tem quantos itens?
i = int((1 - fator) * len(precos_imoveis))

#Agora vamos entender qual conta temos que fazer para dividir a lista em 2 listas. Uma com 90% dos valores e outra com 10%
precos_treino = precos_imoveis[:i]
precos_teste = precos_imoveis[i:]
# print(precos_treino)
# print(precos_teste)


# precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37,2.4,1.72,2,1.69,1.63,2.01,2.25,1.61,1.02,1.19,1.86,2.15,2.03,1.61,1.52,1.56,1.69,1.47,1.09,2.47,1.62,2.15,1.81,2.49,2.08,1.02,1.68,1.53,1.2,1.29,1.88,1.92,2.14,1.95,2.48,2.44,1.41,1.98,1.89,1.69,1.95,1.42,1.57,2.32,1.23,1.43,1.35,1.49,2.39,2.37,1.3,2.25,1.5,1.35,2.06,1.05,1.7,2.29,2.44,2.09,1.81,2.04,2.45,1.42,2.09,2.19,2.09,1,2.23,1.39,2,1.29,1.55,1.67,2.06,1.89,2.07,2.39,1.93,1.51,1.73,1.66,1.18,1.13,1.69,2.48,1.26,1.75, 1.51, 1.73]
# tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147,222,165,184,175,147,217,214,171,86,111,180,211,210,168,156,154,179,163,99,246,162,205,195,263,198,121,149,140,122,119,197,210,218,202,258,256,135,203,173,152,197,145,154,252,141,141,151,133,232,229,134,215,155,138,186,120,152,213,256,219,200,210,238,140,224,233,222,120,233,151,185,111,149,186,194,194,222,223,185,157,154,164,129,128,169,240,136,191, 157, 154]
#
# def separar_listas(precos, tamanho, fator=0.1):
#     if len(precos) == len(tamanho):
#         i = int((1 - fator) * len(precos_imoveis))
#         precos_imoveis_treino = precos[:i]
#         precos_imoveis_teste = precos[i:]
#
#         tamanho_imoveis_teste = tamanho[i:]
#         tamanho_imoveis_treino = tamanho[:i]
#         return precos_imoveis_treino, precos_imoveis_teste, tamanho_imoveis_treino, tamanho_imoveis_teste
#
#
#     else:
#         print('As listas de preços e tamanhos dos imoveis não tem a mesma quantidade de itens')
#         return
#
# precos_treino, precos_teste, tamanho_treino, tamanho_teste = separar_listas(precos_imoveis, tamanho_imoveis)
#
# print(precos_teste)
# print(tamanho_teste)





'''Docstring e Annotations


Estrutura - São ferramentas "apenas" para organização:
Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função e também pode ser que a gente precise usar essa mesma função semanas, meses ou até anos depois da sua criação.

Por isso é importante usarmos DocStrings e Annotations



Docstring -> diz o que a função faz, quais valores ela tem como argumento e o que significa cada valor
Annotation -> diz o que devem ser os argumentos e o que a função retorna
Em muitas empresas, o time de tecnologia vai ter um padrão que você deve seguir para isso, mas caso não tenha, vamos te mostrar um padrão bom a ser utilizado.

Docstring:'''


def minha_soma(num1, num2, num3):
    '''Faz a soma de 3 números inteiros e devolve como resposta um inteiro

    Parameters:
        num1 (int): primeiro número a ser somado
        num2 (int): segundo número a ser somado
        num3 (int): terceiro número a ser somado

    Returns:
        soma (int): o valor da soma dos 3 números dados como argumento
    '''
    return num1 + num2 + num3


'''Annotation:


def minha_funcao(arg1: isso, arg2: aquilo) -> o que a função retorna:
    ...
    return ...


def minha_soma(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num'''



'''EXCEÇÕES E ERROS EM FUNÇÕES

COMO "TESTAR" ERROS E TRATAR EXCEÇÕES


try:
    o que eu quero tentar fazer
except:
    o que devo fazer se caso dê erro'''



def descobrir_servidor(email):
    try:
        posicao_a = email.index("@")
    except:
        raise ValueError('Email digitado não tem @, digite novamente')
    else:
        confe = email[posicao_a:]
        if "gmail" in confe:
            return "gmail"
        elif "hotmail" in confe or "outlook" in confe or "live" in confe:
            return "hotmail"
        elif "yahoo" in confe:
            return "yahoo"
        elif 'uol' in confe:
            return 'uol'
        else:
            return "não determinado"
# email = "dhemiongmail.com"
#
# print(descobrir_servidor(email))


'''Cuidado: uma vez dentro do try, qualquer erro vai levar ao except

Como "printar" um erro em uma function 


raise Exception('O erro foi esse')

ou então avisando qual o tipo de erro que ele teve

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse'
'''

# def descobrir_servidor(email):
#     posicao_a = email.index('@')
#     servidor = email[posicao_a:]
#     if 'gmail' in servidor:
#         return 'gmail'
#     elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
#         return 'hotmail'
#     elif 'yahoo' in servidor:
#         return 'yahoo'
#     elif 'uol' in servidor or 'bol' in servidor:
#         return 'uol'
#     else:
#         return TypeError'não determinado'


email = 'dhemisongmail.com'
# print(descobrir_servidor(email))


'''Tratamento Completo:

try:
    tente fazer isso
except ErroEspecífico:
    deu esse erro aqui que era esperado 
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.
'''


'''Quantidade indefinidas de argumentos 
Utilidade:
    Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

estrutura:

*args para positional arguments -> vêm em formato de tupla

def minha_funcao(*args):
    ...
    

**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):
    ...
    '''

def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
# print(minha_soma(25,12,521))


def preco_final(preco, **adicionais):
    """

    :rtype: object
    """
    print(preco,adicionais)
    '''
    Adicione um desconto para o cliente
    '''
    if "desconto" in adicionais:
        preco *= (1 - adicionais["desconto"])
    '''
    Adicione uma garantia extra para o cliente
    '''
    if "garantia_extra" in adicionais:
        preco += adicionais["garantia_extra"]
    '''
    Adicione o preço de imposto
    '''
    if "imposto" in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

# print(preco_final(1000, desconto=0.))

'''ORDEM DOS ARGUMENTOS

Extrutura:

    Sempre os positional arguments vêm antes e depois os keywords arguments.
    Sempre os argumentos individuais vêm antes e depois os "multiplos"
    
def minha_funcao(arg1, arg2, arg3, arg4, *args, k=kwarg, k=kwarg2, k=kwarg3, k=kwarg4, k=kwarg5, **kwargs):
'''

# EXEMPLO
# def minha_soma(*numeros, num1):
#     soma = 0
#     for numero in numeros:
#         soma += numero
#     soma += num1
#     return soma
#
# print(minha_soma(1,5,2, num1 = 5))

                                # EXERCÍCIOS

'''
1. Criando uma Lista de Produtos

Muitas vezes as listas de produtos, de clientes, de funcionários, etc que temos nas empresas não são 100% confiáveis.

Isso significa que na prática, caímos em muitos casos de ter uma lista de produtos, mas quando olhamos por exemplo uma base com a posição em estoque 
de cada produto, surge nessa 
"Base" produtos que não existiam na nossa lista inicial.

Então agora vamos fazer uma function justamente com esse objetivo.

Digamos que você receba, 2, 3, 5 ou até 10 bases com a posição em estoque de vários produtos.

Vamos Criar uma function que pega todas essas listas e cria, a partir dela, uma lista de produtos.
Com o objetivo de saber todos os produtos que temos na empresa. Repare que a function 
pode receber 1, 2, 3 ou quantas listas de estoque forem necessárias.

Obs: Lembre dos "sets" para fazer a lista de produtos não ter produtos repetidos

lista_estoque1 = [
    (produto, qtde_estoque),
    (produto2, qtde_estoque2),
    ...
]
'''
#crie sua function aqui
def listar_produtos(*listas):
    lista_produtos = []
    for lista in listas:
        for produto, estoque, in lista:
            lista_produtos.append(produto)
    lista_produtos = set(lista_produtos)
    lista_produtos = list(lista_produtos)
    return lista_produtos


estoque_fim_jan = [('BSA2199', 396), ('PPF5239', 251), ('BSA1212', 989), ('PPF2154', 449), ('BEB3410', 241),
                   ('PPF8999', 527), ('EMB9591', 601), ('BSA2006', 314), ('EMB3604', 469), ('EMB2070', 733),
                   ('PPF9018', 339), ('PPF1468', 906), ('BSA5819', 291), ('PPF8666', 850), ('BEB2983', 353),
                   ('BEB5877', 456), ('PPF5008', 963), ('PPF3877', 185), ('PPF7321', 163), ('BSA8833', 644),
                   ('PPF4980', 421), ('PPF3063', 757), ('BSA2089', 271), ('BSA8398', 180), ('EMB4622', 515),
                   ('EMB9814', 563), ('PPF3784', 229), ('PPF2398', 270), ('BEB3211', 181), ('PPF8655', 459),
                   ('PPF1874', 799), ('PPF8789', 126), ('PPF6324', 375), ('EMB9290', 883), ('BSA5516', 555),
                   ('BSA8451', 243), ('BSA8213', 423)]
estoque_fim_fev = [('BSA2199', 849), ('PPF5239', 877), ('BSA1212', 336), ('PPF2154', 714), ('BEB3410', 834),
                   ('PPF8999', 201), ('EMB9591', 576), ('BSA2006', 985), ('EMB3604', 615), ('EMB2070', 182),
                   ('PPF9018', 127), ('PPF1468', 212), ('BSA5819', 338), ('PPF8666', 751), ('BEB2983', 363),
                   ('BEB5877', 916), ('PPF5008', 331), ('PPF3877', 744), ('PPF7321', 488), ('BSA8833', 277),
                   ('PPF4980', 530), ('PPF3063', 796), ('BSA2089', 396), ('BSA8398', 478), ('EMB4622', 603),
                   ('EMB9814', 784), ('PPF3784', 434), ('PPF2398', 896), ('BEB3211', 826), ('PPF8655', 748),
                   ('PPF1874', 210), ('PPF8789', 891), ('PPF6324', 250), ('EMB6618', 611), ('BSA3409', 984),
                   ('BSA9866', 870), ('BSA1792', 672)]
estoque_fim_mar = [('BSA2199', 772), ('PPF5239', 394), ('BSA1212', 409), ('PPF2154', 473), ('BEB3410', 831),
                   ('PPF8999', 764), ('EMB9591', 942), ('BSA2006', 482), ('EMB3604', 745), ('EMB2070', 451),
                   ('PPF9018', 608), ('PPF1468', 675), ('BSA5819', 431), ('PPF8666', 795), ('BEB2983', 439),
                   ('BEB5877', 588), ('PPF5008', 442), ('PPF3877', 950), ('PPF7321', 606), ('BSA8833', 464),
                   ('PPF4980', 819), ('PPF3063', 687), ('BSA2089', 253), ('BSA8398', 437), ('EMB4622', 769),
                   ('EMB9814', 178), ('PPF3784', 996), ('PPF2398', 588), ('BEB3211', 247), ('PPF8655', 309),
                   ('PPF1874', 305), ('PPF8789', 878), ('PPF6324', 826), ('EMB6618', 534), ('BSA3409', 705),
                   ('BSA9895', 618), ('BSA4319', 690)]
estoque_fim_abr = [('BSA2199', 647), ('PPF5239', 292), ('BSA1212', 551), ('PPF2154', 802), ('BEB3410', 712),
                   ('PPF8999', 603), ('EMB9591', 963), ('BSA2006', 481), ('EMB3604', 199), ('EMB2070', 635),
                   ('PPF9018', 956), ('PPF1468', 161), ('BSA5819', 787), ('PPF8666', 771), ('BEB2983', 867),
                   ('BEB5877', 539), ('PPF5008', 614), ('PPF3877', 715), ('PPF7321', 336), ('BSA8833', 961),
                   ('PPF4980', 116), ('PPF3063', 876), ('BSA2089', 579), ('BSA8398', 814), ('EMB4622', 434),
                   ('EMB9814', 981), ('PPF3784', 498), ('PPF2398', 498), ('BEB3211', 606), ('PPF8655', 168),
                   ('PPF1874', 518), ('PPF8789', 157), ('PPF6324', 501), ('EMB6618', 932), ('BSA3409', 247),
                   ('BSA9895', 287), ('BSA4319', 477)]
# agora aplique com as listas fornecidas para ver se ela está funcionando
todo_estoque = listar_produtos(estoque_fim_jan, estoque_fim_fev, estoque_fim_mar, estoque_fim_abr)

print(len(todo_estoque))
print(todo_estoque)
