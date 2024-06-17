# aula2_questao6.py
par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

def main():
    while True:
        valor = int(input("Digite um valor (digite 0 para finalizar): "))
        if valor == 0:
            break
        print(par_ou_impar(valor))

if __name__ == "__main__":
    main()
