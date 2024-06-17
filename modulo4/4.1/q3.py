def verificar_aprovacao(nota):
    if nota >= 60:
        return "Aprovado"
    else:
        return "Reprovado"

# Exemplo de uso:
nota_aluno = float(input("Digite a nota do aluno: "))
resultado = verificar_aprovacao(nota_aluno)
print(f"O aluno está {resultado}.")
