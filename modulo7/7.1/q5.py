# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Inicializa contagem de vogais e índices
vogais = 'aeiouAEIOU'
contagem_vogais = 0
indices_vogais = []

# Conta as vogais e seus índices
for i, char in enumerate(frase):
    if char in vogais:
        contagem_vogais += 1
        indices_vogais.append(i)

# Exibe o resultado
print(f"{contagem_vogais} vogais")
print(f"Índices {indices_vogais}")
