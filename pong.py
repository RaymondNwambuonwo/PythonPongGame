# Pong game 


import turtle


wind = turtle.Screen() 
wind.title("Pong by Raymond")
wind.bgcolor("blue")
wind.setup(width= 800, height=600)
wind.tracer(0)

# Scpre
score_1 = 0
score_2 = 0


# Paddle 1
Paddle_1 = turtle.Turtle()
Paddle_1.speed(0)
Paddle_1.shape("square")
Paddle_1.color("red")
Paddle_1.shapesize(stretch_wid=5, stretch_len=1)
Paddle_1.penup()
Paddle_1.goto(-350, 0)


# Paddle 2
Paddle_2 = turtle.Turtle()
Paddle_2.speed(0)
Paddle_2.shape("square")
Paddle_2.color("orange")
Paddle_2.shapesize(stretch_wid=5, stretch_len=1)
Paddle_2.penup()
Paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("pink")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

#  Function
def Paddle_1_up():
    y = Paddle_1.ycor()
    y += 20
    Paddle_1.sety(y)

def Paddle_1_down():
    y = Paddle_1.ycor()
    y -= 20
    Paddle_1.sety(y)

def Paddle_2_up():
    y = Paddle_2.ycor()
    y += 20
    Paddle_2.sety(y)

def Paddle_2_down():
    y = Paddle_2.ycor()
    y -= 20
    Paddle_2.sety(y)

# Keyboard binding
wind.listen()
wind.onkeypress(Paddle_1_up, "w")
wind.onkeypress(Paddle_1_down, "s")
wind.onkeypress(Paddle_2_up, "Up")
wind.onkeypress(Paddle_2_down, "Down")

# Main game loop
while True:
    wind.update()

    #  Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Paddle_2.ycor() + 40 and ball.ycor() > Paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Paddle_1.ycor() + 40 and ball.ycor() > Paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1