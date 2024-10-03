'''Estrutura de Repetição: for
Funcionamento:

for i in range(n):
    repetir código n vezes

Imagine que você está construindo uma automação para enviar todo dia por e-mail um resumo da produção de uma fábrica.
Construa um código que exiba a quantidade produzida de cada os produto nesse "e-mail"'''

# for i in range(5):
#     print(i)

# produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
# producao = [15000, 12000, 13000, 5000, 250]
#
# tamanho = len(produtos)
# for i in range(tamanho):
#     print('{} unidades  produzidas de {}'.format(producao[i], produtos[i]))

# for i in range(10):
#     print(i)


"""AULA 02"""

'''        For "each"

Estrutura:
O for no Python consegue percorrer uma lista e a cada "loop" retornar o valor do item.'''

'''for i in range(5):
    print(i)

range(5) é na verdade uma lista do tipo: [0, 1, 2, 3, 4]'''

'''Usando para listas:'''

'''for item in lista:
    print(item)

ou então para string:

for ch in texto:
    print(ch)'''

# produtos = ['coca', 'pepsi','futurama',  'guarana', 'sprite','camarada', 'fanta']
# texto = 'lira@gmail.com'
#
# for produto in produtos:
#     print('o produto é {}'.format(produto))
# for ch in texto:
#     print(ch)

'''for + if
Estrutura:

for item in lista:
    if condicao:
        faça alguma coisa
    else:
        outra coisa'''

'''Digamos que a gente esteja analisando a meta de vendas de vários funcionários de uma empresa. A meta de vendas é de 1000 reais em 1 dia.
Temos uma lista com as vendas de todos os funcionários e quero calcular qual o % de pessoas que bateram a meta.'''

# vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
# meta = 1000
#
# qntd_bateu_meta = 0
# for venda in vendas:
#     if venda >= meta:
#         qntd_bateu_meta += 1
# qntd_funcionarios = len(vendas)
# print(qntd_funcionarios)
# print('{:.1%}% funcionarios conseguiram bater a meta'.format(qntd_bateu_meta/qntd_funcionarios))


'''Enumerate
Estrutura:
O enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item.
for normalmente

for item in lista:
    resto do código'''

# funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
# nome = input('Procurando por: ')
# for funcionario in funcionarios:
#     if nome in funcionario:
#         print('Tem {} na lista'.format(funcionario))



'''for i, item in enumerate(lista):
    resto do código'''

# funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
#
# for i, funcionario in enumerate(funcionarios):
#     print('{} é o funcionário {}'.format(i, funcionario))

'''RESULTADO = 
0 é o funcionário Maria
1 é o funcionário José
2 é o funcionário Antônio
3 é o funcionário João
4 é o funcionário Francisco
5 é o funcionário Ana
6 é o funcionário Luiz
7 é o funcionário Paulo
8 é o funcionário Carlos
9 é o funcionário Manoel
10 é o funcionário Pedro
11 é o funcionário Francisca
12 é o funcionário Marcos
13 é o funcionário Raimundo
14 é o funcionário Sebastião
15 é o funcionário Antônia
16 é o funcionário Marcelo
17 é o funcionário Jorge
18 é o funcionário Márcia
19 é o funcionário Geraldo
20 é o funcionário Adriana
21 é o funcionário Sandra
22 é o funcionário Luis'''




'''Exemplo Prático
Vamos pegar um exemplo de nível mínimo de estoque. Em uma fábrica você tem vários produtos e não pode deixar que os produtos fiquem em falta. 
Para isso, foi definido uma quantidade mínima de estoque que os produtos precisam ter:

Identifique quais produtos estão abaixo do nível mínimo de estoque.'''


# estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
# produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
# nivel_minimo = 508
#
# for i, estoq in enumerate(estoque):
#     if estoq > nivel_minimo:
#         print('{}: {} unidades'.format(produtos[i], estoque[i]))

'''RESULTADO:

Tem coca:
1200 unidades

Tem guarana:
800 unidades

Tem skol:
1500 unidades

Tem brahma:
1900 unidades

Tem agua:
2750 unidades

Tem vinho branco:
1100 unidades

Tem tequila:
999 unidades

Tem champagne:
900 unidades

Tem gin:
880 unidades

Tem guaracamp:
870 unidades

Tem leite de castanha:
1111 unidades

Tem fanta:
800 unidades'''



# produtos = ["iphone", "ipad", "airpod", "macbook"]
# precos = [7000, 10000, 2500, 14000]





'''Exercícios
1. Criando um Registro de Hóspedes
Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, 
os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

    1- Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)

    2- De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa,
         a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
         
    3- O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o 
        nome da pessoa e o cpf da pessoa, assim:'''

