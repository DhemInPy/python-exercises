'''O que é um iterable?

Explicação não programadora

Um iterable é uma estrutura que armazena dados que pode ser "iterada" ou seja, que você pode fazer um loop como um for
dentro dela e ir passando de item a item. É como se fosse um tipo de lista de coisas que você pode ir olhando cada um dos elementos dentro dela.

Até agora as principais que vimos foram:

Listas'''
# print('\nListas:')
# produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
#
# for produto in produtos:
#     print(produto)


'''Strings:'''
# print('\nSTINGS:' )
# texto = 'lira@gmail.com'
#
# for ch in texto:
#     print(ch)



'''Tuplas'''

# print('\nTuplas:')
# produtos = ('iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus')
#
# for produto in produtos:
#     print(produto)

'''Dicionários'''
# print('\nDicionários:')
# vendas_produtos = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
#
# for produto in vendas_produtos:
#     #print(produto)
#     print('{}: {} unidades'.format(produto, vendas_produtos[produto]))
# print('\n')



'''Range
Estrutura:
range(tamanho)
ou

range(inicio, fim)
ou

range(inicio, fim, passo)'''


#uso mais comum no for:
# produtos = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
# estoque = [50, 100, 20, 5, 80]
#
# for i in range(5):
#     print('{}: {} unidades em estoque'.format(produtos[i], estoque[i]))


#range com inicio e fim
# print(range(1, 10))

#vamos olhar no for para entender
# for i in range(1,10):
#     print(i)


'''Exemplo: Modelo Jack Welch da G&E

Classe A: 10% melhor
Classe B: 80% mantém/busca melhorar
Classe C: 10% pior
Quem são os funcionários classe B?'''

# funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
# vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]
#
# print('Funcionário classe B:')
# for i in range(2,18):
#     print('Funcionário {} fez {} vendas.'.format(funcionarios[i], vendas[i]))
#
# print('-'*50)
#
# for i in range(0,18,3):
#     print('Funcionário {} fez {} vendas.'.format(funcionarios[i], vendas[i]))


'''Set
Estrutura:
meu_set = {valor, valor, valor, valor,...}

Observações:
Não pode ter valores duplicados
Não tem ordem fixa'''

# set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}
# print(set_produtos)

'''Aplicação bem útil:

Quantos clientes tivemos na loja?'''

# cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']
# set_cliente = set(cpf_clientes)
# print('temos {} clientes na loja.'.format(len(cpf_clientes)))


'''Métodos de Sets
Esses são os métodos mais usados de set
add -> adiciona um item no set'''
# meu_set = {'iphone', 'macbook', 'ipad'}
# meu_ = meu_set.add('Dhemison')
# print(meu_set)

'''remove -> retira um item de um set'''
# rmv_dhe = meu_set.remove('Dhemison')
# print(meu_set)

'''clear -> retira todos os itens de um set'''
# ret_set = meu_set.clear()
# print(meu_set)

'''union -> junta as informações de 2 sets. Se houver algum valor duplicado, 
ele constará apenas 1 vez no set final'''
# produtos = {'iphone', 'macbook', 'ipad'}
# lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
# todos_os_produtos = produtos.union(lancamentos)
# print(todos_os_produtos)

'''intersection -> pega apenas as informações que existem nos 2 sets ao mesmo tempo'''

# produtos = {'iphone', 'macbook', 'ipad'}
# lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
# intersecao = produtos.intersection(lancamentos)
# print(intersecao)

'''difference -> retorna todas as informações de um set que não fazem parte de outro set'''

produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
produtos_nao_lancamentos = produtos.difference(lancamentos)
print(produtos_nao_lancamentos) #repare que ipad foi retirado do resultado porque ele estava contido no set de lançamentos

























