

#  Aula sobre prints e separadores
"""
separar as palavras com pontos, virgular, tracinho: sep='.' sep=',' sep='-'
para juntar os prints se usa a função end=''
e para juntar os print e colocar um separador ao final do print que voce chamado a funçao
se usa end='-' ou pode substituir por qualquer outra coisa.
"""

#  print('Joao', 'e', 'maria', sep='-', end='')
#  Desafio 1 pegar esse CPF 824.176.070-18 e deixar ele separado com pontos e no final com o -

#  Primeira forma usando a função sep e end.
print('824', '176', '070', sep='.', end='-')
print('18')

#  Segunda Forma mais direta
cpf = '824.176.070-18'
print(cpf)

