# Reescreva o Ex03 usando try e except para tratamento caso o usuário não informe um número

horas = input('Informe a quantidade de horas trabalhadas: ')
salarioPH = input('Informe seu salário por hora: ')
try:
    horas = int(horas)
    salarioPH = int(salarioPH)
except:
    print('Por favor informe um valor numérico!')
    quit()

if horas <= 40:
    pagamento = horas * salarioPH
else:
    pagamento = (salarioPH * 40) + ((horas - 40) * (salarioPH * 1.5))

print('Pagamento:', pagamento)