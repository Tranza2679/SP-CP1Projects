#Santiago Pineda, Turtle Race
import turtle as t
import random 
round = 0 
program_end = False
def setUp(turtle):
    global color
    turtle.penup()
    turtle.shape('turtle')
    color = random.randint(0,5)
    if color == 1:
        turtle.color('red')
    elif color == 2:
        turtle.color('gold')
    elif color == 3:
        turtle.color('green')
    elif color == 4:
        turtle.color('blue')
    else:
        turtle.color('darkviolet')
    turtle.goto(-500, random.randint(-500,500))
    turtle.pendown()
def moveTurtle(turtle):
    turtle.forward(random.randint(0,300))
def goal_checker(check):
    if check.xcor() >=500:
        t.exitonclick()
    else:
        pass

turtle_one = t.Turtle()
turtle_two = t.Turtle()
turtle_three = t.Turtle()
turtle_four = t.Turtle()
turtle_five = t.Turtle()
goal = t.Turtle()
goal.color("black")
goal.penup()
goal.goto(500,500)
goal.pendown()
goal.goto(500,-500)
setUp(turtle_one)
setUp(turtle_two)
setUp(turtle_three)
setUp(turtle_four)
setUp(turtle_five)


while program_end == False:
    moveTurtle(turtle_one)
    goal_checker(turtle_one)
    
    moveTurtle(turtle_two)
    goal_checker(turtle_two)

    moveTurtle(turtle_three)
    goal_checker(turtle_three)
    moveTurtle(turtle_four)
    goal_checker(turtle_four)
    moveTurtle(turtle_five)
    goal_checker(turtle_five)

    round =+ 1

print(f"It took {round} rounds")