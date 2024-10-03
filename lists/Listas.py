
'''Listas em Python'''

'''Estrutura:'''

'''lista = [valor, valor, valor, valor, ...]'''

''''- Lista é um dos objetos mais importantes de Python, por isso vamos trabalhar bastante neles
- Quando importamos uma base de dados para o Python, normalmente ele é lido como uma "lista" ou como alguma "variação de lista"
- Listas em Python foram feitas para serem homogêneas, apesar de aceitarem valores heterogêneos
- Exemplos de Lista:'''

'''Listas de Produtos de uma Loja:'''


# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

"""Lista de Unidades Vendidas de cada Produto da Loja"""

# vendas = [1000, 1500, 350, 270, 900]


# Estrutura:

'''lista = [valor, valor, valor, valor, ...]'''

'''lista[i] -> é o valor de índice i da lista. ''
Obs: Lembre que no python o índice começa em 0, então o primeiro item de uma lista é o item lista[0]'''

'''Para substituir um valor de uma lista você pode fazer:''
lista[i] = novo_valor

Listas de Produtos de uma Loja:'''


'''produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']'''

"""Lista de Unidades Vendidas de cada Produto da Loja"""

'''vendas = [1000, 1500, 350, 270, 900]'''

"""### Nesse caso, as listas funcionam da seguinte forma:

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
              0 ,      1   ,    2   ,     3    ,     4
vendas = [  1000,    1500  ,   350  ,    270   ,    900  ]
"""



'''texto = 'lira@gmail.com'

Como descobrir o índice de um item de uma lista?

i = lista.index('item')

Exemplo:

Digamos que você puxou do Banco de Dados da sua empresa uma lista com todos os produtos que a empresa vende e a quantidade em estoque de todos eles.'''

# produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
# estoque = [100, 150, 100, 120, 70, 180, 80]

'''Nesse caso a lista é "pequena" para fins didáticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.'''

'''E agora, como eu faço para descobrir a quantidade em estoque do produto geladeira?'''

"""Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, 
ele deve ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto"""
# nome = input('informe o produt: ')
# if nome in produtos:
#     i = produtos.index(nome)
#     qntd_estoque = estoque[i]
#     print('Temos {} unidades de {}'.format(qntd_estoque, nome))
# else:
#     print(f'nao temos {nome} em estoque')

"""Listas 04.ipynb
aula 4

# Adicionar e Remover itens de uma lista

Adicionar:
lista.append(item)

Remover:
item_removido = lista.pop(indice)
lista.remove(item)

Digamos que você está construindo o controle de produtos da Apple.
E a Apple lançou o IPhone 11 e irá tirar dos seus estoques o IPhone X
"""

# produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']
# rmv = input('Qual produto deseja remover: ')

# if rmv in produtos:
#     i = produtos.index(rmv)
#     produto_rmv = produtos.pop(i)
#     print('O item removido foi {}'.format(produto_rmv))
# else:
#     print('Não temos {} em estoque'.format(rmv))


"""## Existem 2 formas de tratar o erro:

1. Criar um if para evitar que ele aconteça

2. Esperar que ele possa acontecer e tratar caso o erro aconteça com:

try:
    tentar fazer
except:
    caso dê errado
"""
# rmv = input('Qual produto deseja remover: ')
# try:
#     if rmv in produtos:
#         i = produtos.index(rmv)
#         produto_rmv = produtos.pop(i)
#         print('O item removido foi {}'.format(produto_rmv))
# except:
#     print(rmv)


"""Listas 05.ipynb

# Algumas Funções Básicas de Lista

## Tamanho da Lista

tamanho = len(lista)
"""

# produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']
#
# """- Quantos produtos temos a venda?"""
# qntd = len(produtos)
# print('temos {} produtos a venda'.format(qntd))
#
# """## Maior e Menor Valor
# maior = max(lista)
# menor = min(lista)
# """
# vendas = [1000, 1500, 15000, 270, 900, 100, 1200]
#
# """- Qual o item mais vendido?
# - Qual o item menos vendido?
# """
# mais_vendido = vendas.index(max(vendas))
# print('O mais vendido foi o {}, com {} unidades vendidas'.format(produtos[mais_vendido], vendas[mais_vendido]))
# menos_vendido = vendas.index(min(vendas))
# print('O que foi menos vendido foi o {}, com {} unidades vendidas'.format(produtos[menos_vendido], vendas[menos_vendido]))

