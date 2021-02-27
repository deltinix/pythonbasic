'''
COMPARADORES

== igual
> maior
< menor
!= diferente
>= maior ou igual
<= menor ou igual

Exemplo:

1 == 1 and 1 == 2  (AND, os dois lados precisam ser igual pra dar TRUE)
1 == 1 or 1 == 2  (OR, se um dos lados estiver certo então vai dar TRUE)

'''

var_verdade = True
var_falso = False

if var_verdade == True:
    print('Var_Verdade é Verdadeiro')

a = 2
b = 20


if a > b:
    print(a, 'é maior do que', b)
else:
    print(a, 'não é maior do', b)


vlr1 = input('Digite o Valor 1:')
vlr2 = input('Digite o Valor 2:')

if str(vlr1) == str(vlr2):
    print(vlr1, 'é igual a', vlr2)
if str(vlr1) > str(vlr2):
    print(vlr1, 'é maior do que', vlr2)
if str(vlr1) < str(vlr2):
    print(vlr1, 'é menor do que', vlr2)

print('================================================')
print('============== ESCOLHA SUA OPÇÃO ===============')
print('================================================')
print('(1) Verificar portas')
print('(2) Brute Force')
print('(3) Scan Netbios')
print('(4) Web Attack')
print('(5) Sair\n')
opcao = input('Selecione a Opção.:')

if opcao == '1':
    print('Verificando Portas... aguarde')
elif opcao == '2':
    print('Acionando módulo Brute Force... aguarde')
elif opcao == '3':
    print('Escaneando Netbios Protocol... aguarde')
elif opcao == '4':
    print('Atacando Web Server... aguarde')
else:
    print('Saindo do programa!')

# USANDO NOT

print(not False)
print(not True)

idade = 51

if not idade == 50:
    print('Você não tem 50 anos')
else:
    print('Você tem 50 anos')

'''
EXERCÍCIO DA AULA 3

Faça um programa que pergunte a idade, o peso e altura de uma pessoa
e decide se ela está apta a ser do exército)

Para entrar no exército tem que ter mais de 18 anos
mais de 60kg e mais ou igual a 1.70 metros.

'''
