# Beautiful Soap - BS4 - pip install bs4
'''
Beautiful Soup é uma biblioteca Python para extrair dados de arquivos HTML e XML.
Ele funciona com seu analisador favorito para fornecer maneiras idiomáticas de navegar, pesquisar e modificar
a árvore de análise. Geralmente, isso economiza horas ou dias de trabalho dos programadores.

Site: putsreq.com permite criar requisições
'''

import requests

# import bs4

cabecalho = {'User-Agent': 'Windows 12',
             'Referer': 'https://www.playboy.com'}

meus_cookies = {'Ultima-visita': '01-03-2021'}
dados = {'username': 'ricardo',
         'password': '123'}

requisicao = None

try:
    # url = input("Digite a URL do Site.:")
    # requisicao = requests.get(url)

    requisicao = requests.post("https://putsreq.com/0olxJI7nBLHmVwbwibHQ",
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)

    #    requisicao2 = requests.post("https://putsreq.com/0olxJI7nBLHmVwbwibHQ")

    texto = requisicao.text
    #   texto2 = requisicao2

    #    print(type(requisicao))
    #    print(requisicao)
    #    print(requisicao.status_code)

    print(texto)
#    print(texto2)

except Exception as error:
    print("Erro ao tentar carregar o site!!")
    print("Código do Erro.:", error)
