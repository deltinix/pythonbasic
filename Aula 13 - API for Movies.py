import requests
import json
req = None

def requisicao(titulo):
   try:
       req = requests.get('https://www.omdbapi.com/?t='+ titulo + '&type=movie' + '&apikey=8ad64395')
       dicionario = json.loads(req.text)
       return dicionario
   except:
        print("Erro carregando dados do filme...")
        return None

def printar_detalhes(filme):
    print('')
    print('Titulo:', filme['Title'])
    print('Atores:', filme['Actors'])
    print('Lançamento:', filme['Released'])
    print('Enredo:', filme['Plot'])
    print('Idioma:', filme['Language'])
    print('País:', filme['Country'])
#   print('Bilheteria:', filme['BoxOffice'])
    print('Prêmios:', filme['Awards'])
    print('Poster:', filme['Poster'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...\n')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado!')
        else:
            printar_detalhes(filme)


'''

EXERCÍCIOS

Faça um programa que permita a realização de uma pesquisa dentro do site da OMBDAPI
Retornar todos os filmes que contenham aquela string de busca

'''