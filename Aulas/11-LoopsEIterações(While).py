### Loop While ###
# Loops servem para repetir um determinado trecho de código pela quantidade de vezes que o usuário desejar
# Essa quantidade de vezes é dada por uma variável de iteração (algo como auxiliar) que determinará
# quantas vezes deverá ser repetido o trecho do código.
# Essa variável de iteração vai mudar a cada execução do Loop (geralmente i = i -1)

# Exemplo 1: um loop com 5 iterações
i = 5
while i > 0:
    print(i)
    i = i - 1
print('Finalizado!')
print(i)

### Loops Infinitos e Break ###
# Podemos criar loops infinitos utilizando a palavra reservada True (verdadeiro), por tanto, while True é um loop infinito
# Podemos interromper o fluxo de execução de um loop de forma imediata utilizando a palavra break

# Exemplo 2: Loop infinito + break. Obs.: vai executar até que o usuário digite finalizar
while True:
    line = input('> ')
    if line == 'finalizar':
        break
    print(line)
print('Finalizado!')

# Para os loops, também existe o continue, o continue faz com que o loop volte para o inicio do trecho de código em loop
# Exemplo 3: usando continue para ignorar strings que comecem com #
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'finalizar':
        break
    print(line)
print('Finalizado!')

# Exemplo 4:
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1