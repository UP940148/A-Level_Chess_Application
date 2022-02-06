import Data_Structure_Library as ds
import turtle

TILESIZE = 65
ORIGIN = -4*TILESIZE + 1, -4*TILESIZE + 1
BLACKCOLOUR = '#59260B'
WHITECOLOUR = '#CBA135'

turtle.setup(width = 8*TILESIZE +50, height = 8*TILESIZE +50)
turtle.speed(0)
turtle.hideturtle()

def BlackTile():
    turtle.pencolor(BLACKCOLOUR)
    turtle.fillcolor(BLACKCOLOUR)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(TILESIZE-1)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(TILESIZE)
    turtle.left(90)
    
def WhiteTile():
    turtle.penup()
    turtle.right(90)
    turtle.forward(TILESIZE)
    turtle.left(90)
    
def ReturnToOrigin():
    turtle.penup()
    turtle.goto(ORIGIN)
    turtle.setheading(0)
    turtle.forward(1)
    turtle.left(90)

def DrawBorder():
    turtle.setheading(180)
    turtle.forward(1)
    turtle.left(90)
    turtle.forward(1)
    turtle.pendown()
    turtle.fillcolor(WHITECOLOUR)
    turtle.begin_fill()
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(8*TILESIZE + 1)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(1)
    turtle.left(90)
    turtle.forward(1)
    
def DrawBlankBoard():
    for i in range(4):
        ReturnToOrigin()
        turtle.forward(2*TILESIZE*i)
        for j in range(4):
            BlackTile()
            WhiteTile()
        ReturnToOrigin()
        turtle.forward(TILESIZE+2*TILESIZE*i)
        for k in range(4):
            WhiteTile()
            BlackTile()
        ReturnToOrigin()
        turtle.forward(2*TILESIZE+2*TILESIZE*i)


def MoveTurtle(x, y):
    x -= 4*TILESIZE
    y -= 4*TILESIZE
    turtle.penup()
    turtle.goto(x, y)

def MovePiece(Turtle, x, y):
    '''0 ≤ x, y ≤ 7'''
    x = x*TILESIZE - (3*TILESIZE +TILESIZE/2) + 1 
    y = y*TILESIZE - (3*TILESIZE +TILESIZE/2) + 1
    Turtle.penup()
    Turtle.goto(x, y)

def RegisterShapes():
    turtle.register_shape("WPawn.gif")
    turtle.register_shape("BPawn.gif")
    turtle.register_shape("WRook.gif")
    turtle.register_shape("BRook.gif")
    turtle.register_shape("WKnight.gif")
    turtle.register_shape("BKnight.gif")
    turtle.register_shape("WBishop.gif")
    turtle.register_shape("BBishop.gif")
    turtle.register_shape("WQueen.gif")
    turtle.register_shape("BQueen.gif")
    turtle.register_shape("WKing.gif")
    turtle.register_shape("BKing.gif")

def LoadTurtles():
    TurtleList = ds.Array(8, 8)
    for i in range(8):
        a = turtle.Turtle()
        b = turtle.Turtle()
        c = turtle.Turtle()
        d = turtle.Turtle()
        
        TurtleList.Set(a, i, 0)
        TurtleList.Set(b, i, 1)
        TurtleList.Set(c, i, 6)
        TurtleList.Set(d, i, 7)
    for i in range(8):
        for j in range(8):
            if TurtleList.Get(i, j) != None:
                TurtleList.Get(i, j).penup()
                TurtleList.Get(i, j).speed(9)
                MovePiece(TurtleList.Get(i, j), i, j)
                TurtleList.Get(i, j).setheading(90)
                TurtleList.Get(i, j).speed(1)
                
    RegisterShapes()
    ##Pawns
    for i in range(8):
        TurtleList.Get(i, 1).shape("WPawn.gif")
        TurtleList.Get(i, 6).shape("BPawn.gif")
    ##Rooks
    TurtleList.Get(0, 0).shape("WRook.gif")
    TurtleList.Get(7, 0).shape("WRook.gif")
    TurtleList.Get(0, 7).shape("BRook.gif")
    TurtleList.Get(7, 7).shape("BRook.gif")
    ##Knights
    TurtleList.Get(1, 0).shape("WKnight.gif")
    TurtleList.Get(6, 0).shape("WKnight.gif")
    TurtleList.Get(1, 7).shape("BKnight.gif")
    TurtleList.Get(6, 7).shape("BKnight.gif")
    ##Bishops
    TurtleList.Get(2, 0).shape("WBishop.gif")
    TurtleList.Get(5, 0).shape("WBishop.gif")
    TurtleList.Get(2, 7).shape("BBishop.gif")
    TurtleList.Get(5, 7).shape("BBishop.gif")
    ##Kings
    TurtleList.Get(4, 0).shape("WKing.gif")
    TurtleList.Get(4, 7).shape("BKing.gif")
    ##Queens
    TurtleList.Get(3, 0).shape("WQueen.gif")
    TurtleList.Get(3, 7).shape("BQueen.gif")
    return TurtleList
        

def LoadGame():
    ReturnToOrigin()
    DrawBorder()
    DrawBlankBoard()
    return LoadTurtles()






    


