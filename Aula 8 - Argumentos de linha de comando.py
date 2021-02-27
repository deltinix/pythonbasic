import sys  # Biblioteca que permite realizar operações no sistema operacional

# argumentos = sys.argv
# print(argumentos)

# O argumento numero 0 é passar o path do sistema

argumentos = sys.argv   # arg1 metodo // arg 2 - n1 // arg 3 - n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)

