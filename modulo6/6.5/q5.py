def pares_unicos(numeros, soma_objetivo):
    pares = []
    vistos = set()
    for num in numeros:
        complemento = soma_objetivo - num
        if complemento in vistos:
            pares.append((min(num, complemento), max(num, complemento)))
        vistos.add(num)
    return list(set(pares))

# Exemplo de uso
nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)  # Saída esperada: [(3, 7), (4, 6)]
