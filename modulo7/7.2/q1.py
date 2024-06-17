# Solicita a data de nascimento do usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Lista de meses por extenso
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Divide a data em dia, mês e ano
dia, mes, ano = data_nascimento.split('/')

# Converte o mês para o nome do mês por extenso
mes_extenso = meses[int(mes) - 1]

# Imprime a data com o mês por extenso
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