'''quarto = [
    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],
]'''

'''Para simplificar, não vamos nos preocupar com possibilidades de ("tentar colocar mais de 1 hóspede, digitar o cpf errado, etc.  "
"Nosso objetivo é treinar a criação de uma rotina de cadastro)'''

# qntd_pessoas = int(input('Quantas pessoas? '))
# quarto = []
# for i in range(qntd_pessoas):
#     nome = input('Nome:')
#     cpf = int(input('Cpf: '))
#     hospede = [nome, 'Cpf: {}'.format(cpf)]
#     quarto.append(hospede)
# print(quarto)



'''2. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar)
quais os vendedores que bateram a meta e qual foi o valor que eles venderam.'''

# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]
#
# #seu código aqui
# for venda in vendas:
#     if venda[1] >= meta:
#         print(venda[0],'Bateu a meta de',venda[1])


'''3. Comparação com Ano Anterior
Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

Dica: lembre do enumerate, ele pode facilitar seu "for"'''

# produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
# vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
# vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
# #seu código aqui
#
# for i, produto in enumerate(produtos):
#     if vendas2019[i] > vendas2020[i]:
#         crescimento = vendas2020[i] / vendas2019[i] - 1
#         print('{} Vendeu R${:,} em 2019, R${:,} em 2020 e teve {:.1%}% de crescimento'.format(produto, vendas2019[i], vendas2020[i], crescimento))



'''For dentro de For
Quando temos listas dentro de listas, às vezes precisamos fazer um "for dentro de for"

for item in lista: 
    for item2 in lista2:
        codigo aqui

Vamos pegar um exemplo de nível mínimo de estoque. Em uma fábrica você tem vários produtos e não pode deixar que os produtos fiquem em falta. Para isso, foi definido uma quantidade mínima de estoque que os produtos precisam ter:

Identifique quais fábricas tem algum produto abaixo do nível de estoque

Agora ao invés de analisar o estoque de apenas 1 fábrica, vamos analisar o estoque de várias fábricas'''


estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
]
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50
fabricas_abaixo_nivel = []

for i, lista in enumerate(estoque):
    print(fabricas[i], lista)

'''Exercícios
1. Calculando % de uma lista
Faremos algo parecido com "filtrar" uma lista. 
Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta,
eu quero conseguir calcular o % de vendedores que bateram a meta. 
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.'''


#
# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]



'''Vamos resolver de 2 formas:
Criando uma lista auxiliar apenas com os vendedores que bateram a meta
Fazendo o cálculo diretamente na lista que já temos'''


'''lista auxiliar'''
#seu código aqui
# acima_meta = []
# for venda in vendas:
#     if venda[1] >= meta:
#         acima_meta.append(venda)
# print(acima_meta)

# resultado: [['João', 15000], ['Julia', 27000], ['Ana', 10300]]
# 50.0% dos vendedores bateram a meta
# print('{:.1%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))

'''cálculo diretamente na lista'''
# qntd_vendedores_acima_meta = 0
# for venda in vendas:
#     if venda[1] >= meta:
#         qntd_vendedores_acima_meta += 1
#
# print('{:.1%} dos vendedores bateram a meta'.format(qntd_vendedores_acima_meta / len(vendas)))



'''Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?'''

# maior_venda = 0
# melhor_vendedor = ''
#
# for venda in vendas:
#     if venda[1] > maior_venda:
#         maior_venda = venda[1]
#         melhor_vendedor = venda[0]
# print('O melhor vendedor foi {} com {} unidades vendidos'.format(melhor_vendedor, maior_venda))


'''Formas de interromper um for
2 Opções:
break -> interrompe e finaliza o for
continue -> interrompe e vai para o próximo item do for'''

# vendas = [100, 150, 1500, 2000, 120]

'''Caso 1: Se todas as vendas forem acima da meta, a loja ganha bônus'''
# meta = 110

# for venda in vendas:
#     if venda > meta:
#         print('Não ganha bonus')
#         break
#     print(venda)


'''Caso 2: Exiba quem bateu a meta'''

# vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']
# meta = 130
#
#
# for venda in vendas:
#     if venda < meta:
#         continue
#     print(venda)


'''Exercicios'''


'''Listas
Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta.
Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.'''

"""1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média
de vendas."""

# vendas = [1000, 1500, 1200, 1300]
# vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]
#
# for i, venda in enumerate(vendas):
#     print('Vendedor: {}, Vendas: {}'.format(vendedores[i], vendas[i]))
# media = sum(vendas) / len(vendas)
# print('Média: {}'.format(media))


