
# Condições no Python -> If

## Estrutura:

### Uso mais simples:

'''if condição:
    o que fazer caso a condição seja verdadeira'''

### Exemplo Real (informações 100% hipotéticas e inventadas):

'''Digamos que você trabalha na Amazon (que tem centenas de milhares, se não milhões de produtos) e está analisando o resultado de vendas dos produtos.

Você precisa criar um programa que vai analisar o resultado de vendas dos produtos da Amazon em um mês. Para simplificar vamos pensar em um único produto: um Iphone.

Meta de Vendas do Iphone = 50.000 unidades<br>
Quantidade vendida no Mês = 65.300 unidades

O seu programa deve avisar (usaremos o print por enquanto) caso o produto tenha batido a meta do mês. Então devemos fazer:<br>
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, o seu programa não deve fazer nada'''
"""

meta = 50000
qtde_vendida = 65300

if qtde_vendida > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendida))

"""### Tratando a condição falsa:
'''Quando usamos o if, nem sempre queremos apenas analisar o caso verdadeiro, em boa parte das vezes queremos fazer alguma coisa caso a condição seja verdadeira e fazer outra coisa caso a condição seja falsa.

Nesse caso usaremos:

if condição:
    o que eu quero fazer caso a condição seja verdadeira
else:
    o que eu quero fazer caso a condição seja falsa

Voltando ao nosso Exemplo Real da Amazon e do Iphone, agora nossa programa deve avisar nos 2 casos:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, devemos exibir a mensagem: "Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades"'''
"""

meta = 50000
qtde_vendida = 15000

if qtde_vendida > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendida))
else:
    print('Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades'.format(qtde_vendida, meta))

###### Aula 2  ######

# Blocos e Identação

## Estrutura
Sempre que usamos o if ou qualquer outra estrutura no Python, devemos usar a identação para dizer para o Programa onde a estrutura começa e onde ela termina.

Isso vai ajudar muito quando tivermos mais de 1 condição ao mesmo tempo e quando tivermos várias ações para fazer dentro de um if.

### Várias ações em 1 if:

if condicao:
    alguma coisa
    outra coisa
    outra coisa mais
    outra coisa ainda mais
else:
    uma coisa
    uma coisa mais
    coisa final

## Exemplo
Vamos fazer um novo exemplo abaixo:

Digamos que você precisa criar um programa para um fundo de investimentos conseguir avaliar o resultado de uma carteira de ações e o quanto de taxa deverá ser pago.

A regra desse fundo de investimentos é:

- O fundo se compromete a entregar no mínimo 5% de retorno ao ano.
- Caso o fundo não consiga entregar os 5% de retorno, ele não pode cobrar taxa dos seus investidores.
- Caso o fundo consiga entregar mais de 5% de retorno, ele irá cobrar 2% de taxa dos seus investidores.
- Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa dos seus investidores.
"""

meta = 0.05
taxa = 0
rendimento = 0.25

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print('A taxa foi de {}'.format(taxa))
    else:
        taxa = 0.02
        print('A taxa foi de {}'.format(taxa))
else:
    taxa = 0
    print('A taxa foi de {}'.format(taxa))

"""### Mais de uma condição ao mesmo tempo:

if condicao_1:
    o que fazer se a condição 1 for verdadeira
    if condicao_2:
        o que fazer se a condição 1 e 2 for verdadeira
    else:
        o que fazer se a condição 2 for falsa (mas a condição 1 é verdadeira)
else:
    o que fazer se a condição 1 for falsa

## Cuidado importante: repetição de código

Sempre que possível, evite repetir código. De forma geral:<br>
"Se você está repetindo um código, existe uma forma melhor de fazer"
"""

#### Aula 3 ####

# elif

'''E se temos mais do que um caso de sim e não?

E se tivermos 3 casos?

Usamos o elif da seguinte forma:

if condição:
    o que fazer se a condição 1 for verdadeira
elif condição_2:
    o que fazer se a condição 1 for falsa e a condição 2 for verdadeira
else:
    o que fazer se a condição 1 e a condição 2 forem falsas'''

### Exemplo:

'''Vamos criar um programa para analisar o bônus dos funcionários de uma empresa (pode parecer "simples", mas uma empresa como a Amazon tem 900.000 funcionários)

Para os cargos de vendedores, a regra do bônus é de acordo com a meta de vendas da pessoa:

Se ela vendeu abaixo da meta dela, ela não ganha bônus.

Se ela vendeu acima da meta dela, ela ganha como bônus 3% do valor que ela vendeu.

Se ela vendeu mais do que o dobro da meta dela, ela ganha como bônus 7% do valor que ela vendeu.

Vamos criar um programa para avaliar uma pessoa que tinha como meta de vendas 20.000 reais e calcular o bônus dela de acordo com o valor de vendas que ela tiver.'''


meta = 20000
vendas = 15000

if vendas < meta:
    print('Não ganhou bônus')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print('Ganhou {} de bônus'.format(bonus))
else:
    bonus = 0.03 * vendas
    print('Ganhou {} de bônus'.format(bonus))


