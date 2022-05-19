"""Foram anotadas as idades e alturas de 30 alunos. FaÃ§a um Programa
que determine quantos alunos com mais de 13 anos possuem altura inferior Ã 
mÃ©dia de altura desses alunos."""

id=[]
alt=[]

for x in range(1,4):
    id.append(int(input(f'Digite a idade da {x}º pessoa ')))
    alt.append(float(input(f'Digite a altura da {x}º pessoa ')))

print (id)
print (alt)
mediaalt= sum(id)/len(alt)
print (mediaalt)
quant = 0

for x in range (1,len(id)):
    if id[x] >13 and alt[x] < mediaalt:
        quant+=1

print (f'a quantidade de alunos mais de 13 anos e altura inferior da media é {quant} ')