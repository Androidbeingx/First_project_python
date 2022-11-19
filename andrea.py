from turtle import *
import utility
hideturtle()

def draw_oval(x: int, y: int):
    penup()
    goto(x,y)
    pendown()
    
    left(45)
    for i in range(2):
        circle(170, 90)
        circle(320, 90)
        
    penup()
    right(45)
    
#Def funciones Andrea
#------------------------------------------------------------------------------
def draw_three_point(x: int, y: int, angle: int):
    utility.positioning(x, y, angle + 80)
    for i in range(3):
        right(120)
        fillcolor("black")
        begin_fill()
        circle(2)
        end_fill()
        penup()
        forward(25)
        pendown()
#Def eyes
#----------------------------------------------------------------------------------        
def design_black_eye():
    
    circle(50)
    fillcolor("black")
    begin_fill()
    circle(50)
    end_fill()
    
def design_big_white_dot():
    
    circle(10)
    fillcolor("white")
    begin_fill()
    circle(10)
    end_fill()
    
def design_small_white_dot():
    
    circle(5)
    fillcolor("white")
    begin_fill()
    circle(5)
    end_fill()
    
#Draw eyes
#-------------------------------------------------------------------------------
    
def draw_eye(x: int, y: int, angle: int):
    "Draw one eye, copy for the other"
    
    utility.positioning(x, y, angle)
    
    design_black_eye()
    
    utility.positioning(x - 30, y - 15, 0)
    
    design_big_white_dot()
    
    utility.positioning(x + 13, y - 45, angle)
    
    design_small_white_dot()

#Drawing snout
#-------------------------------------------------------------------------    
   
def draw_cat_nose(x: int, y: int, angle: int):
    "Drawing a triangle with curve angles"
    
    utility.positioning(x , y, angle + 180)
    
    fillcolor("black")
    begin_fill()
    
    utility.draw_right_curved_line(6, 3, 1)
    
    circle(-10, 110)
    
    utility.draw_right_curved_line(6, 3, 1)
    
    circle(-10, 110)
    
    utility.draw_right_curved_line(6, 3, 1)
    
    circle(-10, 110)
    end_fill()
    
    utility.positioning(x, y, angle)
    
    right(80)
        
def draw_left_mouth(x: int, y: int, angle: int):
    "Left side of the mouth"
    
    utility.positioning(x, y, angle)
    
    pensize(2)
    utility.draw_right_curved_line(30, 5, 5)
    
    left(180)
    utility.draw_left_curved_line(30, 5, 5)
    
def draw_right_mouth(x: int, y: int, angle: int):
    "Right side of the mouth"
    
    utility.positioning(x, y, angle + 205)
    
    pensize(2)
    utility.draw_left_curved_line(30, 5, 5)
    
    right(180)
    utility.draw_right_curved_line(30, 5, 5)

#Draw whiskers
#-------------------------------------------------------------------------    
def draw_left_whiskers(x: int, y: int, angle: int):
    "Three left whiskers, same origin"
    
    utility.positioning(x, y, angle)
    utility.draw_left_curved_line(10, 10, 2)
    
    utility.positioning(x, y, angle + 40)
   
    utility.draw_left_curved_line(10, 10, 2)
    
    utility.positioning(x, y, angle + 43)
    
    utility.draw_left_curved_line(10, 12, 2)

def draw_right_whiskers(x: int, y:int, angle: int):
    "Three right whiskers, same origin"
    
    utility.positioning(x, y, angle)
    utility.draw_right_curved_line(10, 12, 3)
    
    utility.positioning(x, y, angle + 40)
    utility.draw_right_curved_line(10, 10, 2)
    
    utility.positioning(x, y, angle + 45)
    utility.draw_right_curved_line(10, 10, 2)
    
#Extra functions
#---------------------------------------------------------------------
    
def design_star(lenght: int):
    "Defenition of the cat toy"
    
    list1 = ["black", "purple2"]
    
    for i in range(5):
        color(list1[i%2])
        forward(lenght)
        right(180 -36)
        
def draw_spiral_star(x: int, y: int, angle: int):
    "Draw cat toy"
        
    utility.positioning(x + 320, y - 375, angle)
   
   
    for i in range(68):
        design_star(65)
        right(5)

        
#Draw cat face at all
#-------------------------------------------------------------------        
def draw_cat_face(x: int, y: int, angle: int):
    "Draw the entire face"
    "DO NOT CHANGE THE COORDENATES, PLEASE"
    
    utility.positioning(x + 0, y + 0, angle + 0)
    
    draw_eye(x - 160, y - 5, angle + 5)
    draw_eye(x + 60, y - 5, angle + 0)
    
    draw_cat_nose(x - 70, y - 140, angle - 125)
    
    draw_left_mouth(x - 60, y - 130, angle - 95)
    draw_right_mouth(x -60, y - 130, angle - 22)
    
    draw_left_whiskers(x - 300, y - 100, angle - 56)
    draw_right_whiskers(x + 170, y - 100, angle - 96)
    
    draw_three_point(19, -258, 0)
    draw_three_point(-127, -258, 0)
    right(207)
