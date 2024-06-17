frase = "O rato roeu a roupa da Alice"

vogais = "aeiouAEIOU"
resultados = [(indice, char) for indice, char in enumerate(frase) if char in vogais]

# Exibindo os resultados
for indice, vogal in resultados:
    print(f"Vogal: {vogal}, Índice: {indice}")
