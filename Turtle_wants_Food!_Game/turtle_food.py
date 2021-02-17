import turtle
import time
import random

delay = 0.1

window = turtle.Screen()
window.bgcolor('black')
window.title("Turtle Wants Food Game")
window.setup(width = 600, height = 600)
window.tracer(0)

abby = turtle.Turtle()
abby.speed(0)
abby.shape("turtle")
abby.pencolor('white')
abby.penup()
abby.goto(0,100)
abby.direction = "stop"


def move():
    if abby.direction == "up":
        y = abby.ycor() #y coordinate of the turtle
        abby.sety(y + 20)
 
    if abby.direction == "down":
        y = abby.ycor() #y coordinate of the turtle
        abby.sety(y - 20)
 
    if abby.direction == "right":
        x = abby.xcor() #y coordinate of the turtle
        abby.setx(x + 20)
 
    if abby.direction == "left":
        x = abby.xcor() #y coordinate of the turtle
        abby.setx(x - 20)
def go_up():
    if abby.direction != "down":
        abby.direction = "up"
 
def go_down():
    if abby.direction != "up":
        abby.direction = "down"
 
def go_right():
    if abby.direction != "left":
        abby.direction = "right"
 
def go_left():
    if abby.direction != "right":
        abby.direction = "left"
        
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("white")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
score = 0


while True:
    window.update()
    move()
    time.sleep(delay)
    if abby.distance(food) <15:
        x = random.randint(-350, 350)
        y = random.randint(-290, 290)
        food.goto(x, y)
        score = score+10
        pen.clear()
        pen.write("Score: {} ".format(score), align="left", font=("Courier", 24, "normal"))

    if abby.xcor() > 400 or abby.xcor() < -400 or abby.ycor() > 400 or abby.ycor() < -400:
        time.sleep(1)
        abby.goto(0, 0)
        score = 0
        abby.direction = "stop"
        pen.clear()
        

    

        
   
