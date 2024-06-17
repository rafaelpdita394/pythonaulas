import random

# Função de criptografia
def encrypt(nomes):
    n = random.randint(1, 10)
    criptografados = [''.join(chr(((ord(char) - 33 + n) % 94) + 33) for char in nome) for nome in nomes]
    return criptografados, n

# Lista de nomes
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)

print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")
