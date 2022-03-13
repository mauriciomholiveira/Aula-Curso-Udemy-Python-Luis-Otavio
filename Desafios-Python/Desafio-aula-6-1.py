#  Aqui perguntamos ao usuario alguns dados sobre o peso e altura
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso em Kg: "))

#  É feito o calculo do imc
imc = peso / altura ** 2

#  Imprimos o IMC
print("Seu IMC é: %.4f" % imc)

# Caso abaixo dos 16 ele mostra esse resultado Magreza Grave
if imc < 16:
    print("Magreza grave")
# Caso abaixo dos 17 ele mostra esse resultado Magreza Moderada
elif imc < 17:
    print("Magreza moderada")
# Caso abaixo dos 18.5 ele mostra esse resultado Magreza Leve
elif imc < 18.5:
    print("Magreza leve")
# Caso abaixo dos 16 ele mostra esse resultado Saudavel
elif imc < 25:
    print("Saudável")
# Caso abaixo dos 18.5 ele mostra esse resultado Sobrepeso
elif imc < 30:
    print("Sobrepeso")
# Caso abaixo dos 18.5 ele mostra esse resultado Obesidade Grau I
elif imc < 35:
    print("Obesidade Grau I")
# Caso abaixo dos 18.5 ele mostra esse resultado Obesidade Grau II (severa)
elif imc < 40:
    print("Obesidade Grau II (severa)")
# Caso abaixo dos 18.5 ele mostra esse resultado Obesidade Grau III (mórbida)
else:
    print("Obesidade Grau III (mórbida)")
