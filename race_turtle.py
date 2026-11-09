#Santiago Pineda, Turtle Race
import turtle as t
import random 
import time
round = 0 
def moveTurtle(turtle):
    turtle.forward(random.randint(0,300))
turtle_one = t.Turtle()
turtle_two = t.Turtle()
turtle_three = t.Turtle()
turtle_four = t.Turtle()
turtle_five = t.Turtle()
goal = t.Turtle()
turtle_one.color("green")
turtle_one.shape('turtle')
turtle_two.color("red")
turtle_two.shape('turtle')
turtle_three.color("gold")
turtle_three.shape('turtle')
turtle_four.color("purple")
turtle_four.shape('turtle')
turtle_five.color("blue")
turtle_five.shape('turtle')
goal.color("black")
goal.penup()
goal.goto(1000,1000)
print(turtle_one.pos())
turtle_two.penup()
turtle_two.goto(0.0, 100)
turtle_three.penup()
turtle_three.goto(0.0, -50)
turtle_four.penup()
turtle_four.goto(0.0, 50.0)
turtle_five.penup()
turtle_five.goto(0, -100)
while True:
    moveTurtle(turtle_one)
    moveTurtle(turtle_two)
    moveTurtle(turtle_three)
    moveTurtle(turtle_four)
    moveTurtle(turtle_five)
    round =+ 1

t.exitonclick()