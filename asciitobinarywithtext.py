#programa converte uma string inteira para binario
string=input('digite uma palavra ')
lista=list(string)
binario=[]
i=0
for i in range(len(lista)):
  binario.append(bin(ord(lista[i])))
  #print(binario[i])
print(binario)



by: Gusttavomarinho

