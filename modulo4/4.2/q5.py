# Questão 5
print("Questão 5:")
N = int(input("Digite o número de linhas: "))
M = int(input("Digite o número de colunas: "))

# Imprimir cabeçalho das colunas
print(" ", end=" ")
for col in range(1, M + 1):
    print(col, end=" ")
print()

# Imprimir linhas com números de linha e posições jogáveis
for linha in range(1, N + 1):
    print(linha, end=" ")
    for col in range(1, M + 1):
        print("/", end=" ")
    print()
