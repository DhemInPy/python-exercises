# Estruturas de decisão
# Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta. Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.
#
# 1. Faça um Programa que peça dois números e imprima o maior deles.

primeiro_n = int(input('Digite o primeiro numero:'))
segundo_n = int(input('Digite o numero '))

if primeiro_n > segundo_n:
    print('O maior numero é:', primeiro_n)
elif segundo_n > primeiro_n:
    print('O maior numero é:', segundo_n)
else:
    print('Os numeros são iguais')



# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = float(input('Valor: '))
if numero > 0:
    print('{:.0f} é positivo'.format(numero))
elif numero < 0:
    print('{:.0f} é negativo'.format(numero))
else:
    print('O numero é {:.0f}'.format(numero))

# 3. Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil, exemplo:
# Usuário digita: C
# Seu programa deve responder: C - Casado

estado_sivil = input('Qual estado: ')
if estado_sivil == 'C':
    print('C - Casado')
elif estado_sivil == 'S':
        print('S - Solteiro')
elif estado_sivil == 'D':
        print('D - Divorciado')
elif estado_sivil == 'V':
        print('V - Viuvo')

elif estado_sivil == 'O':
        print()
else:
    print('O - Ourtros')


# 4. Faça um Programa que verifique se o e-mail digitado faz parte dos e-mails de spam.
emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"
email = input('Qual email:')

if email in emails_spam:
    print('Tem esse email na caixa de spam')
else:
    print('nao tem esse email na caixa de spam')

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input('1° Nota: '))
nota2 = float(input('2° Nota: '))
media = (nota1 + nota2) / 2


if media == 10:
    print("{:.1f} Aprovado com Distinção".format(media))
elif media > 7:
    print('Aprovado')
else:
    print('Reprovado, A media do aluno foi de {:.0f}'.format(media))



# 6. Faça um Programa que leia o orçamento de 3 empresas e mostre o maior deles.
empresa1 = float(input('Orçamento da esmpresa 1: '))
empresa2 = float(input('Orçamento da esmpresa 2: '))
empresa3 = float(input('Orçamento da esmpresa 3: '))
orcamentos = []
orcamentos.append(empresa1)
orcamentos.append(empresa2)
orcamentos.append(empresa3)
print('O maior orçamento da empresa é de R${}'.format(max(orcamentos)))



# 7. Faça um Programa que leia três orçamentos e mostre o maior e o menor deles.
empresa1 = float(input('Orçamento da esmpresa 1: '))
empresa2 = float(input('Orçamento da esmpresa 2: '))
empresa3 = float(input('Orçamento da esmpresa 3: '))
orcamentos = []
orcamentos.append(empresa1)
orcamentos.append(empresa2)
orcamentos.append(empresa3)
print('O maior orçamento da empresa é de R${} reais. \nO menor orçamento é de R${} reais.'.format(max(orcamentos), min(orcamentos)))



# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1 = input('Digite o nome do produto: ')
preco_p1 = float(input('Preço do produto 1: '))
produto2 = input('Digite o nome do produto: ')
preco_p2 = float(input('Preço do produto 2: '))
produto3 = input('Digite o nome do produto: ')
preco_p3 = float(input('Preço do produto 3: '))
produtos = []
precos = []
produtos.append(produto1)
precos.append(preco_p1)
produtos.append(produto2)
precos.append(preco_p2)
produtos.append(produto3)
precos.append(preco_p3)
maior_preco = max(produtos)
menor_preco = min(precos)
i = precos.index(menor_preco)
loc = produtos[i]
print('Deve comprar o produto {}, pois é o mais em conta de todos, apenas R${} reais;'.format(loc, menor_preco))



# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input('Digite um numero'))
num2 = float(input('Digite um numero'))
num3 = float(input('Digite um numero'))
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.sort(reverse=True)
print(lista)


# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = input('Periodo você eestuda: ')
n = 'Boa noite!'
v = 'Boa tarde!'
m = 'Bom dia!'
periodo = [m, v, n]

if turno == 'M':
    print(periodo[0])
elif turno == 'N':
    print(periodo[2])
elif turno == 'V':
    print(periodo[1])
else:
    print('Periodo inválido ')


# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
# programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
salario_colaborador = float(input('Digite o seu salário: '))

if salario_colaborador > 280:
    if salario_colaborador > 700:
        if salario_colaborador > 1500:
            porcento = 0.05
            valor_aumento = porcento * salario_colaborador
            nv_salario = salario_colaborador + valor_aumento
        else:
            porcento = 0.10
            valor_aumento = porcento * salario_colaborador
            nv_salario = salario_colaborador + valor_aumento
    else:
        porcento = 0.15
        valor_aumento = porcento * salario_colaborador
        nv_salario = salario_colaborador + valor_aumento

