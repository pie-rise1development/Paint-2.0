from turtle import *

t = Turtle() 
t.shape('circle')
t.width(5)
t.speed(0)
size = 5

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def tomato():
    t.color('Tomato')
def blue():
    t.color('MidnightBlue')
def green():
    t.color('SeaGreen')
def yellow():
    t.color('GreenYellow')
def brown():
    t.color('SaddleBrown')
def coral():
    t.color('Coral')
def snow():
    t.color('Snow')
def darkblue():
    t.color('MediumSlateBlue')

def up():
    t.goto(t.xcor(), t.ycor()+10)

def down():
    t.goto(t.xcor(), t.ycor()-10)

def left():
    t.goto(t.xcor()-10, t.ycor())

def right():
    t.goto(t.xcor()+10, t.ycor())

def beg_fill():
    t.begin_fill()

def e_fill():
    t.end_fill()

def low_size():
    global size
    if size > 1:
        size -= 2
        t.pensize(size)

def hight_size():
    global size
    size += 2
    t.pensize(size)

screen = t.getscreen()
screen.onscreenclick(move)

screen.onkey(tomato, 'r')
screen.onkey(blue, 'b')
screen.onkey(green, 'g')
screen.onkey(yellow, 'y')
screen.onkey(brown, 'w')
screen.onkey(coral, 'c')
screen.onkey(snow, 's')
screen.onkey(darkblue, 'd')

screen.onkey(up, 'Up')
screen.onkey(right, 'Right')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')

screen.onkey(hight_size, 'x')
screen.onkey(low_size, 'z')


screen.onkey(beg_fill, ',')
screen.onkey(e_fill, '.')

t.ondrag(draw)
screen.listen()
mainloop()