### Aula 4 ###
'''
# Comparadores

==    igual
!=    diferente
>     maior que (>= maior ou igual)
<     menor que (<= menor ou igual)
in    texto existe dentro de outro texto
not   verifica o contrário da comparação

Obs: Se em alguma condição você não quiser fazer nada, você pode simplesmente escrever:
pass
"""

faturamento_loja_1 = 2500
faturamento_loja_2 = 2200
email = "liragmail.com"

print('Programa 1')
if faturamento_loja_1 == faturamento_loja_2:
    print('Os faturamentos são iguais')
else:
    print('Os faturamentos são diferentes')

print('Programa 2')
if email != 'lira@gmail.com':
    print('Esse não é o email do Lira')
else:
    print('Email errado')

print('Programa 3')
email_usuario = input('Insira seu e-mail:')
if not '@' in email_usuario:
    print('Email Inválido')
else:
    pass

#### Aula 5 ####

# Casos com várias condições/comparações

### Estrutura:

'''Quando temos várias comparações, ao invés de criar if dentro de if podemos usar os operadores "and" e "or" para tratar essas condições.

Funciona assim:

if condicao_1 and condicao_2:
    vai ser executado se as 2 condições forem verdadeiras ao mesmo tempo

outro caso:

if condicao_1 or condicao_2:
    vai ser executado se pelo menos uma das condições forem verdadeiras'''

### Exemplo

Vamos voltar ao exemplo de cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcionário e também com o resultado da empresa como um todo.

Nesse caso, a regra funciona da seguinte forma:
- Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas da loja, o funcionário ganha 3% do que ele vendeu em forma de bônus.
- Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um todo, o funcionário não ganha bônus.'''

"""
meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 0

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')

"""### Outro exemplo

'''Agora vamos levar essa análise mais a fundo.

Nessa empresa, existe um outro caso também que garante que o funcionário ganhe um bônus, independente das vendas que ele fez naquele mês.

Todo mês os diretores da empresa fazem uma avaliação qualitativa de todos os funcionários. Nessa avaliação os diretores dão uma nota de 0 a 10 para cada funcionário. Se a nota do funcionário for 9 ou 10, ele também ganha o bônus de 3% do valor de vendas. (os bônus não são cumulativos)'''

"""
nota_funcionario = 5
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionario foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')


# Exercícios com if

## 1. Cálculo de Bônus

- Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas.<br>
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.<br>
Caso contrário o valor de bônus do funcionário é 0.<br>
Print o bônus dos 3 funcionários
"""

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

#crie seu código aqui
if vendas_funcionario1 >= 1000:
    print('O funcionário 1 ganhou {} de bônus'.format(vendas_funcionario1 * 0.1))

if vendas_funcionario2 >= 1000:
    bonus = vendas_funcionario2 * 0.1
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))

if vendas_funcionario3 >= 1000:
    bonus = vendas_funcionario3 * 0.1
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 270 de bônus

## 2. Cálculo de bônus com uma nova regra

- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas<br>
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

Use as mesmas variáveis de vendas_funcionários
"""

#crie seu código aqui
#obs: há 2 formas de fazer, com if dentro de if ou então com if e elif. Escolha a que você preferir

if vendas_funcionario1 >= 1000:
    if vendas_funcionario1 >= 2000:
        bonus = 0.15 * vendas_funcionario1
    else:
        bonus = 0.1 * vendas_funcionario1
else:
    bonus = 0
print('O funcionário 1 ganhou {} de bônus'.format(bonus))

#2ª maneira -> if e elif

if vendas_funcionario2 >= 2000:
    bonus = 0.15 * vendas_funcionario2
elif vendas_funcionario2 >= 1000:
    bonus = 0.1 * vendas_funcionario2
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))


if vendas_funcionario3 >= 1000:
    if vendas_funcionario3 >= 2000:
        bonus = 0.15 * vendas_funcionario3
    else:
        bonus = 0.1 * vendas_funcionario3
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 405 de bônus
"""



#### Aula 6 ####


# Comparações Contraintuitivas

'''Existem algumas comparações no Python que não são tão intuitivas quando vemos pela primeira vez, mas que são muito usadas, principalmente por programadores mais experientes.

É bom sabermos alguns exemplos e buscar sempre entender o que aquela comparação está buscando verificar.
'''
### Exemplo 1:

'''Digamos que você está construindo um sistema de controle de vendas e precisa de algumas informações para fazer o cálculo do resultado da loja no fim de um mês.'''

"""
faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de {} reais".format(lucro))
else:
    print('Preencha o faturamento e o lucro corretamente')

"""

## Resumo


''' Algumas comparações contraintuitivas muito usadas:

If 0:

If '':

Temos outras também, mas que são usadas para verificar listas vazias, dicionários vazios, objetos vazios e assim vai. Quando chegarmos nesses módulos vamos relembrar esse conceito, mas o importante é saber dessa possibilidade e entender seu uso.'''

"""
#### Aula 7#####

# Exercícios

## 1. Criando um mini sistema de controle de estoque

- Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
- Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
- Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

- alimentos -> Estoque mínimo: 50
- bebidas -> Estoque mínimo: 75
- limpeza -> Estoque mínimo: 30

Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.<br>
Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.<br>
Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.
"""

#seu código aqui
produto = input('Qual o produto?')
categoria = input('Qual a categoria do produto?')
qtde = input('Qual a quantidade atual do produto?')

if produto and categoria and qtde:
    qtde = int(qtde)
    if categoria == 'bebidas':
        if qtde < 75:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    elif categoria == 'limpeza':
        if qtde < 30:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    else:
        if qtde < 50:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
else:
    print('Preencha todas as informações')
