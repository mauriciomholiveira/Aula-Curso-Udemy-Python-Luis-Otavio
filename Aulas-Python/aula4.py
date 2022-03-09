"""
Tipos de dados.
str - string - textos "assim" ou 'assim'
int - inteiro - 12345 (que nao possua ponto, é valido numeros negativos tambem)
float - real/flutuante - negativo ou positivo com numeros com pontos (1.6, 50.95, -0.96)
bool - booleano/logica - True ou False
"""
print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print('L' == 'L') or ('L' == 'l')

'''
converter qualquer outro valor ou string 
'''

print('Luiz', type('Luiza'), bool('Luiz'))

#  Desafio 2: fazer uma ficha cadastral

print('Nome Completo: ', 'Mauricio Henrique de Oliveira', type('Mauricio Henrique de Oliveira'))
print('Idade: ', 25, type(25))
print('É maior de idade? ', 18 > 25, type(18 > 25))
print('Altura: ', 1.70, type(1.70))
