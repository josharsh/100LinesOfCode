import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(1400, 760)
t = Turtle("turtle")
t.speed(-1)

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickright(x, y):
    t.clear()

    
def up():
    t.color('red')

def down():
    t.color('green')

def left():
    t.color('blue')

def right():
    t.pensize(5)


def main():
    turtle.listen()


    t.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)

    turtle.onkey(up, 'r')
    turtle.onkey(down, 'g')
    turtle.onkey(left, 'b')
    turtle.onkey(right, 'Up')

    screen.mainloop()

main()
