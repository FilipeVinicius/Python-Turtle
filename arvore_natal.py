import turtle
t = turtle.Turtle()
t.shape('turtle')
t.penup()
t.goto(0, -250)
t.pendown()

#tronco
t.color('brown')
t.forward(30)
t.begin_fill()
t.fillcolor('brown')
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(100)
t.end_fill()

#posição inicial
t.penup()
t.sety(-150)
t.setx(-60)
t.pendown
t.color('green')


#Triangulo
def triangulo(base, altura, cor):
  t.begin_fill()
  t.fillcolor(cor)
  t.left(90)
  t.fd(base)
  t.left(120)
  t.fd(altura)
  t.left(120)
  t.fd(base)
  t.end_fill()
  
triangulo(160,160, "green")

#Outro triangulo
t.fd(-65)
t.setx(-57)
t.left(30)
t.color('#90ee90')
triangulo(150, 150, "#90ee90")

t.fd(-65)
t.setx(-50)
t.left(30)
t.color('green')
triangulo(140, 140, "green")

t.fd(-65)
t.setx(-50)
t.left(30)
t.color('#90ee90')
triangulo(140, 140, "#90ee90")

t.fd(-65)
t.setx(-36)
t.left(30)
t.color('green')
triangulo(110, 110, "green")

t.fd(-60)
t.setx(-23)
t.left(30)
t.color('#90ee90')
triangulo(80, 80, "#90ee90")

#Circulos
def circulo(raio, cor):
	t.color(cor)
	t.begin_fill()
	t.fillcolor(cor)
	t.circle(raio)
	t.end_fill()

t.home()
t.goto(-53, -156)
circulo(9, 'red')

t.fd(69)
circulo(10, 'blue')

t.fd(76)
circulo(9, 'light green')

t.left(90)
t.fd(60)
circulo(9, 'purple')

t.left(90)
t.fd(70)
t.sety(-86)
t.fd(70)
circulo(9, '#Add8e6')

t.right(90)
t.fd(50)
t.setx(-36)
circulo(9, 'purple')

t.fd(54)
circulo(9, 'blue')

t.fd(54)
t.setx(-32)
circulo(9, 'orange')

t.right(90)
t.fd(41)
t.right(90)
circulo(9, '#Add8e6')

t.fd(52)
circulo(9, 'orange')

t.fd(55)
circulo(9, 'red')

t.fd(59)
circulo(9, 'orange')

t.left(90)
t.fd(81)

t.left(90)
t.fd(56)
circulo(9, 'orange')

t.fd(59)
circulo(9, 'blue')
t.fd(53)
t.setx(80)
circulo(9, 'red')

t.goto(-10, 160)
t.right(19)
t.begin_fill()
t.fillcolor('yellow')
for i in range(5):
  t.fd(80)
  t.right(144)
  
t.end_fill()
