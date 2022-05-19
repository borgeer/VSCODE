print ("1= SOMA, 2= DIVISAO, 3= SUBTRAÇÃO, 4= MULTIPLICAÇÃO 5=POTENCIA 6=SAIR")
op = int(input("Digite o numero da operação que gostaria de fazer: "))


while op>=7 or op<=0:
    print("Digite um numero válido de operação ")

    op = int(input("Digite o numero da operação que gostaria de fazer: "))
    op = int(input("Digite 6 para sair "))

if op==1:
    soma=0
    a=int(input("Digite primeiro numero: "))
    b=int(input("Digite o segundo numero: "))
    soma= a+b
    print (f'A soma de {a}+{b}= {soma}')

if op==2:
    a=int(input("Digite primeiro numero: "))
    b=int(input("Digite o segundo numero: "))
    divisao = a/b
    print (f'A divisão de {a}/{b}= {divisao:.2f}')

if op==3:
    a=int(input("Digite primeiro numero: "))
    b=int(input("Digite o segundo numero: "))
    sub=a-b
    print (f' A subtração de {a}-{b}={sub} ')

if op==4:
    a=int(input("Digite primeiro numero: "))
    b=int(input("Digite o segundo numero: "))
    mul=a*b
    print (f'A multicação de {a}x{b}={mul}')

if op==5:
    a=int(input("Digite primeiro numero: "))
    b=int(input("Digite o segundo numero: "))
    ex=a**b
    print(f'O numero {a} elevado a {b} é {ex}')

if op == 6:
    print ("Finalizou a calculadora ")