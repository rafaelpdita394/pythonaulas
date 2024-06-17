import re
from collections import Counter

# Lendo o arquivo
with open("estomago.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Removendo pontuações e transformando o texto em minúsculas
palavras = re.findall(r'\b\w+\b', texto.lower())

# Contando as palavras
contador_palavras = Counter(palavras)

# Ordenando o dicionário por frequência das palavras
dicionario_ordenado = dict(sorted(contador_palavras.items(), key=lambda item: item[1], reverse=True))

# Exibindo o dicionário ordenado
print(dicionario_ordenado)
