media = 0

for num in range (2):
    num= int(input("Digite somente numeros inteiros: "))
    if num>=0:
        media = num+media
    
    if num <0:
        print ("Numero ignorado por ser invalido")

media = media/2
if media <=0:
    print ("Media não pode ser calculada pois numeros são invalidos")
else:
    print (media)
