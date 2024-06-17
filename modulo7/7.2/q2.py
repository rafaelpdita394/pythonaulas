# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Substitui as vogais por "*"
frase_modificada = ''.join(['*' if char in 'aeiouAEIOU' else char for char in frase])

# Imprime a frase modificada
print(f"Frase modificada: {frase_modificada}")
