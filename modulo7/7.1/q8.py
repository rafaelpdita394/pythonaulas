def calcula_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11:
        return "Inválido"

    multiplicadores_primeiro_digito = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores_segundo_digito = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_digito = calcula_digito(cpf, multiplicadores_primeiro_digito)
    segundo_digito = calcula_digito(cpf, multiplicadores_segundo_digito)

    return "Válido" if cpf[-2:] == primeiro_digito + segundo_digito else "Inválido"

# Solicita o CPF do usuário
cpf_usuario = input("Digite o CPF (XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf_usuario))
