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