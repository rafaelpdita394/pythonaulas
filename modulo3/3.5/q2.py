# Solicita os comprimentos dos lados do triângulo e converte para float
lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

# Verifica o tipo do triângulo
if lado1 == lado2 == lado3:
    print("Triângulo: Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo: Isóceles")
else:
    print("Triângulo: Escaleno")
