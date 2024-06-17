import os

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "q1frase.txt"

# Salva a frase no arquivo
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo
caminho_completo = os.path.abspath(nome_arquivo)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {caminho_completo}")
