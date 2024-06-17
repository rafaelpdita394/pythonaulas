def diferenca_listas(lista1, lista2):
    contador1 = {x: lista1.count(x) for x in lista1}
    contador2 = {x: lista2.count(x) for x in lista2}
    
    diferenca = []
    for item in contador1:
        if item in contador2:
            diff = contador1[item] - contador2[item]
            if diff > 0:
                diferenca.extend([item] * diff)
        else:
            diferenca.extend([item] * contador1[item])
    
    return diferenca

# Exemplo de uso
lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]
resultado = diferenca_listas(lista1, lista2)
print(resultado)  # Saída esperada: [3, 3, 4, 7]
