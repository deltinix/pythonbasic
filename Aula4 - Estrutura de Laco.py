import time
nomes = ['Ricardo', 'Dalziro', 'Sérgio', 'Tatiane', 'Tiago', 'Elerson', 'Edenir', 'Marcia', 'Fabricio', 'Rosana']
lista_de_numeros = range(6)      #Imprime 6 números
lista_de_numeros2 = range(5, 10)  #Imprime de 5 a 10
lista_de_numeros3 = range(0, 100, 2) #Imprime de 0 a 100 de 2 em 2
palavra = 'Ricardo Rocha'
lista_de_frutas = ['Pera', 'Uva', 'Abacaxi', 'Laranja', 'Goiaba', 'Ameixa']
contador = 0

for fruta in lista_de_frutas:   # Exibe a quantidade de itens dentro da lista
    contador += 1
print(contador)

time.sleep(2)

print(len(lista_de_frutas))

time.sleep(2)

print('\n')

numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

time.sleep(5)

print('\n')
print(nomes)
print(nomes[0])
for nome in nomes:
    print(nome)

print('\n')

for i in lista_de_numeros:
    print(i)

print('\n')

for a in lista_de_numeros2:
    print(a)

print('\n')

for b in lista_de_numeros3:
    print(b)

print('\n')
for i in range(10):
    print(nomes[i])

print('\n')
for i in nomes:
    print(i)

print('\n')
for i in range(len(nomes)):   # len nomes retorna o número 10
    print(nomes[i])
    nomes.append('OII')
print(nomes)

print('\n')
for i in palavra:
    print(i)


i = 0

while i < 10:
    print('i ainda é menor do que 10')
    i = i+1
print('i agora é maior ou igual a 10')

print('\n')

while True:
    print('Loop infinito', i)
    i = i + 1


i = 0
i = i + 1
i =+ 1   #Sempre adiciona +1 pro i, semelhante à linha acima

'''
EXERCÍCIO DA AULA 4

Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
E após isso irá imprimir todos os nomes da lista.

'''