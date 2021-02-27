'''
EXERCÍCIO AULA 7

Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção

Faça outra função que retorna o menor número dessa coleção

'''

numeros = []

n1 = input('Digite o Número 1..:')
numeros.append(n1)
n2 = input('Digite o Número 2..:')
numeros.append(n2)
n3 = input('Digite o Número 3..:')
numeros.append(n3)
n4 = input('Digite o Número 4..:')
numeros.append(n4)
print(numeros)

print('O maior valor é..:', max(int(numero) for numero in numeros))
print('O menor valoe é..:', min(int(numero) for numero in numeros))


