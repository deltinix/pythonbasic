'''
EXERCÍCIO DA AULA 4

Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
E após isso irá imprimir todos os nomes da lista.

'''
import time
convidados = []
qtd_pessoas = int(input('Qtas Pessoas? '))

for i in range(qtd_pessoas):
    print('Convidado ',i)
    nomes = input('Digite o Nome do Convidado:')
    convidados.append(nomes)
    i += 1

print('\nTodos os', qtd_pessoas, 'convidados foram cadastrados!')
time.sleep(2)

pergunta = input('\nDeseja exibir em tela? <S/N> ')

if pergunta == 'S' or pergunta == 's':
    i = 0
    for i in range(qtd_pessoas):
        print(convidados[i])
else:
    print('Saindo do programa...')


