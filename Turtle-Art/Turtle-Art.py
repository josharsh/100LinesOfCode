from turtle import *
from random import *


speed(0) 

bgcolor('black') 

x = 1

while x < 400:

    #random colors from 0 to 255 each time the loop runs
    r = randint(0,255) 
    g = randint(0,255) 
    b = randint(0,255) 

    colormode(255)

 
              
    pencolor(r,g,b) 
                   
    fd(50 + x)
    rt(90.9111)
        
    x = x+1 

exitonclick() 