else:
    porcento = 0.20
    valor_aumento = porcento * salario_colaborador
    nv_salario = salario_colaborador + valor_aumento

print('O salário antes do reajuste é de: R${:.2f} Reais'.format(salario_colaborador))
print('O valor do aumento foi de: R${:.2f} reais'.format(valor_aumento))
print('O percentual aplicado foi de: {}%'.format(porcento))
print('O novo salario é de: R${:.2f} reais'.format(nv_salario))
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

# Obs: Não vamos nos preocupar tanto com a formatação dos números (nº de casas decimais, por exemplo, veremos isso no próximo módulo)





# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
# quantidade de horas trabalhadas no mês.
# Desconto do IR:

valor_hora = float(input('Digite o valor da hora: '))
hora_trabalhada = float(input('Digite sua hora: '))
salario_usario =  valor_hora * hora_trabalhada


print(salario_usario + total_descontos)

# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
if salario_usario > 900:
    if salario_usario > 1500:
        if salario_usario > 2500:
            salario_usario = salario_usario - 0.2

            print(salario_usario)

        else:
            salario_usario = salario_usario - 0.1
            print(salario_usario)

    else:
        salario_usario = salario_usario - 0.05
        print(salario_usario)

else:
    pass

# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%) : R$ 55,00
# (-) INSS ( 10%) : R$ 110,00
# FGTS (11%) : R$ 121,00
# Total de descontos : R$ 165,00
# Salário Liquido : R$ 935,00
# Obs: Não vamos nos preocupar tanto com a formatação dos números (nº de casas decimais, por exemplo, veremos isso no próximo módulo)




# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.
# dias_dasemana = ['Domingo', 'Segunda-Feira', 'terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo']
dias = [1, 2,3,4,5,6,7]
outro_dia = [8,9,10,11,12,13,14]
diaaa = int(input('Digite o dia: '))

if diaaa >= 7:
    outros_dias = outro_dia.index(diaaa)
    print(dias_dasemana[outros_dias])
else:
    i = dias.index(diaaa)
    print(dias_dasemana[i])





# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# Em seguida, mostre qual conceito o aluno teve. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))
nota_final = nota1 + nota2 / 2
if nota_final >= 4.0:
    if nota_final >= 6.0:
        if nota_final >= 7.5:
            if nota_final >= 9.0:
                if nota_final <= 10.0:
                    print('A')
                else:
                    print('A')
            else:
                print('B')
        else:
            print('C')
    else:
        print('D')
else:
    print('E')
print('O aluno tirou a média de {}'.format(nota_final))




# 15. Você está construindo um calendário para controlar dias de trabalho a pedido do RH. Nessa construção,
# você vai precisar definir quais anos são bissextos e quais não são, para montar o calendário de forma correta.
# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
# Dica para determinar se um ano é bissexto:
# - São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
# - São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400,
# p.ex.: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028...
# - Não são bissextos todos os demais anos.
#
# ex1: 2004 é múltiplo de 4, mas não é múltiplo de 100, então é bissexto.
# ex2: 2000 é múltiplo de 4, mas é múltiplo de 100, só que também é multiplo de 400, então é bissexto
# (porque todo ano múltiplo de 400 é bissexto, independente do resto).
# ex3: 1900 é múltiplo de 4, é múltiplo de 100, mas não é múltiplo de 400, então não é bissexto
#
# Dica: lembre que: numero % 4 é o resto da divisão do número por 4, ex: 10 % 3 = 1 (já que 10/3 = 3 e resta 1)
#
ano = 2028
if ano % 4 == 0:

    print('Ano Bissesto')

elif ano %
else:
    print('Não bissesto')




# 16. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
nota1 = 10
nota2 = 10
nota3 = 10
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    if media >= 9.9:
        print('Aprovado com distinção {:.1f}'.format(media))
    else:
        print('Aprovado {:.1f}'.format(media))
else:
    print('reprovado {:.1f}'.format(media))





# 17. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
peso_de_peixes = 94587
kg = peso_de_peixes / 1000

if kg >= 50:
    menos = kg - 50
    multa = menos * 4.00
    print('O peso é de {} kg, O peso a mais foi de {} kg, a multa aplicada será de R${} reais'.format(kg, menos, multa))
else:
    print('Não terá multa, pois o peso é de {} kg'.format(kg))







# 18. Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.
# Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.
# Dica2: numero % 10 vai te dar o resto da divisão do número por 10.



dinheiro = float(input('Digite a quatia que deseja sacar: '))
notas100 = dinheiro // 100
resto = dinheiro % 100


notas100 = bool(notas100)
if notas100 == True:
    notas100 = dinheiro // 100
    resto = dinheiro % 100
    print('Será {:.0f} notas de 100, restante {} '.format(notas100, resto))
else:
    print('restante {}'.format(resto))


notas50 = dinheiro // 50
resto = dinheiro % 50
notas50 = bool(notas50)

