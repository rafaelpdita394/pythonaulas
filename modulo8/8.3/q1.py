def contagem_caracteres(s):
    dicionario = {}
    for char in s:
        if char in dicionario:
            dicionario[char] += 1
        else:
            dicionario[char] = 1
    return dicionario

# Exemplo de uso:
frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)
