from xmlrpc.client import boolean


soma=0

for cont in range (3):
    numero = int(input("Digite numeros validos para soma: \n"))
    if numero >=0:
        soma+=numero
        cont+1
    if numero <0:
        print ("Seu numero é invalido ")
        numero = (input)
    
print (f' Soma dos numero e {soma}')