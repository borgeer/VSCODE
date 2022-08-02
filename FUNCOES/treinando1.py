

def inicio():
    d=int(input("Digite um numero: "))
    e=int(input("Digite outro numero: "))
    
    if d>=e:
        soma=d+e
        print (f'O numero {d} é maior ou igual que o {e} e a soma é: {soma}')
    else:
        soma=d*e
        print(f'O numero {d} é menor que o {e} e a multiplicação é: {soma}')


    x = int(input(f'Caso queria continuar digite {1} pra sim e pra nao {2}: '))
    if x==1:
        return inicio()
    else:
        print("forte abraço ")
inicio ()

