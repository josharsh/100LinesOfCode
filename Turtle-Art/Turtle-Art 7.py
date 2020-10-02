import turtle 
  
# turtle object 
pen = turtle.Turtle() 
  
# function for creation of eye 
def eye(col, rad): 
    pen.down() 
    pen.fillcolor(col) 
    pen.begin_fill() 
    pen.circle(rad) 
    pen.end_fill() 
    pen.up() 
  
  
# draw face 
pen.fillcolor('yellow') 
pen.begin_fill() 
pen.circle(100) 
pen.end_fill() 
pen.up() 
  
# draw eyes 
pen.goto(-40, 120) 
eye('white', 15) 
pen.goto(-37, 125) 
eye('black', 5) 
pen.goto(40, 120) 
eye('white', 15) 
pen.goto(40, 125) 
eye('black', 5) 
  
# draw nose 
pen.goto(0, 75) 
eye('black', 8) 
  
# draw mouth 
pen.goto(-40, 85) 
pen.down() 
pen.right(90) 
pen.circle(40, 180) 
pen.up() 
  
# draw tongue 
pen.goto(-10, 45) 
pen.down() 
pen.right(180) 
pen.fillcolor('red') 
pen.begin_fill() 
pen.circle(10, 180) 
pen.end_fill() 

pen.hideturtle() 