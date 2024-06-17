# aula1_questao1.py
def main():
    # Solicita os dois números decimais do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Calcula a diferença absoluta
    diferenca = abs(num1 - num2)
    
    # Arredonda a diferença para duas casas decimais
    diferenca_arredondada = round(diferenca, 2)
    
    # Exibe o resultado
    print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")

if __name__ == "__main__":
    main()
