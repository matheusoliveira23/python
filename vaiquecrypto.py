#cript vai que
import random
textoplano=input('digite a mensagem: ')
vet=list(textoplano)
random.shuffle(vet)
num=[]
for i in range(len(vet)):
    num.append(ord(vet[i]))
    num.append((num[i]+40))
    random.shuffle(num)
print('mensagem encriptada na forma decimal: ',num)
#def decripta(vet):
    #random
    
