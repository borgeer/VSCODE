
soma=0


n=int(input("Digite quantas vezes irá se repetir: "))

for g in range(1, n+1):
    print (f'o numero da sequencia {g}/{n}')
    numero = int(input("Digite o numero a ser somado: "))
    soma= soma+numero 

print ("A soma dos",n,"numero é",soma)

