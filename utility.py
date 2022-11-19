from turtle import*
hideturtle()

#Basic definitions, used by all the members
#------------------------------------------------------------------------------------
    
def configure_canvas():
    canvas_height: int = 1500
    canvas_width: int = 1500
    
    window_origin_x: int = 0
    window_origin_y: int = 0
    
    setup(canvas_height,
          canvas_width,
          window_origin_x,
          window_origin_y)
    speed(13)
    width(2)
    bgcolor("bisque")
    


def draw_right_curved_line(repetition: int, pixel: int, angle: int):
    for i in range(repetition):
        forward(pixel)
        right(angle)
        
def draw_left_curved_line(repetition: int, pixel: int,angle: int):
    for i in range(repetition):
        forward(pixel)
        left(angle)
        
        
def positioning(x: int, y: int, angle: int):
    "Taking position"
    penup()
    goto(x, y)
    right(angle)
    pendown()

def write_names(x: int, y: int):
    "Typping author of the drawing"
    
    pencolor("indian red")
    penup()
    goto(x, y)
    
    name_list = ["Daniel Majer", "Andrea Morales Mata", "Ani Valle Banegas", "DAWBIO1-Gato.py" ]

    for i in range(len(name_list)):
        list_element: str = name_list[i]
        write(list_element, font=("arial", 20, "bold italic"))
        goto(x, ycor() - 50)
