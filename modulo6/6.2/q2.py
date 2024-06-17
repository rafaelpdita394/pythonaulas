import random

# Gere aleatoriamente um valor entre 5 e 20
num_elementos = random.randint(5, 20)

# Gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Cálculos
soma_valores = sum(elementos)
media_valores = soma_valores / num_elementos

# Impressão dos resultados
print("Lista elementos:", elementos)
print("Soma dos valores da lista:", soma_valores)
print("Média dos valores da lista:", media_valores)
