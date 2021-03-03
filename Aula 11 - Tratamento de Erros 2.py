import time

def abre_arquivo():
    try:
        arquivo = open("arquivodoido.txt")
        return True
    except Exception as erro:
        print("Aconteceu algum erro", erro)
        return False

while not abre_arquivo():
    print("Tentando abrir o arquivo...Aguardando 5 seg")
    time.sleep(5)
    print("Consegui finalmente abrir o arquivo...")
