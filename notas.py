notas=[5]
n=0
soma=0
for i in range(5):
    notas.append(float(input("digite a nota: ")))
while n<5:
    soma=notas[n] + soma    
    n=n+1
media=soma/5
print('sua media foi: ',media)
    
