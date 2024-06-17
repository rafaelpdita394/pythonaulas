def encontrar_maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
maior_numero = encontrar_maior(num1, num2)
print(f"O maior número é: {maior_numero}")
