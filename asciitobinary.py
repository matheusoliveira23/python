#este programa converte um caractere para seu binario equivalente seguindo a tabela ascii

#Recebendo os valores do usuario
texto=input("digite alguma letra: ")
a=int(ord(texto))
b=bin(a)
print("o binario da lera digitada é",b)
