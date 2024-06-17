import random

# Gere aleatoriamente 20 valores inteiros entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Liste ordenada, sem modificar a lista original
lista_ordenada = sorted(lista)

# Índice do maior valor da lista
indice_maior = lista.index(max(lista))

# Índice do menor valor da lista
indice_menor = lista.index(min(lista))

# Impressão dos resultados
print("Lista original:", lista)
print("Lista ordenada:", lista_ordenada)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
