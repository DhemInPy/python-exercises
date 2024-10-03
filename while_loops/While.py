'''Estrutura while:
Funcionamento:
Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.

A lógica é: enquanto a condição for verdadeira, o while executa o código. Assim que ela terminar de ser verdadeira, o código "sai" do while.'''

'''while condicao:
    repete esse código'''

'''Exemplo: Quando criamos automações na internet
Exemplo2: Crie um programa que funcione como o registro de vendas de uma empresa.'''

'''Nele, a pessoa deve inserir o nome do produto e o produto deve ser adicionado na lista de venda.'''
'''Enquanto o usuário não encerrar o programa, significa que ele está registrando novos produtos, '''
'''então o programa deve permitir e entrada de quantos produtos o usuário quiser.'''



# venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
# vendas = []
# #crie aqui o programa
#
# while venda != '':
#     vendas.append(venda)
#     venda = input('Registre um produto. ')
#
# print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))

'''Exemplo: 
Digamos que temos uma lista de vendedores e as quantidades vendidas e 
queremos identificar todos os vendedores que bateram a meta de 50 vendas.'''

# vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
# vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
# meta = 80
#
# nv_lista = []
# i = 0
# while vendas[i] >= meta:
#     print(vendedores[i],'bateu a meta de', vendas[i])
#     i += 1


'''Exercícios
1. Input até o usuário parar

Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.

O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.

Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha.
Sugestão para sua lista de produtos vendidos:
'''

vendas =[
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]
estoque = []

while True:
    produto = input('Produto: ')
    if not produto:
        break
    qntd = int(input('Quantidade: '))
    estoque.append([produto, qntd])

print(estoque)




















