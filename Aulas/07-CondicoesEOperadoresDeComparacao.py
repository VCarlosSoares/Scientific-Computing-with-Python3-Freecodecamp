### Operadores de Comparação ###
# <  : Menor que
# <= : Menor igual que
# == : Igual a
# >= : Maior igual que
# >  : Maior que
# != : Diferente de

### Condicional ###
# if : Através dos operadores de comparação, compara valores e retorna um tipo boolean (verdadeiro ou falso)
# se for verdadeiro ele vai executar o que está identado após o if
# se for falso ele vai ignorar o que está identado após o if e seguir o fluxo de execução do programa

# elif : Adiciona mais alternativas ao if
# exemplo - if x > 3:
#               ...
#           elif x < 5:
#               ...

# else : É uma contraposição do if e do elif
# se alguma condição (if ou elif) for verdadeira vai executar a identação que for verdadeira
# se todas as alternativas retornarem falso, vai executar a identação do else

x = 5
if x < 10:
    print('O Valor de X é menor que 10')
elif x > 20:
    print('O Valor de X é maior que 20')
else:
    print('O Valor de X está entre 10 e 20')

if x == 5:
    print('O Valor de X é igual a 5')
else:
    print('O Valor de X é diferente de 5')

### A importância da Identação no Python ###

if x > 1:
    print('O Valor é maior que 1')
    if x < 100:
        print('O Valor é menor que 100')
print('Finalizado!')

