indice = 0
nomes = []
salarios = []
inss = 0
irrf = 0
cad_nome=""
cad_salario=0


# Cálculo INSS - verifica no bloco de IFs em qual alíquota o salário se enquadra e faz o cálculo para definir o INSS
def cal_inss():
    global indice, inss, salarios
    salario = salarios[indice]
    if salario <= 1212.00:
        inss = salario * 0.075
    elif 1212.01 <= salario <= 2427.35:
        inss = ((salario - 1212.01) * 0.09) + 90.90
    elif 2427.36 <= salario <= 3641.03:
        inss = ((salario - 2427.36) * 0.12) + 90.90 + 109.3806
    elif 3641.04 <= salario <= 7087.22:
        inss = ((salario - 3641.04) * 0.14) + 90.90 + 109.3806 + 145.6404
    else:
        inss = 828.39


# Cálculo IRRF - desconta do salario o INSS e depois verifica no bloco de IFs qual a alíquota de desconto será aplicada
def cal_irrf():
    global indice, salarios, inss, irrf
    base_calculo = salarios[indice] - inss
    if base_calculo <= 1903.98:
        irrf = base_calculo * 0.0
    elif 1903.99 <= base_calculo <= 2826.65:
        irrf = (base_calculo * 0.075) - 142.80
    elif 2826.66 <= base_calculo <= 3751.05:
        irrf = (base_calculo * 0.15) - 354.80
    elif 3751.06 <= base_calculo <= 4664.68:
        irrf = (base_calculo * 0.225) - 636.13
    else:
        irrf = (base_calculo * 0.275) - 869.36


# Cálcula o salário liquido e imprime o funcionário, seu salário bruto, descontos de INNS e IRRF e seu salário liquido
def imprime():
    global indice, nomes, salarios, inss, irrf
    salario_liq = salarios[indice] - inss - irrf
    print(f'1. Funcionário: {nomes[indice]}\n'
          f'2. Salário Bruto: R${round(salarios[indice], 2)}\n'
          f'3. Desconto INSS: R${round(inss, 2)}\n'
          f'4. Desconto IRRF: R${round(irrf, 2)}\n'
          f'5. Salário Liquido: R${round (salario_liq, 2)}\n')


# Menu de interação no terminal
run = True
while run:
    menu = input('Escolha uma opção:\n'
                 '1. Cadastrar funcionário\n'
                 '2. Imprimir contracheque\n'
                 'Digite a opção: ')
    if (menu == '1'):
            cad_nome = (input('\nDigite o nome do funcionário: '))
            nomes.append(cad_nome)
            cad_salario = int(input('Digite o salário do funcionário: '))
            salarios.append(cad_salario)
            print(f'Funcionário {cad_nome} cadastrado com o salário de R${cad_salario}\n')
    elif (menu=='2'):
            indice = int(input('\nQual o índice do funcionário que deseja imprimir o contracheque? Digite o ID: '))
            cal_inss()
            cal_irrf()
            imprime()