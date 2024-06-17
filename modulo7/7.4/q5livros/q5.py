import csv

# Dados dos livros
livros = [
    {"Título": "O Hobbit", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1937, "Número de páginas": 310},
    {"Título": "A Guerra dos Tronos", "Autor": "George R.R. Martin", "Ano de publicação": 1996, "Número de páginas": 694},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "A Menina que Roubava Livros", "Autor": "Markus Zusak", "Ano de publicação": 2005, "Número de páginas": 480},
    {"Título": "Dom Quixote", "Autor": "Miguel de Cervantes", "Ano de publicação": 1605, "Número de páginas": 863},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 144},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1178},
    {"Título": "Crime e Castigo", "Autor": "Fiódor Dostoiévski", "Ano de publicação": 1866, "Número de páginas": 551},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417}
]

# Nome do arquivo CSV
nome_arquivo = "meus_livros.csv"

# Abrir o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Criar o escritor CSV
    escritor_csv = csv.writer(arquivo_csv)

    # Escrever o cabeçalho
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])

    # Escrever os dados dos livros
    for livro in livros:
        escritor_csv.writerow([livro["Título"], livro["Autor"], livro["Ano de publicação"], livro["Número de páginas"]])

print(f'Arquivo "{nome_arquivo}" criado com sucesso.')
