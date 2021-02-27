minha_lista = ['Jose', 'Maria']  #LISTA (list)

minha_tupla = ('Maria', 'Jose')  #TUPLA NAO É MUTÁVEL IGUAL A LISTA. NÃO CONSIGO REMOVER OU ADICIONAR OBJETOS DENTRO DA LISTA
                                 # USAR A TUPLA QUANDO TIVER UM CONJUNTO DE INFORMAÇÕES QUE NÃO IRÃO SE ALTERAR

meu_dicionario = {'Nome': 'Ricardo', 'Idade': 27}   # DICT - Dicionário - Composto por uma chave e um valor


meu_conjunto = {'Ricardo', 'João'}  #Em um conjunto não pode ter itens repetidos. O conjunto é dinâmico igual a lista
                                    #Conjunto não é ordenado, não tem índice

# Tudo isso acima são coleções ou estrutura de dados

print(type(minha_tupla))
print(minha_tupla)

print(minha_tupla[0])
print(minha_tupla[1])

for nome in minha_tupla:
    print(nome)

minha_tupla = ('Ricardo', 'Pereira')
print(minha_tupla)

# Perguntando se um objeto tá lá dentro ou não da LISTA/TUPLA

if 'Josefina' in minha_tupla:
    print('Ricardo está na Tupla')
else:
    print('Ricardo não está na Tupla')


# Perguntando se um objeto tá lá dentro ou não do Dicionário


print(meu_dicionario['Nome'])


# LISTA E TUPLA POSSUEM INDICE (0,1,2,3) mas no dicionário não!!!
# PARA BUSCAS, O DICIONÁRIO É MUITO MAIS EFICIENTE, É MAIS ESTRUTURADO OS DADOS.


print(len(meu_dicionario))

#O LEN pode ser usado para qualquer conjunto


if 'Ricardo' in meu_dicionario.values():
    print('Ricardo está no dicionário')
else:
    print('Ricardo não está no dicionário')


for valores in meu_dicionario.values():
    print(valores)

for valores in meu_dicionario.keys():
    print(valores)

meu_dicionario ['Nome'] = 'Lucas'
print(meu_dicionario)

meu_dicionario ['Endereco'] = 'Avenida Antonio Barros, 223'
meu_dicionario ['Telefone'] = 19971204004
print(meu_dicionario)

# ==================================================================
# MEU CONJUNTO
# ==================================================================

print(meu_conjunto)
meu_conjunto.add('Maria')
print(meu_conjunto)

# NO CONJUNTO NÃO REPETE DADOS

if 'Ricardo' in meu_conjunto:
    print('Ricardo encontrado no Meu Conjunto')
else:
    print('Ricardo não encontrado no conjunto!!')

# EM UM PROGRAMA REAL - VERDADEIRA A DIFERENÇA É MUITO GRANDE ENTRE CONJUNTO E LISTA
# NA LISTA O PYTHON PERCORRE A LISTA INTEIRA PROCURANDO O OBJETO
# JÁ NO CONJUNTO ELE É UMA TABELA HASH QUE É CONVERTIDO EM NÚMERO E É CARREGADO NA MEMÓRIA, OU SEJA,
# MESMO QUE TENHA 1 BILHÃO DE ITENS, O RESULTADO DA BUSCA É PRATICAMENTE INSTANTÂNEO
# QUANDO TIVER QUE PESQUISAR EM UMA ESTRUTURA DE DADOS MUITO GRANDE VOCÊ USA DICIONÁRIO OU CONJUNTO AO INVÉS DE LISTA
# A LISTA É SEQUENCIAL, OU SEJA, DEMORA DEMAIS ATÉ ENCONTRAR O OBJETO

print(meu_conjunto)
meu_conjunto.remove('Ricardo')
print(meu_conjunto)

# COMO INICIALIZAR VAZIO

lista = []
tupla = ()
dicionario = {}
conjunto = set()

loucura = [(1,2), (3,4), (5,6), ({'João', 'Maria'}), ({'Gabriel'})]

# NO EXEMPLO ACIMA VOCÊ PODERÁ COLOCAR UMA ESTRUTURA DENTRO DA OUTRA

print(loucura)