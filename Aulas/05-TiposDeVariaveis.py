### Tipos de Variaveis ###

inteiro = 1
real = 2.3
frase = 'Ola'
booleano = 3 > 2

print(type(inteiro))
print(type(real))
print(type(frase))
print(type(booleano))
print(type(5))
print(type('Sou uma str'))

### Conversão dos Tipos de Variaveis ###
# Obs.: Caso converta de string para float/int o valor da string deve ser totalmente numerico, se tiver letras vai bugar #

i = 1
print(type(i))

f = float(i)   #convertendo para float
print(type(f))

s = str(f)     #convertendo para string
print(type(s))

valorEmString = '123'
valorEmInteiro = int(valorEmString)
print(valorEmInteiro * 2)

### Divisão de Números Inteiros ###
# Obs.: O Python3 sempre vai gerar um número real na divisão de dois números inteiros #

print(10 / 2)
print(9 / 2)
print(99 / 100)
print(99.0 / 100.0)