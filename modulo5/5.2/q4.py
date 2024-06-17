# aula2_questao4.py
def inverteValor(numero):
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero //= 10
    return invertido

def verificaInverso(original, invertido):
    return (original % 2 == 0 and invertido % 2 == 0) or (original % 2 != 0 and invertido % 2 != 0)

def main():
    numero = int(input("Digite um número inteiro: "))
    invertido = inverteValor(numero)
    resultado = verificaInverso(numero, invertido)
    print(f"Valor invertido: {invertido}")
    print(f"Valores são igualmente par ou ímpar: {resultado}")

if __name__ == "__main__":
    main()
