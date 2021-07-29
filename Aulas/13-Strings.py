# String são uma sequência de caracteres
# Podemos utilizar tanto aspas simples 'Hello' quanto aspas duplas "Hello" para representar uma string
# Quando "somamos" duas strings por meio do +, na verdade estamos concatenando (mesclando) elas
# Mesmo sendo uma string numérica '123' ainda sim é uma string, e podemos convertela para int/float com a sintaxe int() e float()

#Exemplo 1: concatenando e convertendo string
str1 = 'Olá'
str2 = 'Vitor'
bem_vindo = str1 + str2
print(bem_vindo)

str3 = '123'
str4 = str3 + '1'
print(str4)

x = int(str3) + 1
print(x)

a = 'Olá'
b = a + 'Vitor'
print(b)

c = a + ' ' + 'Vitor'
print(c, '\n')

### Dados de Entrada ###
# É recomendado/default que se leia os dados como uma string e que possa realizar conversões posteriormente se necessário
# Isso nos da mais controle sobre erros de utilização ou entradas invalidas (try/except)

### Por dentro da string ###
# Como citado, uma string é uma cadeia de caracteres e podemos acessar esses caracteres por meio de um indice (posição)
# um indice deve ser um número inteiro e começar da posição 0
# se olharmos para a string fruta = 'banana' teremos:
# indíce:                    012345
# portanto, fruta[3] == a, fruta[0] == b

# Exemplo 2: acessando os índices da string 'banana'
fruta = 'banana'
letra = fruta[0]
print(letra)

x = 3
w = fruta[x - 1]
print(w, '\n')

# Devemos tomar cuidado em acessar um indice, caso tente acessar um indice invalido: ex.: fruta[15] vai gerar erro

# Exemplo 3: tratando erro de indice invalido
fruta = 'banana'
indice = input('Digite um índice válido da string banana: ')
try:
    letra = fruta[int(indice)]
    print(letra, '\n')
except:
    print('Indice inválido!\n')


### String len ###
# conseguimos obter a quantidade de caractéres de uma string utilizando a função len()
# Obs.: devemos tomar cuidado com len e indice
# Ex.: len('banana') = 6
# se quisermos pegar a ultima letra da banana e colocarmos letra = banana[6]
# vai dar bug, pois a ultima letra está armazenada no indice 5
# portanto, podemos acessar o indice da ultima letra da string indice = len(string - 1)

# Exemplo 4: obtendo o tamanho da string 'banana' e acessando a ultima letra
fruta = 'banana'
tamanho = len(fruta)
print(tamanho)

ultimaLetra = fruta[tamanho - 1]
print(ultimaLetra, '\n')

# Exemplo 5: acessando e mostrando todos os indices da string usando loops (while)
indice = 0
fruta = 'banana'
while indice < len(fruta):
    letra = fruta[indice]
    print('Indice: {}: {}'.format(indice, letra))
    indice = indice + 1
print('Finalizado!\n')

# Exemplo 5.1: usando loops (for) # Obs.: nesse caso não precisa de variável de iteração
fruta = 'banana'
for letra in fruta:
    print(letra)
print('Finalizado!\n')

# Exemplo 6: procurando a quantidade de vezes que a letra 'a' aparece na string 'banana'
qtdA = 0
for letra in 'banana':
    if letra == 'a':
        qtdA = qtdA + 1
print('Quantidade total em que aparece a letra a na string banana:', qtdA)


### Cortando uma String ###
# Podemos "cortar" um pedaço de uma string com a sintaxe frase[4:7]
# Devemos passar dois elementos para cortar a string, o indice de onde começa e o indice de onde acaba
# Vale ressaltar que isso inclui o elemento do indice inicial (4) mas não inclui o elemento do indice final (7)
# Obs.: Quando passamos um índice maior do que a string possui no segundo valor, o python entende
# que é para ir até o final da strng

# Se não inserirmos o primeiro elemento, exemplo [:7] o python assume que queremos ir do começo até o elemento indicado (7)
# Se não inserirmos o segundo elemento, exemplo [4:] o python assume que queremos partir daquele elemento até o final da string

# Exemplo 7: utilizando pedaços de uma string 'Monty Python'
# Indice:                                      0123456789...
s = 'Monty Python'
print('\nString:', s)

print('Indice 0 até o 4:', s[0:4])
print('Indice 6 até o 7:', s[6:7])
print('Indice 6 até o 20 (obs.: não existe indice 20 para essa string):', s[6:20])

print('Do começo da string até o indice 7:', s[:7])
print('O indice 7 até o final da string:', s[7:])
print('Toda a string: ', s[:], '\n')

### in ###
# Podemos utilizar o operador lógico in para encontrar um caractere ou um pedaço de string dentro de outra string
# Ele vai retornar um tipo booleano (true ou false) caso encontre ou não
# Podemos utilizar o in junto a um if por exemplo

# Exemplo 8: utilizando o operador in para encontrar uma parte de string em outra string
fruta = 'banana'
n = 'n' in fruta
print(n)

print(('m' in fruta))

print(('nan' in fruta))

if 'a' in fruta:
    print('A fruta possui a letra a\n')

# Podemos utilizar os operadores < e > para verificar se uma parte da string está no começo ou no final da string
# Exemplo 9: Comparando strings com < e >
fruta = 'banana'
palavra = 'ba'

if palavra < 'banana':
    print('Está no começo da string banana\n')
elif palavra > 'banana':
    print('Está no final da string banana\n')
else:
    print('Sua string é banana\n')

### Biblioteca integrada para String ###
# O Python possui uma biblioteca integrada de funções para strings, quando chamamos uma string e colocamos um . podemos observa-lá
# Vamos utilizar algumas dessas funções, começando com:
# str.lower(): deixa todas as letras minusculas
# str.upper(): deixa todas as letras maiusculas

# Exemplo 10: função para tornar todas as letras maiúsculas ou minúsculas
msg = 'Olá Vitor'
print(msg)

msgMin = msg.lower()  # lower = minúsculo
print(msgMin)

print(msg.upper())    # upper = maiúsculo

print('Olá'.upper())

