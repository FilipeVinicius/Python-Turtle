import turtle 

tartaruga = turtle.Turtle()
tartaruga.shape('turtle')

 #RETÂNGULO
tartaruga.begin_fill()
tartaruga.color('#FFC000')
tartaruga.fillcolor('#FFC000')
tartaruga.forward(250)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(250)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.end_fill()

#janela1 - configurando a posição
tartaruga.penup()
tartaruga.color('#000000')
tartaruga.setx(30)
tartaruga.sety(-30)
tartaruga.pendown()

#função para desenhar janela
def desenharJanela():
  tartaruga.begin_fill()

  for i in range(2):
        tartaruga.fillcolor('#000000')
        tartaruga.right(90)
        tartaruga.forward(70)
        tartaruga.right(90)
        tartaruga.forward(28)
  tartaruga.end_fill()

#desenhar janela 1
desenharJanela()

#desenhar janela 2
tartaruga.penup()
tartaruga.setx(145)
tartaruga.pendown()
desenharJanela()

#Voltar para o ponto inicial
tartaruga.penup()
tartaruga.home()
tartaruga.pendown()

#desenhar quadrado
tartaruga.left(180)
tartaruga.color('#FF8200')
tartaruga.begin_fill()
tartaruga.fillcolor('#FF8200')

for i in range(3):
  tartaruga.forward(100)
  tartaruga.left(90)
  
tartaruga.end_fill()

#desenhar porta
tartaruga.color('#000000')
tartaruga.penup()
tartaruga.setx(-30)
tartaruga.sety(-101)
tartaruga.begin_fill()
tartaruga.fillcolor('#000000')

tartaruga.forward(55)
tartaruga.left(90)
tartaruga.forward(40)
tartaruga.left(90)
tartaruga.forward(55)

tartaruga.end_fill()

#Desenhar triângulo
tartaruga.home()
tartaruga.color('#C0504D')
tartaruga.begin_fill()
tartaruga.fillcolor('#C0504D')

for i in range(3):
  tartaruga.left(120)
  tartaruga.forward(100)
  
tartaruga.end_fill()

#desenhar telhado
tartaruga.color('#C00000')
tartaruga.begin_fill()
tartaruga.fillcolor('#C00000')

tartaruga.forward(250)
tartaruga.left(120)
tartaruga.forward(100)
tartaruga.left(60)
tartaruga.forward(250)

tartaruga.end_fill()

