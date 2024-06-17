# Solicita o valor total da compra e converte para float
valor_total = float(input("Digite o valor total da compra: "))

# Calcula o desconto com base no valor total
if valor_total >= 100:
    desconto = 20
elif valor_total >= 50:
    desconto = 10
else:
    desconto = 0

# Calcula o valor final com desconto
valor_final = valor_total * (1 - desconto / 100)

# Imprime o desconto aplicado e o valor final com desconto
print(f"Desconto aplicado: {desconto:.1f}%")
print(f"Valor final com desconto: R${valor_final:.2f}")
