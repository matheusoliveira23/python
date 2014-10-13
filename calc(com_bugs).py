#calculadora básica
n1=int()

print("digite o primeiro numero ")
n1=input(n1)
n2=int()
print("digite o segundo numero numero ")
n2=input(n2)
operacao=int()
print("digite o codigo da operação sendo 1 para soma 2 para subtração 3 para multiplicação 4 para divisão 5 para potenciação e 6 para radiciação   ")
operacao=input(operacao)
print(operacao)
resultado=int()

if operacao==1:
    soma=n1+n2
    resultado=soma
elif operacao==2:
    subtracao=n1-n2
    resultado=subtracao
elif operacao==3:
    mult=n1*n2
    resultado=mult
elif  operacao==4:
    div=n1/n2
    resultado=div
elif operacao==5:
    pot=n1*n2
    resultado=pot
elif operacao==6:
    rad=n1**(1/n2)
    resultado=rad
print('o resultado da operacao solicitada é ',resultado)


