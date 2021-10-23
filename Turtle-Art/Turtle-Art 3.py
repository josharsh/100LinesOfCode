import turtle

window = turtle.Screen()
window.setup(width=1500, height=700, startx=5, starty=5)
window.bgcolor('black')
euler = turtle.Turtle()  
euler.shape("turtle")
scale = 5 
euler.penup()
euler.setpos(-390, 0)
euler.pendown()
euler.pencolor('white')

current = 0   
seen = set()  

for step_size in range(1, 100):

    backwards = current - step_size

    if backwards > 0 and backwards not in seen:
        euler.setheading(90)  # 90 degrees is pointing straight up
        # 180 degrees means "draw a semicircle"
        euler.circle(scale * step_size/2, 1800)
        current = backwards
        seen.add(current)

    # Otherwise, go forwards
    else:
        euler.setheading(270)  # 270 degrees is straight down
        euler.circle(scale * step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done()