#calculadora básica

#Funcionando com numeros inteiros (https://github.com/Gusttavomarinho/)
n1=int()
print("digite o primeiro numero ")
n1=float(input())
n2=int()
print("digite o segundo numero numero ")
n2=float(input())
operacao=int()
print("digite o codigo da operação sendo 1 para soma 2 para subtração 3 para multiplicação 4 para divisão 5 para potenciação e 6 para radiciação   ")
operacao=int(input())
print('sua escolha eh :',operacao)
if operacao < 0:
        print('Error - opção negativa')
elif operacao == 1:
        soma=int(n1+n2)
        print('Seu resultado:',soma)
elif operacao == 2:
        sub=int(n1-n2)
        print(sub)
        print('Seu resultado:',sub)
elif operacao == 3:
        mult=int(n1*n2)
        print('Seu resultado:',mult)
elif operacao ==4:
        div=int(n1/n2)
        print('Seu resultado:',div)
elif operacao ==5:
        pot=n1**n2
        print('seu resultado',pot)
elif operacao ==6:
        rad=n1**(1/n2)
        print('seu resultado',rad)
else:
        print('Opção invalida - Digite um valor de 1 a 6 na opção')

