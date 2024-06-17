# aula1_questao5.py
import emoji
## pip install emoji pra funcionar!

def main():
    # Exibe a lista de emojis disponíveis
    print("Emojis disponíveis:")
    print("❤️ - :red_heart:")
    print("👍 - :thumbs_up:")
    print("🤔 - :thinking_face:")
    print("🥳 - :partying_face:")
    
    # Solicita uma frase codificada ao usuário
    frase = input("Digite uma frase e ela será emojizada: ")
    
    # Converte a frase codificada em uma frase com emojis
    frase_emojizada = emoji.emojize(frase, use_aliases=True)
    
    # Exibe a frase emojizada
    print(f"Frase emojizada:\n{frase_emojizada}")

if __name__ == "__main__":
    main()
