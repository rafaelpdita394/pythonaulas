# Questão 6
print("Questão 6:")
maior = float('-inf')  # Inicializa com o menor valor possível
menor = float('inf')   # Inicializa com o maior valor possível

while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))
    
    if valor == 0:
        break
    
    if valor > maior:
        maior = valor
    
    if valor < menor:
        menor = valor

print(f"Maior: {maior}")
print(f"Menor: {menor}")
