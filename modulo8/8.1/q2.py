def tem_elementos_comuns(lista1, lista2):
    # Convertendo as listas em sets
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Verificando a interseção entre os sets
    return not set1.isdisjoint(set2)

# Testando a função
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7]
resultado = tem_elementos_comuns(lista1, lista2)
print(resultado)  # Saída esperada: True
