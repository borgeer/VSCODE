
ne=0
cont=0
res=[]
perg1 = ['Telefonou para a vítima?', 'Esteve no local do crime?','Mora perto da vítima?' , 'Devia para a vítima?', 'Já trabalhou com a vítima?']

for x in range(0, len(perg1)):
    res= str(input(f'Digite a resposta de {perg1[x]}'))
    if res=='sim':
        cont+=1
    else:
        ne+=1

if cont==2:
    print ('Suspeita')
if cont ==3<=4:
    print ("Complice")
if cont ==5:
    print("Assassino")

if ne ==5:
    print ("O cara é o melhor")
