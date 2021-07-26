# Escreva um programa que calcule quanto um funcionário deve receber.
# O usuário deverá informar a quantidade de horas trabalhadas e o salário por hora

horas = int(input('Horas Trabalhadas: '))
salarioPH = float(input('Salário por hora: '))

pagamento = horas * salarioPH
print('Pagamento:', pagamento)

# Obrigando a saída a ter 1 casa decimal por meio da função round
print('Pagamento:', round(pagamento, 1))