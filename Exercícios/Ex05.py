# reescreva o Ex04 utilizando funções

def computepay(horas, salarioPH):
    if horas <= 40:
        return horas * salarioPH
    else:
        return (salarioPH * 40) + ((horas - 40) * (salarioPH * 1.5))

try:
    horas = int(input('Informe a quantidade de horas trabalhadas: '))
    salarioPH = float(input('Informe seu salário por hora: '))
except:
    horas = salarioPH = -1

if horas > 0:
    print('Pagamento:', computepay(horas, salarioPH))
else:
    print('Por favor, informe um valor numérico e positivo!')