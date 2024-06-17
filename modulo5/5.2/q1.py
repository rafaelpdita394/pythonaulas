# aula2_questao1.py
def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

def main():
    n = int(input("Digite o valor de n: "))
    resultado = fatorial(n)
    print(f"O fatorial de {n} é: {resultado}")

if __name__ == "__main__":
    main()
