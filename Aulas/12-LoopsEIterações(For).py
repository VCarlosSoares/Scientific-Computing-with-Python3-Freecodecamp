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

### Tipo None ###
# O tipo de variável None só assume um valor: nenhum
# é útil quando não sabemos qual valor atribuir a uma variável que posteriormente será comparada com outra variável
# por exemplo:
# antes de uma lista começar, você não pode assumir que o menor valor de uma lista é -1 pois não sabe quais valores contém naquela lista

### Operador is e is not ###
# podemos comparar o is com ==, e o is not com !=, entretanto, o is/is not é mais poderoso que o == e o !=
# a diferença entre esses operadores é que o is/is not compara também o tipo da variável
# exemplos:
# 0 == 0.0   # o resultado de retorno dessa operação será True
# 0 is 0.0   # o resultado de retorno dessa operação será False, pois uma variável é int e a outra é float

# Exemplo 3: encontrando o maior valor em uma lista de números começando com o valor None
maior_numero = None
print('Antes do Loop, maior número:', maior_numero)
for numero in [9, 41, 12, 3, 74, 15]:
    if maior_numero == None:
        maior_numero = numero
    elif numero > maior_numero:
        maior_numero = numero
    print('Durante o Loop, maior número:', maior_numero)
print('Finalizou o Loop, maior número:', maior_numero, '\n')

# Exemplo 4: encontrando o menor número em uma lista começando com o valor None
menor = None
contador = 0
print('Lista de Números: 9, 41, 12, 3, 74, 15')
for numero in [9, 41, 12, 3, 74, 15]:
    if menor is None:
        menor = numero
    elif menor > numero:
        menor = numero
    contador = contador + 1
    print('Execução número {} - Menor valor encontrado: {}'.format(contador, menor))
print('Loop finalizado! O menor número encontrado foi:', menor, '\n')

### Variável Sentinela ###
# Uma variável sentinela, ou variável contadora, serve para identificar a quantidade de vezes que um loop foi executado
# Geralmente essa variável começa com o valor inicial de i = 0, a cada execução do loop i = i + 1,
# no final das execuções, a variável i vai conter a quantidade de vezes em que o loop foi executado

# Exemplo 5: usando variável sentinela para contar quantas execuções teve no loop for
i = 0
for numero in [9, 41, 12, 3, 74, 15]:
    i = i + 1
    print('Execução número:', i)
print('Total de iterações no loop:', i, '\n')

# Exemplo 6: somando os valores de uma lista
i = 0
soma = 0
print('Valores na lista: 9, 41, 12, 3, 74, 15')
for numero in [9, 41, 12, 3, 74, 15]:
    i = i + 1
    soma = soma + numero
    print('Execução número: {}, número adicionado: {}, total somado: {}'.format(i, numero, soma))
print('Total da soma dos valores:', soma)

# Exemplo 7: calculando a média (a importância da variável sentinela)
contador = 0   #Variável sentinela
soma = 0
print('Valores na lista: 9, 41, 12, 3, 74, 15')
for numero in [9, 41, 12, 3, 74, 15]:
    contador = contador + 1
    soma = soma + numero
    print('Execução número: {}, número adicionado: {}, total somado: {}'.format(i, numero, soma))
print('Finalizando o loop, total de execução: {}, total somado: {}, média dos valores: {}\n'
      .format(contador, soma, round((soma / contador), 2)))

# Exemplo 8: usando o if para filtrar o loop (mostrar apenas valores > 20)
print('Valores na lista: 9, 41, 12, 3, 74, 15')
for numero in [9, 41, 12, 3, 74, 15]:
    if numero > 20:
        print('Número grande:', numero)
print('Finalizado!\n')

# Exemplo 9: procurando se em uma lista contém um determinado valor utilizando variável booleana (True ou False)
achou = False
numeroDesejado = 3
print('Número desejado:', numeroDesejado)
print('Lista de Números: 9, 41, 12, 3, 74, 15')
for numero in [9, 41, 12, 3, 74, 15]:
    if numero == numeroDesejado:
        achou = True
        #break - poderiamos adicionar um break aqui já que nosso objetivo é verificar se o número desejado está na lista
    print(achou, numero)
print('Loop finalizado! Encontramos o número desejado?', achou, '\n')

# Exemplo 10: usando range
frase = 'Vitor'
for i in range(len(frase)):
    print(i)
    