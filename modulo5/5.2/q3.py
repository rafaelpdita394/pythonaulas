# aula2_questao3.py
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = soma_digitos(numero)
    print(f"A soma dos dígitos do número é: {resultado}")

if __name__ == "__main__":
    main()
