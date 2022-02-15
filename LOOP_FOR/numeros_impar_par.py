pares = 0 
impar = 0 

for cont in range(3):
    numero = int(input("Digite numeros para ver se é par ou nao: "))
    if (numero % 2):
        impar  = impar  +1
    else:
        pares= pares +1 
print (f'Na sequencia tem {impar} impar e {pares} par')