import re

# Nome dos arquivos
arquivo_frase = "q1frase.txt"
arquivo_palavras = "q2palavras.txt"

# Lê o conteúdo do arquivo "q1frase.txt"
with open(arquivo_frase, "r") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos e separa as palavras
palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo)

# Salva as palavras no arquivo "q2palavras.txt", cada uma em uma linha
with open(arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo "q2palavras.txt"
with open(arquivo_palavras, "r") as arquivo:
    conteudo_palavras = arquivo.read()

print("Conteúdo do arquivo 'q2palavras.txt':")
print(conteudo_palavras)
