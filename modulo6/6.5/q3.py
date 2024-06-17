# Função para ordenar por comprimento
def ordena_por_comprimento(lista):
    return sorted(lista, key=lambda x: len(x))

# Aplicando a função
nomes = ["Joao", "Maria", "Jose", "Gabriela", "Sol", "Luna", "Bento", "Enzo", "Fernanda"]
nomes_ordenados = ordena_por_comprimento(nomes)

print(nomes_ordenados)
