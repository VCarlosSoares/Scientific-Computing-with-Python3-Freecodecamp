# A função armazena linhas de códigos dentro da memória secundária para que possa ser usado posteriormente.
# Isso significa que quando você insere códigos dentro de uma função, você não vai executar aqueles códigos
# durante a escrita, apenas armazenalos na memória.
# Aqueles códigos armazenados só serão executados caso o usuário chame a função (que ele pode atribuir um nome).
# Sua principal contribuição é a necessidade de escrever apenas uma vez uma parte do código que será requisitada várias vezes

# Existem várias funções já criadas e utilizadas pelo python: type(), print(), input(), float(), max(), min(), etc.
# Geralmente passamos parâmetros (valores) dentro da () para que eles possam ser utilizados pela função
# Exemplo: print('ola mundo')
# A string 'ola mundo' está sendo utililizada como parâmetro (valor) para a função print

# Exemplo 1: Chame a função integrada (max e min) para obter o maior e o menor valor de uma sequência de números
print('Valores: 3, 9, 5, 4, 1')
print('Maior valor:', max(3, 9, 5, 4, 1))
print('Menor valor:', min(3, 9, 5, 4, 1))


