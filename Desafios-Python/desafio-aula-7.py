"""
*Criar variavel com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos  os valores na tela usando f-strings (com chaves)
"""
nome = str(input('Qual seu nome? '))
idade = int(input('Quantos anos vc tem? '))
altura = float(input('Qual sua altura? '))
peso = int(input('Qual seu peso? '))
ano_atual = int(input('Em que ano estamos? '))
imc = peso / altura ** 2
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa{peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}. ')
print(f'{nome} nasceu em {ano_nascimento}')
