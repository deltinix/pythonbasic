'''

EXERCÍCIOS

Faça um programa que permita a realização de uma pesquisa dentro do site da OMBDAPI
Retornar todos os filmes que contenham aquela string de busca

'''

import requests
import json

def menu():
    print("==================================")
    print("        LOCADORA PYTHON")
    print("==================================")
    print("[ 1 ] Buscar Nomes de Filmes")
    print("[ 2 ] Buscar Dados de Filme")
    print("[ 3 ] Sair")
    print('')
    escolha = int(input('Opção..:'))

    if escolha == 1:
        buscar_nome_filmes()
    elif escolha == 2:
        busca_dados_filme()
    else:
        print('')
        print('Saindo...')
        exit()

def buscar_nome_filmes():
    print('')
    op = input('Digite o nome do filme..:')
    filmes = requests.get('https://www.omdbapi.com/?s=' + op + '&type=movie' + '&apikey=8ad64395')
    filme = json.loads(filmes.text)

    for busca in filme['Search']:
        print(busca['Title'])
    print('')
    pergunta = str(input('Desejar repetir essa busca? <s/n> '))
    if pergunta in ['s', 'S', 'sim', 'Sim', 'SIM', 'sIM']:
        buscar_nome_filmes()

def busca_dados_filme():
    titulo = input("\nDigite o nome do filme..:")
    req = requests.get('https://www.omdbapi.com/?t='+ titulo + '&type=movie' + '&apikey=8ad64395')
    dicionario = json.loads(req.text)
    print('')
    print('Titulo:', dicionario['Title'])
    print('Atores:', dicionario['Actors'])
    print('Lançamento:', dicionario['Released'])
    print('Enredo:', dicionario['Plot'])
    print('Idioma:', dicionario['Language'])
    print('País:', dicionario['Country'])
#   print('Bilheteria:', dicionario['BoxOffice'])
    print('Prêmios:', dicionario['Awards'])
    print('Poster:', dicionario['Poster'])
    print('')
    pergunta = str(input('Desejar repetir essa busca? <s/n> '))
    if pergunta in ['s', 'S', 'sim', 'Sim', 'SIM', 'sIM']:
        busca_dados_filme()

while True:
    menu()