"""Listas 06.ipynb
# Juntar Listas, Ordenar e Cuidados Especiais

### 2 formas:

- lista1.extend(lista2)
- lista_nova = lista1 + lista2

Obs: o Método .append não junta listas, mas adiciona um valor no final da lista
"""

# produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
# novos_produtos = ['iphone 12', 'ioculos']
# produtos += novos_produtos
# produtos.append(novos_produtos)
# produtos.extend(novos_produtos)
# nv_lista = produtos + novos_produtos
# print(produtos)

"""### Cuidado:

- [1] + [2] não é a mesma coisa que 1 + 2, então cuidado sempre com o formato dos valores na hora de fazer operações.
"""

# vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
# vendas_iphonex = [15000]
# vendas_iphone11 = [20000]
# vendas_adc = vendas_iphonex + vendas_iphone11
# vendas += vendas_adc
# print(vendas)


"""### Ordenar listas
lista.sort()
"""
# produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
# vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
# produtos.sort()
# vendas.sort(reverse=False)

# print(produtos,'\n', vendas)
# resltado = ['IPad', 'airpods', 'apple tv', 'apple watch', 'iphone 11', 'iphone x', 'mac', 'mac book']
#  [100, 270, 900, 1000, 1200, 1500, 15000, 20000]

"""Listas 07.ipynb

# Print de Listas

2 Opções:
- print "normal"
- método join -> texto.join(lista)
"""
# produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
# produtos = '\n'.join(produtos)
# resultado = apple tv
# mac
# iphone x
# iphone 11
# IPad
# apple watch
# mac book
# airpods

"""Lembrando do método split de strings:
lista = texto.split(separador)
"""
# produtos = 'apple tv, mac, iphone x, iphone 11, IPad, apple watch, mac book, airpods'
# print(produtos.split(','))
# resultado = ['apple tv', ' mac', ' iphone x', ' iphone 11', ' IPad', ' apple watch', ' mac book', ' airpods']

"""List Python - Cartilha de Métodos.ipynb

# Métodos Específicos de Lista em Python

- list.append(valor)
Adiciona um valor ao final de uma lista

Uso:
    vendas = [150, 320]
    vendas.append(110)
Resultado:
    vendas = [150, 320, 110]

- list.extend(lista2)
Adiciona todos os valores da lista2 na lista original

Uso:
    vendas = [150, 320, 110, 450, 390, 370]
    vendas_2semestre = [440, 470, 900, 1000, 1100, 1050]
    vendas.extend(vendas_2semestre)
Resultado:
    vendas = [150, 320, 110, 450, 390, 370, 440, 470, 900, 1000, 1100, 1050]

- list.insert(posicao, valor)
Adiciona um valor em uma posição específica em uma lista. 
Não é recomendado usar a não ser que seja realmente necessário inserir em uma posição específica, porque o método append é mais eficiente.

Uso:
    vendas = [150, 320]
    vendas.insert(1, 110)
Resultado:
    vendas = [150, 110, 320]
Obs:
    Compare com o caso do list.append para ver a diferença

- list.remove(valor)
Remove o valor da lista (apenas a 1ª ocorrência, então caso haja 2 vezes o valor na lista, apenas a 1ª será removida). Além disso, dá um erro caso valor não exista dentro da lista.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.remove('Maria')
Resultado:
    vendedores = ['João', 'Julia', 'Ana', 'Paulo', 'Marcus']

- list.pop(posicao)
Remove o item que está na posicao (índice) passado. Além disso, esse item é dado como resultado do pop, 
portanto pode ser armazenado em uma variável ou usado para outra coisa na mesma linha de código.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.pop(2)
Resultado:
    vendedores = ['João', 'Julia', 'Ana', 'Paulo', 'Marcus']

- list.clear()
Remove todos os itens de uma lista

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.clear()
Resultado:
    vendedores = []

- list.index(valor)
Retorna a posição do valor dentro da lista (em qual índice está o valor). Dá erro caso não haja o valor dentro da lista.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    posicao_Joao = vendedores.index('João')
Resultado:
    posicao_Joao = 0

- list.count(valor)''
Retorna a quantidade de vezes que o valor aparece na lista

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus', 'João']
    qtde_Joao = vendedores.count('João')
Resultado:
    qtde_Joao = 2

- list.sort(reverse=False)''
Ordena os valores da lista em ordem crescente, ou alfabética, (reverse=False) ou decrescente (reverse=True).

Uso:
    vendas = [150, 300, 190, 480]
    vendas.sort(reverse=True)
Resultado:
    vendas = [480, 300, 190, 150]

- list.reverse()''
Inverte a ordem dos elementos de uma lista.

Uso:
    vendas = [150, 300, 190, 480]
    vendas.reverse()
Resultado:
    vendas = [480, 190, 300, 150]

- list.copy()''
Cria uma cópia da lista original. Outra opção é fazer lista2 = lista1[:]

Uso:
    vendas = [150, 300, 190, 480]
    vendas2 = vendas.copy()
Resultado:
    vendas2 = [150, 300, 190, 480]
"""

