from turtle import *
import utility
hideturtle()

#Def funciones de Daniel
#------------------------------------------------------------------------------------
#Spots and backround

def draw_bg_circle(x: int, y: int, angle: int):
    "White background circle"
    
    utility.positioning(-15, -850, 0)
    
    fillcolor("white")
    begin_fill()
    
    circle(650)
    
    end_fill()
    utility.positioning(x, y, angle)
    

def draw_big_spot(x: int, y: int, angle: int):
    "Spot in cat body"
    
    utility.positioning(x, y, angle - 45)
    
    pencolor("gray")
    fillcolor("gray")
    begin_fill()
    
    for i in range(2):
        circle(20,90)
        circle(100,90)
        
    end_fill()
    right(45)
    pencolor("black")
    
def draw_small_spot(x: int, y: int, angle: int):
    "Spot in cat body"
    
    utility.positioning(x, y, angle - 45)
    
    pencolor("gray")
    fillcolor("gray")
    begin_fill()
    
    for i in range(2):
        circle(15,90)
        circle(85,90)
        
    end_fill()
    right(45)
    pencolor("black")
    
def draw_tiny_spot(x: int, y: int, angle: int):
    "Spot in cat tail"
    
    utility.positioning(x, y, angle - 45)
    
    pencolor("gray")
    fillcolor("gray")
    begin_fill()
    
    circle(18)
                
    end_fill()
    right(45)
    pencolor("black")
    
 
    
def place_spots(x: int, y: int, angle: int):
    "Place all the spots"
    
    draw_big_spot(x + 150, y + 20, angle)
    draw_small_spot(x - 83, y + 55, angle)
    draw_tiny_spot(x + 40, y + 300, angle)
    draw_tiny_spot(x + 50, y + 315, angle)
    draw_tiny_spot(x - 12, y + 200, angle)
    draw_tiny_spot(x - 15, y + 195, angle)
    pencolor("black")
    
#Def cat fuctions        
#----------------------------------------------------------------------------------
def draw_oval(x: int, y: int):
    "Form of the face"
    
    penup()
    goto(x,y)
    pendown()
    
    left(45)
    for i in range(2):
        circle(170, 90)
        circle(320, 90)
        
    penup()
    right(45)
    
    
def design_cat_ear(x: int, y: int, angle: int):
    "Desing of cat ears"
    
    utility.positioning(x, y, angle)
    left(103)
    
    utility.draw_right_curved_line(20, 10, 1)
    
    circle(-10, 110)
    
    utility.draw_right_curved_line(20, 10, 1)
    
    utility.positioning(x, y, 0)
    
def draw_cat_ear(x: int, y: int, angle: int):
    "Draw of the cat ear"
    
    utility.positioning(x, y, angle)
    fillcolor("white")
    begin_fill()
    design_cat_ear(x, y, angle)
    design_cat_ear(x+320, y+85, angle+10)
    end_fill()
    right(80)
    
def design_cat_foot(x: int, y: int, angle: int):
    "Form of the front paws"
    
    utility.positioning(x, y,angle-45)
    
    fillcolor("white")
    begin_fill()
    
    for i in range(2):
        circle(40, 90)
        circle(80, 90)
        
    end_fill()    
    penup()
    right(45)
    
#Desing of cat fingers of booth paws
#------------------------------------------------------------------------------------    
def design_cat_left_finger(x: int, y: int, angle: int):
    "Fingers of left paw"
    
    utility.positioning(x, y, angle)
    circle(-35, 90)

def design_cat_right_finger(x: int, y: int, angle: int):
    "Fingers of right paw"
        
    utility.positioning(x, y, angle)
    circle(35, 90)
    
def draw_inner_line(x: int, y: int):
    "Draws the ear's inner lines."
    
    "Left ear inner lines--------------------------------------------------------"
    utility.positioning(x - 176, y + 77, -73)
    utility.draw_left_curved_line(9, 10, 2)
    utility.positioning(x - 176, y + 77, 91)
    utility.draw_left_curved_line(14, 10, 1)

    "Right ear inner lines-------------------------------------------------------"
    utility.positioning(x + 60, y + 77, 95)
    utility.draw_right_curved_line(14, 10, 1)
    utility.positioning(x + 60, y + 77, 65)
    utility.draw_right_curved_line(9, 10, 2)
    
    "Return turtle to the default angle."
    right(182)

#Draw all the fuctions together
#-----------------------------------------------------------------------------------    
def draw_cat_head(x: int, y: int, angle: int):
    "Drawing cat head. [Under NO circumstances change ANY of these coordinates, please!] "
    draw_bg_circle(0, 0, 0)
    place_spots(0, 0, 0)
    draw_oval(x + 165, y-220)
    draw_cat_ear(x - 300, y + 0, angle + 0)
    right(angle + 176)
 
    design_cat_foot(x - 200, y - 280, 0)
    design_cat_foot(x + 200, y - 280, 0)
    
    design_cat_left_finger(x - 235, y - 300, angle + 230)
    design_cat_left_finger(x - 275, y - 300, angle + 270)
    
    design_cat_right_finger(x + 120, y - 300, angle + 0)
    design_cat_right_finger(x + 160, y - 300, angle + 90)
    draw_inner_line(x + 0, y + 0)
    
    "Return turtle to the angle for Ani`s part to continue."
    right(3)

