# A Exceção serve para previnir erros de execução que travam o seu programa
# Caso a tentativa (try) consiga ser executada sem nenhum problema, a exceção (except) é ignorada e o fluxo segue normalmente
# Caso a tentativa (try) falhe, gerando bug, o programa pula para a exceção (except) onde há um tratamento genérico para o problema
# Este tratamento genérico não interrompe o fluxo de execução do programa, o que aconteceria se não tivesse o try/except

# Obs.: o try é executado seguencialmente e até que ocorra uma exceção (ou totalmente caso não ocorra exceção)
# Exemplo:
#   linha 1 - Ok                  (será executada sem nenhum problema)
#   linha 2 - ocorreu o bug       (aqui ocorre o bug e o programa vai "pular" para a exceção a partir daqui)
#   linha 3 - Ok                  (está linha não será executada, apesar de estar Ok)


# Exemplo 1: Tentando convertar uma string não numérica para int (bug proposital) para cair no except
frase = 'Olá Vitor'
try:
    emNumero = int(frase)
except:
    emNumero = -1

print('Exemplo 1:', emNumero)

# Exemplo 2: Convertendo uma string de números para int (funciona) e não gerar exceções
frase = '123'
try:
    emNumero = int(frase)
except:
    emNumero = -1

print('Exemplo 2:', emNumero)

# Exemplo 3: É possível observar que o try é executado normalmente até que aconteça a exceção (linha 35)
frase = 'Vitor'
try:
    print('Olá')
    emNumero = int(frase)
    print('Aluno')
except:
    emNumero = -1

print('Finalizado', emNumero)

# Exemplo 4: Perguntando um número ao usuário
numero = input('Informe um numero inteiro positivo: ')
try:
    iNumero = int(numero)
except:
    iNumero = -1

if iNumero > 0:
    print('Bom Trabalho!')
else:
    print('Isso não é um número válido!')