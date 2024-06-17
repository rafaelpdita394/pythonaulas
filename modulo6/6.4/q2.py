def main():
    frase = input("Digite uma frase: ")
    vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
    consoantes = [char for char in frase if char.lower() not in 'aeiou' and char.isalpha()]

    print("Vogais:", vogais)
    print("Consoantes:", consoantes)

if __name__ == "__main__":
    main()
