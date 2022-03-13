"""
Formatar texto com f strings
"""

nome = "Mauricio"
idade = 25
peso = 84
altura = 1.70
imc = peso / altura ** 2

print(f'Olá {nome} voce tem {idade} anos e seu imc é {imc:.2f}')
print('Olá {} voce tem {} anos e seu imc é {:.2f}'.format(nome,  idade, imc))
print('Olá {n} voce tem {i} anos e seu imc é {im:.2f}'.format(n=nome,  i=idade, im=imc))
