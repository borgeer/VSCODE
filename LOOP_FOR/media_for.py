media= 0
final = 0

n = int(input("Quantas notas o aluno tem? "))
for nota in range(n):
    nota= float(input(f'Digite as notas do aluno {nota+1}/{n} : '))
    media=nota+media
    
final = media/n    
print (f' A media do aluno ficou em {final:.2f}')