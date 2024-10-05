
salarioBruto = float(input('Digite o seu salário bruto: ' + '\n'))


def calculaINSS(salarioBruto):
    
    if salarioBruto <= 1212:
        inss = salarioBruto * 0.075
    elif salarioBruto > 1212 and salarioBruto < 2427.35:
        inss = salarioBruto * 0.09
    elif salarioBruto > 2427.35 and salarioBruto < 3641.03:
        inss = salarioBruto * 0.12
    elif salarioBruto > 3641.03 and salarioBruto < 7087.22:
        inss = salarioBruto * 0.14
    else:
        inss = 828.39
    
    
    salarioDescInss = salarioBruto - inss
    print(f'INSS: {inss:.2f}')
    
    return salarioDescInss

def calculaIRPF(salarioDescInss): 

    if salarioDescInss <= 1903.98:
        irpf = 0
    elif salarioDescInss > 1903.98 and salarioDescInss < 2826.65:
        irpf = salarioDescInss * 0.075 - 142.80
    elif salarioDescInss > 2826.65 and salarioDescInss < 3751.05:
        irpf = salarioDescInss * 0.15 - 354.80
    elif salarioDescInss > 3751.05 and salarioDescInss < 4664.68:
        irpf = salarioDescInss * 0.22 - 636.13
    elif salarioDescInss > 4664.68:
        irpf = salarioDescInss * 0.275 - 869.36

    salarioLiquido = salarioDescInss - irpf
    print(f'IRPF: {irpf:.2f}')

    return salarioLiquido

salarioDescInss = calculaINSS(salarioBruto)
salarioLiquido = calculaIRPF(salarioDescInss)
fgts = salarioBruto * 0.08

print(f'Salario Líquido: {salarioLiquido:.2f}')
print(f'Parcela do FTGS: {fgts}')

