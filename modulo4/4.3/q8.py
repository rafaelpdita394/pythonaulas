# Questão 8
print("Questão 8:")
resultado = 0

while True:
    entrada = input("Digite um número ou operador (+ ou -) (ou 'Fim' para encerrar): ")
    
    if entrada == "Fim":
        break
    
    if entrada == "+":
        operando = float(input("Digite o número a ser somado: "))
        resultado += operando
    elif entrada == "-":
        operando = float(input("Digite o número a ser subtraído: "))
        resultado -= operando
    else:
        # Se não for um operador, assume-se que é um número
        operando = float(entrada)
        resultado = operando  # Inicia o resultado com o primeiro número digitado

print(f"Resultado: {resultado}")
