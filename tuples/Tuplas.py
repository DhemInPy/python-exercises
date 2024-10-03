'''
Tuplas
Estrutura:

tupla = (valor, valor, valor, ...)

Diferença

Parece uma lista, mas é imutável.

Vantagens:

Mais eficiente (em termos de performance)
Protege a base de dados (por ser imutável)
Muito usado para dados heterogêneos
'''

'''Criando tuplas'''
# vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')

# print(vendas)
#
'''Acessando o valor de uma tupla'''
# # vendas[3] = 3000


# cargo = vendas[4]
# salario = vendas[3]
# data = vendas[2]
# data_de_congregacao = vendas[1]
# nome = vendas[0]
# print(salario)

# vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
# nome, data_de_comeco, data_termino, salario, cargo = vendas
# print(data_termino)

'''
o enumerate que vínhamos usando até agora, na verdade, cria uma tupla para a gente. Vamos ver na prática:'''

# vendas = [1000, 2000, 300, 300, 150]
# funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']
#
# for item in enumerate(vendas):
#     i,venda = item
#     print('Funcionário {} vendeu {} unidades. '.format(funcionarios[i], venda))


'''Aplicação de Tupla - Lista de Tuplas

Estrutura:
Além de casos como o do enumerate, em que usamos uma função para transformar itens em tuplas porque isso ajuda 
o nosso código, temos também listas de tuplas como algo comum dentro do Python.

lista = [
    tupla1,
    tupla2,
    tupla3,
    ]
    
ou seja

lista = [
    (valor1, valor2, valor3),
    (valor4, valor5, valor6),
    (valor7, valor8, valor9),
    ]
    
Exemplo:
Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.

Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:'''


# vendas = [
#     ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
#     ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
#     ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
#     ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
#     ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
#     ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
#     ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
#     ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
# ]


'''Qual foi o faturamento de IPhone no dia 20/08/2020?
Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?'''
# produ = []
#
# faturamento = 0
# for venda in vendas:
#     data,produto,cor,capacidade,unidades,preco = venda
#     if data == '20/08/2020' and produto == 'iphone x':
#         faturamento += preco*unidades
#         faturamento_ipad = 'faturamento de {} na data {} foi de {}'.format(produto,data,faturamento )
#
#     if data == '21/08/2020':
#         produ.append(preco)
#         mais_vendido = 'Produto {} foi o mais vendido, {} Unidades '.format(produto, unidades)
#
# print('\n',faturamento_ipad,'\n''\n', mais_vendido)



'''Exercícios'''

'''São exercícios bem parecidos com os que fizemos com listas. Mas na tupla, podemos não só trabalhar com índices, 
mas fazer o "unpacking" das tuplas, o que pode facilitar nossos códigos.'''

'''1. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar)
quais os vendedores que bateram a meta e qual foi o valor que eles venderam.'''

# meta = 10000
# vendas = [
#     ('João', 15000),
#     ('Julia', 27000),
#     ('Marcus', 9900),
#     ('Maria', 3750),
#     ('Ana', 10300),
#     ('Alon', 7870),
# ]
#
# for vendedor, valor_vendido in vendas:
#     if valor_vendido >= meta:
#         print(vendedor,' >> ', f'{valor_vendido:,}')




'''2. Comparação com Ano Anterior
Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano
 de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

A lógica da tupla é: (produto, vendas2019, vendas2020)'''



vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for produto,vendas19,vendas20 in vendas_produtos:
    crescimento = (vendas20 / vendas19 - 1)
    if vendas20 > vendas19:
        print('O produto {} foi maior em 2020 com {} unidades e {} 2019, com o crescimento de {:.1%}.'.format(produto, vendas20,vendas19, crescimento))



















