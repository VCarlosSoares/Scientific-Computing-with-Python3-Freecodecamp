# Um programa que pergunte um número até que o usuário digite 'done'
# Quando o programa é finalizado, mostre a soma e a média dos números digitados
soma = 0.0
contador = 0
while True:
    num = input('Digite um número:')
    try:
        iNum = float(num)
        soma = soma + iNum
        contador = contador + 1
    except:
        if num == 'done':
            break
        else:
            print('Entrada invalida!')
print('\nNúmeros digitados: {}\nSoma total: {}\nMédia: {}'.format(contador, soma, soma / contador))