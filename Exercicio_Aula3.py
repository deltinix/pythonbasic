'''
EXERCÍCIO DA AULA 3

Faça um programa que pergunte a idade, o peso e altura de uma pessoa
e decide se ela está apta a ser do exército)

Para entrar no exército tem que ter mais de 18 anos
mais de 60kg e mais ou igual a 1.70 metros.

'''

print('==============================================')
print('============ EXÉRCITO BRASILEIRO =============')
print('==============================================')
print('Você está apto para o Exército?\n')
idade = int(input('Digite a sua Idade..:'))
peso  = int(input('Digite o seu Peso...:'))
altura= float(input('Digite a sua Altura.:'))
print('\n')

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Parabéns! Você está apto a entrar para o Exército Brasileiro')
else:
    print('Desculpe! Você não está apto a entrar para o Exército Brasileiro')