"""07.07.02 Exercícios Listas.ipynb

# Exercícios

## 1. Faturamento do Melhor e do Pior Mês do Ano
Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""
# meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
# vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
# vendas_1sem.extend(vendas_2sem)
# pior_mes = min(vendas_1sem)
# qntd_vnd = vendas_1sem.index(pior_mes)
# mes_ruim = meses[qntd_vnd]

"""## 2. Continuação
Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""


# print('O pior mês do ano foi {}, com {} unidades vendidas'.format(mes_ruim, pior_mes))
# mes_bom = max(vendas_1sem)
# qntd_vnd = vendas_1sem.index(mes_bom)
# melhor_mes = meses[qntd_vnd]
# print('O melhor mês do ano foi {}, com {} unidades vendidas'.format(melhor_mes, mes_bom))
# Para somar tudo que tem na lista
# fat_total = sum(vendas_1sem)
# print('Ofaturamento total do ano foi de: {:,}'.format(fat_total))
# para pegar o percentual
# percentual = mes_bom / fat_total
# print('A porcentagem anual foi de {:.1%}%'.format(percentual))


"""## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")
Dica: o método remove retira um item da lista.
"""

# produto1 = max(vendas_1sem)
# i = vendas_1sem.index(produto1)
# p1 = vendas_1sem.pop(i)
#
# produto2 = max(vendas_1sem)
# i = vendas_1sem.index(produto2)
# p2 = vendas_1sem.pop(i)
#
# produto3 = max(vendas_1sem)
# i = vendas_1sem.index(produto3)
# p3 = vendas_1sem.pop(i)
#
# top3 = []
# top3.append(p1)
# top3.append(p2)
# top3.append(p3)
# print(top3)

"""Listas 08.ipynb


# Alterações de Variáveis

Estrutura:

- variavel = variavel + outro_valor

ou então

- variavel += outro_valor

Exemplo: vamos adicionar às variáveis criadas o Produto IPad, 500 vendas
"""

# lista = ['mac', 'iphone']
# vendas = [100, 200]

'''#adicionando IPad na lista'''
# nv_produto = ['Ipad']
# lista += nv_produto
# print(lista)


# soma_vendas = 300
'''#adicionando na soma a quantidade de IPad'''
# soma_vendas += 500
# print(soma_vendas)

# email = 'Esse mês vendemos um total de {} produtos, sendo:\n{} unidades de {}\n{} unidades de {}'.format(soma_vendas, vendas[0], lista[0], vendas[1], lista[1])
'''#adicionando no fim do texto o Ipad'''
# email = email + '\n{} unidades de {}'.format(500, lista[2])
# print(email)
# print(lista)


"""Listas 09.ipynb

# Copiar e "Igualdade" de Listas

### Estrutura:

- Quando fazemos:
lista2 = lista1
não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.

- Se quisermos copiar lista devemos fazer
lista2 = lista1.copy()
ou entao
lista2 = lista1[:]

Para entender bem isso, vamos ver na prática:
"""
# lista = ['ipad', 'iphone x', 'apple tv']
# lista2 = lista
# lista[1] = 'iphone 11'
# print(lista2, lista)

"""### Agora copiando:"""

# lista = ['ipad', 'iphone x', 'apple tv']
# lista2 = lista[:]
# lista[1] = 'iphone 11'
# print(lista2[2:], lista)


"""Listas 10.ipynb

# Listas de Listas

### Estrutura:

Cada item de uma lista pode ser qualquer tipo de variável. Inclusive, uma lista.

Quando dentro de uma lista temos cada item como sendo uma outra lista, temos uma "nested list", ou seja, uma lista de listas.

Todas as regras de lista e tudo que vimos até agora funciona exatamente igual, mas vamos ver como isso funciona na prática
"""

# vendedores = ['Lira', 'João', 'Diego', 'Alon']
# produtos = ['ipad', 'iphone']
# vendas = [
#     [100, 200],
#     [300, 500],
#     [50, 1000],
#     [900, 10],
# ]

'''- Quanto João vendeu de IPad?
- Quanto Diego vendeu de IPhone
- Qual o total de vendas de IPhone?'''

