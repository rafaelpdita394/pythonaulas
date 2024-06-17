# aula2_questao2.py
def soma_quadrados(num1, num2):
    return num1**2 + num2**2

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = soma_quadrados(num1, num2)
    print(f"A soma dos quadrados dos números é: {resultado}")

if __name__ == "__main__":
    main()
