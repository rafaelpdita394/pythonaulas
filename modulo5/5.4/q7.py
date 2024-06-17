# aula2_questao7.py
def main():
    opcao = int(input("Opções: (1) maior ou (2) menor? \nOpção: "))
    valores = []

    while True:
        valor = int(input("Digite um valor (digite 0 para finalizar): "))
        if valor == 0:
            break
        valores.append(valor)

    if opcao == 1:
        resultado = max(valores, default=None)
        if resultado is not None:
            print(f"O maior valor é: {resultado}")
        else:
            print("Nenhum valor foi inserido.")
    elif opcao == 2:
        resultado = min(valores, default=None)
        if resultado is not None:
            print(f"O menor valor é: {resultado}")
        else:
            print("Nenhum valor foi inserido.")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
