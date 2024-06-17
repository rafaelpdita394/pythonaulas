# Questão 7
print("Questão 7:")
produto = 1

while True:
    valor = int(input("Digite um valor (ou 0 para encerrar): "))
    
    if valor == 0:
        break
    
    if valor > 0:
        produto *= valor

print(f"Produto: {produto}")
