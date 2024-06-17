def filtrar_dicionario(dic, chaves):
    return {chave: dic[chave] for chave in chaves if chave in dic}

# Exemplo de uso:
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)
# Saída esperada: {'a': 1, 'c': 3, 'e': 5}
