'''
open('aula10.txt', 'r')  #Abre para leitura
open('aula10.txt', 'w')  #Abre para gravação
open('aula10.txt', 'r+') #Abre leitura com possibilidade de gravação
open('aula10.txt', 'a')  #Abre jogando pro final do arquivo (append)
'''

'''
arquivo = open("arquivo.txt", "w")
arquivo.write("\nSabe quem é?!\n")
type(print(arquivo))

for i in range(0, 1001):
arquivo.write("Numero:" +str(i) + "\n")

'''
arquivo = open('arquivo.txt', 'r')
print(arquivo.read())
