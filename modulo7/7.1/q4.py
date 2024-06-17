# Solicita o número de celular
numero = input("Digite o número: ")

# Verifica e formata o número
if len(numero) == 8:
    numero_completo = '9' + numero
elif len(numero) == 9 and numero[0] == '9':
    numero_completo = numero
else:
    print("Número inválido")
    exit()

# Adiciona o separador "-"
numero_formatado = numero_completo[:5] + '-' + numero_completo[5:]

print(f"Número completo: {numero_formatado}")
