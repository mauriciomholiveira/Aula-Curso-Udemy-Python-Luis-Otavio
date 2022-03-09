""""
str - string que seria um texto veja os exemplos abaixo
"""

print("Essa e ma srting!")

'''porem caso eu queira colocar as dentro de um tempo como que ficaria?
vejamos no exemplo abaixo
'''

print("aqui tem um 'texto' ")
print('aqui tem um "texto" ')

'''
o que vimos acima foi o seguinte, tivemos que colocar outro tipo de aspas no texto desejado
pois dessa maneira o codigo nao daria erro, e se caso colocassemos com a mesma aspas o 
interpretador iria executar porem daria erro
veja outro exemplo com erro
'''

print("aqui um ""texto")
'''
dessa maneira nosso codigo daria erro pois esta faltando aspas
e caso colocassemos  as mesmas aspas ele entenderia que a terceira aspas iniciaria um novo
texto, e tem um comando no print que faz ele ignorar qualquer outro comando dado dentro de aspas
veja exemplo
'''

print(r"aqui um \n texto")
""" se colocar um r antes das aspas ele ignora qualquer outro
comando dentro das aspas como foi o exemplo de \n que seria quebra de linha 
"""