# vendas_ipad_joao = vendas[1][0]
# print(vendas_ipad_joao)
#
# vendas_iphone_diego = vendas[2][1]
# print(vendas_iphone_diego)
#
# total_vendas_iphone = vendas[0][1] +  vendas[1][1] +  vendas[2][1] +  vendas[3][1]
# print(total_vendas_iphone)

'''- E se Lira na verdade fez apenas 50 vendas de IPhone, como eu modifico na minha lista o valor de vendas dele?'''
# vendas[0][1] = 50
# print(vendas)

'''- E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em cada um dos vendedores?'''
# produtos.append('mac')
# vendas_mac = [10, 15, 6, 70]
# vendas[0].append(vendas_mac[0])
# vendas[1].append(vendas_mac[1])
# vendas[2].append(vendas_mac[2])
# vendas[3].append(vendas_mac[3])
# print(vendas)


"""07.11 Exercícios Listas.ipynb


# Exercícios

## 1. Mudança de Carga Tributária

- Reformas e mudanças de cargas tributárias são bem comuns no Brasil.

Digamos que você trabalhe em uma empresa de ecommerce

No Brasil, o imposto sobre livros é zerado. 
De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o 
registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.

Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa 
(ou seja, quanto que o imposto vai aumentar de custo para a empresa)

Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário
para qualquer quantidade de livros na sua lista.

Obs2: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa
"""

# produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']
#
# #cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
# produtos_ecommerce = [
#     [10000, 2500],
#     [50000, 40],
#     [7000, 1200],
#     [20000, 1500],
#     [5800, 1300],
#     [7200, 2500],
#     [200, 800],
#     [3300, 700],
#     [1900, 400]
# ]
# qntd = 50000
# preco = 40
# total = qntd * preco
# print('{:,}'.format(total))
#
#
# if 'livro' in produtos:
#     i_livro = produtos.index('livro')
#     total_antigo = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
#     produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
#     novo_total = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
#     print('Vamos pagar de imposto a mais: R$ {:,}'.format(novo_total - total_antigo))


'''Exercício 1
Crie um sistema de cadastro de produtos em uma lista de produtos
Seu sistema deve:
- Pegar o usuário qual produto vai ser cadastrado por meio de um input
- Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
- Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
- Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com 
sucesso e em seguida printar a lista completa'''

# produtos = ["celular", "camera", "fone de ouvido", "monitor"]
#
# novo_produto = input('Qual produto será cadastrado? ')
# novo_produto = novo_produto.casefold()

# if novo_produto in produtos:
#     print("Produto já existente, tente novamente")
# else:
#     produtos.append(novo_produto)
#     print('Produto "{}" cadastrado com sucesso\n'.format(novo_produto), produtos)


'''Exercício 2
Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
       - Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente'''

# produtos = ["celular", "camera", "fone de ouvido", "monitor"]
# precos = [1500, 1000, 800, 2000]
#
# consulta_produto = input('Qual produto procura: ')
# consulta_produto = consulta_produto.casefold()
#
# if consulta_produto in produtos:
#     i_consulta_produto = produtos.index(consulta_produto)
#     preco_produto = precos[i_consulta_produto]
#     print('O produto "{}" custa "R${:,}" reais'.format(consulta_produto, preco_produto))
# else:
#     print("Produto não encontrado, tente novamente")

'''Exercício 3
Crie um sistema de consulta de bônus dos funcionários
Seu sistema deve:
- Pegar o valor de vendas do funcinoário por meio de um input
- Calcular o bônus do funcionário de acordo com a seguinte regra:
      - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
      - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
      - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
- Printar no final o valor do bônus do funcionário
'''
# vendas_func = int(input('Qual foi a venda do funcionário? '))
#
# if vendas_func > 1000:
#     bonus = vendas_func * 2
#
# elif vendas_func > 5000:
#     bonus = vendas_func * 2 + 1000
# else:
#     bonus = 0
#     print('bonus: {}'.format(bonus))



'''Exercício 4
Crie um programa que consiga descobrir qual dos vendedores vendeu mais
As vendas dos vendedores são listas com a quantidade vendida por cada vendedor'''
vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]
# soma0_total = sum(vendas[0])
# soma1_total = sum(vendas[1])
# if soma0_total > soma1_total:
#     print('A mais vendida foi a lista 0 com {} vendidos'.format(soma0_total))
# elif soma1_total > soma0_total:
#     print('A mais vendida foi a lista 1 com {} vendidos'.format(soma1_total))
# else:
#     print('As listas são iguais')