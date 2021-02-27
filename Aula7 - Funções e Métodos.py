print('Olá mundo')
print(len('Olá mundo'))

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(75, 1289)

print(retorno)

# A IDÉIA DA FUNÇÃO É NÃO TER QUE FICAR REESCREVENDO O MESMO CÓDIGO EM VÁRIAS PARTE DO SISTEMA

retorno = soma(76.33, 1091.2)
print(retorno)

def imprime_oi():
    print('Oiii')

imprime_oi()
imprime_oi()
imprime_oi()

'''
while True:
    imprime_oi()

Imprime Oiii infinitamente!
'''

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

if tem_sete_itens('12345267'):
    print('Tem 7 letras!!')
else:
    print('Não tem 7 letras!')


'''
EXERCÍCIO AULA 7

Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção

Faça outra função que retorna o menor número dessa coleção

'''