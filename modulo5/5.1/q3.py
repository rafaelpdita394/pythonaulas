# aula1_questao3.py
import random

def main():
    # Gera um número aleatório entre 1 e 10
    numero_aleatorio = random.randint(1, 10)
    
    acertou = False
    
    while not acertou:
        # Solicita o palpite do usuário
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        
        if palpite < numero_aleatorio:
            print("Muito baixo, tente novamente!")
        elif palpite > numero_aleatorio:
            print("Muito alto, tente novamente!")
        else:
            print(f"Correto! O número é {palpite}.")
            acertou = True

if __name__ == "__main__":
    main()
