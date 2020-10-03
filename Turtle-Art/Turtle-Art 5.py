import turtle    
import time 
import random 
  
num_str = input("Enter the side number of the shape you want to draw: ") 
if num_str.isdigit(): 
    foo = int(num_str) 
  
angle = 180 - 180*(foo-2)/foo 

turtle.title("Turtle Makes Shapes!")
turtle.up 
turtle.shape("turtle")
  
x = 0 
y = 0
turtle.setpos(x, y) 
  
  
numshapes = 12
for x in range(numshapes): 
    turtle.color(random.random(), random.random(), random.random()) 
    x += 5
    y += 5
    turtle.forward(x) 
    turtle.left(y) 
    for i in range(foo): 
        turtle.begin_fill() 
        turtle.down() 
        turtle.forward(70) 
        turtle.left(angle) 
        turtle.forward(70) 
        turtle.up() 
        turtle.end_fill() 
  
turtle.done() 