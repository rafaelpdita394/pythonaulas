# aula1_questao2.py
import random
import math

def main():
    # Solicita o valor de n do usuário
    n = int(input("Digite o valor de n: "))
    
    # Gera n valores inteiros aleatórios entre 0 e 100
    numeros = [random.randint(0, 100) for _ in range(n)]
    
    # Calcula a soma dos valores
    soma = sum(numeros)
    
    # Calcula a raiz quadrada da soma
    raiz_quadrada = math.sqrt(soma)
    
    # Exibe o resultado
    print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada:.2f}")

if __name__ == "__main__":
    main()
