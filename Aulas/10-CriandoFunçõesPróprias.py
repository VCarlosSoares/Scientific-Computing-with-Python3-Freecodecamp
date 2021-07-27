# Existem dois tipos de funções, a void functions e return funcions
# A void functions são funções que executam uma função mas não retornam nenhum valor
# As return functions retornam um valor para "quem chamou" ela (variável, função, etc.)

# Podemos criar nossas funções utilizando a palavra reservada def (função definida),
# onde podemos passar parâmetros para a função se quisermos

# Exemplo 1: void function
def print_welcome():
    print('Ola')
    print('Aluno')

x=5
print('Antes da Função')
print_welcome()
print(x+5, '\n')

# Se quisermos passar parâmetros para a função, devemos incluir esses parâmetros dentro do () na declaração da função:
# Exemplo 2: void function com parâmetro
def boas_vindas(lang):
    if lang == 'pt':
        print('Olá\n')
    elif lang == 'fr':
        print('Bonjour\n')
    else:
        print('Hello\n')


boas_vindas('pt')
boas_vindas('fr')
boas_vindas('default') # qualquer argumento que não está presente dentro dos if/elif vai ativar o else (inglês)

# Também podemos definir que a função retorne (return) valores para que possamos utilizar em qualquer ocasião:
# atribuir este valor a uma variável, passar como parâmetro para outra função, etc
# Quando se encontra o 'return' na função, ela retorna um valor para a função/variável que chamou ela e encerra a função
# Exemplo 3: return function
def boas_vindas():
    return 'Olá'

print(boas_vindas(), 'Vitor')
print(boas_vindas(), 'Carlos\n')

# Exemplo 4: Refaça o exemplo 2 utilizando return (return function com parâmetro)
def boas_vindas(lang):
    if lang == 'pt':
        return 'Olá'
    if lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(boas_vindas('pt'), 'Vitor')
print(boas_vindas('fr'), 'Vitor')
print(boas_vindas('qlqcoisa'), 'Vitor\n')

# Exemplo 5: Retorne a soma de dois valores (return function com dois parâmetros)
def soma(a, b):
    #sum = a + b
    #return sum
    return a + b

print('2 + 5 =', soma(2, 5))
print('5 + 8 =', soma(5, 8))

x = soma(1, 1)
print('1 + 1 =', x)

print(x, '+', x, '=', soma(x, x))
print('{} + {} = {}'.format(x, x, soma(x, x)))