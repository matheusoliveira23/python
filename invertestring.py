#inverte nome é inutil mas deu vontade de fazer
texto=''
texto=input(texto)
tam=len(texto)
i=0
inv=slice(texto)
for i in range(tam):
    inv[i]=inv[i-1]
    


