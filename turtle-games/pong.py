#simple pong in python 3

import turtle

wn= turtle.Screen()
wn.title('Pong by GE')
wn.bgcolor('brown')
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('circle')
paddle_a.color('orange')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370, 0)

#Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('circle')
paddle_b.color('orange')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(370, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize()
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 18
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 18
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 18
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 18
    paddle_b.sety(y)


#Keybord binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down, 'Down')


#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font=('Courier', 24, 'normal'))

    # Paddle and ball colisions
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle_b.ycor() + 48 and ball.ycor() > paddle_b.ycor() - 48):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < paddle_a.ycor() + 48 and ball.ycor() > paddle_a.ycor() - 48):
        ball.setx(-360)
        ball.dx *= -1
        