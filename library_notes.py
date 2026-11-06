#Santiago Pineda
import turtle as t
# using from turtle import * means the same thing. Along with import turtle as t. The only difference with t is that you don't grab the WHOLE library
red = t.Turtle()
t.showturtle()
t.color('darkviolet')
t.width(10)
t.circle(120)
t.width(5)
t.forward(250)
t.left(120)

t.color('blue')
t.forward(250)
t.left(120)

t.color('green')
t.forward(250)
t.left(120)
t.clearscreen()

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
loop_helper = 0

t.speed(1000)
for num in range(300):
    t.color(colors[loop_helper])
    t.fd(3)
    t.left(1)

    loop_helper += 1
    if loop_helper  == 6:
        loop_helper = 0

print(t.pos()) #helps you know when it reaches a certain point
print(t.xcor())
print(t.ycor())

t.clearscreen()
t.hideturtle()
t.forward(200)
t.showturtle()
t.forward(200)
t.shape("turtle")
t.shapesize(1,1,1)
for x in range(0,100):
    t.tilt(x)
t.shearfactor(20)
t.shapetransform(10,5,3,2)

t.exitonclick()