import turtle

# SE O CÓDIGO NÃO FUNCIONAR, DESATIVE A LINHA 4
import wn as wn

# Setup do projeto
turtle.bgcolor('#a8a8a8')
turtle.title('Jogo de FUP by João Victor')

velocidade = 10
def desenha():
    bola.forward(velocidade)
    if bola.xcor() > 630 or bola.xcor() < -630:
        bola.left(100)
    elif bola.ycor() > 330 or bola.ycor() < -330:
        bola.left(90)
    janela.ontimer(desenha, 1000 // 24)
    

caneta = turtle.Turtle()
caneta.pensize(10)
for k in range(4):
    for i in range(4):
        if (i % 2 == 0):
            caneta.color('black')
        else:
            caneta.color('black')
            caneta.begin_fill()
#Criando o campo onde será jogado
caneta.speed(0)
caneta.up()
caneta.forward(650)
caneta.left(90)
caneta.down()
caneta.color('#c7c7c7')
caneta.forward(350)
caneta.left(90)
caneta.color('#c7c7c7')
caneta.forward(1300)
caneta.left(90)
caneta.color('#c7c7c7')
caneta.forward(690)
caneta.left(90)
caneta.forward(1300)
caneta.left(90)
caneta.forward(400)
turtle.hideturtle()
janela = turtle.Screen()
#Criação da imagem de funddo
'''
ima = turtle.Screen()
ima.bgpic('jaja1.gif')
'''

#Criação da bola
bola = turtle.Turtle()
bola.shape('circle')
bola.color('green')
bola.speed(0)
bola.up()

desenha()
#Criar o jogador A
jogadorA = turtle.Turtle()
jogadorA.speed(0)
jogadorA.shape('turtle')
jogadorA.color('#4a8c38')
jogadorA.shapesize(stretch_wid=5, stretch_len=3)
jogadorA.penup()

#Criar o jogador B
jogadorB = turtle.Turtle()
jogadorB.speed(0)
jogadorB.shape('turtle')
jogadorB.color('#9c601c')
jogadorB.shapesize(stretch_wid=5, stretch_len=3)
jogadorB.penup()

#criar fruta do jogo
frutaA = turtle.Turtle()
frutaA.speed(0)
frutaA.shape('classic')
frutaA.color('red')
frutaA.shapesize(stretch_wid=4, stretch_len=4)
frutaA.penup()

#Funções do jogador A

def jogadorA_up():
    y = jogadorA.ycor()
    y += 20
    jogadorA.sety(y)
def jogadorA_down():
    y = jogadorA.ycor()
    y -= 20
    jogadorA.sety(y)
def jogadorA_left():
    x = jogadorA.xcor()
    x -= 20
    jogadorA.setx(x)
def jogadorA_right():
    x = jogadorA.xcor()
    x += 20
    jogadorA.setx(x)

# Funções do jogador B
def jogadorB_up():
    y = jogadorB.ycor()
    y += 20
    jogadorB.sety(y)
def jogadorB_down():
    y = jogadorB.ycor()
    y -= 20
    jogadorB.sety(y)
def jogadorB_left():
    x = jogadorB.xcor()
    x -= 20
    jogadorB.setx(x)
def jogadorB_right():
    x = jogadorB.xcor()
    x += 20
    jogadorB.setx(x)
    
#Ouvidoria ouvir o teclado
janela.listen()

# player 1 control
janela.onkeypress(jogadorA_up, 'w')
janela.onkeypress(jogadorA_left, 'a')
janela.onkeypress(jogadorA_down, 's')
janela.onkeypress(jogadorA_right, 'd')

# player 2 control
janela.onkeypress(jogadorB_up, 'Up')
janela.onkeypress(jogadorB_left, 'Left')
janela.onkeypress(jogadorB_down, 'Down')
janela.onkeypress(jogadorB_right, 'Right')

#colisao da bola com os jogadores

janela.mainloop()