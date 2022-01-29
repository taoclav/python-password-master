# importing package
from multiprocessing.connection import wait

import turtle
turtle.color('red', 'yellow')
turtle.pensize(5)
# method to call on drag
wn = turtle.Screen()
def fxn(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color('red', 'green')
    turtle.pendown()
    turtle.begin_fill()
  
wn.onclick(fxn)
def fxn1(x, y):
  
    # stop backtracking
    turtle.ondrag(None) 
  
    # move the turtle's angle and direction 
    # towards x and y
    turtle.setheading(turtle.towards(x, y))
  
    # go to x, y
    turtle.goto(x, y)
    turtle.color('red', 'yellow')
    
  
    # call again
    turtle.ondrag(fxn1)
  
# set turtle speed
turtle.speed(15)
  
# make turtle screen object
sc = turtle.Screen()
  
# set screen size
sc.setup(1920, 1080)
  
# call fxn on drag
turtle.ondrag(fxn1)

# take screen in mainloop
sc.mainloop()