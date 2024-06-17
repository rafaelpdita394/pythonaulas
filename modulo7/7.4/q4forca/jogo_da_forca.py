### Passo 2: Implementação do Jogo

import random

# Função para ler as palavras do arquivo gabarito_forca.txt
def ler_palavras():
 try:
     with open('gabarito_forca.txt', 'r', encoding='utf-8') as arquivo:
         palavras = arquivo.readlines()
         # Remover quebras de linha e espaços em branco
         palavras = [palavra.strip() for palavra in palavras]
         return palavras
 except FileNotFoundError:
     print("Arquivo gabarito_forca.txt não encontrado.")
     return []

# Função para escolher uma palavra aleatória da lista
def escolher_palavra(palavras):
 return random.choice(palavras)

# Função para inicializar o jogo
def jogar_forca():
 palavras = ler_palavras()

 if not palavras:
     print("Não foi possível iniciar o jogo.")
     return

 palavra_secreta = escolher_palavra(palavras)
 letras_corretas = set()
 letras_incorretas = set()
 tentativas = 6

 print("Bem-vindo ao jogo da forca!")
 print("Adivinhe a palavra secreta.")

 while tentativas > 0:
     print("\nPalavra secreta:", end=" ")
     for letra in palavra_secreta:
         if letra in letras_corretas:
             print(letra, end=" ")
         else:
             print("_", end=" ")
     print("\n")

     # Exibir desenho da forca correspondente às tentativas restantes
     desenho_forca(tentativas)

     # Verificar se o jogador ganhou
     if all(letra in letras_corretas for letra in palavra_secreta):
         print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
         break

     # Entrada do jogador
     tentativa = input("Digite uma letra: ").strip().lower()

     if len(tentativa) != 1 or not tentativa.isalpha():
         print("Entrada inválida. Digite apenas uma letra.")
         continue

     # Verificar se a letra já foi tentada
     if tentativa in letras_corretas or tentativa in letras_incorretas:
         print("Você já tentou essa letra. Tente outra.")
         continue

     # Verificar se a letra está na palavra secreta
     if tentativa in palavra_secreta:
         letras_corretas.add(tentativa)
     else:
         letras_incorretas.add(tentativa)
         tentativas -= 1

 else:
     print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)
     # Exibir desenho da forca final
     desenho_forca(0)

 print("\nFim do jogo.")

# Função para exibir o desenho da forca conforme as tentativas
def desenho_forca(tentativas):
 print("  |---|")
 if tentativas == 6:
     print("      |")
     print("      |")
     print("      |")
 elif tentativas == 5:
     print("    O |")
     print("      |")
     print("      |")
 elif tentativas == 4:
     print("    O |")
     print("    | |")
     print("      |")
 elif tentativas == 3:
     print("    O |")
     print("   /| |")
     print("      |")
 elif tentativas == 2:
     print("    O |")
     print("   /|\\|")
     print("      |")
 elif tentativas == 1:
     print("    O |")
     print("   /|\\|")
     print("   /  |")
 elif tentativas == 0:
     print("    O |")
     print("   /|\\|")
     print("   / \\|")
 print("=========")

# Executar o jogo
if __name__ == "__main__":
 jogar_forca()
