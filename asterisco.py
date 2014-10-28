#pseudocripto pythons para zumbis
txt=open('mensagem.txt')
cript=open('cript.txt','w')

for linha in txt.readlines():
    for letra in linha: 
        cript.write('*')
txt.close()
cript.close()
