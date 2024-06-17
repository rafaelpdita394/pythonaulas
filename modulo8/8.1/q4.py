A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

# Convertendo as listas em sets
set_A = set(A)
set_B = set(B)

# Encontrando a diferença entre os sets
diferenca = set_A.symmetric_difference(set_B)

# Identificando qual lista está desfalcada
if len(A) > len(B):
    print(f"O elemento {diferenca.pop()} está faltando na segunda lista")
else:
    print(f"O elemento {diferenca.pop()} está faltando na primeira lista")
