# Pong game 


import turtle


wind = turtle.Screen() 
wind.title("Pong by Raymond")
wind.bgcolor("blue")
wind.setup(width= 800, height=600)
wind.tracer(0)

# Paddle 1
Paddle_1 = turtle.Turtle()
Paddle_1.speed(0)
Paddle_1.shape("square")
Paddle_1.color("red")
Paddle_1.shapesize(stretch_wid=5, stretch_len=1)
Paddle_1.penup()
Paddle_1.goto(-350, 0)


# Paddle 2


# Ball


# Main game loop
while True:
    wind.update()