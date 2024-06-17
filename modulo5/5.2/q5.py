# aula2_questao5.py
import math

def calcula_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(lado1, lado2=None):
    if lado2 is None or lado2 == 0:
        return 4 * lado1
    return 2 * (lado1 + lado2)

def main():
    while True:
        print("1 - Calcular perímetro triângulo")
        print("2 - Calcular perímetro círculo")
        print("3 - Calcular perímetro retângulo")
        print("4 - Sair")
        
        opcao = int(input("Opção: "))
        
        if opcao == 1:
            lado1 = int(input("Digite o primeiro lado do triângulo: "))
            lado2 = int(input("Digite o segundo lado do triângulo: "))
            lado3 = int(input("Digite o terceiro lado do triângulo: "))
            perimetro = calcula_perimetro_triangulo(lado1, lado2, lado3)
            print(f"O perímetro é: {perimetro}")
        elif opcao == 2:
            raio = int(input("Digite o raio do círculo: "))
            perimetro = calcula_perimetro_circulo(raio)
            print(f"O perímetro é: {perimetro:.2f}")
        elif opcao == 3:
            lado1 = int(input("Digite o primeiro lado do retângulo: "))
            lado2 = int(input("Digite o segundo lado do retângulo (ou 0 se for um quadrado): "))
            perimetro = calcula_perimetro_retangulo(lado1, lado2)
            print(f"O perímetro é: {perimetro}")
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
