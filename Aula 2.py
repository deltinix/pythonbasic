nome = 'Ricardo'
idade = 38
tipo_nome = type(nome)
tipo_idade = type(idade)
altura = 1.75
tipo_altura = type(altura)
frase = nome, 'tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura'

print('Olá Mundo!\nSegundo Print\nTerceiro Print\nTestando 123')
print('Seu nome é',nome)
print('O tipo do seu nome é',tipo_nome)
print('Sua idade é',idade)
print('O tipo da sua idade é',tipo_idade)
print('Sua altura é',altura)
print('O tipo de altura é',tipo_altura)

print(nome, 'tem', idade, 'anos', 'e', altura, 'de altura')
print(nome, 'tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')
print(frase)

nome2 = input('Escreva o seu Nome.....: ')
idade2 = input('Escreva a sua Idade...: ')
altura2 = input('Escreva a sua Altura.: ')
print(nome2, 'sua idade é de', idade2, 'anos e sua altura é de', altura2, 'metros')

print(type(idade2), type(altura2), type(nome2))

valor1 = 27
valor2 = 53
valor3 = 4.5

resultado = valor1 + (valor2 / valor3) * 5

print(resultado)


'''
EXERCÍCIO PROPOSTO

Faça um formulário que pergunte o Nome, CPF, Endereço, Idade, Altura e Telefone
e imprima isso em um relatório organizado!

'''
