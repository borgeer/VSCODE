

nota=[]

for x in range(1,5):
    nota.append(float(input(f'Digite a nota do {x}º aluno ')))

for x in range(0,len(nota)):
    if nota[x] >=7 and nota[x]<=10:
        print (f'O aluno {x}º aprovou com nota {nota[x]} ')
    if nota[x]>=0 and nota[x]<=6.9:
        print (f'O aluno {x+1}º reprovou com nota {nota[x]} ')