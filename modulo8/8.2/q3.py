def ordenar_tuplas(lista):
    # Ordena a lista de tuplas com base no segundo elemento de cada tupla (média)
    return sorted(lista, key=lambda aluno: aluno[1], reverse=True)

# Exemplo de uso
alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
resultado = ordenar_tuplas(alunos_notas)
print(resultado)
# Saída esperada: [('Charlie', 9.0), ('David', 8.8), ('Alice', 8.5), ('Bob', 7.2)]
