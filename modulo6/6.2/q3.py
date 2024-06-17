import random
from collections import Counter

# Preencha duas listas com 20 valores inteiros aleatórios entre 0 a 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Crie a lista de interseção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

# Contagem de elementos em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Impressão dos resultados
print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)
print("Contagem")

for elem in interseccao:
    print(f"{elem}: (lista1={contagem_lista1[elem]}, lista2={contagem_lista2[elem]})")
