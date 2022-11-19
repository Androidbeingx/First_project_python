from turtle import *
import utility
hideturtle()

# Def Ani functions.
#---------------------------------------------------------------------
def draw_cat_torso(x: int, y: int, angle: int):
    
    utility.positioning(x - 230, y + 165, angle + 89)
    utility.draw_right_curved_line(38, 10, 2)
        
              
def draw_cat_tail(x: int, y: int, angle: int):
    
    utility.positioning(x - 30, y + 235, angle + 230)
    
    circle(-130, 50)
    circle(130, 50)
    circle(85, 102)
    
    utility.draw_left_curved_line(20, 2, 8)

    utility.positioning(x - 50, y + 235, angle + 240)
    
    circle(-100, 70)
    circle(119, 50)
    circle(53, 91)
      
    utility.positioning(x , y, angle)
    
#Extra defenitions
#--------------------------------------------------------------------------------------
def draw_three_spots(x: int, y: int, angle: int):
    "Draw three lines in top head like three spots"

    utility.positioning(x - 50, y - 10, angle)
    width(10)
    pencolor("gray")
    right(90)
    for i in range (10):
        forward(5)
    utility.positioning(x - 10, y - 10, angle)
    right(15)
    for i in range (10):
        forward(5)
    utility.positioning(x - 90, y - 10, angle)
    left(30)
    for i in range (10):
        forward(5)
    
    
    utility.positioning(x, y, angle)

def draw_carpet(x: int, y: int, angle: int):
    "Draw a carpet under the cat--------------"
    
    width(4)
    utility.positioning(x -339, y -190, angle)
    pencolor("indian red")
    goto(-550, -190)
    goto(-450, -480)
    goto(550, -480)
    goto(350, -190)
    goto(215, -190)
    "I don't know any other way to optimize the five goto--------"
    
    utility.positioning(x, y, angle)
    
def draw_threads_carpet(x: int, y: int, angle: int):
    "Definition of threads of the carpet in each side"
    
    width(3)
    utility.positioning(x -550, y -190, -75)
    angle: int=140
    side: int=45
    
    for i in range (10):
        forward(side)
        right(angle)
        forward(side)
        left(angle)
    "threads from the right side of the carpet------------------------------"
    width(3)
    utility.positioning(x +500, y -480, -60)
    
    for i in range (9):
        forward(side - 2)
        right(-angle + 10)
        forward(side - 2)
        left(-angle + 10)
    forward(side -18)
        
    utility.positioning(x, y, angle)
    
#Draw cat body together
#------------------------------------------------------------------------------------    
    
    "Do not delete or modify the below, please!-------------------------------"
def draw_cat_body(x: int, y: int, angle: int):
    utility.positioning(x, y, angle)
    draw_cat_torso(x, y - 0, 0)
    draw_cat_tail(x, y - 8, 0)
     