'''2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a 
quantidade de alunos com média maior que 7.'''

# alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
# notas = [
#     [10, 9, 8, 8],
#     [9, 7, 6, 4],
#     [10, 10, 10, 10],
#     [5, 3, 10, 9],
#     [7, 6, 6, 6],
#     [7, 7, 8, 7],
#     [7, 7, 7, 9],
#     [8, 5, 6, 7],
#     [10, 9, 7, 4],
#     [10, 1, 3, 3],
# ]


# medias = []
# for i in range(len(notas)):
#     media = sum(notas[i]) / len(notas[i])
#     medias.append(media)
#     print(alunos[i], f'{media}')

# qntd_alunos = 0
# for media in medias:
#     if media >= 7:
#         qntd_alunos += 1
# print(f'{qntd_alunos} alunos tiveram nota maior ou igual a 7')

'''3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com 
mais de 25 anos possuem salário inferior à média de todos os salários.'''

# idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
# salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]
#
# media = sum(salarios) / len(salarios)
# print('media: {}'.format(media))
# funcionarios = 0
# print('Valor do funcionarios antes de entrar no "FOR": {}'.format(funcionarios))
# for i, idade in enumerate(idades):
#     if idade > 25 and salarios[i] < media:
#         funcionarios += 1
#         print('valor da idade: {}'.format(idade))
#     # print('Valor do funcionarios dps de entrar no "FOR": {}'.format(funcionarios))
#
# print('São {} Funcionarios com mais de 25 anos'.format(funcionarios))


'''4.Em quais meses a média de temperatura foi maior do que a média nacional?'''

# meses = [
#     'Janeiro',
#     'Fevereiro',
#     'Março',
#     'Abril',
#     'Maio',
#     'Junho',
#     'Julho',
#     'Agosto',
#     'Setembro',
#     'Outubro',
#     'Novembro',
#     'Dezembro'
# ]
#
# temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]
#
# media_nacional = sum(temperaturas) / len(temperaturas)
# print('Média nacional:', media_nacional)
# for i, mes in enumerate(meses):
#     if temperaturas[i] > media_nacional:
#         print(f'mes:{mes}: {temperaturas[i]} graus')



'''5. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou.
 Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
 chegou-se a seguinte forma de cálculo:
. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
O programa dever'''

'''O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.
Projeção de Gastos com Abono
============================ '''

# lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
# abonos = []
# print('Salario - Abono')
# conta_min = 0
#
# for salario in lista_salarios:
#     abono = salario * 0.2
#     if abono < 100:
#         abono = 100
#     abonos.append(abono)
#     if abono == 100:
#         conta_min += 1
#     print(f'R${salario} -- R${abono}')
#
# qntd = len(lista_salarios)
# total = sum(abonos)
# maximo = max(abonos)
#
# print('Foram processados', qntd, 'colaboradores')
# print(f'total gasto com abonos: R${total:.2f}')
# print('Valor minimo pago a', conta_min, 'colaboradoes')
# print(f'Maior valor de abono pago: R$ {maximo:.2f}')


'''6. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
Calcule e mostre:'''
'''
    a. O modelo do carro mais econômico;
    b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
    considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.
     O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.'''

# print('Comparativo de Consumo de Combustível')
# veiculos = ['fusca',' gol', 'uno', 'vectra', 'peugeot']
# autonomias = [7, 10, 12.5, 9, 14.5]
#
# print('Relatorio final')
# for i, autonomia in enumerate(autonomias):
#     print(f'{i+1} - {veiculos[i]} - {autonomia:.1f} - {1000/autonomia:.2f} - R${1000/autonomia* 2.25:.2f}')


'''7. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine
quantos vendedores receberam salários nos seguintes intervalos de valores:
200−299  300-399 400-499 500−599 600−699 700−799 800−899 900−999 $1000 em diante'''

'''Existem várias formas de fazer. Faça primeiro da forma que parecer mais intuitiva para você.'''
'''Em seguida, caso queira um desafio: Desafio: Crie uma forma para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''

# vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
# faixas = []
# menores_que_mil = 0
# tamanho_faixas = 100
# qtde_faixas = 9
#
# for venda in vendas:
#     bonus = venda * 0.09
#     salario = 200 + bonus
#     print(salario)
#     faixa = int(bonus / tamanho_faixas) + 1
#     faixas.append(faixa)
#
# for i in range(qtde_faixas - 1):
#     print(f'Entre {i * 100 + 200} e {i * 100 + 299}:', faixas.count(i + 1))
#     menores_que_mil += faixas.count(i + 1)
#
# print('Mais que mil:', len(vendas) - menores_que_mil)


