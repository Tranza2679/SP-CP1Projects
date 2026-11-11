#Santiago Pineda, Turtle Race
import turtle as t
import random 
round = 0 
program_end = False
def setUp(turtle, distance):
    turtle.penup()
    turtle.shape('turtle')
    color = random.randint(1,5)
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
    turtle.goto(-350, distance)
    turtle.pendown()
def moveTurtle(turtle):
    turtle.forward(random.randint(0,300))
def goal_checker(check):
    return check.xcor()>500


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
setUp(turtle_one,200)
setUp(turtle_two, 100)
setUp(turtle_three, 0)
setUp(turtle_four, -100)
setUp(turtle_five, -200)


while True:
    moveTurtle(turtle_one)
    if goal_checker(turtle_one):
        print("Turtle one won!")
        break
    
    moveTurtle(turtle_two)
    if goal_checker(turtle_two):
        print("Turtle two won!")
        break

    moveTurtle(turtle_three)
    if goal_checker(turtle_three):
        print("Turtle three won!")
        break

    moveTurtle(turtle_four)
    if goal_checker(turtle_four):
        print("Turtle four won!")
        break

    moveTurtle(turtle_five)
    if goal_checker(turtle_five):
        print('Turtle five won!')
        break

    round += 1

print(f"It took {round} rounds")