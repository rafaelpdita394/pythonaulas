def comprimir_tuplas(lista):
    # Usando um dicionário para somar os valores das palavras idênticas
    dicionario = {}
    for palavra, numero in lista:
        if palavra in dicionario:
            dicionario[palavra] += numero
        else:
            dicionario[palavra] = numero
    # Convertendo o dicionário de volta para uma lista de tuplas
    return list(dicionario.items())

# Exemplo de uso
tuplas_originais = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
resultado = comprimir_tuplas(tuplas_originais)
print(resultado)
# Saída esperada: [('maçã', 8), ('banana', 5), ('laranja', 1)]
