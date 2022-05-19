"""Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, 
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )"""


temp=[]
meses =["Janeiro", "Fevereiro", "MarÃ§o", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]



for x in range (1,5):
    temp.append(float(input("Digite a temperatura de casa mês ")))

mediatemp = sum(temp)/len(temp)

for x in range(1, len(temp)):
    if temp[x] >=mediatemp:
        print (f'A temperatura que foi acima da média {temp[x]}ºC no mês de {meses[x]} ')
