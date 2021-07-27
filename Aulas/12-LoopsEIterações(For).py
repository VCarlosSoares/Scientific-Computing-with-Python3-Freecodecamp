# O Loop for é considerado um loop definido, ou seja, nos definimos com exatidão a quantidade de vezes que será executado
# Podemos faze-lo executar um trecho de código a quantidade de vezes que tem um elemento de uma lista por exemplo,
# ou então a quantidade de linhas em um arquivo por exemplo.
# Vale ressaltar que a variável de iteração irá assumir o valor do elemento,
# e vai assumir o valor posterior a cada execução do loop até que não haja mais elementos

# Exemplo 1: Executando o print pela quantidade de elementos em uma lista
for i in [9, 7, 5, 3, 1]:
    print(i)
print('Finalizado!\n')

# Exemplo 2: um print de boas vindas para cada aluno em uma lista
alunos = ['Vitor', 'Carlos', 'Soares']
for aluno in alunos:
    print('Bem-vindo {}!'.format(aluno))
print('Finalizado!\n')