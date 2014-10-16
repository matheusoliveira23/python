texto=' '
texto=input("digite aqui uma palavra: ")
i=0
troca=" "
for i in range(len(texto)):
    
    if texto[i] in 'aeiou':
        troca=troca + "*"
    else:
        troca=troca + texto[i]
        
print(troca)
