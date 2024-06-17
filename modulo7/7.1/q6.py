from collections import Counter

# Solicita uma frase e a palavra objetivo do usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Função para verificar se duas palavras são anagramas
def sao_anagramas(palavra1, palavra2):
    return Counter(palavra1) == Counter(palavra2)

# Encontra todos os anagramas na frase
palavras = frase.split()
anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo)]

print(f"Anagramas: {anagramas}")
