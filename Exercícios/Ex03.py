# Reescreva o programa Ex02, o usuário deve receber um bonus de 1.5x de salário por hora trabalhada após 40 horas de trabalho

horas = int(input('Informe a quantidade de horas trabalhadas: '))
salarioPH = float(input('Informe seu salário por hora: '))

if horas <= 40:
    pagamento = horas * salarioPH
else:
    pagamento = (salarioPH * 40) + ((horas - 40) * (salarioPH * 1.5))

print('Pagamento:', pagamento)