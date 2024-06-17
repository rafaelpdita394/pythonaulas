# aula2_questao1.py

# Definindo as variáveis
salario_por_hora = 20
horas_por_semana = 40

# Calculando o salário bruto semanal
salario_bruto = salario_por_hora * horas_por_semana

# Calculando os descontos
inss = 0.1 * salario_bruto  # 10% do bruto
sindicato = 0.05 * salario_bruto  # 5% do bruto

# Calculando o salário líquido
salario_liquido = salario_bruto - inss - sindicato

# Imprimindo os resultados
print("Salário semanal bruto:", salario_bruto)
print("Valor descontado por semana INSS:", inss)
print("Valor descontado por semana pelo sindicato:", sindicato)
print("Salário semanal líquido:", salario_liquido)
