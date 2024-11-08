import turtle
import random

#Lista com tartarugas, cores e a posição inicial delas no eixo y
lista_tartaruga = []
lista_tartaruga_cores = ['red', 'green', 'blue', 'black', 'purple']
lista_tartaruga_posicao_y = [-100, -50, 0, 50, 100]

 #Entrada da aposta
print("Bem-vindo ao Turtle Racing! Faça sua aposta agora mesmo!")
aposta = input("Em qual tartaruga você deseja apostar? red, green, blue, black ou purple? ")


#Fazendo a linha de chegada
linhaChegada = turtle.Turtle()
linhaChegada.shape()
linhaChegada.penup()
linhaChegada.setx(50)
linhaChegada.sety(120)
linhaChegada.pendown()
linhaChegada.right(90)
linhaChegada.forward(250)

#Criando as tartarugas e posicionando elas
for i in range(5):
  t = turtle.Turtle()
  t.shape('turtle')
  t.color(lista_tartaruga_cores[i])
  t.penup()
  t.setx(-200)
  t.sety(lista_tartaruga_posicao_y[i])
  t.speed(random.randint(1,10))
  lista_tartaruga.append(t)

#Algoritmo para definir a vencedora
tartaruga_vencedora = None
while tartaruga_vencedora == None:
  for tartaruga in lista_tartaruga:
    tartaruga.forward(random.randint(1,10))
      
    if tartaruga.xcor() > 40:
     tartaruga_vencedora = tartaruga.color()[0]   

#Mostrando se o usuário acertou a aposta ou não     
print("A tartaruga vencedora foi:",tartaruga_vencedora)  
if tartaruga_vencedora == aposta:
  print("Parabéns! Você acertou.") 
else:
  print("Poxa vida! Você errou.")