if notas50 == True:
    notas50 = dinheiro // 50
    resto = dinheiro % 50
    print('Será {:.0f} notas de 50, restante {} '.format(notas50, resto))

else:
    print('Restante {}'.format(resto))


notas10 = dinheiro // 10
resto = dinheiro % 10
notas10 = bool(notas50)

if notas10 == True:
    notas10 = dinheiro // 10
    resto = dinheiro % 10
    print('Será {:.0f} notas de 10, restante {} '.format(notas10, resto))

else:
    print('Restante {}'.format(resto))

notas5 = dinheiro // 5
resto = dinheiro % 5
notas5 = bool(notas5)

if notas5 == True:
    notas5 = dinheiro // 5
    resto = dinheiro % 5
    print('Será {:.0f} notas de 5, restante {} '.format(notas5, resto))
else:
    print('Restante {}'.format(resto))

nota1 = dinheiro // 1
resto = dinheiro % 1
nota1 = bool(notas5)

if nota1 == True:
    nota1= dinheiro // 1
    resto = dinheiro % 1
    print('Será {:.0f} notas de 1, restante {} '.format(nota1, resto))
else:
    print('Restante {}'.format(resto))



# 19. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

tel = input("Telefonou para a vítima?")
local = input("Esteve no local do crime?")
moradia = input("Mora perto da vítima?")
devia = input("Devia para a vítima?")
trabalho = input("Já trabalhou com a vítima?")
todo = [tel, local, moradia,devia , trabalho]
sim = todo.count('sim')
if sim >= 2:
    if 3 <= sim <= 4:
       print('cumplice')
    elif 4 < sim < 6:
        print('Assassina')
    else:
        print('Suspeita')
else:
    print('não aparenta ser nada')



# 20. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litro_vendido = float(input('Quanto litro será: '))
tipo_combustivel = input('Digite o tipo de combustivel: ')

if tipo_combustivel == 'A':
    preco_por_litro = 1.90
    if litro_vendido <= 20:
        desconto = 0.03
        preco_por_litro = preco_por_litro * litro_vendido
        desconto = preco_por_litro - desconto
        print('Desconto de', desconto, 'Irá pagar apenas', preco_por_litro, 'Com desconto de', desconto)
    else:
        desconto = 0.05
        preco_por_litro = preco_por_litro * litro_vendido
        desconto = preco_por_litro - desconto
        print('Desconto de', desconto, 'Irá pagar apenas', preco_por_litro, 'Com desconto de', desconto)


elif tipo_combustivel == 'G':
    preco_por_litro = 2.50
    if litro_vendido <= 20:
        print('Desconto de', 0.03)
    else:
        print('Desconto de', 0.06)

else:
    print('Não existe esse combustivel')



# 21. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango_ate_5kg = 2.50
morango_acima_5kg = 2.20
maca_ate_5kg = 1.80
maca_ate_5kg = 1.50
kgmorango = 6.5

if kgmorango > 5:
    print('desconto de :',morango_acima_5kg)

else:
    print('desconto de :',morango_ate_5kg)








# 22. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
# 23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# area = float(input('Informe o tamanho da área a ser pintada em m²: '))
# litros_tinta = area / 6
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.
# Dica: lembre dos operadores // e % mostrados em exercícios anteriores
# Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.
# Dica2: numero % 10 vai te dar o resto da divisão do número por 10.
#
# 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)
# 2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)
# 3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# O custo da lata é 80/18 = 4,44 R$/L
#
# O custo do galão é 25/3,6 = 6,94 R$/L
#
# A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas. Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:
#
# Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.
#
# Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.
#
# Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar 2 galões.
#
# Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.
#
# Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar uma lata.
#
# 3 galões custam 75 reais, 4 galões custam 100 reais. Então, se for possível completar com até 3 galões escolhe-se galões. Qualquer quantidade maior que 3 galões, usa-se latas.
#
# Podemos ir ao exercício:

# Lista de Estrutura Sequencial
# 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.
# 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."
# 3. Faça um Programa que peça dois números e imprima a soma.
# 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
# 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).
# 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
# 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
#
# 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C=59(F−32)
#
# 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F=95C+32
#
# 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# P=72,7h−58
#
# Lembrando que "algoritmo" nada mais é do que um programa, como todos os outros que você vem fazendo
#
# 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#
# a. Para homens:
# P=72,7h−58
#
# b. Para mulheres:
# P=62,1h−44,7
#
#
# 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.


# Calcule o salário bruto (horas * salario por hora)


# Calcule o desconto do IR (11% do salário bruto)

# Calcule o desconto do INSS (8% do salário bruto)


# Calcule o desconto do sindicato (5% do salário bruto)


# Calcule o salário líquido (salário bruto - descontos)


# 13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)


# 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


# Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte.




