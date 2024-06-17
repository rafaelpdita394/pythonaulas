# aula2_questao2.py

# Definindo as variáveis
salario_por_hora = 20  # valor em reais por hora
horas_trabalhadas_semana = 40

# Calculando o salário bruto e líquido em uma expressão
salario_bruto, salario_liquido = salario_por_hora * horas_trabalhadas_semana, salario_por_hora * horas_trabalhadas_semana * 0.85

# Imprimindo os resultados
print(f"Salário semanal bruto: R$ {salario_bruto:.2f}")
print(f"Salário semanal líquido: R$ {salario_liquido:.2f}")
