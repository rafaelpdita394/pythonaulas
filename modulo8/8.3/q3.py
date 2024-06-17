def mesclar_dicionarios(dic1, dic2):
    resultado = dic1.copy()  # Começa com os itens do primeiro dicionário
    for chave, valor in dic2.items():
        if chave in resultado:
            resultado[chave] = max(valor, resultado[chave])
        else:
            resultado[chave] = valor
    return resultado

# Exemplo de uso:
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)
# Saída esperada: {'a': 1, 'b': 4, 'c': 3, 'd': 5}
