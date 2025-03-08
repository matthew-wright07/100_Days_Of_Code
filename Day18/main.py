from turtle import Turtle, Screen
tim = Turtle()

for _ in range(4):
    for _ in range(10):
        tim.pendown()
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        
    tim.right(90)

screen = Screen()
screen.exitonclick()